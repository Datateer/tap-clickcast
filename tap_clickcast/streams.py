"""Stream type classes for tap-clickcast."""
from pathlib import Path

from tap_clickcast.client import ClickcastStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class EmployersStream(ClickcastStream):
    name = "employers"
    path = "/employers"
    schema_filepath = SCHEMAS_DIR / "employers.json"
    primary_keys = ["employer_id"]
    replication_key = None
    # how to limit ot just the selected fields?


# class UsersStream(ClickcastStream):
#     """Define custom stream."""

#     name = "users"
#     path = "/users"
#     primary_keys = ["id"]
#     replication_key = None
#     # Optionally, you may also use `schema_filepath` in place of `schema`:
#     # schema_filepath = SCHEMAS_DIR / "users.json"
#     schema = th.PropertiesList(
#         th.Property("name", th.StringType),
#         th.Property("id", th.StringType),
#         th.Property("age", th.IntegerType),
#         th.Property("email", th.StringType),
#         th.Property("street", th.StringType),
#         th.Property("city", th.StringType),
#         th.Property("state", th.StringType),
#         th.Property("zip", th.StringType),
#     ).to_dict()


# class GroupsStream(ClickcastStream):
#     """Define custom stream."""

#     name = "groups"
#     path = "/groups"
#     primary_keys = ["id"]
#     replication_key = "modified"
#     schema = th.PropertiesList(
#         th.Property("name", th.StringType),
#         th.Property("id", th.StringType),
#         th.Property("modified", th.DateTimeType),
#     ).to_dict()
