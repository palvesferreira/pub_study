#!/bin/bash
set -e
docker-compose up -d "$@" # --build # frontend
# docker-compose logs -f backend -n 100
