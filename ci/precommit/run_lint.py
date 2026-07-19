#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

index_path = ROOT / '.ai' / 'index.json'
policies_path = ROOT / '.ai' / 'policies.yaml'
readme_path = ROOT / '.ai' / 'README.ai'

if not index_path.exists():
    raise SystemExit('index.json missing')
if not policies_path.exists():
    raise SystemExit('policies.yaml missing')
if not readme_path.exists():
    raise SystemExit('README.ai missing')

payload = index_path.read_text(encoding='utf-8').strip()
if not payload.startswith('{') or not payload.endswith('}'):
    raise SystemExit('index.json must be compact JSON')
json.loads(payload)

lines = [line.strip() for line in readme_path.read_text(encoding='utf-8').splitlines() if line.strip()]
if len(lines) > 3:
    raise SystemExit('README.ai must be <= 3 lines')

for path in [readme_path, index_path, policies_path]:
    text = path.read_text(encoding='utf-8')
    for pattern in ['password=', 'secret=', 'api_key=', 'sk-']:
        if re.search(pattern, text, flags=re.IGNORECASE):
            raise SystemExit(f'Suspicious secret-like content in {path}')

print('Lint checks passed')
