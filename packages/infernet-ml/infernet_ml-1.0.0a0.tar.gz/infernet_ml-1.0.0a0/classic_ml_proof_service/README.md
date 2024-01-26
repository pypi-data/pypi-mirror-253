# classic ml proof service

Simple service that generates ZK Proofs for ML workflows that perform EZKL based proofs based on a Huggingface backend.

The service assumes a flat repo structure, and requires the following files to be located in the root directory:

* network.compiled - the EZKL compiled model file
* settings.json - the settings file used to set up EZKL proving
* proving.key - the proving key required for generating proofs
* verifying.key - the verifying key required for verifying proofs
* kzg.srs - the structured reference string used as part of the KZG ceremony

Note these are all artifacts generated as part of an EZKL model proving, and should can be incorporated into the deployment step of a classic training workflow.

# Custom EZKL Library

Note that for the proving service, we currently require custom build of EZKL in order to support obtaining the calldata required for verification and data attestation. The patched source files are in the ezkl directory. See the classic_ml_proof_service.Dockerfile for instructions on how to build it from source.

# End points

/**get_data_attester_calldata** - helper function to get hex encoded call data for the data attester. Expects a generated proof json as input, as well as a argument "verifier_address" that specifies the address of the verifier.

/**get_verifier_calldata** - Helper function to return hex encoded call data to verifier function. Expects a generated proof json as input.

/**generate_witness** - Generates a witness file and along with processed outputs if relevant. The format of this input depends on our target setup.

We expect the json to conform to WitnessData in the following model -

/**service_output** -

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

The classic ml proof service currently only supports OFFCHAIN data. The data is expected to be a json payload that conforms to WitnessInputData (onchain source not yet supported):

```python
class AccountCall(BaseModel):
    call_data: list[Tuple[HexStr, int]]
    address: HexStr

class OnChainSource(BaseModel):
    calls: list[AccountCall]
    rpc: str

class WitnessInputData(BaseModel):
    input_data: Optional[Union[OnChainSource, list[Any]]]
    output_data: Optional[Union[OnChainSource, list[Any]]]
```
The endpoint generates a proof and returns a dict containing hex encoded values of the
processed_input, processed_output, raw_input, raw_output, proof (as calldata) values. This is mainly used by the Infernet node for dynamic service processing.

```
{
  "processed_input": Optional[HexStr]
  "processed_output": Optional[HexStr]
  "raw_input":Optional[HexStr]
  "raw_output":Optional[HexStr]
  "proof": Optional[HexStr]
}

```

/**generate_proof** - Generates a proof, given a generatd witness file json.

/**verify_proof** - helper function that verifies a proof offchain. Expects proof as json input. Returns json with single key "result", and boolean value indicating verification result.



# Environment Arguments

**FLASK_MODEL_NAME** - name of the model. Should conform to Hugginface model, i.e repo_id + model name. (str is expected)

**HUGGING_FACE_HUB_TOKEN** - to download files from huggingface hub

# Launching

The easiest way to launch this service is to run from the dockerhub image, which hosts the service via hypercorn:

```bash
# start container
sudo docker run --name=classic_proof_service -d -p 4997:3000 --env-file classic_proof_service.env "ritualnetwork/infernet-classic-proving:0.0.5" --bind=0.0.0.0:3000 --workers=2
```

This starts the service via hypercorn with 2 workers at port 4997, reading in environment variables from classic_proof_service.env.


if you have custom dependencies, you should create your own image using the provided one as a base.


Example Curl Command:

```bash
curl -X POST http://localhost:4997/service_output \
     -H "Content-Type: application/json" \
     -d '{"source": 1, "data": {"input_shapes": [[69]], "input_data": [[-0.011291295289993286, -0.09783737808465957, -0.5926278710365296, -3.5630358695983886, -0.3165785476565361, 0.34296469688415526, -0.29916933327913287, -0.19399006217718123, 0.18778093233704568, 0.27716260254383085, -0.0462317630648613, 0.2000526398420334, 0.31595549583435056, -2.897480010986328, 0.20964456647634505, 0.14053640905767678, -0.04807716980576515, 0.1371978059411049, -0.27893678545951844, 0.27935349456965924, 0.13819805905222893, 0.13069433271884917, -0.15898748636245727, -3.6215885639190675, -0.1634165309369564, 0.0675600565969944, 0.01265382468700409, 0.051773407496511936, 0.18748415410518646, 0.18870795518159866, -0.28589439690113067, -0.07374711409211158, -0.5523416638374329, -0.07117006629705429, -1.520055317878723, 0.14321593642234803, -0.3372545152902603, 0.17787650860846044, -0.33194555044174195, -0.2739240199327469, 0.7220144987106323, 0.5928373098373413, -0.13491590097546577, -0.5064725816249848, 0.0026401311159133913, -0.1505637913942337, 0.38300642371177673, -0.07082562204450368, -0.5169946551322937, -0.09643385717645288, 0.438362181186676, -0.333197757601738, 0.06922336518764496, -0.37011549472808836, -0.2389164961874485, -0.40170862078666686, -2.508833122253418, 0.1671809248626232, -0.5798491060733795, -0.4889169275760651, -0.412348522990942, 0.25244922041893003, 0.17055379822850228, -0.18325912337750197, 0.44572556018829346, -6.839046955108643, 0.1667347952723503, 0.22297277450561523, 0.060141101479530334]], "output_data": [[0]]}}'
```

If local deployment is desired, ensure your python path includes the src directory, either by installing the ml project or by manually setting PYTHONPATH, and run the flask dev server:

```bash
pip install -r requirements.txt
export PYTHONPATH=src
flask --app classic_ml_proof_service run -p 4997
```
