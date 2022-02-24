#!/bin/bash
# Run App

docker pull ${docker_repository}/base-api:latest
docker-compose -f /home/ec2-user/docker-compose.prod.yml --env-file /home/ec2-user/.env up -d
