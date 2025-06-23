#!/bin/bash
set -e
docker-compose --env-file .env.develop -f docker-compose.yml -f docker-compose.develop.yml up -d "$@"
docker-compose --env-file .env.develop -f docker-compose.yml -f docker-compose.develop.yml logs -f backend -n 100
