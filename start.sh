source ./venv/bin/activate
pip freeze > requirements.txt
export DYLD_LIBRARY_PATH=/usr/local/mysql/lib/
cd app
cd app
python3 main.py