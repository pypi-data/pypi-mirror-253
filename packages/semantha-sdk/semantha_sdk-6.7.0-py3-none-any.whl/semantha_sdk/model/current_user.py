
from dataclasses import dataclass

from marshmallow_dataclass import class_schema

from semantha_sdk.rest.rest_client import RestSchema

from typing import List
from typing import Optional


@dataclass
class CurrentUser:
    """ author semantha, this is a generated class do not change manually! """
    name: Optional[str] = None
    valid_until: Optional[int] = None
    roles: Optional[List[str]] = None

CurrentUserSchema = class_schema(CurrentUser, base_schema=RestSchema)
