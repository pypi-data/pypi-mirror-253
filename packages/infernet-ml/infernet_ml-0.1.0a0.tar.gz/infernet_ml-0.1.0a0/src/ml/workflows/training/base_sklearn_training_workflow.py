"""
workflow base class for sklearn model workflows.
"""
import logging
import pathlib
from collections.abc import Collection
from typing import Any

import mlflow  # type: ignore
import numpy as np
import pandas as pd
from ml.workflows.training.base_classic_training_workflow import (
    BaseClassicTrainingWorkflow,
)
from pandas import DataFrame
from sklearn.base import BaseEstimator  # type: ignore
from sklearn.metrics import accuracy_score  # type: ignore
from sklearn.model_selection import GridSearchCV, train_test_split  # type: ignore

logger: logging.Logger = logging.getLogger(__name__)


class BaseSklearnTrainingWorkflow(BaseClassicTrainingWorkflow):
    """
    Workflow for ScikitLearn models.
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        construcutor.
        subclasses should call this with
        kwargs model_class and model_params set -
        the appropriate model will be instantiated
        as part of training (see do_train)

        Raises:
            ValueError: _description_
        """
        super().__init__(*args, **kwargs)

        # check model params specified
        _ = self.kwargs["model_class"]
        _ = self.kwargs["model_params"]

        # keep track of scoring results
        self.y_predict = None

        # check ingest files specified
        if (type(self).do_ingest == BaseSklearnTrainingWorkflow.do_ingest) and (
            "ingest_files" not in kwargs
        ):
            raise ValueError("missing value for named parameter ingest_files.")

    def do_train(self, X_train: DataFrame, y_train: DataFrame) -> BaseEstimator:
        """implements training. Creates an instance of the SKLearn model,
        fits it with the training data, optionally performing cross validation
        of cross_validator_param_grid was provided as a kwarg.

        Returns:
            BaseEstimator: initialzed and trained model
        """
        # create instance of model

        model_class = self.kwargs["model_class"]
        model_params = self.kwargs["model_params"]
        model = model_class()

        # update hyperparams
        model.set_params(**model_params)

        if "cross_validator_param_grid" in self.kwargs:
            logger.info("applying cross validation")
            cv_params = self.kwargs.get("cv_params", {})
            # apply cross validation
            cv = GridSearchCV(
                model, self.kwargs["cross_validator_param_grid"], **cv_params
            )
            cv.fit(X_train, y_train)
            model = cv.best_estimator_
        else:
            # fit model with training data
            model.fit(X_train, y_train)

        if mlflow.active_run():
            # log model. We are forced to log here rather than base class
            # because MLFlow model logging is framework specific
            mlflow.sklearn.log_model(model, "model", input_example=X_train)

        return model

    def do_ingest(self) -> list[DataFrame]:
        """
            Should implmement ingestion of raw data into a dataframe/tensor type.
            The file format of the data is not assumed.

        Returns:
            Any: data in a form suitable for transformation / loading
        """
        raw_data = []
        for filename in self.kwargs["ingest_files"]:
            if pathlib.Path(filename).suffix == ".csv":
                if mlflow.active_run():
                    mlflow.log_artifact(filename)
                raw_data.append(pd.read_csv(filename))
            else:
                raise ValueError(f"file format unsupported: {filename}")

        return raw_data

    def do_inference(self, input_data: np.ndarray[Any, Any]) -> Any:
        """inference implementation. simply calls predict on the model.

        Args:
            input_data (np.ndarray[Any, Any]): input data to the model

        Returns:
            Any: result of model output
        """
        return self.model.predict(input_data)

    def do_validate(self, raw_data: list[DataFrame]) -> list[DataFrame]:
        """
        validate implementation by default does nothing. Subclass
        and override as needed.

        Args:
            raw_data (list[DataFrame]): data to validate

        Returns:
            list[DataFrame]: validated data
        """
        return raw_data

    def do_transform(self, validated_data: list[DataFrame]) -> list[DataFrame]:
        """
        transform data by default does noting.
        Subclass and override as needed.

        Args:
            validated_data (list[DataFrame]): data to transform

        Returns:
            list[DataFrame]: transormed data
        """
        return validated_data

    def do_scoring(self) -> dict[str, float]:
        """
        perform scoring. by default, only accuracy is captured.
        override as needed.

        Returns:
            dict[str, float]: dict containing
            accuracy key and accuracy value
        """
        # perform prediction and capture perf metrics
        self.y_predict = self.model.predict(self.X_test)

        # log accuracy
        accuracy = accuracy_score(self.y_test, self.y_predict)

        logger.info("model accuracy (test_data): %s", accuracy)

        return {"accuracy": accuracy}

    def do_split(self, features: Collection[Any], labels: Collection[Any]) -> Any:
        """
        split features and labels into training and test data.
        uses train_test_split from sklearn library.

        Args:
            features (Collection[Any]): feature data
            labels (Collection[Any]): label data

        Returns:
            Any: split feature and label data
        """
        assert len(features) == len(
            labels
        ), f"features and y len different: features len {len(features)} labels len {len(labels)}"  # noqa: E501

        #  flip Y data to a row as is convention
        args = self.kwargs.get("split_args", {})
        return train_test_split(features, labels, **args)
