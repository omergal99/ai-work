#!/usr/bin/env python3
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT

source = ROOT / '.ai'
destination = TARGET / '.ai'
if destination.exists():
    shutil.rmtree(destination)
shutil.copytree(source, destination)
print(f'Installed AI config into {TARGET}')
