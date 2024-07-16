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
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/current/

echo -e "<html>
    <head>
    </head>
    <body>
        <h1>Joseph&#39;s web page</h1>
    </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

for file in /data/web_static/current/*
do
    if [ -L "$file" ]
    then
	    rm /data/web_static/current/*
    fi
done

sudo ln -s /data/web_static/releases/test/* /data/web_static/current

sudo chown -R ubuntu:ubuntu /data

# Update the Nginx configuration
replace_string="server_name devjoseph.tech www.devjoseph.tech;\n\tlocation \
	/hbnb_static {\n\t\talias /data/web_static/current/;\
	\n\t\tindex index.html;\n\t}"

sudo sed -i "s|server_name _;|${replace_string}|" /etc/nginx/sites-enabled/default

# Restart nginx server

sudo service nginx restart
