#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT_DIR"

python3 -m pip install --upgrade pip >/dev/null 2>&1 || true
python3 -m pip install pyyaml >/dev/null 2>&1 || true

python3 - <<'PY'
import json
import sys
from pathlib import Path

root = Path('.').resolve()
index_path = root / '.ai' / 'index.json'
policies_path = root / '.ai' / 'policies.yaml'
readme_path = root / '.ai' / 'README.ai'

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

print('Lint checks passed')
PY

python3 - <<'PY'
import re
import sys
from pathlib import Path

root = Path('.').resolve()
for path in [root / '.ai' / 'README.ai', root / '.ai' / 'index.json', root / '.ai' / 'policies.yaml']:
    text = path.read_text(encoding='utf-8')
    for pattern in ['password=', 'secret=', 'api_key=', 'sk-']:
        if re.search(pattern, text, flags=re.IGNORECASE):
            raise SystemExit(f'Suspicious secret-like content in {path}')
    if re.search(r'(?<![A-Za-z0-9_])(token|token_budget)(?![A-Za-z0-9_])', text, flags=re.IGNORECASE):
        continue
print('Secrets scan passed')
PY

python3 - <<'PY'
from pathlib import Path

root = Path('.').resolve()
text = (root / '.ai' / 'README.ai').read_text(encoding='utf-8')
if 'token_budget=1500' not in text:
    raise SystemExit('README.ai is missing the expected token budget policy')
print('Token policy check passed')
PY
