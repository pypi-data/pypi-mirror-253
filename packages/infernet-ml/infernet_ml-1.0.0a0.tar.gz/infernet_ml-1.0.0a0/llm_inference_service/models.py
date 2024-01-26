"""
Module containing data models used by the service
"""
from typing import Optional

from pydantic import BaseModel


class LLMRequest(BaseModel):
    """
    Represents an LLM Inference Request
    """

    key: str
    messageId: str
    text: str  # actual query to the LLM backend
    history: list[Optional[dict[str, str]]]  # rolling query history
