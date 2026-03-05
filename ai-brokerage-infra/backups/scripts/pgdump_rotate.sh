#!/usr/bin/env bash
set -euo pipefail
mkdir -p backups
pg_dump "${DATABASE_URL:?DATABASE_URL required}" > "backups/db-$(date +%F).sql"
find backups -name '*.sql' -mtime +7 -delete
