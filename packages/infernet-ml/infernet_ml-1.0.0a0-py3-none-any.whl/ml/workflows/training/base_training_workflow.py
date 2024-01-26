"""
Module implementing base training workflow
"""
import abc
import logging
from typing import Any

logger: logging.Logger = logging.getLogger(__name__)


class BaseTrainingWorkflow(metaclass=abc.ABCMeta):
    """
    Base class for a machine learning training workflow.
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self.args: Any = args
        self.kwargs: Any = kwargs
        self.is_setup: bool = False
        self.__inference_count: int = 0
        self.__proof_count: int = 0

    def setup(self) -> Any:
        """
        calls setup
        """
        logger.info("Training: Setting up")
        res = self.do_setup()
        self.is_setup = True
        return res

    @abc.abstractmethod
    def do_setup(self) -> Any:
        """implement setup here"""

    def inference(self, input_data: Any) -> Any:
        """performs inference. Checks that model is set up before
        performing inference.
        Subclasses should implement do_inference.

        Args:
            input_data (typing.Any): raw input from user

        Raises:
            ValueError: if setup not called beforehand

        Returns:
            typing.Any: result of inference
        """
        if not self.is_setup:
            raise ValueError("setup not called before inference")

        logger.info("inference: Input Data %s", input_data)
        label = self.do_inference(input_data)
        self.__inference_count += 1
        return label

    @abc.abstractmethod
    def do_inference(self, input_data: Any) -> Any:
        """perform inference with model here. input_data type is
        left generic since depending on model type (LLM vs. classical)
        it may different

        Args:
            input_data (typing.Any): input into model

        Returns:
            typing.Any: result of model inference
        """

    def scoring(self) -> Any:
        """
        calls scoring. Scoring refers
        to measuring the perf of the model
        post training.
        """
        if not self.is_setup:
            raise ValueError("setup not called before scoring")
        logger.info("Training: Scoring")
        return self.do_scoring()

    @abc.abstractmethod
    def do_scoring(self) -> dict[str, Any]:
        """
        implement scoring. Return dict of
        metric to score mappings.
        """

    def generate_proof(self) -> Any:
        """
        Generates proof. checks that setup performed before hand.
        """
        if not self.is_setup:
            raise ValueError("setup not called before attempting to generate proof")

        if self.__inference_count <= self.__proof_count:
            logging.warning(
                "generated %s inferences only but attempting to generate proof %s",
                self.__inference_count,
                self.__proof_count + 1,
            )
        logger.info("Training: generating proof")
        res = self.do_generate_proof()
        self.__proof_count += 1
        return res

    @abc.abstractmethod
    def do_generate_proof(self) -> Any:
        """
        Generates proof, which may vary based on proving system
        """

    def deploy(self) -> Any:
        """calls deploy"""
        logger.info("Training: deploying")
        self.do_deploy()

    def do_deploy(self) -> Any:
        """implement deployment here"""
        raise NotImplementedError
