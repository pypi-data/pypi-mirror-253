# infernet-ml

infernet-ml is a lightweight library meant to simplify the implementation
of machine learning workflows for models intended for Web3.

# Library Installation

## NOTE: It is strongly recommended that you use a virtual environment for development. The library is has been tested with Python 3.10.

To install this library locally for development(i.e. inside an IDE), the easiest path is to run
```bash
python -m venv .venv
source .venv/bin/activate
pip install "infernet-ml[all]"
```
which will install all python dependencies, including test requirements (note you may need to install [Anvil](https://book.getfoundry.sh/getting-started/installation#using-foundryup) depending on the test):

```bash
curl -L https://foundry.paradigm.xyz | bash && source ~/.bashrc && foundryup
```

Alternatively, you may install with a subset of the targets [proving,classic_inf,llm_inf] depending on your use case. For example, to only install llm inference related dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install "infernet-ml[llm_inf]"
```

In this case, to be able to run tests, you will need to install the test dependencies, located in requirements-test.txt:
```bash
pip install -r requirements-test.txt
# install Foundry Anvil
curl -L https://foundry.paradigm.xyz | bash && source ~/.bashrc && foundryup
```

If you prefer to install requirements manually, we also maintain a requirements.txt file.

Alternatively,if you want to modify the library source code directly, and you do not want to use pip install -e (for editable installation), you can install the dependencies from requirements.txt and set the PYTHONPATH:

```bash
python3 -m venv .venv
source .venv/bin/activate
cd infernet-ml
pip install -r requirements.txt
# make sure to set your classpath
export PYTHONPATH=src
```

Note that for proving, we currently require custom build of EZKL in order to support obtaining the calldata required for verification and data attestation. See the classic_ml_proof_service.Dockerfile for instructions on how to build it.


# The library

There are broadly 2 classes of workflows: inference and training.

training workflows provides various workflow base classes intended to be extended and subclassed, and leverages the [MLFLow](https://mlflow.org) library for
persisting workflow artifacts, and serving classical machine learning models.

Inference workflows add hooks to help structure and organize common tasks related machine learning inference, such as preprocessing for prompt tuning or appending output with custom metadata for downstream services. Inference workflows are directly served by the Infernet ML Inference services.

ml/drivers/example_workflow_driver demonstrates a simple training workflow that trains a scikit-learn `DecisionTreeClassifier` model based on the [UC, Irvine balance scale dataset](https://archive.ics.uci.edu/ml/machine-learning-databases/balance-scale/balance-scale.data) ([`balance (left, right, balanced)`, `left_weight`, `left_distance`, `right_weight`, `right_distance`]).

Proof generation is also demonstrated, with the implementation logic mostly residing in the ml/utils/ezkl_utils.py module.

**For compilation:** note that EZKL currently has a solc version dependency of ^0.8.20 and above.


![Class Hierarchy](https://github.com/origin-research/infernet-ml/raw/refactor/classes.png)


## Running Tests locally

Please install Anvil and test dependencies as needed.
We test using pytest:

```bash
python3 -m venv .venv
source .venv/bin/activate
cd infernet-ml
# if library not installed
# pip install -r requirements.txt
# pip install -r requirements-test.txt
# export PYTHONPATH=src
python -m pytest tests
```

## Running Workflow drivers locally

```bash
python3 -m venv .venv
source .venv/bin/activate
cd infernet-ml
pip install -r requirements.txt
export PYTHONPATH=src
python3 src/ml/drivers/example_workflow_driver.py
```


## Running mlflow ui

By default, the mlflow runs directory is stored as a subdirectory of ml. To view run artifacts through the web UI, execute the following command in the same parent directory as the mlruns directory:
```bash
# Run locally
mlflow ui
```

## Running mlflow remotely

By default, mlflow artifacts are stored locally on disk. However, a MLFLow Server instance can be instantiated either locally or remotely. To help facilitate this, a docker file is provided with dependencies for using a postgres/mysql metadata backend and Google Cloud Storage artifact backend.

To ensure we connect to the remote mlflow Server, you set
the MLFLOW_TRACKING_URI environment variable with the server address. Note that dotenv files are read to help facilitate testing (place the .env file in the src
directory.)

After a container is buit from the docker image, assuming we are using Google GCS and Postgres, you can issue the following command to start the server. See [MLFLow documentation](https://mlflow.org/docs/latest/index.html) for more details.


```bash
mlflow server \
 --default-artifact-root gs://path/to/your/artifact-store \
 --backend-store-uri postgresql://yourusername:yourpassword@localhost:5432/postgres
```


## Building docker service containers
Included with the workflow class hierarchy are several services that can be used to serve model inference and proving. Official images can be downloaded from our [docker hub repositories](https://hub.docker.com/orgs/ritualnetwork/repositories), but if you wish to build them locally:

```bash
# build containers
docker build -t "infernet_ml_llm:local" -f llm_inference_service.Dockerfile .
docker build -t "infernet_ml_proof:local" -f classic_ml_proof_service.Dockerfile .
docker build -t "infernet_ml_classic:local" -f classic_ml_inference_service.Dockerfile .

```

Note: if you have custom workflow dependencies, you should create your own image using the provided images from docker hub as base images.

To start the containers:

```bash
# start containers
sudo docker run --name=llm_inf_service -d -p 4999:3000 --env-file llm_inference_service.env "ritualnetwork/infernet-llm-inference:0.0.4" --bind=0.0.0.0:3000 --workers=2
sudo docker run --name=classic_inf_service -d  -p 4998:3000 --env-file classic_ml_inference_service.env  "ritualnetwork/infernet-classic-inference:0.0.4" --bind=0.0.0.0:3000 --workers=2
sudo docker run --name=classic_proof_service -d -p 4997:3000 --env-file classic_proof_service.env "ritualnetwork/infernet-classic-proving:0.0.5" --bind=0.0.0.0:3000 --workers=2
```

with environment files configured as per below:

## Service configuration

Classic ML Inference Service (classic_ml_inference_service.env)-
```bash
CLASSIC_INF_WORKFLOW_CLASS="ml.workflows.inference.torch_inference_workflow.TorchInferenceWorkflow"
CLASSIC_INF_WORKFLOW_POSITIONAL_ARGS=[]
CLASSIC_INF_WORKFLOW_KW_ARGS={"model_name":"your_model_org/your_model_name"}

# the hugging face token is required to download the model
HUGGING_FACE_HUB_TOKEN=YOUR_HUGGING_FACE_TOKEN
```

Classic ML Proof Service (classic_proof_service.env)-
```bash
# The name of the model we are generating proofs for
CLASSIC_PROOF_MODEL_NAME=your_model_org/your_model_name
# the hugging face token is required to download necessary artifacts
HUGGING_FACE_HUB_TOKEN=YOUR_HUGGING_FACE_TOKEN
```

LLM Inference Service (llm_inference_service.env)-
```bash
LLM_INF_WORKFLOW_CLASS="ml.workflows.inference.llm_inference_workflow.LLMInferenceWorkflow"
# path of inference HF / Prime inference backend
LLM_INF_WORKFLOW_POSITIONAL_ARGS='["http://ENTER-URL-HERE"]'
LLM_INF_WORKFLOW_KW_ARGS={}
# the hugging face token is required to download necessary artifacts
HUGGING_FACE_HUB_TOKEN=YOUR_HUGGING_FACE_TOKEN

```

## Deployment Utility
For ML Engineers that already have an existing pipeline and just want to deploy their classic machine learning models with EZKL proving support, please use the deployer.py utility script (located at /src/ml/utilities/deployer.py).

If running the script directly, please ensure the infernet-ml library is installed or your PYTHONPATH (see installation instructions above) is set to the source directory. Note that a solidity compiler must be installed, currently version ^0.8.20 and above (you can use (solc-select)[https://github.com/crytic/solc-select] to manage versions):

```bash
source .venv/bin/activate
solc-select use 0.8.21 --always-install
python3 src/ml/utils/deployer.py --model PATH_TO_YOUR_MODEL --sample_input_json PATH_TO_YOUR_INPUT
```

You can also leverage the docker image:

```bash
sudo docker run -it -v .:/app ritualnetwork/deployer:0.0.1 --model LOCAL_MODEL.TORCH --sample_input_json LOCAL_SAMPLE_INPUT.json
```

Run the script with --help for more info.
