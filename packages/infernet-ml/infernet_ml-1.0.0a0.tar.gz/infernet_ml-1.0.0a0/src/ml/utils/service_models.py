"""
Module containing data models used by the service
"""
from enum import IntEnum
from typing import Annotated, Any, Union

from pydantic import BaseModel, StringConstraints, model_validator

HexStr = Annotated[
    str, StringConstraints(strip_whitespace=True, pattern="^[a-fA-F0-9]+$")
]


class InfernetInputSource(IntEnum):
    CHAIN = 0
    OFFCHAIN = 1


class InfernetInput(BaseModel):
    source: InfernetInputSource
    data: Union[HexStr, dict[str, Any]]

    @model_validator(mode="after")
    def check_data_correct(self) -> "InfernetInput":
        src = self.source
        dta = self.data
        if (
            src is not None
            and dta is not None
            and (
                (src == InfernetInputSource.CHAIN and not isinstance(dta, str))
                or (src == InfernetInputSource.OFFCHAIN and not isinstance(dta, dict))
            )
        ):
            raise ValueError(
                f"InfernetInput data type ({type(dta)}) incorrect for source ({str(src)})"  # noqa: E501
            )
        return self
