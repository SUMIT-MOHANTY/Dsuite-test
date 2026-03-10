#!/usr/bin/env bash
#
# run_loadtest.sh
# Spins up Locust, runs 500u/2min ramp, dumps HTML + CSV.
#
set -euo pipefail
HOST=${1:-http://localhost:5000}
RESULT_DIR="/workspace/tests/load/results"
mkdir -p "$RESULT_DIR"
# Absolute path juggling
SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)

echo "Installing load-test deps..."
python -m pip install -q -r "$SCRIPT_DIR/requirements-load.txt"

echo "Starting load test against $HOST with Locust..."
locust \
  --host="$HOST" \
  --locustfile "$SCRIPT_DIR/locustfile.py" \
  --headless \
  --run-time 2m \
  --users 500 \
  --spawn-rate 50 \
  --html "$RESULT_DIR/loadtest.html" \
  --csv "$RESULT_DIR/stats" \
  --only-summary

echo "Analyzing metrics..."
cd "$RESULT_DIR"
python3 "$SCRIPT_DIR/analysis.py"
