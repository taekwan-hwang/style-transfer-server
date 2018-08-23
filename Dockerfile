FROM ubuntu:16.04

LABEL maintainer "xorhks0005@gmail.com"

# Update packages, Install dependencies
RUN \
  apt-get update && \
  apt-get upgrade && \
  apt-get install -y software-properties-common && \
  add-apt-repository ppa:jonathonf/python-3.6 && \
  apt-get update && \
  apt-get install -y git python3.6 python3-pip

# Install python system-level packages
RUN python3.6 -m pip install pipenv
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

# clone repository, Run flask app
RUN \
  git clone https://github.com/taekwan-hwang/style-transfer-server.git
WORKDIR /style-transfer-server
RUN pipenv install

# Configuration and start up
COPY .env .
