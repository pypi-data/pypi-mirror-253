
from dataclasses import dataclass

from marshmallow_dataclass import class_schema

from semantha_sdk.rest.rest_client import RestSchema

from typing import Optional


@dataclass
class TransactionSummary:
    """ author semantha, this is a generated class do not change manually! """
    number_of_documents: Optional[int] = None
    number_of_pages: Optional[int] = None
    service: Optional[str] = None

TransactionSummarySchema = class_schema(TransactionSummary, base_schema=RestSchema)
