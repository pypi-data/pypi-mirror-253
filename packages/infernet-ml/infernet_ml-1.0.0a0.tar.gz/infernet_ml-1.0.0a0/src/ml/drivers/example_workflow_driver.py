"""
Example Workflow implementation
"""
import logging
import typing

from ml.drivers.base_driver import BaseTrainingDriver
from ml.workflows.training.example_workflow import BalanceClassifierEzklWorkflow


class ExampleWorkflowDriver(BaseTrainingDriver):
    """
    This module demonstrates a simple example driver of the
    example BalanceClassifierEzklWorkflow object defined at
    example_workflow.py. As part of setting up the worflow,
    the driver goes through a simple ETL pipeline of extracting
    and transforming raw data for training, trains the result,
    generates an inference, than verifies the result offchain.
    """

    def __init__(self) -> None:
        super().__init__(BalanceClassifierEzklWorkflow())

    def do_run(self) -> None:
        # setup workflow
        self.workflow.setup()

        # generate inference
        input_list = (
            typing.cast(BalanceClassifierEzklWorkflow, self.workflow).X_test[:1].values
        )
        output = self.workflow.inference(input_list)

        logging.info("Inference Results for input: %s output: %s", input_list, output)

        # score
        self.workflow.scoring()

        # call deploy
        self.workflow.deploy()


if __name__ == "__main__":
    ExampleWorkflowDriver().run()
