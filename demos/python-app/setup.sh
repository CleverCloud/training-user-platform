#!/usr/bin/env bash
# Trainer helper: deploy the plain Python app from scratch (backup app, or to prepare a demo).
# Trainees do these steps by hand in Lab 1 — this script is not for them.
#
# Usage: ./setup.sh <org> <app-name> [zone] [--with-db]
#   Copies the app to ~/cc-training/<app-name>, makes it a Git repo, creates the
#   Clever Cloud app, sets its variables and deploys it.
#   --with-db also creates a PostgreSQL add-on "<app-name>-pg", links it and restarts.
set -euo pipefail

ORG="${1:?org required}"; NAME="${2:?app name required}"; ZONE="${3:-par}"
WITH_DB=false; for a in "$@"; do [[ "$a" == "--with-db" ]] && WITH_DB=true; done
[[ "$ZONE" == "--with-db" ]] && ZONE=par

SRC="$(cd "$(dirname "$0")" && pwd)"
WORK="$HOME/cc-training/$NAME"
mkdir -p "$WORK"
cp -n "$SRC/app.py" "$SRC/requirements.txt" "$SRC/.gitignore" "$SRC/README.md" "$WORK/"
cd "$WORK"

if [[ ! -d .git ]]; then
  git init -q && git add . && git commit -qm "Initial commit"
fi
if [[ ! -f .clever.json ]]; then
  clever create --type python --org "$ORG" --region "$ZONE" "$NAME"
fi

clever env set CC_PYTHON_MODULE app:app
clever env set CC_PYTHON_VERSION 3.13
clever env set CC_HEALTH_CHECK_PATH /health
clever deploy --same-commit-policy restart

if $WITH_DB; then
  clever addon create postgresql-addon "$NAME-pg" --plan dev --region "$ZONE" --org "$ORG"
  clever service link-addon "$NAME-pg"
  clever restart
fi

clever domain
echo "Done. App folder: $WORK"
