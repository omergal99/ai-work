#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT_DIR"

python3 -m pip install --upgrade pip >/dev/null 2>&1 || true
python3 -m pip install pyyaml >/dev/null 2>&1 || true

python3 ci/precommit/run_lint.py
