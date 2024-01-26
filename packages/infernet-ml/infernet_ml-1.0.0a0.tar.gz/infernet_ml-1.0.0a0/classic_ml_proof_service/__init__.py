"""
This module serves as the driver for classic ml proof service.
"""
import json
import logging
import tempfile
from typing import Any, Optional, cast

import ml.utils.ezkl_utils as ezkl_utils
from eth_abi import encode  # type: ignore
from huggingface_hub import hf_hub_download  # type: ignore
from ml.utils.encode import encode_multidim_array
from ml.utils.service_models import InfernetInput, InfernetInputSource
from pydantic import ValidationError
from quart import Quart, abort
from quart import request as req
from werkzeug.exceptions import HTTPException

import ezkl

from .models import WitnessInputData

logger = logging.getLogger(__file__)

DUMMY_ADDR = "0x0000000000000000000000000000000000000000"


def create_app(test_config: Optional[dict[str, Any]] = None) -> Quart:
    """
    Factory function that creatse and configures an instance
    of the Quart application

    Args:
        test_config (dict, optional): test config. Defaults to None.

    Returns:
        Quart: Quart App
    """
    app = Quart(__name__)
    app.config.from_mapping(
        # should be overridden by instance config
        MODEL_NAME="YOUR_MODEL_HERE"
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_prefixed_env(prefix="FLASK")
    else:
        # load the test config if passed in
        app.config.update(test_config)

    MODEL_NAME = app.config["MODEL_NAME"]

    logger.info("Preloading %s prover files...", MODEL_NAME)
    logger.info(ezkl_utils.download_prover_files_hf(MODEL_NAME))

    compiled_model_path = hf_hub_download(MODEL_NAME, "network.compiled")
    settings_path = hf_hub_download(MODEL_NAME, "settings.json")
    pk_path = hf_hub_download(MODEL_NAME, "proving.key")
    vk_path = hf_hub_download(MODEL_NAME, "verifying.key")
    srs_path = hf_hub_download(MODEL_NAME, "kzg.srs")
    settings_path = hf_hub_download(MODEL_NAME, "settings.json")

    @app.route("/get_data_attester_calldata", methods=["POST"])
    async def get_data_attester_calldata() -> str:
        """helper function to get call data for data attester
        for a given address of verifier as a request argument
        and proof json from the request data.

        Returns:
            str: hex encoded attest and verify call data
        """

        if req.method == "POST" and (data := await req.get_json()):
            verifier_addr = req.args.get("verifier_address")
            # load proof as file
            with tempfile.NamedTemporaryFile("w+", suffix=".pf") as tf:
                # get data_path from file
                json.dump(data, tf)
                tf.flush()
                data_path = tf.name

                return ezkl.generate_encoded_data_attester_calldata(  # type: ignore
                    data_path, verifier_addr
                )

        abort(400)

    @app.route("/get_verifier_calldata", methods=["POST"])
    async def get_verifier_calldata() -> str:
        """Helper function to return call data to verifier function.
        Expects proof json from the request.
        Returns:
            str: hex encoded verifier call data
        """
        if req.method == "POST" and (data := await req.get_json()):
            # load proof as file
            with tempfile.NamedTemporaryFile("w+", suffix=".pf") as tf:
                # get data_path from file
                json.dump(data, tf)
                tf.flush()
                data_path = tf.name

                return ezkl.generate_encoded_verifier_calldata(  # type: ignore # noqa: E501
                    data_path
                )

        abort(400)

    @app.route("/generate_witness", methods=["POST"])
    async def generate_witness() -> dict[str, Any]:
        """
        Generates witness data json
        Returns:
            dict: json containing witness data
        """
        logging.info("generating witness")

        if req.method == "POST" and (data := await req.get_json()):
            # parse witness data
            WitnessInputData(**data)

            with tempfile.NamedTemporaryFile("w+", suffix=".json") as tf:
                # get data_path from file
                json.dump(data, tf)
                tf.flush()
                data_path = tf.name

                with open(settings_path, "r", encoding="utf-8") as sp:
                    settings = json.load(sp)

                    input_v = (
                        "Hashed"
                        if "Hashed" in settings["run_args"]["input_visibility"]
                        else settings["run_args"]["input_visibility"]
                    )
                    output_v = settings["run_args"]["output_visibility"]
                    param_v = settings["run_args"]["param_visibility"]

                    logging.info(
                        "input_v: %s output_v: %s param_v: %s",
                        input_v,
                        output_v,
                        param_v,
                    )

                    with tempfile.NamedTemporaryFile("w+", suffix=".json") as wf:
                        witness_dict, ip, mp, op = ezkl_utils.generate_witness(
                            data_path,
                            compiled_model_path,
                            wf.name,
                            input_visibility=input_v,
                            params_visibility=param_v,
                            output_visibility=output_v,
                        )

                        return {
                            "witness_file": witness_dict,
                            "processed_input": ip,
                            "processed_params": mp,
                            "processed_output": op,
                        }
        abort(400)

    @app.route("/generate_proof", methods=["POST"])
    async def generate_proof() -> dict[str, Any]:
        """Generate a proof for model .

        Returns:
            dict: a dict representing the proof
        """
        if req.method == "POST" and (witness := await req.get_json()):
            logging.info("loading witness")

            with tempfile.NamedTemporaryFile("w+", suffix=".json") as wf:
                # write witness to disk
                json.dump(witness, wf)
                wf.flush()

                with tempfile.NamedTemporaryFile("w+", suffix=".pf") as pf:
                    proof_res = ezkl.prove(  # type: ignore
                        wf.name,
                        compiled_model_path,
                        pk_path,
                        pf.name,
                        srs_path,
                        "single",
                    )

                    assert proof_res, "unable to generate proof"

                    ezkl.verify(  # type: ignore   # noqa: E501
                        pf.name, settings_path, vk_path, srs_path
                    )

                    # ezkl proof_res != actual proof!
                    # we need to return the actual saved proof
                    proof: dict[str, Any] = json.load(pf)

                    return proof
        abort(400)

    @app.route("/verify_proof", methods=["POST"])
    async def verify_proof() -> dict[str, bool]:
        """Function to verify proof. Note that this function
        does NOT verify the proof onchain, and is instead provided for
        sanity check / development purposes.

        Returns:
            dict: a dict with a single key "result" and value equal
            to the verification result
        """

        if req.method == "POST" and (data := await req.get_json()):
            logging.info("verifying proof %s", data)
            with tempfile.NamedTemporaryFile("w+", suffix=".pf") as tf:
                # get data_path from file
                json.dump(data, tf)
                tf.flush()
                proof_path = tf.name

                res = ezkl.verify(  # type: ignore
                    proof_path,
                    settings_path,
                    vk_path,
                    srs_path,
                )

                return {"result": res}
        abort(400)

    @app.route("/service_output", methods=["POST"])
    async def service_output() -> dict[str, Optional[str]]:
        # input should look like {"input_data": [...], "output_data": [...]}
        if req.method == "POST" and (data := await req.get_json()):
            logger.info("recieved data: %s", data)
            try:
                infernet_input = InfernetInput(**data)
                if infernet_input.source != InfernetInputSource.OFFCHAIN:
                    abort(400, "only OFFCHAIN input supported right now")

                # parse witness data
                witness_data = WitnessInputData(
                    **cast(dict[str, Any], infernet_input.data)
                )
            except ValidationError as e:
                abort(400, f"error validating input: {e}")

            with tempfile.NamedTemporaryFile("w+", suffix=".json") as tf:
                # get data_path from file
                json.dump(witness_data.model_dump(), tf)
                tf.flush()
                data_path = tf.name

                with open(settings_path, "r", encoding="utf-8") as sp:
                    settings = json.load(sp)

                    input_v = (
                        "Hashed"
                        if "Hashed" in settings["run_args"]["input_visibility"]
                        else settings["run_args"]["input_visibility"]
                    )
                    output_v = settings["run_args"]["output_visibility"]
                    param_v = settings["run_args"]["param_visibility"]

                    logging.info(
                        "input_v: %s output_v: %s param_v: %s",
                        input_v,
                        output_v,
                        param_v,
                    )

                    with tempfile.NamedTemporaryFile("w+", suffix=".json") as wf:
                        wf_path = wf.name
                        _, ip, _, op = ezkl_utils.generate_witness(
                            data_path,
                            compiled_model_path,
                            wf_path,
                            input_visibility=input_v,
                            params_visibility=param_v,
                            output_visibility=output_v,
                        )

                        with tempfile.NamedTemporaryFile("w+", suffix=".pf") as pf:
                            res = ezkl.prove(  # type: ignore
                                wf_path,
                                compiled_model_path,
                                pk_path,
                                pf.name,
                                srs_path,
                                "single",
                            )

                            assert res, "unable to generate proof"

                            ezkl.verify(  # type: ignore # noqa: E501
                                pf.name, settings_path, vk_path, srs_path
                            )

                            processed_input = (
                                encode(
                                    ["uint256"], [int(ip[0], 0)]
                                ).hex()  # type: ignore # noqa: E501
                                if ip
                                else None
                            )
                            logger.info(
                                "processed input: %s, encoded: %s", ip, processed_input
                            )

                            processed_output = (
                                encode(
                                    ["int256[]"], [[int(x, 0) for x in op]]
                                ).hex()  # type: ignore # noqa: E501
                                if op
                                else None
                            )

                            logger.info(
                                "processed output: %s, encoded: %s",
                                op,
                                processed_output,
                            )

                            raw_input = (
                                encode_multidim_array(witness_data.input_data).hex()
                                if isinstance(witness_data.input_data, list)
                                else None
                            )

                            logger.info(
                                "raw input: %s, encoded: %s",
                                witness_data.input_data,
                                raw_input,
                            )

                            raw_output = (
                                encode_multidim_array(witness_data.output_data).hex()
                                if isinstance(witness_data.output_data, list)
                                else None
                            )

                            logger.info(
                                "raw ouput: %s, encoded: %s",
                                witness_data.output_data,
                                raw_output,
                            )

                            proof_calldata: str = ezkl.generate_encoded_data_attester_calldata(  # type: ignore  # noqa: E501
                                pf.name, DUMMY_ADDR
                            )

                            # Collect padded verifier calldata from attestor calldata
                            proof_calldata = proof_calldata[
                                proof_calldata.find("1e8e1e13") :
                            ]

                            logger.info(
                                "generating proof calldata for proof: %s",
                                proof_calldata,
                            )

                            return {
                                "processed_output": processed_output,
                                "processed_input": processed_input,
                                "raw_output": raw_output,
                                "raw_input": raw_input,
                                "proof": proof_calldata,
                            }

        abort(400)

    @app.errorhandler(HTTPException)
    def handle_exception(e: Any) -> Any:
        """Return JSON instead of HTML for HTTP errors."""

        # start with the correct headers and status code from the error

        response = e.get_response()
        # replace the body with JSON

        response.data = json.dumps(
            {
                "code": str(e.code),
                "name": str(e.name),
                "description": str(e.description),
            }
        )

        response.content_type = "application/json"
        return response

    return app
