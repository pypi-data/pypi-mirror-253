"""
simple test for a BaseMLWorkFlow
"""
import logging
import typing

import pytest

from ml.workflows.training.base_training_workflow import BaseTrainingWorkflow


class DummyWorkflow(BaseTrainingWorkflow):
    """dummy workflow"""

    def do_setup(self) -> typing.Optional[dict[str, str]]:
        print("setup")
        return None

    def do_inference(self, input_data: typing.Any) -> typing.Any:
        print("inference")
        return None

    def do_generate_proof(self) -> typing.Any:
        print("generate_proof")
        return None

    def do_scoring(self) -> typing.Any:
        return {}


@pytest.fixture
def dummy_workflow():  # type: ignore
    return DummyWorkflow()


def test_setup_enforced(dummy_workflow) -> None:  # type: ignore
    with pytest.raises(ValueError) as exinfo:
        dummy_workflow.inference("test")
    assert str(exinfo.value) == "setup not called before inference"


# to test logging
LOGGER = logging.getLogger(BaseTrainingWorkflow.__name__)
LOGGER.propagate = True


def test_no_inference_warning(dummy_workflow, caplog) -> None:  # type: ignore
    dummy_workflow.setup()
    caplog.set_level(logging.WARNING)
    dummy_workflow.generate_proof()
    assert "but attempting to generate proof" in caplog.text
