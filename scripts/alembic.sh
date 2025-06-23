#!/bin/bash

set -e

cd backend
alembic "$@"
# upgrade head
# revision --autogenerate -m "initial"
