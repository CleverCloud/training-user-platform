#!/usr/bin/env bash
# "The team updated the configuration." Run it from your app folder, before deploying:
#   bash $LAB/demos/5-fs-bucket-config/configure.sh
set -euo pipefail
clever env set UPLOAD_DIR data
echo "Configuration updated. Now: clever deploy"
