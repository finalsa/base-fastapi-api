#!/bin/bash

pip freeze > requirements.txt
export DYLD_LIBRARY_PATH=/usr/local/mysql/lib/
export PATH=/usr/lib/postgresql/X.Y/bin/:$PATH
alembic upgrade head
python3 /app/app/main.py