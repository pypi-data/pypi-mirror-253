"""
Base Workflow Driver. Organizes workflow runs
into experiments based on the class by default.
"""

from typing import Optional

import mlflow  # type: ignore

from ml.workflows.training.base_training_workflow import BaseTrainingWorkflow


class BaseTrainingDriver:
    """Simple base driver that makes sure that runs are
    associated with an experiment.
    """

    def __init__(
        self,
        workflow: BaseTrainingWorkflow,
        experiment: Optional[str] = None,
        run_tags: Optional[dict[str, str]] = None,
    ) -> None:
        """constructor.

        Args:
            workflow (BaseMLWorkflow): workflow associated with this driver
            run_tags (dict[str, str], optional): any tagging you want
             with this run
        """
        self.workflow: BaseTrainingWorkflow = workflow
        self.tags: Optional[dict[str, str]] = run_tags
        self.experiment: Optional[str] = experiment

    def run(self) -> None:
        if not self.experiment:
            experiment = mlflow.set_experiment(self.__class__.__name__)
        else:
            experiment = mlflow.set_experiment(self.experiment)

        with mlflow.start_run(experiment_id=experiment.experiment_id):
            if self.tags:
                mlflow.set_tags(self.tags)
            self.do_run()

    def do_run(self) -> None:
        pass
