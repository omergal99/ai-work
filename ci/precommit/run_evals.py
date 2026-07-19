#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
result = subprocess.run([sys.executable, '-m', 'unittest', '-q', 'tests.test_ai_config'], cwd=ROOT)
sys.exit(result.returncode)
