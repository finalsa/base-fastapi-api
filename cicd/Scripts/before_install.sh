#!/bin/bash

echo "" > /home/ec2-user/.env
export AWS_DEFAULT_REGION=us-east-1
echo AWS_DEFAULT_REGION=us-east-1 >> /home/ec2-user/.env
SECRET_STRING=$(aws secretsmanager get-secret-value --secret-id changelog_bot --query SecretString --output text --region ${AWS_DEFAULT_REGION})
CI_REGISTRY=($(echo $SECRET_STRING | jq -r '.CI_REGISTRY'))
CI_JOB_TOKEN=($(echo $SECRET_STRING | jq -r '.CI_JOB_TOKEN'))
echo CI_REGISTRY=$CI_REGISTRY >> /home/ec2-user/.env
echo $SECRET_STRING | jq -r '.DB_URL'           | echo DB_URL=$(cat)            >> /home/ec2-user/.env
echo PORT=80 >> /home/ec2-user/.env
echo ENV=prod >> /home/ec2-user/.env
echo APP_NAME=base_api >> /home/ec2-user/.env

echo $CI_JOB_TOKEN | docker login --username gitlab-ci-token --password-stdin $CI_REGISTRY

set +e 
sudo yum install jq -y
docker rm -vf $(docker ps -a -q)
docker rmi -f $(docker images -a -q)
echo ok