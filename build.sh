#!/bin/bash

#Clear ._ files 
find . -type f -name '._*' -delete

#Variables
ECR_URI="720332985926.dkr.ecr.us-east-1.amazonaws.com"
DOCKER_USER=${1}
IMG_TAG=${2}

#Docker login
docker login

#Login to AWS
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin $ECR_URI

#Build and push to both registries
docker buildx build --platform linux/amd64 --provenance=false \
        -t $DOCKER_USER/task-pilot:$IMG_TAG -t $ECR_URI/task-pilot:$IMG_TAG --push .

#Dispaly message
echo "------ Image pushed to ECR ------"