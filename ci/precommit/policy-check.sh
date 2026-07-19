#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT_DIR"

python3 - <<'PY'
import sys
from pathlib import Path
import yaml

path = Path('.ai/policies.yaml')
p = yaml.safe_load(path.read_text(encoding='utf-8'))
required = ['history_retention_days', 'evals', 'token_budget', 'memory', 'secrets']
for key in required:
    if key not in p:
        raise SystemExit(f'Missing policy: {key}')
if 'required_for' not in p['evals']:
    raise SystemExit('Missing eval requirement list')
print('Policies OK')
PY
