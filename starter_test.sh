#!/bin/bash

# Variables
ROOT_PATH="./srv6_delay_measurement"
GRPC_STUBS_PATH="${ROOT_PATH}/commons/protos/srv6pm/gen-py"
VENV_ACTIVATE_SCRIPT="./.venv/bin/activate"
TEST_FILENAME="${ROOT_PATH}/test/test_stamp.py"

# Add the path to the gRPC stubs
export PYTHONPATH="${PYTHONPATH}:${GRPC_STUBS_PATH}:${ROOT_PATH}"

# Activate virtual environment
source ${VENV_ACTIVATE_SCRIPT}

# Start the reflector
python ${TEST_FILENAME}

# Deactivate virtual environment
deactivate