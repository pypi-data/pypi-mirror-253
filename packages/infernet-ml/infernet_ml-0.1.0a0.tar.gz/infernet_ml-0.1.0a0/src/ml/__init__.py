"""
specify module level settings here
"""
import logging
import os
from sys import stdout
from typing import Union

from dotenv import load_dotenv
from mlflow import set_tracking_uri  # type: ignore

ML_RUNS_DIRECTORY: str = f"{os.path.dirname(os.path.abspath(__file__))}/../../mlruns"
# load dotenv files defined in module
load_dotenv()

LOGLEVEL: Union[str, int] = os.getenv("LOGLEVEL", default=logging.INFO)

# define the default logging config for the ml module here
logging.basicConfig(
    level=LOGLEVEL,
    format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
    datefmt="%d/%b/%Y %H:%M:%S",
    stream=stdout,
)

if not os.getenv("MLFLOW_TRACKING_URI"):
    # we store ML flow runs in the mlruns directory if it is not specified
    set_tracking_uri(ML_RUNS_DIRECTORY)
    logging.debug("Setting MLFlow tracking URI: %s", ML_RUNS_DIRECTORY)
else:
    logging.info("Detected MLFlow tracking URI: %s", os.getenv("MLFLOW_TRACKING_URI"))
