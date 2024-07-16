#!/usr/bin/env bash
# This script sets up my web servers for the deployment of web_static.

# Install nginx if not already installed
if ! dpkg-query -W -f='${Status}' nginx | grep -q "ok installed"
then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

# Create necessary files and directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/current

echo -e "
<html>
    <head>
    </head>
    <body>
        <h1>Joseph&#39;s web page</h1>
    </body>
</html>
" > sudo tee /data/web_static/releases/test/index.html

sudo ln -s /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data

# Update the Nginx configuration
echo -e "
server {
    listen 80;
    listen [::]:80;

    server_name devjoseph.tech www.devjoseph.tech;
    
    location /hbnb_static {
        alias /data/web_static/curent/;
    }
" > sudo tee /etc/nginx/sites-available/hbnb_static

sudo ln -s /etc/nginx/sites-available/hbnb_static /etc/nginx/sites-enabled/hbnb_static

sudo service nginx restart
