"""
this module serves as the driver for the llm inference service.
"""

import importlib
import json
import logging
from typing import Any, Optional, Type, Union

from pydantic import ValidationError as PydValError
from quart import Quart, abort
from quart import request as req
from text_generation.errors import (  # type: ignore
    BadRequestError,
    GenerationError,
    IncompleteGenerationError,
    NotFoundError,
    NotSupportedError,
    OverloadedError,
    RateLimitExceededError,
    ShardNotReadyError,
    ShardTimeoutError,
    UnknownError,
    ValidationError,
)
from werkzeug.exceptions import HTTPException

from ml.utils.service_models import InfernetInput
from ml.workflows.inference.llm_inference_workflow import LLMInferenceWorkflow

from .models import LLMRequest


def get_workflow_class(full_class_path: str) -> Optional[Type[LLMInferenceWorkflow]]:
    """Returns a LLMInferenceWorkflow instance from a class path string.

    Args:
        full_class_path (str): class to load

    Returns:
        Optional[Type[LLMInferenceWorkflow]]: None if error loading the class
    """
    module_name, class_name = full_class_path.rsplit(".", 1)
    try:
        class_ = None
        module_ = importlib.import_module(module_name)
        try:
            class_ = getattr(module_, class_name)
            if not issubclass(class_, LLMInferenceWorkflow):
                logging.error("%s is not a subclass of BaseMLWorkflow", class_)
                class_ = None
        except AttributeError:
            logging.error("Class does not exist")
    except ImportError as e:
        logging.error("Module does not exist: %s", e)

    return class_


def create_app(test_config: Optional[dict[str, Any]] = None) -> Quart:
    """application factory for the LLM Inference Service

    Args:
        test_config (Optional[dict[str, Any]], optional): Defaults to None.

    Raises:
        ImportError: thrown if error loading the workflow
        PydValError: thrown if error duing input validation

    Returns:
        Quart: Quart App instance
    """
    app: Quart = Quart(__name__)
    app.config.from_mapping(
        # should be overridden by instance config
        LLM_WORKFLOW_CLASS="ml.workflows.inference.llm_inference_workflow.LLMInferenceWorkflow",
        LLM_WORKFLOW_POSITIONAL_ARGS=["http://server_url_here"],
        LLM_WORKFLOW_KW_ARGS={},
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_prefixed_env(prefix="FLASK")
    else:
        # load the test config if passed in
        app.config.update(test_config)

    LLM_WORKFLOW_CLASS = app.config["LLM_WORKFLOW_CLASS"]
    LLM_WORKFLOW_POSITIONAL_ARGS = app.config["LLM_WORKFLOW_POSITIONAL_ARGS"]
    LLM_WORKFLOW_KW_ARGS = app.config["LLM_WORKFLOW_KW_ARGS"]

    logging.info(
        "%s %s %s",
        LLM_WORKFLOW_CLASS,
        LLM_WORKFLOW_POSITIONAL_ARGS,
        LLM_WORKFLOW_KW_ARGS,
    )

    clazz = get_workflow_class(LLM_WORKFLOW_CLASS)

    if clazz is None:
        raise ImportError(
            f"Unable to import specified Workflow class {LLM_WORKFLOW_CLASS}"
        )

    # create workflow instance from class, using specified arguments
    LLM_WORKFLOW = clazz(*LLM_WORKFLOW_POSITIONAL_ARGS, **LLM_WORKFLOW_KW_ARGS)

    # setup workflow
    LLM_WORKFLOW.setup()

    @app.route("/")
    async def index() -> str:
        """Default index page. Displays the LLM URI that
        this service will forward requests to
        Returns:
            str: simple heading
        """
        return f"<p>Lightweight LLM Inference Service to {clazz.__name__}</p>"

    @app.route("/service_output", methods=["POST"])
    @app.route("/inference", methods=["POST"])
    async def inference() -> Union[str, dict[str, Any]]:
        """implements inference. Expects json/application data,
        formatted according to the InferenceRequest schema.
        Returns:
            dict: inference result
        """
        if req.method == "POST" and (data := await req.get_json()):
            # we will get the file from the request
            try:
                ## load data into model for validation
                inf_input = InfernetInput(**data)
                if isinstance(inf_input.data, dict):
                    llm_req = LLMRequest(**inf_input.data)
                    logging.info("recieved LLM Request: %s", llm_req)

                    ## send parsed output back
                    result: Union[str, dict[str, Any]] = LLM_WORKFLOW.inference(
                        input_data=llm_req.model_dump()
                    )

                    logging.info("recieved result fromm workflow: %s", result)
                    return result
                else:
                    raise PydValError(
                        "Invalid InferentInput type: expected mapping for offchain input type"  # noqa: E501
                    )

            except PydValError as e:
                abort(400, e)
            except (
                BadRequestError,
                GenerationError,
                IncompleteGenerationError,
                NotFoundError,
                NotSupportedError,
                OverloadedError,
                RateLimitExceededError,
                ShardNotReadyError,
                ShardTimeoutError,
                UnknownError,
                ValidationError,
            ) as e:
                abort(500, e)
        abort(400, "Invalid method or data")

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
