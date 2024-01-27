"""
workflow  class for torch inference workflows.
"""
import logging
import os
from typing import Any, Optional, Union

import torch
import torch.jit
from huggingface_hub import hf_hub_download  # type: ignore
from ml.utils.ezkl_utils import generate_witness_data
from ml.workflows.inference.base_classic_inference_workflow import (
    BaseClassicInferenceWorkflow,
)

logger: logging.Logger = logging.getLogger(__name__)

MODEL_FILE_NAME = os.getenv("TORCH_MODEL_FILE_NAME", "model.torch")

# whether or not to use torch script
USE_JIT = os.getenv("USE_JIT", "False").lower() in ("true", "1", "t")

# dtypes we support for conversion to corresponding torch types.
DTYPES = {
    "float": torch.float,
    "double": torch.double,
    "cfloat": torch.cfloat,
    "cdouble": torch.cdouble,
    "half": torch.half,
    "bfloat16": torch.bfloat16,
    "uint8": torch.uint8,
    "int8": torch.int8,
    "short": torch.short,
    "int": torch.int,
    "long": torch.long,
    "bool": torch.bool,
}


class TorchInferenceWorkflow(BaseClassicInferenceWorkflow):
    """
    Inference workflow for Torch based models.
    models are loaded using the default torch pickling by default
    (i.e. torch.load). This can be changed to use torch script
    (torch.jit) if the USE_JIT environment variable is enabled.
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.model: Optional[torch.nn.Module] = None

    def do_setup(self) -> Any:
        """set up here (if applicable)."""
        return self.load_model()

    def load_model(self) -> bool:
        """loads the model. if called
        will attempt to download latest version
        of model.

        Returns:
            bool: True on completion of loading model
        """
        # look up repo to download from
        repo_id: str = self.kwargs["model_name"]

        logger.info("Loading torch model from HF repo %s", repo_id)

        # download model
        model_path: str = hf_hub_download(repo_id, MODEL_FILE_NAME)

        self.model = torch.jit.load(model_path) if USE_JIT else torch.load(model_path)  # type: ignore  # noqa: E501

        # turn on inference mode
        self.model.eval()  # type: ignore

        logging.info("model loaded")

        return True

    def do_preprocessing(self, input_data: dict[str, Any]) -> torch.Tensor:
        # lookup dtype from str
        dtype = DTYPES.get(input_data["dtype"], None)
        values = input_data["values"]
        return torch.tensor(values, dtype=dtype)

    def do_model_predict(
        self, preprocessed_data: torch.Tensor
    ) -> tuple[torch.Tensor, torch.Tensor]:
        model_result = self.model.predict(preprocessed_data)  # type: ignore
        return preprocessed_data, model_result

    def do_postprocessing(
        self, output_data: tuple[torch.Tensor, torch.Tensor]
    ) -> Union[str, dict[str, Any]]:
        torch_input, torch_output = output_data
        # Format data for EZKL Proof processing
        return generate_witness_data(torch_input, torch_output, None)
