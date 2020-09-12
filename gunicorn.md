[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/violet.com
ExecStart=/home/ubuntu/violet.com/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/ubuntu/violet.com/ecom.sock ecom.wsgi:applicati$

[Install]
WantedBy=multi-user.target
