"""
Module implementing a base inference workflow.

This class is not meant to be subclassed directly; instead,
subclass one of [LLMInferenceWorkflow, BaseClassicInferenceWorkflow]


"""
import abc
import logging
from typing import Any

logger: logging.Logger = logging.getLogger(__name__)


class BaseInferenceWorkflow(metaclass=abc.ABCMeta):
    """
    Base class for an inference workflow
    """

    def __init__(self) -> None:
        self.is_setup = False
        self.__inference_count: int = 0
        self.__proof_count: int = 0

    def setup(self) -> Any:
        """
        calls setup and keeps track of whether or not setup was called
        """
        self.is_setup = True
        return self.do_setup()

    @abc.abstractmethod
    def do_setup(self) -> Any:
        """set up your workflow here.
        For LLMs, this may be parameters like top_k, temperature
        for classical LLM, this may be model hyperparams.

        Returns: Any
        """

    def inference(self, input_data: Any) -> Any:
        """performs inference. Checks that model is set up before
        performing inference.
        Subclasses should implement do_inference.

        Args:
            input_data (typing.Any): input from user

        Raises:
            ValueError: if setup not called beforehand

        Returns:
            Any: result of inference
        """
        if not self.is_setup:
            raise ValueError("setup not called before inference")
        res = self.do_inference(input_data)
        self.__inference_count += 1
        return res

    @abc.abstractmethod
    def do_inference(self, input_data: Any) -> Any:
        """perform inference with model here. input_data type is
            left generic since depending on model type
        Args:
            input_data (typing.Any): input into model

        Returns:
            typing.Any: result of model inference
        """

    def generate_proof(self) -> None:
        """
        Generates proof. checks that setup performed before hand.
        """
        if self.__inference_count <= self.__proof_count:
            logging.warning(
                "generated %s inferences only but "
                + "already generated %s. Possibly duplicate proof.",
                self.__inference_count,
                self.__proof_count,
            )

        self.do_generate_proof()
        self.__proof_count += 1

    @abc.abstractmethod
    def do_generate_proof(self) -> Any:
        """
        Generates proof, which may vary based on proving system
        """
