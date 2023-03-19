#!/bin/bash

# Exit early on errors
set -eu

# Export environment variables
export PYTHONUNBUFFERED=1
export DB_FILE=./db/db.sqlite
export SECRET_KEY=wuwoeh80w8-0283u9-u-bdii23-

# Create virtual environment
VIRTUALENV=./venv

if [ ! -d $VIRTUALENV ]; then
  python3 -m venv $VIRTUALVENV
fi


# Install pip into virtual environment
if [ ! -f $VIRTUALENV/bin/pip ]; then
  curl --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py | $VIRTUALENV/bin/python
fi

# Install the requirements
$VIRTUALENV/bin/pip install -r requirements.txt

# Run application
$VIRTUALENV/bin/python3 main.py