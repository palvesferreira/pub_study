#!/bin/bash
# filepath: /workspace/frontend/setup_frontend.sh

set -e

npm install

if [ ! -f "package.json" ]; then
  echo "Initialize Svelte project (non-interactive)"
  npx sv create
  echo "Svelte project initialized in /workspace/frontend"
fi
