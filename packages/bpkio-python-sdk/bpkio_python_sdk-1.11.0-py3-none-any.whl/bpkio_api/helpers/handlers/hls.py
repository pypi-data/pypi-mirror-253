import os
from functools import lru_cache
from typing import Dict, List
from urllib.parse import urlparse

import m3u8
from bpkio_api.exceptions import BroadpeakIoHelperError
from bpkio_api.helpers.codecstrings import CodecStringParser
from bpkio_api.helpers.handlers.generic import ContentHandler


class HLSHandler(ContentHandler):
    content_types = ["application/x-mpegurl", "application/vnd.apple.mpegurl"]
    file_extensions = [".m3u8", ".hls"]

    def __init__(self, url, content: bytes | None = None, **kwargs):
        super().__init__(url, content, **kwargs)
        self._document: m3u8.M3U8 = None

    @property
    def document(self) -> m3u8.M3U8:
        if not self._document:
            try:
                self._document = m3u8.loads(content=self.content.decode(), uri=self.url)
            except Exception as e:
                raise BroadpeakIoHelperError(
                    message="The HLS manifest could not be parsed.",
                    original_message=e.args[0],
                )
        return self._document

    def read(self):
        return "Handling HLS file."

    @staticmethod
    def is_supported_content(content):
        return content.decode().startswith("#EXTM3U")

    def has_children(self) -> bool:
        if self.document.is_variant:
            return True
        return False

    def get_child(self, index: int):
        playlists = self.document.playlists + self.document.media

        try:
            return HLSHandler(
                url=playlists[index - 1].absolute_uri, headers=self.headers
            )
        except IndexError as e:
            raise BroadpeakIoHelperError(
                message=f"The HLS manifest only has {len(self.document.playlists)} renditions.",
                original_message=e.args[0],
            )

    @lru_cache()
    def _fetch_sub(self, uri):
        try:
            return m3u8.load(
                uri,
                headers=self.headers,
                verify_ssl=True
                if self.verify_ssl is True
                else False,  # TODO - ability to set exact CERT. See https://github.com/globocom/m3u8?tab=readme-ov-file#using-different-http-clients
            )
        except Exception as e:
            raise BroadpeakIoHelperError(
                message=f"The HLS media playlist could not be parsed: {uri}",
                original_message=e.args[0] if e.args and len(e.args) else str(e),
            )

    def is_live(self):
        """Checks if the HLS is a live stream (ie. without an end)

        Returns:
            bool
        """
        # Check the first sub-playlist
        if len(self.document.playlists):
            sub = self._fetch_sub(self.document.playlists[0].absolute_uri)
            if not sub.is_endlist:  # type: ignore
                return True
            else:
                return False

        else:
            return not self.document.is_endlist

    def get_duration(self):
        """Calculates the duration of the stream (in seconds)

        Returns:
            int
        """
        if self.is_live():
            return -1
        else:
            sub = self._fetch_sub(self.document.playlists[0].absolute_uri)
            return sum([seg.duration for seg in sub.segments])

    def num_segments(self):
        """Calculates the number of segments in the stream

        Returns:
            int
        """
        sub = self._fetch_sub(self.document.playlists[0].absolute_uri)
        return len(sub.segments)

    def has_muxed_audio(self) -> bool:
        """Checks is the audio stream is muxed in with video

        Returns:
            bool
        """
        for media in self.document.media:
            if media.type == "AUDIO":
                if media.uri is None:
                    return True
        return False

    def extract_info(self) -> Dict:
        info = {
            "format": "HLS",
            "version": self.document.version,
            "type": "Live" if self.is_live() else "VOD",
            "duration (in sec)": "N/A" if self.is_live() else self.get_duration(),
            "segments": self.num_segments(),
        }

        return info

    def get_segment_for_url(self, url):
        for segment in self.document.segments:
            if segment.uri == url:
                return segment

    def extract_features(self) -> List[Dict]:
        """Extracts essential information from the HLS manifest"""
        arr = []
        index = 0

        if self.document.is_variant:
            for playlist in self.document.playlists:
                index += 1

                si = playlist.stream_info

                data = dict(
                    index=index,
                    type="variant",
                    # manifest=playlist.uri,
                    # url=playlist.absolute_uri,
                    codecs=si.codecs,
                )

                # extract info from codecs
                cdc = CodecStringParser.parse_multi_codec_string(si.codecs)
                cdc_v = next((d for d in cdc if d.get("type") == "video"), None)
                cdc_a = next((d for d in cdc if d.get("type") == "audio"), None)

                if cdc_a:
                    data["codeca"] = cdc_a["cc"]
                if cdc_v:
                    data["codecv"] = cdc_v["cc"]
                    data["profilev"] = cdc_v["profile"]
                    data["levelv"] = cdc_v["level"]

                res = (
                    "{} x {}".format(
                        si.resolution[0],
                        si.resolution[1],
                    )
                    if si.resolution
                    else ""
                )
                data["resolution"] = res
                data['bandwidth'] = si.bandwidth

                # parse URI and extract the last part of the path
                u = urlparse(playlist.uri)
                shortened_url = u.path[-50:]
                if u.query:
                    shortened_url += "?..."

                data["uri_short"] = shortened_url

                arr.append(data)

            for media in self.document.media:
                if media.uri:
                    index += 1
                    arr.append(
                        dict(
                            index=index,
                            type="media",
                            manifest=media.uri,
                            language=media.language,
                            url=media.absolute_uri,
                        )
                    )

        return arr
