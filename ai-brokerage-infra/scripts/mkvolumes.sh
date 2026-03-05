#!/usr/bin/env bash
set -euo pipefail
BASE=${1:-/srv/docker/volumes}
mkdir -p "$BASE"/{postgres,nextcloud,n8n,odoo,pgadmin}
