#!/usr/bin/env bash
set -euo pipefail
SNAPSHOT_ID=${1:-latest}
TARGET=${2:-/restore}
restic restore "$SNAPSHOT_ID" --target "$TARGET"
