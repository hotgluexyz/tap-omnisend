"""Stream type classes for tap-omnisend."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_omnisend.client import omnisendStream

# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")
# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
#       - Copy-paste as many times as needed to create multiple stream types.


class Contacts(omnisendStream):
    """Define custom stream."""
    name = "contacts"
    path = "/contacts"
    primary_keys = ["contactID"]
    records_jsonpath = "$.contacts[*]"
    replication_key = None

    schema = th.PropertiesList(
        th.Property("email", th.StringType),
        th.Property("contactID", th.StringType),
        th.Property("createdAt", th.DateTimeType),
        th.Property("firstName", th.StringType),
        th.Property("lastName", th.StringType),
        th.Property("country", th.StringType),
        th.Property("countryCode", th.StringType),
        th.Property("state", th.StringType),
        th.Property("city", th.StringType),
        th.Property("postalCode", th.StringType),
        th.Property("address", th.StringType),
        th.Property("gender", th.StringType),
        th.Property("phone", 
            th.ArrayType(
                th.Property("status", th.StringType)
            )
        ),
        th.Property("phoneNumber", th.StringType),
        th.Property("birthdate", th.DateTimeType),
        th.Property("sent", th.NumberType),
        th.Property("opened", th.NumberType),
        th.Property("clicked", th.NumberType),
        th.Property("status", th.StringType),
        th.Property("lists", th.StringType),
        th.Property("statuses", 
            th.ArrayType(
                th.ObjectType(
                    th.Property("status", th.StringType),
                    th.Property("date", th.DateTimeType),
                )
            )
        ), 
        th.Property("optIns", 
            th.ArrayType(
                th.ObjectType(
                    th.Property("date", th.DateTimeType),
                )
            )
        ), 
        th.Property("doubleOptIns", 
            th.ArrayType(
                th.ObjectType(
                    th.Property("date", th.DateTimeType),
                )
            )
        ),
        th.Property("tags", th.ArrayType(th.StringType)),
        th.Property("customProperties", th.ObjectType(
            th.Property("externalCreated", th.DateTimeType),
        )),
        th.Property("identifiers", 
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.StringType),
                    th.Property("type", th.StringType),
                    th.Property("channels", th.ObjectType(
                            th.Property("email", th.ObjectType(
                                th.Property("status", th.StringType),
                                th.Property("statusDate", th.DateTimeType),
                            ))
                        ))
                    )
                )
            )
        ).to_dict()
