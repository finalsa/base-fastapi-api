sudo apt install python3-pip -y
sudo apt install python3-virtualenv -y
sudo apt-get install nginx -Y
sudo apt-get install libmysqlclient-dev -y


pip3 install -r requirements.txt

pip3 install gunicorn uvicorn

./venv/bin/python3 ./setup/nlsetup.py
touch /etc/nginx/sites-available/app
sudo cat ./setup/nginx.conf  > /etc/nginx/sites-available/app

sudo ln -s /etc/nginx/sites-available/app /etc/nginx/sites-enabled/
sudo systemctl restart nginx.service

sudo cat ./setup/app.service > /etc/systemd/system/app.service
sudo cat ./setup/celery.service > /etc/systemd/system/celery.service

sudo systemctl daemon-reload

sudo systemctl start app.service
sudo systemctl start celery.service
