
from dataclasses import dataclass

from marshmallow_dataclass import class_schema

from semantha_sdk.rest.rest_client import RestSchema

from typing import Optional


@dataclass
class LanguageDetection:
    """ author semantha, this is a generated class do not change manually! """
    language: Optional[str] = None

LanguageDetectionSchema = class_schema(LanguageDetection, base_schema=RestSchema)
