"""
Simple test for on chain verification
"""
import json
import logging
import subprocess
import time
from tempfile import TemporaryDirectory
from typing import Any, Union

import torch
from ml.utils.ezkl_utils import RPC_URL, generate_verifier, verify_onchain_proof
from ml.workflows.training.example_workflow import BalanceClassifierEzklWorkflow
from solcx import compile_standard  # type: ignore
from web3 import HTTPProvider, Web3

# setup web3 instance
w3 = Web3(HTTPProvider(RPC_URL))


def start_anvil() -> subprocess.Popen[Any]:
    """helper fn to start anvil
    Raises:
        Exception: if failed to start process

    Returns:
        subprocess.Popen: anvil process
    """
    anvil_process = subprocess.Popen(
        ["anvil", "-p", "3030", "--code-size-limit=41943040"]
    )
    if anvil_process.returncode is not None:
        raise RuntimeError("failed to start anvil process")
    time.sleep(3)
    return anvil_process


def stop_anvil(process: subprocess.Popen[Any]) -> None:
    """
    helper fn to stop anvil
    """
    if process is not None:
        process.terminate()


def count_decimal_places(num: Union[float, int]) -> int:
    """helper fn to count number of decimal places in a number

    Args:
        num (Union[float, int]): float or int

    Returns:
        int: number of decimals of the number
    """

    num_str = str(num)
    if "." in num_str:
        return len(num_str) - 1 - num_str.index(".")
    else:
        return 0


def generate_on_chain_data(tensor: torch.Tensor) -> list[dict[str, Any]]:
    # Step 0: Convert the tensor to a flat list
    data: list[Any] = tensor.view(-1).tolist()

    # Step 1: Prepare the data
    decimals = [count_decimal_places(x) for x in data]
    scaled_data = [int(x * 10 ** decimals[i]) for i, x in enumerate(data)]

    # Step 2: Prepare and compile the contract.
    # We are using a test contract here but in production you would
    # use whatever contract you are fetching data from.
    contract_source_code = """
    // SPDX-License-Identifier: UNLICENSED
    pragma solidity ^0.8.17;

    contract TestReads {

        uint[] public arr;
        constructor(uint256[] memory _numbers) {
            for(uint256 i = 0; i < _numbers.length; i++) {
                arr.push(_numbers[i]);
            }
        }
    }
    """

    compiled_sol = compile_standard(
        {
            "language": "Solidity",
            "sources": {"testreads.sol": {"content": contract_source_code}},
            "settings": {
                "outputSelection": {"*": {"*": ["metadata", "evm.bytecode", "abi"]}}
            },
        }
    )

    # Get bytecode
    bytecode = compiled_sol["contracts"]["testreads.sol"]["TestReads"]["evm"][
        "bytecode"
    ]["object"]

    # Get ABI
    # In production if you are reading from really large contracts you can just
    #  use a stripped down version of the ABI of the contract you are calling,
    #  containing only
    # the view functions you will fetch data from.
    abi = json.loads(
        compiled_sol["contracts"]["testreads.sol"]["TestReads"]["metadata"]
    )["output"]["abi"]

    # Step 3: Deploy the contract
    test_reads = w3.eth.contract(abi=abi, bytecode=bytecode)
    tx_hash = test_reads.constructor(scaled_data).transact()
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    # If you are deploying to production you can skip the
    #  3 lines of code above and just
    # instantiate the contract like this,
    # passing the address and abi of the contract you are fetching data from.
    contract = w3.eth.contract(address=tx_receipt["contractAddress"], abi=abi)

    # Step 4: Interact with the contract
    calldata = []
    for i, _ in enumerate(data):
        call = contract.functions.arr(i).build_transaction()
        logging.info(call)
        calldata.append((call["data"][2:], decimals[i]))
        # In production you would need to manually decide what the optimal decimal place
        # for each value should be.
        # Here we are just using the number of decimal places in a
        # randomly generated tensor.

    # Prepare the calls_to_account object
    # If you were calling view functions across multiple contracts,
    # you would have multiple entries in the calls_to_account array,
    # one for each contract.

    calls_to_account = [
        {
            "call_data": calldata,
            "address": contract.address[2:],  # remove the '0x' prefix
        }
    ]

    return calls_to_account


def test_onchain_verification() -> None:
    with TemporaryDirectory() as tmp_dir:
        workflow: BalanceClassifierEzklWorkflow = BalanceClassifierEzklWorkflow(
            base_dir=tmp_dir
        )
        logging.info(workflow.ezkl_paths)

        # setup workflow
        workflow.setup()

        # ensure artifacts generated
        workflow.deploy()

        # obtain test data for inference
        X_test = workflow.X_test

        # test input that we will be generating inference on and verifying from
        input_list = X_test[:1].values

        logging.info("Input: %s", input_list)

        # generate inference
        result = workflow.inference(input_list)

        logging.info("Inference Result: %s", result)

        # generate proof
        workflow.generate_proof()

        # on chain parts require local test net
        anvil = start_anvil()

        # Now let's create our test data function and call it
        calls_to_account = generate_on_chain_data(torch.tensor(input_list))

        data = dict(input_data={"rpc": RPC_URL, "calls": calls_to_account})

        # store the data
        if workflow.ezkl_paths.data_path:
            json.dump(data, open(workflow.ezkl_paths.data_path, "w", encoding="utf-8"))

        # verify offchain just as a sanity check
        tmp = workflow.ezkl_paths.da_addr_path
        workflow.ezkl_paths.da_addr_path = None

        logging.info("verifying on chain")

        # generate and deploy verifier
        generate_verifier(workflow.ezkl_paths)

        assert verify_onchain_proof(workflow.ezkl_paths), "offchain verify failed"
        workflow.ezkl_paths.da_addr_path = tmp

        # stop the process
        stop_anvil(anvil)

        logging.info("ezkl paths: %s", workflow.ezkl_paths)
