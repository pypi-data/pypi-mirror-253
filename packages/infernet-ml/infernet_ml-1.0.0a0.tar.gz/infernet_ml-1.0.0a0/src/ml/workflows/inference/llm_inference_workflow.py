"""
Module containing a LLM Inference Workflow object.
"""

import json
import logging
import os
from typing import Any, Optional, Union

from ml.workflows.inference.base_inference_workflow import BaseInferenceWorkflow
from retry.api import retry_call
from text_generation import Client  # type: ignore
from text_generation.errors import (  # type: ignore
    OverloadedError,
    RateLimitExceededError,
    ShardNotReadyError,
    ShardTimeoutError,
)

TGI_REQUEST_TRIES: int = json.loads(os.getenv("TGI_REQUEST_TRIES", "3"))
TGI_REQUEST_DELAY: int = json.loads(os.getenv("TGI_REQUEST_DELAY", "3"))
TGI_REQUEST_MAX_DELAY: Optional[Any] = json.loads(
    os.getenv("TGI_REQUEST_MAX_DELAY", "null")
)
TGI_REQUEST_BACKOFF: int = json.loads(os.getenv("TGI_REQUEST_BACKOFF", "2"))
TGI_REQUEST_JITTER: tuple[float, float] | float = (
    jitter
    if isinstance(
        jitter := json.loads(os.getenv("TGI_REQUEST_JITTER", "[0.5,1.5]")), float
    )
    else tuple(jitter)
)


class LLMInferenceWorkflow(BaseInferenceWorkflow):
    """
    Base workflow object for LLM based inference models.
    The interface of the LLM Inference server is
    assumed to be the same as Huggingface TGI.
    """

    def __init__(
        self, server_url: str, timeout: int = 30, **inference_params: dict[str, Any]
    ) -> None:
        """
        constructor. Any named arguments passed to LLM during inference.

        Args:
            server_url (str): url of inference server
        """
        super().__init__()
        self.client: Client = Client(server_url, timeout=timeout)
        self.inference_params: dict[str, Any] = inference_params
        # dummy call to fail fast if client is misconfigured
        self.client.generate("hello", **inference_params)

    def do_setup(self) -> bool:
        """
        no specific setup needed
        """
        return True

    def do_preprocessing(self, input_data: dict[str, Any]) -> str:
        """
        Implement any preprocessing of the raw input.
        For example, you may want to append additional context.
        By default, returns the value associated with the text key in a dictionary.

        Args:
            input_data (Union[dict[str]]): raw input
        Returns:
            str: transformed user input prompt
        """
        return str(input_data["text"])

    def do_postprocessing(
        self, input_data: dict[str, Any], gen_text: str
    ) -> Union[str, dict[str, Any]]:
        """
        Implement any postprocessing here. For example, you may need to return
        additional data.

        Args:
            input_data (Union[dict[str]]): raw input
            gen_text (str): str result from LLM model
        Returns:
            Any: transformation to the gen_text
        """

        return gen_text

    def do_inference(self, input_data: dict[str, Any]) -> Union[str, dict[str, Any]]:
        """
        Inference implementation. Generally,
        you should not need to change this implementation
        directly, as the code already implements calling
        an LLM server.

        Instead, you can perform any preprocessing or
        post processing in the relevant abstract methods.

        Args:
            dict (str): user input

        Returns:
            Any: result of inference
        """
        logging.info("preprocessing data...")
        preprocessed_data: str = self.do_preprocessing(input_data)

        logging.info(
            f"querying tgi client with [{preprocessed_data}] with params "
            f"{self.inference_params}..."
        )

        # TODO: consider async
        gen_text: str = retry_call(
            self.client.generate,
            [preprocessed_data],
            self.inference_params,
            exceptions=(
                ShardNotReadyError,
                ShardTimeoutError,
                RateLimitExceededError,
                OverloadedError,
            ),
            tries=TGI_REQUEST_TRIES,
            delay=TGI_REQUEST_DELAY,
            max_delay=TGI_REQUEST_MAX_DELAY,
            backoff=TGI_REQUEST_BACKOFF,
            jitter=TGI_REQUEST_JITTER,
        ).generated_text

        logging.info(f"post processing data [{gen_text}]...")
        return self.do_postprocessing(input_data, gen_text)

    def do_generate_proof(self) -> Any:
        """
        raise error by default
        """
        raise NotImplementedError
