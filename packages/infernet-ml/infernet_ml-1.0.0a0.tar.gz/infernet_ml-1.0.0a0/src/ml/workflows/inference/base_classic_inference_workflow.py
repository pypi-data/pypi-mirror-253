"""
Module containing a Base Classic Inference Workflow object.
"""
import logging
from abc import abstractmethod
from typing import Any, Union

from ml.workflows.inference.base_inference_workflow import BaseInferenceWorkflow


class BaseClassicInferenceWorkflow(BaseInferenceWorkflow):
    """
    Base workflow object for classic inferencing.
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        constructor.
        """
        super().__init__()
        self.args: list[Any] = list(args)
        self.kwargs: dict[Any, Any] = kwargs

    @abstractmethod
    def do_model_predict(self, preprocessed_data: Any) -> Any:
        pass

    def do_preprocessing(self, input_data: dict[Any, Any]) -> Any:
        """
        Implement any preprocessing of the raw user input.
        For example, you may need to apply feature engineering
        on the input before it is suitable for model inference.

        Args:
            data (Union[dict[str]]): raw user input

        Returns:
            str: transformed input
        """
        return input_data

    @abstractmethod
    def do_postprocessing(self, output_data: Any) -> Union[str, dict[Any, Any]]:
        """
        Implement any postprocessing here. for ease of
        serving, we must return a dict or string.

        Args:
            output_data (Any):  raw output from model

        Returns:
            Union[str, dict]: output suitable for serving
        """

    def do_inference(self, input_data: Any) -> Union[str, dict[Any, Any]]:
        """
            Inference implementation. You should
            not need to change this function.
            Instead, subclass and implemement abstract methods

            Args:
                data (str): raw user input

        Returns:
            Any: result of inference
        """
        logging.info("preprocessing input_data %s", input_data)
        preprocessed_data = self.do_preprocessing(input_data)

        logging.info("querying model with %s", preprocessed_data)
        model_output = self.do_model_predict(preprocessed_data)

        logging.info("postprocessing model_output %s", model_output)
        return self.do_postprocessing(model_output)

    def do_generate_proof(self) -> Any:
        """
        raise error by default. Override in subclass if needed.
        """
        raise NotImplementedError
