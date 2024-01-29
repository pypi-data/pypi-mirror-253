
from dataclasses import dataclass

from marshmallow_dataclass import class_schema

from semantha_sdk.rest.rest_client import RestSchema

from typing import Optional


@dataclass
class Info:
    """ author semantha, this is a generated class do not change manually! """
    title: Optional[str] = None
    vendor: Optional[str] = None
    time: Optional[str] = None
    git: Optional[str] = None
    version: Optional[str] = None

InfoSchema = class_schema(Info, base_schema=RestSchema)
