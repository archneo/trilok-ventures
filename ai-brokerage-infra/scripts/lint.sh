#!/usr/bin/env bash
set -euo pipefail
terraform fmt -check terraform/cloud terraform/onprem
helm lint helm/charts/rag-gateway
