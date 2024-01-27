"""
Workflow class for classical ML.
"""
import abc
import logging
from typing import Any

from ml.workflows.training.base_training_workflow import BaseTrainingWorkflow

logger: logging.Logger = logging.getLogger(__name__)


class BaseClassicTrainingWorkflow(BaseTrainingWorkflow):
    """
    Base class for a classical machine learning workflow.
    Declares several abstract functions generally
    relevant in MLOps / ML Engineering.
    """

    def __init__(self, *args: list[Any], **kwargs: dict[Any, Any]) -> None:
        super().__init__(*args, **kwargs)

        # should be set after raw data is ingested
        self.raw_data: Any = None

        # should be set after data is ingested
        self.validated_data: Any = None

        # should be set after raw data is transformed
        self.transformed_data: Any = None

        # training feature data
        self.X_train: Any = None

        # testing feature data
        self.X_test: Any = None

        # training label data
        self.y_train: Any = None

        # testing label data
        self.y_test: Any = None

        # should be set after model is instantiated and trained
        self.model: Any = None

    def do_setup(self) -> None:
        # Extract
        logger.info("setup: ingesting")
        raw_data = self.do_ingest()

        # validate
        logger.info("setup: validating")
        validated_data = self.do_validate(raw_data)

        # Transform
        logger.info("setup: transforming")
        transformed_data = self.do_transform(validated_data)

        # Load
        logger.info("setup: splitting")
        self.X_train, self.X_test, self.y_train, self.y_test = self.split(
            transformed_data
        )

        # train
        logger.info("setup: training")
        self.model = self.do_train(self.X_train, self.y_train)

    @abc.abstractmethod
    def do_feature_generation(self, transformed_data: Any) -> Any:
        """
        Should perform feature generation here.
        Args:
            transformed_data (Any): loaded data

        Returns:
            Any: features, including newly generated
        """

    @abc.abstractmethod
    def do_label_generation(self, transformed_data: Any) -> Any:
        """
        Should perform label generation here.

        Args:
            tranformed_data (Any): loaded data

        Returns:
            Any: labels, including newly generated
        """

    def do_feature_engineering(self, features: Any) -> Any:
        """Should perform feature engineering here. Feature engineering
        is is the process of selecting, extracting, and transforming
         the most relevant features from the available data.

        Args:
            transformed_data (Any): loaded data

        Returns:
            Any: loaded data engineered to include relevant features
        """
        return features

    def do_label_engineering(self, labels: Any) -> Any:
        """_summary_

        Args:
            transformed_data (Any): _description_

        Returns:
            Any: _description_
        """
        return labels

    def split(self, transformed_data: Any) -> Any:
        """wrapper for split step

        Args:
            transformed_data (Any): data to be split

        Returns:
            Any: split data
        """

        logger.info("Split: engineering features")
        features = self.do_feature_generation(transformed_data)
        features = self.do_feature_engineering(features)

        logger.info("Split: engineering labels")
        labels = self.do_label_generation(transformed_data)
        labels = self.do_label_engineering(labels)

        return self.do_split(features, labels)

    @abc.abstractmethod
    def do_split(self, features: Any, labels: Any) -> Any:
        """Should perform train / test split here for the purposes
        of model selection / validation
        Args:
            transformed_data (Any): data to be split

        Returns:
            Any: split data
        """

    @abc.abstractmethod
    def do_train(self, X_train: Any, y_train: Any) -> Any:
        """Should train and perform model selection / validation here.
              The output should be the trained model.

        Args:
            split_data (List[Any]): split data as a list

        Returns:
            Any: trained model
        """

    @abc.abstractmethod
    def do_ingest(self) -> Any:
        """
            Should implmement ingestion of raw data into a target tensor type.
            The file format of the data is not assumed.

        Returns:
            Any: data in a form suitable for transformation / loading
        """

    @abc.abstractmethod
    def do_validate(self, raw_data: Any) -> Any:
        """Should implement validaton

        Args:
            raw_data (Any): data to be validated

        Returns:
            Any: validated data
        """

    @abc.abstractmethod
    def do_transform(self, validated_data: Any) -> Any:
        """Should implement transformation

        Args:
            validated_data (Any): data to be transformed

        Returns:
            Any: transformed data
        """
