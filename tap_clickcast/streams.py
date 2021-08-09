"""Stream type classes for tap-clickcast."""

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_clickcast.client import ClickcastStream

# TODO: Delete this is if not using json files for schema definition
# SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")
# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
#       - Copy-paste as many times as needed to create multiple stream types.


class EmployersStream(ClickcastStream):
    name = "employers"
    path = "/employers"
    primary_keys = ["employer_id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("employer_id", th.StringType),
        th.Property("employer_name", th.StringType),
    ).to_dict()


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
