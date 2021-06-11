#!/usr/bin/env bash
# Preparing server for deployment

sudo apt-get -y update
sudo apt-get -y upgrade

sudo apt-get -y install nginx

# Maybe don't need sudo?
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

sudo echo "Howdy!" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sfn /data/web_static/releases/test/ /data/web_static/current

sudo chown -hR ubuntu:ubuntu /data

# Edit the nginx cfg file
find="^\tlocation / {"
replace="\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n\n\tlocation / {"
sudo sed -i "s@${find}@${replace}@" /etc/nginx/sites-available/default

sudo service nginx restart

exit 0
