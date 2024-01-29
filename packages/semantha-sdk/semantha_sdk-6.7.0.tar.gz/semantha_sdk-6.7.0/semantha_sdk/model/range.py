
from dataclasses import dataclass

from marshmallow_dataclass import class_schema

from semantha_sdk.rest.rest_client import RestSchema

from semantha_sdk.model.rect import Rect
from typing import Optional


@dataclass
class Range:
    """ author semantha, this is a generated class do not change manually! """
    rect: Optional[Rect] = None
    page: Optional[int] = None

RangeSchema = class_schema(Range, base_schema=RestSchema)
