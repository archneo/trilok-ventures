#!/usr/bin/env bash
set -euo pipefail
TARGET=${1:-/restore}
test -d "$TARGET" && echo "restore target exists: $TARGET"
