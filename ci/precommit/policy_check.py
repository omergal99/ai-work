#!/usr/bin/env python3
from pathlib import Path
import sys

import yaml

ROOT = Path(__file__).resolve().parents[2]
path = ROOT / '.ai' / 'policies.yaml'
p = yaml.safe_load(path.read_text(encoding='utf-8'))
required = ['history_retention_days', 'evals', 'token_budget', 'memory', 'secrets']
for key in required:
    if key not in p:
        raise SystemExit(f'Missing policy: {key}')
if 'required_for' not in p['evals']:
    raise SystemExit('Missing eval requirement list')
print('Policies OK')
