"""
This module demonstrates how to leverage the
ML workflow class hiearchy. We define a workflow
class that leverages a TreeBasedClassifier sklearn
model to predict the tilt position of a balance.
The example shows how to extend a SklearnMLWorkflow,
as well as the EZKLProverMixin to simplify generating
EZKL based proofs.
"""
from __future__ import annotations

import json
import os
import tempfile
from typing import Optional

import mlflow  # type: ignore
import pandas as pd
import torch
import torch.jit
from pandas import DataFrame, Series
from sklearn.preprocessing import LabelEncoder  # type: ignore
from sklearn.tree import DecisionTreeClassifier  # type: ignore

import ezkl
from ml.utils import ezkl_utils
from ml.workflows.training.base_sklearn_training_workflow import (
    BaseSklearnTrainingWorkflow,
)

# if defined, we will upload to this model in hugging face
MODEL_NAME: Optional[str] = os.environ.get("EXAMPLE_MODEL_NAME", None)
RESULT_COLUMN_NAME: str = "tilt"

# declare columns to load
COLUMNS: list[str] = [
    RESULT_COLUMN_NAME,
    "l_weight",
    "l_distance",
    "r_weight",
    "r_distance",
]

# UCI balance scale weight and distance database -
# https://archive.ics.uci.edu/dataset/12/balance+scale
RAW_DATA_URI: str = os.path.join(ezkl_utils.DEFAULT_BASE_DIR, "uci.csv")


class BalanceClassifierEzklWorkflow(BaseSklearnTrainingWorkflow):
    """
    Workflow class example that predicts the tilt position
    of a balance, trained on UCI balance data.
    """

    def __init__(
        self, base_dir: str = ezkl_utils.DEFAULT_BASE_DIR, upload: bool = False
    ) -> None:
        super().__init__(
            ingest_files=[RAW_DATA_URI],  # URI to raw data file
            model_class=DecisionTreeClassifier,  # type of model
            model_params=dict(
                criterion="gini",
                max_depth=10,
            ),
            split_params=dict(
                test_size=0.3,  # required: size of test set
            ),
            cross_validator_param_grid={"criterion": ["gini", "entropy"]},
        )

        # base dir
        self.base_dir: str = base_dir

        # state needed for EZKLProverMixin
        self.ezkl_paths: ezkl_utils.EzklFilePaths = ezkl_utils.get_default_ezkl_paths(
            base_dir=base_dir
        )

        # whether or not we upload to huggingface when deploying
        self.upload: bool = upload

        # we use a label encoder to transform our Y data
        self.label_encoder: Optional[LabelEncoder] = None

        # we are using a wrapped sklearn2torch model for inference
        self.torch_model: Optional[torch.nn.Module] = None

        # state needed for EZKLProverMixin
        self.ezkl_setup: bool = False

    def do_transform(self, validated_data: list[DataFrame]) -> list[DataFrame]:
        """
        tranform the position data L, R, B
        (scale position: tipping left, tipping right, balanced)
        using our label encoder
        """
        transformed_data = validated_data[0].copy()
        self.label_encoder = LabelEncoder()
        transformed_data[RESULT_COLUMN_NAME] = self.label_encoder.fit_transform(
            transformed_data[RESULT_COLUMN_NAME]
        )

        return [transformed_data]

    def do_validate(self, raw_data: list[DataFrame]) -> list[DataFrame]:
        assert len(raw_data) == 1
        # Data has no columns
        return raw_data

    def do_feature_generation(self, transformed_data: list[DataFrame]) -> DataFrame:
        return transformed_data[0].drop(columns=RESULT_COLUMN_NAME)

    def do_label_generation(self, transformed_data: list[DataFrame]) -> Series[int]:
        return transformed_data[0][RESULT_COLUMN_NAME]

    def do_ingest(self) -> list[DataFrame]:
        """
        ingest the raw UCI data and log it
        """
        df = pd.read_csv(RAW_DATA_URI, names=COLUMNS, sep=",")
        if mlflow.active_run():
            mlflow.log_artifact(RAW_DATA_URI)

        return [df]

    def do_generate_proof(self) -> None:
        """
        call inherited helper fn to generate a proof. Note that
        though we use EZKL to perform ZK proofs, other workflows
        can implement other types of proving systems, such as
        Optimistic proofs.
        """

        # generate proof
        ezkl_utils.generate_proof(self.ezkl_paths)

        # verify proof
        assert ezkl_utils.verify_proof(self.ezkl_paths)

    def do_deploy(self) -> None:
        # NOTE: Undestand the implications of uploading prover files!
        # in particular, if you redeploy your prover files, you will
        # need to redeploy any corresponding on chain contract as well!

        if self.torch_model is None:
            # create the torch model
            sample_input = [[99, 2, 1, 4]]
            # sample_input = self.X_test[:1].values
            # convert to torch and generate onnx
            assert self.ezkl_paths.onnx_model_path
            torch_model = ezkl_utils.export_models(
                self.model,
                sample_input,
                self.ezkl_paths.onnx_model_path,
            )

            # save torch model to disk
            torch.jit.script(torch_model).save(  # type: ignore
                os.path.join(self.base_dir, "model.torch.jit")
            )

            model_path = os.path.join(self.base_dir, "model.torch")
            torch.save(torch_model, model_path)

        # do inference
        output = torch_model.predict(torch.tensor(sample_input))

        # generate witness data
        ezkl_utils.generate_witness_data(
            torch.tensor(sample_input), output, self.ezkl_paths
        )

        with tempfile.NamedTemporaryFile("w+", suffix=".json") as wf:
            cal_data = {
                "input_data": [
                    self.X_test.to_numpy().reshape(self.X_test.size).tolist()
                ],
            }
            json.dump(cal_data, wf)
            wf.flush()

            self.ezkl_paths.calibration_data_path = wf.name

            # generate and calibrate settings
            # (with witness data) + gen srs + circuit
            ezkl_utils.gen_and_calibrate_settings(self.ezkl_paths)

        assert self.ezkl_paths.data_path
        assert self.ezkl_paths.compiled_model_path
        assert self.ezkl_paths.witness_path
        assert self.ezkl_paths.onnx_model_path
        assert self.ezkl_paths.compiled_model_path
        assert self.ezkl_paths.settings_path
        assert self.ezkl_paths.srs_path

        # generate circuit

        res = ezkl.compile_circuit(  # type: ignore
            self.ezkl_paths.onnx_model_path,
            self.ezkl_paths.compiled_model_path,
            self.ezkl_paths.settings_path,
        )
        assert res is True, "unable to compile circuit"

        # generate srs
        res = ezkl.get_srs(  # type: ignore
            self.ezkl_paths.srs_path, self.ezkl_paths.settings_path
        )
        assert res is True, "unable to generate srs file"

        # generate witness
        ezkl_utils.generate_witness(
            self.ezkl_paths.data_path,
            self.ezkl_paths.compiled_model_path,
            self.ezkl_paths.witness_path,
        )

        # do setup
        ezkl_utils.setup(self.ezkl_paths)

        self.generate_proof()

        if self.upload and MODEL_NAME:
            ezkl_utils.upload_prover_files_hf(
                MODEL_NAME, self.ezkl_paths, model_path=model_path
            )

        ezkl_utils.generate_verifier(self.ezkl_paths, deploy=False)

        # TODO: handle DA generation
