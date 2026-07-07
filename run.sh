#!/usr/bin/env bash

# Stop immediately if a command fails.
set -e

# Change to the directory containing this script.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Verify the virtual environment exists.
if [ ! -d ".venv" ]; then
    echo "Error: .venv not found."
    exit 1
fi

# Activate the virtual environment.
source .venv/bin/activate

echo "================================="
echo " Starting TelnetDM"
echo " Python: $(which python3)"
echo "================================="
echo

python3 main.py
