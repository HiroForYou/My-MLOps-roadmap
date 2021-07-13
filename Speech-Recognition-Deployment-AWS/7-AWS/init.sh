#!/bin/bash

sudo apt-get update

# instalamos docker
sudo apt install docker.io

# iniciamos el servicio de Docker
sudo systemctl start docker
sudo systemctl enable docker

# instalamos docker compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# construimos y ejecutamos el contenedor docker
cd ~/server
sudo docker-compose up --build