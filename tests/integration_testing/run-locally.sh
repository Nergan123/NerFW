#!/bin/sh

docker-compose -f docker-compose.selenium.yml build
docker-compose -f docker-compose.selenium.yml up -d

docker-compose -f docker-compose.integration.yml build
docker-compose -f docker-compose.integration.yml up --abort-on-container-exit

docker-compose -f docker-compose.selenium.yml down
docker-compose -f docker-compose.integration.yml down