from importlib.metadata import version

import requests
import uplink

__version__ = version("bpkio-python-sdk")


class BpkioSdkConsumer(uplink.Consumer):
    def __init__(self, base_url="", verify_ssl=True, **kwargs):
        s = requests.Session()
        s.verify = verify_ssl

        # Hide warnings about InsecureRequestWarning (from not validating SSL self-signed certificates)
        if verify_ssl is False:
            requests.packages.urllib3.disable_warnings()

        super().__init__(base_url, client=s, **kwargs)

        user_agent = f"bpkio-python-sdk/{__version__}"

        if "user_agent" in kwargs:
            user_agent = kwargs["user_agent"] + " " + user_agent

        # Set this header for all requests of the instance.
        self.session.headers["User-Agent"] = user_agent
