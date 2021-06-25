git pull
. venv/bin/activate
pip3 install -r requirements.txt
deactivate
sudo systemctl restart app
sudo systemctl restart celery
sudo systemctl status app
sudo systemctl status celery