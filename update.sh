#!/usr/bin/env bash

# Stop immediately if a command fails.
set -e

# Change to the directory containing this script.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

git fetch
git merge origin/main

