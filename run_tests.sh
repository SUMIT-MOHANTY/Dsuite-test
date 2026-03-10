#!/bin/bash
set -e
cd "$(dirname "$0")"

echo "Installing test dependencies..."
if [ -f requirements-dev.txt ]; then
    pip install -r requirements-dev.txt
fi

echo "Running tests..."
python -m pytest tests -v

echo "Test run complete."
