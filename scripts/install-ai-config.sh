#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET_DIR="${1:-$ROOT_DIR}"

mkdir -p "$TARGET_DIR/.ai"
cp -r "$ROOT_DIR/.ai" "$TARGET_DIR/"

echo "Installed AI config into $TARGET_DIR"
