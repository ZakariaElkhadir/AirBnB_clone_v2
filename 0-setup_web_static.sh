#!/usr/bin/env bash
sudo apt-get -y update
sudo apt-get -y install nginx
sudo service nginx start
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo echo -e "
<html>
  <head>
  </head>
  <body>
    <h1>I am Zakaria Elkhadir, an ALX student.<h1>
  </body>
  </html>" | sudo tee /data/web_static/releases/test/index.html
  sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
  sudo chown -R ubuntu:ubuntu /data/
  path="/etc/nginx/sites-available/default"
  phrase="location /hbnb_static/ {\n\t\talias /data/web_static/current/;\n}\n"
  sudo sed -i "42i $phrase" "$path"
  sudo service nginx restart
  