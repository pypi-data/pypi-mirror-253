"""
Utility functions implementing EZKL proving and verification
"""
import asyncio
import json
import logging
import os
import typing
from dataclasses import dataclass
from typing import Any, Optional, Tuple

import mlflow  # type: ignore
import sk2torch  # type: ignore
import torch
from huggingface_hub import HfApi, hf_hub_download  # type: ignore
from numpy.typing import ArrayLike
from sklearn.base import BaseEstimator  # type: ignore

import ezkl

DTYPES: dict[str, torch.dtype] = {
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

PROVING_FILENAMES: list[str] = [
    "network.compiled",
    "settings.json",
    "proving.key",
    "verifying.key",
    "kzg.srs",
]

# default base directory is the parent ml directory
DEFAULT_BASE_DIR: str = f"{os.path.dirname(os.path.abspath(__file__))}/../../data/"

# path for onnx model
ONNX_MODEL_PATH: str = "network.onnx"

# path for compiled ezkl circuit
COMPILED_MODEL_PATH: str = "network.compiled"

# path for ezkl proving key
PK_PATH: str = "proving.key"

# path for ezkl verification key
VK_PATH: str = "verifying.key"

# path for ezkl settings
SETTINGS_PATH: str = "settings.json"

# path for ezkl srs string
SRS_PATH: str = "kzg.srs"

# path for ezkl witness file
WITNESS_PATH: str = "witness.json"

# path for ezkl model inputs
DATA_PATH: str = "input.json"

# path for ezkl generated proof
PROOF_PATH: str = "test_proof.pf"

# path for ezkl generated verifier sol code path
VF_SOL_CODE_PATH: str = "verifier.sol"

# path for ezkl generated verifier abi path
VF_ABI_PATH: str = "verifier.abi"

# path for ezkl generated da sol code path
DA_SOL_CODE_PATH: str = "data_attester.sol"

# path for ezkl generated data attester abi path
DA_ABI_PATH: str = "data_attester.abi"

# path for ezkl generated verifier address file
VF_ADDR_PATH: str = "verifier_addr.txt"

# path for ezkl generated verifier address file
DA_ADDR_PATH: str = "da_addr.txt"

# url to on chain RPC host (assuming local node)
RPC_URL: str = "http://localhost:3030"


@dataclass
class EzklFilePaths:
    """
    Dataclass containing file path settings related to EZKL
    """

    # location of onnx model to be generated
    onnx_model_path: Optional[str]
    # input data (note that onchain data vs.
    # offchain data schema is not the same)
    data_path: Optional[str]
    # location of the calibration data
    calibration_data_path: Optional[str]
    # location of the proof
    proof_path: Optional[str]
    # location of the witness generation data
    witness_path: Optional[str]
    # location of the compiled circuit
    compiled_model_path: Optional[str]
    # location of the proving key
    pk_path: Optional[str]
    # location of the verification key
    vk_path: Optional[str]
    # location of the srs
    srs_path: Optional[str]
    # location of the EZKL setup settings
    settings_path: Optional[str]
    # location of generated verifier solidity code
    vf_sol_code_path: Optional[str]
    # location of generated verifier abi
    vf_abi_path: Optional[str]
    # location of txt file containing verifier on chain address
    vf_addr_path: Optional[str]
    # location of generated data attester solidity code
    da_sol_code_path: Optional[str]
    # location of generated data attester abi
    da_abi_path: Optional[str]
    # location of txt file containing data attester on chain address
    da_addr_path: Optional[str]
    # url of the on chain RPC node
    rpc_url: Optional[str]


def get_default_ezkl_paths(base_dir: str = DEFAULT_BASE_DIR) -> EzklFilePaths:
    """
    Helper function to get the default ezkl paths.
    """
    return EzklFilePaths(
        os.path.join(base_dir, ONNX_MODEL_PATH),
        os.path.join(base_dir, DATA_PATH),
        None,  # calibration data will be defaulted if not specified
        os.path.join(base_dir, PROOF_PATH),
        os.path.join(base_dir, WITNESS_PATH),
        os.path.join(base_dir, COMPILED_MODEL_PATH),
        os.path.join(base_dir, PK_PATH),
        os.path.join(base_dir, VK_PATH),
        os.path.join(base_dir, SRS_PATH),
        os.path.join(base_dir, SETTINGS_PATH),
        os.path.join(base_dir, VF_SOL_CODE_PATH),
        os.path.join(base_dir, VF_ABI_PATH),
        os.path.join(base_dir, VF_ADDR_PATH),
        os.path.join(base_dir, DA_SOL_CODE_PATH),
        os.path.join(base_dir, DA_ABI_PATH),
        os.path.join(base_dir, DA_ADDR_PATH),
        RPC_URL,
    )


def generate_witness(
    data_path: str,
    compiled_model_path: str,
    witness_path: str,
    input_visibility: str = "hashed",
    params_visibility: str = "private",
    output_visibility: str = "public",
) -> Tuple[
    dict[str, Any], Optional[list[str]], Optional[list[str]], Optional[list[str]]
]:
    """helper function that wraps the built in ezkl gen_witness file to
    return the processed or encrypted inputs as well as the witness circuit itself.

    Args:
        data_path (str): where the data used to generate the witness is generated
        compiled_model_path (str): where the model is located
        witness_path (str): where the witness will be stored on disk
        input_visibility (str, optional): Defaults to "hashed".
        params_visibility (str, optional): Defaults to "private".
        output_visibility (str, optional): Defaults to "public".

    Returns:
        Tuple[
            dict[str, Any],
            Optional[list[str]],
            Optional[list[str]],
            Optional[list[str]]
        ]: A tuple of the witness, followed by a list of the processed_inputs as a
        field element for the model input, model params, and model output.
    """
    ip: Optional[list[str]] = None
    mp: Optional[list[str]] = None
    op: Optional[list[str]] = None

    # generate the witness based on the data and settings
    ezkl.gen_witness(data_path, compiled_model_path, witness_path)  # type: ignore

    with open(witness_path, "r", encoding="utf-8") as wp:
        res = json.load(wp)
        logging.info("witness circuit results: %s", res)

        if input_visibility.lower() == "hashed":
            ip = [
                ezkl.vecu64_to_felt(vecu64)  # type: ignore
                for vecu64 in res["processed_inputs"]["poseidon_hash"]
            ]
        elif input_visibility.lower() == "encrypted":
            ip = [
                ezkl.vecu64_to_felt(vecu64)  # type: ignore
                for vecu64 in res["processed_inputs"]["ciphertexts"]
            ]

        if output_visibility.lower() == "hashed":
            op = [
                ezkl.vecu64_to_felt(vecu64)  # type: ignore
                for vecu64 in res["processed_outputs"]["poseidon_hash"]
            ]
        elif output_visibility.lower() == "encrypted":
            op = [
                ezkl.vecu64_to_felt(vecu64)  # type: ignore
                for vecu64 in res["processed_outputs"]["ciphertexts"]
            ]

        if params_visibility.lower() == "hashed":
            mp = [
                ezkl.vecu64_to_felt(vecu64)  # type: ignore
                for vecu64 in res["processed_params"]["poseidon_hash"]
            ]
        elif params_visibility.lower() == "encrypted":
            mp = [
                ezkl.vecu64_to_felt(vecu64)  # type: ignore
                for vecu64 in res["processed_params"]["ciphertexts"]
            ]

        return res, ip, mp, op


def generate_witness_data(
    torch_input: torch.Tensor,
    torch_output: torch.Tensor,
    config_paths: Optional[EzklFilePaths],
) -> dict[str, list[Any]]:
    """
    Helper to generate data json for ezkl witness generation.
    Requires input and output tensors from a torch model.
    if a data_path is provided, will export the json file to the location.

    Returns:
       typing.Dict[str, list]: dict representing witness data
    """
    # format input for ezkl
    input_data = [((torch_input).detach().numpy()).reshape([-1]).tolist()]

    # format output for ezkl
    output_data = [((o).detach().numpy()).reshape([-1]).tolist() for o in torch_output]

    logging.info(
        "generate_witness_data: input_data %s output_data %s", input_data, output_data
    )
    # create json for ezkl
    data = dict(
        input_shapes=[tuple(list(torch_input.shape)[1:])],
        input_data=input_data,
        output_data=output_data,
    )
    # write the witness data to disk
    if config_paths and config_paths.data_path:
        json.dump(data, open(config_paths.data_path, "w", encoding="utf-8"))

    if mlflow.active_run() and config_paths and config_paths.data_path:
        mlflow.log_artifact(config_paths.data_path)

    return data


def gen_and_calibrate_settings(
    config_paths: EzklFilePaths,
    input_visibility: str = "hashed",
    param_visibility: str = "private",
    output_visibility: str = "public",
) -> None:
    """
    helper function that wraps ezkl settings calibration and generation.
    if calibration data path is set, uses the referenced file to calibrate.
    otherwise uses the data path.


    Args:
        config_paths (EzklFilePaths):  Most relevant are
        calibration_data_path, data_path, onnx_model_path, and settings_path
        input_visibility (str, optional): Defaults to "hashed".
        param_visibility (str, optional): Defaults to "private".
        output_visibility (str, optional): Defaults to "public".
    """
    assert config_paths.onnx_model_path and os.path.isfile(
        config_paths.onnx_model_path
    ), f"no onnx model file found at {config_paths.onnx_model_path}. Did you generate an onnx model?"  # noqa: E501

    # default calibration to data path if not specified
    calibrate_path = (
        config_paths.data_path
        if not config_paths.calibration_data_path
        else config_paths.calibration_data_path
    )

    # by default make everything public for now. Note that changing this may
    # cause an impact to proving speed.

    run_args = ezkl.PyRunArgs()  # type: ignore
    run_args.input_visibility = input_visibility
    run_args.param_visibility = param_visibility
    run_args.output_visibility = output_visibility

    # TODO: consider exposing more run_arg parameters (for example, batch_size)

    # generate settings file
    res = ezkl.gen_settings(  # type: ignore
        config_paths.onnx_model_path, config_paths.settings_path, py_run_args=run_args
    )
    assert res is True, "unable to generate settings"

    # calibrate settings based on model and data
    async def calibrate() -> None:
        # calibration is very verbose - lets increase log level temporarily
        logging_level = logging.getLogger().level
        logging.getLogger().setLevel(logging.ERROR)
        res = await ezkl.calibrate_settings(  # type: ignore
            calibrate_path,
            config_paths.onnx_model_path,
            config_paths.settings_path,
            "resources",
        )
        logging.getLogger().setLevel(logging_level)
        assert res is True, "unable to calibrate settings"

    logging.info("calibrating model (this takes a while - grab some coffee ☕)")
    asyncio.run(calibrate())
    logging.info("done calibrating model")
    if config_paths.calibration_data_path:
        mlflow.log_artifact(config_paths.calibration_data_path)


def setup(config_paths: EzklFilePaths) -> None:
    """
    wraps the ezkl setup function. logs artifacts if ML Flow is active.
    Args:
        config_paths (EzklFilePaths): ezkl paths
    """
    res = ezkl.setup(  # type: ignore
        config_paths.compiled_model_path,
        config_paths.vk_path,
        config_paths.pk_path,
        config_paths.srs_path,
    )
    assert res is True, "unable to perform setup"

    if mlflow.active_run():
        output_dict = {}
        if config_paths.srs_path:
            output_dict["srs_path"] = os.path.basename(config_paths.srs_path)
            mlflow.log_artifact(config_paths.srs_path)
        if config_paths.settings_path:
            output_dict["settings_path"] = os.path.basename(config_paths.settings_path)
            mlflow.log_artifact(config_paths.settings_path)
        if config_paths.compiled_model_path:
            output_dict["compiled_model_path"] = os.path.basename(
                config_paths.compiled_model_path
            )
            mlflow.log_artifact(config_paths.compiled_model_path)
        if config_paths.vk_path:
            output_dict["vk_path"] = os.path.basename(config_paths.vk_path)
            mlflow.log_artifact(config_paths.vk_path)
        if config_paths.pk_path:
            output_dict["pk_path"] = os.path.basename(config_paths.pk_path)
            mlflow.log_artifact(config_paths.pk_path)

        # we keep track of the file name mappings:
        # These is so we can lookup the right artifact
        # easily in mlflow (e.g. for generating proofs)

        mlflow.log_dict(
            output_dict,
            "setup_output.json",
        )


def generate_proof(config_paths: EzklFilePaths) -> None:
    """Generate EZKL based proof.
    Do this after model exporting and setup.

    Args:
        config_paths (EzklFilePaths): ezkl paths
    """

    assert config_paths.compiled_model_path and os.path.isfile(
        config_paths.compiled_model_path
    ), "compiled_model_path file not found"
    assert config_paths.pk_path and os.path.isfile(
        config_paths.pk_path
    ), "pk_path file not found"
    assert config_paths.srs_path and os.path.isfile(
        config_paths.srs_path
    ), "srs_path file not found"
    assert config_paths.settings_path and os.path.isfile(
        config_paths.settings_path
    ), "settings_path file not found"

    assert config_paths.witness_path and os.path.isfile(
        config_paths.witness_path
    ), "witness file not generated"

    res = ezkl.prove(  # type: ignore
        config_paths.witness_path,
        config_paths.compiled_model_path,
        config_paths.pk_path,
        config_paths.proof_path,
        config_paths.srs_path,
        "single",
    )

    assert config_paths.proof_path and os.path.isfile(
        config_paths.proof_path
    ), "proof file not generated"
    assert res is not None, "proof generation failed"

    if mlflow.active_run():
        mlflow.log_artifact(config_paths.witness_path)
        mlflow.log_artifact(config_paths.proof_path)


def verify_proof(config_paths: EzklFilePaths) -> bool:
    """
    wrapper function for offchain verification of proof
    that returns the result of the verification.


    Args:
        config_paths (EzklFilePaths): ezkl paths

    Returns:
        bool: result of verification
    """

    assert config_paths.proof_path and os.path.isfile(
        config_paths.proof_path
    ), "proof_path file not found"
    assert config_paths.settings_path and os.path.isfile(
        config_paths.settings_path
    ), "settings_path file not found"
    assert config_paths.vk_path and os.path.isfile(
        config_paths.vk_path
    ), "vk_path file not found"
    assert config_paths.srs_path and os.path.isfile(
        config_paths.srs_path
    ), "srs_path file not found"

    res = ezkl.verify(  # type: ignore
        config_paths.proof_path,
        config_paths.settings_path,
        config_paths.vk_path,
        config_paths.srs_path,
    )

    return bool(res)


def export_models(
    sklearn_model: BaseEstimator,
    sample_input: ArrayLike,
    onnx_model_path: str,
) -> torch.nn.Module:
    """
    sklearn models are difficult to deal with when it comes
    to conversion to onnx. This function converts an sklearn
    model to a PyTorch one, and exports a corresponding
    onnx model to the provided path.

    Returns the converted torch model for prediction and
    witness data generation
    """

    # create torch model from sklearn model
    torch_model: torch.nn.Module = sk2torch.wrap(sklearn_model)

    # generate torch input
    torch_input = torch.tensor(sample_input)
    logging.info("torch_input: %s", torch_input)
    # Export the model. May create a user warning but generally fine
    torch.onnx.export(
        torch_model,
        torch_input,
        onnx_model_path,
        export_params=True,  # store the trained parameter weights inside the model file
        opset_version=10,  # the ONNX version to export the model to
        do_constant_folding=True,  # whether constant folding for optimization
        input_names=["input"],  # the model's input names
        output_names=["output"],  # the model's output names
        dynamic_axes={
            "input": {0: "batch_size"},  # variable length axes
            "output": {0: "batch_size"},
        },
    )

    return torch_model


def count_decimal_places(num_str: str) -> int:
    """
    This function counts the decimal places of a floating
    point number str

    Args:
        num_str (str): numeric float str

    Returns:
        int: number of decimal places
    """
    return max(0, num_str[::-1].find("."))


def generate_verifier(
    config_paths: EzklFilePaths,
    deploy: bool = True,
) -> None:
    """wrapper for create_evm_verifier and deployment.

    Note if deploying, a RPC URL must be specified as part of the config paths.

    Args:
        config_paths (EzklFilePaths): ezkl paths
        deploy (bool, optional): whether or not to deploy the generated verifier.
         Defaults to True.
    """
    assert config_paths.vk_path is not None, "vk path not specified"
    assert config_paths.srs_path is not None, "srs path not specified"
    assert config_paths.settings_path is not None, "settings path not specified"
    assert config_paths.vf_sol_code_path is not None, "vf sol code path not specified"
    assert config_paths.vf_abi_path is not None, "vf abi path not specified"

    res = ezkl.create_evm_verifier(  # type: ignore
        config_paths.vk_path,
        config_paths.srs_path,
        config_paths.settings_path,
        config_paths.vf_sol_code_path,
        config_paths.vf_abi_path,
    )

    assert res is True, "failed to create evm verifier"

    assert config_paths.vf_addr_path is not None, "vf address path not specified"
    assert config_paths.rpc_url is not None, "rpc url not specified"

    if deploy:
        res = ezkl.deploy_evm(  # type: ignore
            config_paths.vf_addr_path,
            config_paths.vf_sol_code_path,
            config_paths.rpc_url,
        )

        assert res is True, "failed to deploy Verifier EVM"

        if mlflow.active_run():
            # log address from deployment
            mlflow.log_artifact(config_paths.vf_addr_path)
            # log artifacts generated from creation
            mlflow.log_artifact(config_paths.vf_sol_code_path)
            mlflow.log_artifact(config_paths.vf_abi_path)

            # keep track of filename mapping so we can use later via mlflow
            # (e.g) for doing on chain verification
            mlflow.log_dict(
                {
                    "vf_addr_path": os.path.basename(config_paths.vf_addr_path),
                    "vf_sol_code_path": os.path.basename(config_paths.vf_sol_code_path),
                    "vf_abi_path": os.path.basename(config_paths.vf_abi_path),
                    "rpc_url": config_paths.rpc_url,
                },
                "gen_verifier_output.json",
            )


def generate_da_attester(
    config_paths: EzklFilePaths,
    deploy: bool = True,
) -> None:
    """wrapper for create_evm_data_attestation and deployment.

    Note if deploying, a RPC URL must be specified as part of the config paths.

    Args:
        config_paths (EzklFilePaths): ezkl paths
        deploy (bool, optional): whether or not to deploy the generated data
        attester. Defaults to True.
    """
    assert config_paths.vk_path is not None, "vk path not specified"
    assert config_paths.srs_path is not None, "srs path not specified"
    assert config_paths.settings_path is not None, "settings path not specified"
    assert config_paths.da_abi_path is not None, "da abi path not specified"
    assert config_paths.da_sol_code_path is not None, "da sol code path not specified"
    assert config_paths.data_path is not None, "input data path not specified"

    res = ezkl.create_evm_data_attestation(  # type: ignore
        config_paths.vk_path,
        config_paths.srs_path,
        config_paths.settings_path,
        config_paths.da_sol_code_path,
        config_paths.da_abi_path,
        config_paths.data_path,
    )
    assert res, "DA: failed to create evm data attestation verifier"

    if deploy:
        res = ezkl.deploy_da_evm(  # type: ignore
            config_paths.da_addr_path,
            config_paths.data_path,
            config_paths.settings_path,
            config_paths.da_sol_code_path,
            config_paths.rpc_url,
        )

        assert res, "DA: deploying the attesting verifier failed"

        if mlflow.active_run():
            # log artifacts generated from creation
            mlflow.log_artifact(config_paths.da_sol_code_path)
            mlflow.log_artifact(config_paths.da_abi_path)
            mlflow.log_artifact(config_paths.da_addr_path)

            mlflow.log_dict(
                {
                    "da_addr_path": os.path.basename(config_paths.da_addr_path),  # type: ignore   # noqa: E501
                    "da_sol_code_path": os.path.basename(config_paths.da_sol_code_path),
                    "da_abi_path": os.path.basename(config_paths.da_abi_path),
                    "rpc_url": config_paths.rpc_url,
                },
                "gen_verifier_output.json",
            )


def verify_onchain_proof(config_paths: EzklFilePaths) -> bool:
    """
    assuming an onchain verifier is deployed, verifies the proof.
    if using a DA verifier, set attestation to True.
    you will need solc installed in your environment to run this.
    Args:
        config_paths (EzklFilePaths): paths related to ezkl proof generation
    Returns:
        bool: result of proof
    """
    assert config_paths.proof_path and os.path.isfile(
        config_paths.proof_path
    ), f"no proof file found at {config_paths.proof_path}. Did you generate a proof?"  # noqa: E501

    assert config_paths.vf_addr_path and os.path.isfile(
        config_paths.vf_addr_path
    ), f"no address file at {config_paths.vf_addr_path} for verifier. Did you create one?"  # noqa: E501

    assert config_paths.rpc_url is not None, "no rpc url specified"

    addr_verifier = None
    addr_data_attester = None
    if config_paths.vf_addr_path:
        with open(config_paths.vf_addr_path, "r", encoding="utf-8") as f:
            addr_verifier = f.read()

    if config_paths.da_addr_path:
        assert os.path.isfile(
            config_paths.da_addr_path
        ), f"no address file at {config_paths.da_addr_path} for data attester. Did you create one?"  # noqa: E501

        with open(config_paths.da_addr_path, "r", encoding="utf-8") as f:
            addr_data_attester = f.read()

    return ezkl.verify_evm(  # type: ignore
        config_paths.proof_path, addr_verifier, config_paths.rpc_url, addr_data_attester
    )


def upload_prover_files_hf(
    model_name: str, paths: EzklFilePaths, model_path: typing.Optional[str] = None
) -> list[str]:
    """
    helper function to upload prover files to hugging face.

    Args:
        model_name (str): name of model
        paths (EzklFilePaths): ezkl file paths
        model_path (typing.Optional[str], optional): if specified,
        the model file is uploaded as well. Defaults to None.

    Returns:
        list[str]: _description_
    """
    logging.info("Start uploading prover files for %s", model_name)
    api = HfApi()
    local_paths = [
        paths.compiled_model_path,
        paths.settings_path,
        paths.pk_path,
        paths.vk_path,
        paths.srs_path,
    ]

    urls = []
    for local_path, repo_path in zip(local_paths, PROVING_FILENAMES):
        url = api.upload_file(
            path_or_fileobj=local_path,
            path_in_repo=repo_path,
            repo_id=model_name,
            repo_type="model",
        )
        urls.append(url)
        logging.info("Uploaded %s: %s", repo_path, url)

    if model_path:
        url = api.upload_file(
            path_or_fileobj=model_path,
            path_in_repo=os.path.basename(model_path),
            repo_id=model_name,
            repo_type="model",
        )
        urls.append(url)
        logging.info("Uploaded %s: %s", os.path.basename(model_path), url)

    logging.info("Finished uploading prover files for %s", model_name)

    return urls


def download_prover_files_hf(model_name: str) -> list[str]:
    """helper function to download files
    necessary for proving.

    Args:
        model_name (str): name of the model

    Returns:
        list[str]: list of downloaded paths
    """
    paths = [
        hf_hub_download(model_name, name, repo_type="model")
        for name in PROVING_FILENAMES
    ]
    return paths


def create_tensor(data: list[Any], dtype_str: str) -> torch.Tensor:
    """Simple function to help create a tensor of
    a specific type from a str.

    Args:
        data (list): list of data
        str (dtype_str): string that maps to a torch dtype

    Returns:
        torch.Tensor: a tensor with dtype matching the specified dtype string
    """
    dtype = DTYPES.get(dtype_str, None)
    return torch.tensor(data, dtype=dtype)
