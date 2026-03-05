#!/usr/bin/env bash
set -euo pipefail
: "${RESTIC_REPOSITORY:?required}"
: "${RESTIC_PASSWORD:?required}"
restic backup /srv/docker/volumes
