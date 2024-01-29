
from dataclasses import dataclass

from marshmallow_dataclass import class_schema

from semantha_sdk.rest.rest_client import RestSchema

from typing import Optional


@dataclass
class DomainInfo:
    """ author semantha, this is a generated class do not change manually! """
    id: Optional[str] = None
    name: Optional[str] = None
    base_url: Optional[str] = None

DomainInfoSchema = class_schema(DomainInfo, base_schema=RestSchema)
