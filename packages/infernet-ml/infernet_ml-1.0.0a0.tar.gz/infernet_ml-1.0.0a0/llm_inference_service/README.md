# llm inference service
A simple service that serves models via an LLMInferenceWorkflow object. In particular, the backend as well as preprocessing / postprocessing logic is encapsulated in the workflow.

# Custom EZKL Python function
Note that this service patches the EZKL installation to support returing calldata for proving and data verifcation. The modified files can be located under the ezkl directory.

# End point

Infernet services are expected to implement a end point at `/service_output` that takes a json payload that conforms to the InfernetInput model:

```python
HexStr = Annotated[
    str, StringConstraints(strip_whitespace=True, pattern="^[a-fA-F0-9]+$")
]

class InfernetInputSource(IntEnum):
    CHAIN = 0
    OFFCHAIN = 1

class InfernetInput(BaseModel):
    source: InfernetInputSource
    data: Union[HexStr, dict[str, Any]]
```
This is meant to let services handle both CHAIN and OFFCHAIN data. For more info, see Infernet Node documentation.

Currently, the LLM Inference Service only supports OFFCHAIN data and corresponding output.
The data field is a json dict that conforms to the following schema -

```python
class LLMRequest(BaseModel):
  key: str
  messageId: str
  text: str # raw request to LLM
  history: list[Optional[dict[str, str]]] # list containing list of prompt history [{"bot":"msg"}, {"player":"msg"}] (list may be empty)
```

Depending on the backend, either a raw output string response or a valid json dict can be returned (Make sure the LLMInferenceWorkflow returns values that can serialize to JSON, for example convert ndarray's to regular Python lists).


# Environment Arguments

FLASK_LLM_WORKFLOW_CLASS - fully qualified name of workflow class. For example, ml.workflows.inference. (str is expected)
FLASK_LLM_WORKFLOW_POSITIONAL_ARGS - any positional args required to instantiate the llm inference workflow (List is expected)
FLASK_LLM_WORKFLOW_KW_ARGS - any keyword arguments required to instatiate the llm inference workflow. (Dict is expected)
HUGGING_FACE_HUB_TOKEN (optional) - if any files needed from huggingface hub

# Launching

The easiest way to launch this service is to run from the dockerhub image, which hosts the service via hypercorn:

```bash
# start containers
sudo docker run --name=llm_inf_service -d -p 4999:3000 --env-file llm_inference_service.env "ritualnetwork/frenrug-llm-inference:0.0.4" --bind=0.0.0.0:3000 --workers=2
```

This starts the service via hypercorn with 2 workers at port 4999, reading in environment variables from llm_inference_service.env.

if you have custom workflow dependencies, you should create your own image using the provided one as a base.

You can use curl to send an example request to the service:

```bash
curl -X POST http://localhost:4999/service_output \
     -H "Content-Type: application/json" \
     -d '{"source": 1, "data": {"text": "I am launching a revolutionary product today, buy my shares before they are gone!", "key": "123", "messageId": "123456", "history": []}}'

```

 If local deployment is desired, ensure your python path includes the src directory, either by installing the ml project or by manually setting PYTHONPATH, and run the flask dev server:

```bash
pip install -r requirements.txt
export PYTHONPATH=src
flask --app llm_inference_service run -p 4999
QUART_APP=llm_inference_service:create_app quart -e llm_inf.env run --reload

```
