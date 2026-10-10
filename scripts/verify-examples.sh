#!/usr/bin/env bash
# 全量实跑各章 code/*.py。实现见 scripts/verify-examples.py
set -euo pipefail
cd "$(dirname "$0")/.."
exec python3 scripts/verify-examples.py "$@"
