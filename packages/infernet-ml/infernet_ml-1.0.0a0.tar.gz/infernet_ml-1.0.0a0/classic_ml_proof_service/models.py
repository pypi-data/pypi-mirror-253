"""
Module containing data models used by the service
"""
from typing import Any, Optional, Tuple, Union

from pydantic import BaseModel

from ml.utils.service_models import HexStr


class AccountCall(BaseModel):
    call_data: list[Tuple[HexStr, int]]
    address: HexStr


class OnChainSource(BaseModel):
    calls: list[AccountCall]
    rpc: str


class WitnessInputData(BaseModel):
    input_data: Optional[Union[OnChainSource, list[Any]]]
    output_data: Optional[Union[OnChainSource, list[Any]]]
