"""
utility script for deploying trained models to HuggingFace
for serving inference and generating proofs.
"""

import json
import pickle
from os import path

import click
import ezkl
import sk2torch  # type: ignore
import torch
from click import ClickException

from ml.utils import ezkl_utils


@click.command()
@click.option(
    "--model",
    type=click.Path(exists=True, dir_okay=False, readable=True),
    prompt="enter model file path. Currently, torch models and sklearn models (via sk2torch) are supported. If using a sklearn model, be sure to specify --use_sk2torch as well",  # noqa: E501
)
@click.option(
    "--model_name",
    prompt_required=False,
    prompt="enter full model name in HuggingFace. For example, Origin-Research/summarizer_models",  # noqa: E501
    default=None,
)
@click.option("--use_sk2torch/--no_sk2torch", default=False)
@click.option(
    "--sample_input_json",
    type=click.Path(exists=True, readable=True),
    prompt="enter sample input json path. This is generally a json list that gets converted into a torch tensor",  # noqa: E501
)
@click.option(
    "--onchain_data",
    type=click.Path(exists=True, dir_okay=False, readable=True),
    default=None,
)
@click.option(
    "--calibration_data",
    type=click.Path(exists=True, dir_okay=False, readable=True),
    default=None,
)
@click.option(
    "--sample_input_dtype",
    type=click.Choice(list(ezkl_utils.DTYPES.keys())),
    prompt=f"enter sample input dtype. Should be one of {list(ezkl_utils.DTYPES.keys())}",  # noqa: E501
)
@click.option(
    "--output_dir",
    type=click.Path(exists=True, file_okay=False, writable=True),
    default="",
)
@click.option(
    "--input_visibility",
    type=click.Choice(["hashed", "private", "public"], case_sensitive=False),
    default="hashed",
)
@click.option(
    "--output_visibility",
    type=click.Choice(["hashed", "private", "public"], case_sensitive=False),
    default="public",
)
@click.option(
    "--param_visibility",
    type=click.Choice(["hashed", "private", "public"], case_sensitive=False),
    default="private",
)
def deploy_model(
    model: str,
    model_name: str,
    use_sk2torch: bool,
    sample_input_json: str,
    sample_input_dtype: str,
    input_visibility: str,
    output_visibility: str,
    param_visibility: str,
    calibration_data: str,
    onchain_data: str,
    output_dir: str,
) -> None:
    """
    Simple program that deploys a classic model for
    inference and EZKL based ZK Proof serving.
    Currently, Torch and Sklearn (via sk2learn)
    models are supported. Be sure to set up
    the HUGGING_FACE_HUB_TOKEN environment
    variable appropriately.

    Running this program will: \n

    1) (Optionally) convert a sklearn model to a torch model \n
    2) convert the torch model to an onnx model, and compile the EZKL circuit \n
    3) generate the artifacts required for EZKL proving setups \n
    4) (if model_name specified) upload the torch model and artifacts to the specified Huggingface model repo (can be turned off) \n
    5) generate verifier contracts for further deployment \n
    6) (if onchain data provided) generate data attester contracts for further deployment \n
    \b
    onchain data json file should match EZKL expected on chain data format.(see https://github.com/zkonduit/ezkl/blob/main/examples/notebooks/data_attest.ipynb)
    Example:
        {
        "input_data": {
            "rpc": "http://localhost:3030", // The rpc endpoint of the chain you are deploying your verifier to
            "calls": [
            {
                "call_data": [
                [
                    "71e5ee5f0000000000000000000000000000000000000000000000000000000000000000", // The abi encoded call data to a view function that returns a single on-chain data point (we only support uint256 returns for now)
                    7 // The number of decimal places of the large uint256 value. This is our way of representing large wei values as floating points on chain, since the evm only natively supports integer values.
                ],
                [
                    "71e5ee5f0000000000000000000000000000000000000000000000000000000000000001",
                    5
                ],
                [
                    "71e5ee5f0000000000000000000000000000000000000000000000000000000000000002",
                    5
                ]
                ],
                "address": "5fbdb2315678afecb367f032d93f642f64180aa3" // The address of the contract that we are calling to get the data.
            }
            ]
        }
        }

    """  # noqa: E501

    torch_model = None
    model_path = None

    # for sklearn models, we use sk2torch
    if use_sk2torch:
        # torch models are loaded via pickle
        loaded_model = pickle.load(open(model, "rb"))

        # while sk2torch supports a many classes of models,
        # there may be some that are not
        if type(loaded_model) in sk2torch.supported_classes():
            torch_model = sk2torch.wrap(loaded_model)
            # save torch model for inference
            model_path = path.join("model.torch")
            torch.save(torch_model, model_path)
        else:
            raise ClickException(
                f"sklearn model conversion of [{type(loaded_model)}] not supported. Supported models: {sk2torch.supported_classes}"  # noqa: E501
            )
    else:
        model_path = model
        # we are loading a torch model directly
        torch_model = torch.load(model)

    # sample input files are used to determine the expected shape of I/O
    with open(sample_input_json, "r", encoding="utf-8") as sif:
        sample_input = json.load(sif)

        # here we create a tensor, either using the provided input dtype or inferring.
        torch_input = ezkl_utils.create_tensor(sample_input, sample_input_dtype)

        click.echo(f"torch_input ({torch_input.type()}): {torch_input}")
        # do inference
        output = torch_model.predict(torch_input)

        click.echo(f"torch_output: {output}")

        paths = ezkl_utils.get_default_ezkl_paths(output_dir)

        torch.onnx.export(
            torch_model,
            torch_input,
            paths.onnx_model_path,
            # store the trained parameter weights inside the model file
            export_params=True,
            # the ONNX version to export the model to
            opset_version=10,
            # whether to execute constant folding for optimization
            do_constant_folding=True,
            input_names=["input"],  # the model's input names
            output_names=["output"],  # the model's output names
            dynamic_axes={
                "input": {0: "batch_size"},  # variable length axes
                "output": {0: "batch_size"},
            },
        )

        click.echo(f"generating witness data from inference: {paths.data_path}")
        # generate witness data based on direct inference
        ezkl_utils.generate_witness_data(torch_input, output, paths)

        paths.calibration_data_path = calibration_data

        click.echo(f"generating settings: {paths.settings_path}")
        # generate and calibrate settings (with witness data)
        ezkl_utils.gen_and_calibrate_settings(
            paths,
            input_visibility=input_visibility,
            param_visibility=param_visibility,
            output_visibility=output_visibility,
        )

        click.echo(f"compiling circuit: {paths.compiled_model_path}")
        # generate circuit
        res = ezkl.compile_circuit(  # type: ignore
            paths.onnx_model_path,
            paths.compiled_model_path,
            paths.settings_path,
        )
        assert res is True, "unable to compile circuit"

        # generate srs
        click.echo(f"generating srs: {paths.srs_path}")
        res = ezkl.get_srs(paths.srs_path, paths.settings_path)  # type: ignore
        assert res is True, "unable to generate srs file"

        # generate witness
        click.echo(f"generating witness: {paths.witness_path}")
        ezkl_utils.generate_witness(
            paths.data_path,  # type: ignore
            paths.compiled_model_path,  # type: ignore
            paths.witness_path,  # type: ignore
            input_visibility=input_visibility,
            params_visibility=param_visibility,
            output_visibility=output_visibility,
        )

        # do setup
        click.echo(f"Performing setup ceremony: {paths.vk_path},{ paths.pk_path}")
        ezkl_utils.setup(paths)

        # generate proof
        click.echo(f"generating proof: {paths.proof_path}")
        ezkl_utils.generate_proof(paths)

        # verify proof for sanity
        click.echo("verifying proof")
        assert ezkl_utils.verify_proof(paths), "offchain proof succeeded"

        if model_name is not None:
            click.echo(f"uploading files to huggingface for model {model_name}")
            ezkl_utils.upload_prover_files_hf(model_name, paths, model_path=model_path)
        # generate verifier contracts
        click.echo(
            f"generating verifier solidity files: {paths.vf_sol_code_path}, {paths.vf_abi_path}"  # noqa: E501
        )
        ezkl_utils.generate_verifier(paths, deploy=False)

        if onchain_data is not None:
            click.echo(f"using onchain_data: {onchain_data}")
            paths.data_path = onchain_data
            click.echo(
                f"generating data attester solidity files: {paths.da_sol_code_path}, {paths.da_abi_path}"  # noqa: E501
            )
            ezkl_utils.generate_da_attester(paths, deploy=False)

        click.echo("deployer execution complete.")


if __name__ == "__main__":
    # pylint: disable=E1120:no-value-for-parameter
    deploy_model()
