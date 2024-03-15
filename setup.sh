#!/bin/bash

# Construire l'image de l'API
docker build -t mon_api_container:latest .

# Construire les images des tests
docker build -t authentication_test -f Dockerfile.authentication_test .
docker build -t authorization_test -f Dockerfile.authorization_test .
docker build -t content_test -f Dockerfile.content_test .

# Lancer Docker Compose pour exécuter les tests
docker-compose up
