"""clickcast tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers

# TODO: Import your custom stream types here:
from tap_clickcast.streams import EmployersStream

# TODO: Compile a list of custom stream types here
#       OR rewrite discover_streams() below with your custom logic.
STREAM_TYPES = [
    EmployersStream,
]


class TapClickcast(Tap):
    """clickcast tap class."""

    name = "tap-clickcast"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property("partner_token", th.StringType, required=True),
        th.Property("start_date", th.DateTimeType),
        th.Property("api_url_base", th.StringType, default="https://api.clickcast.cloud/clickcast/api"),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
