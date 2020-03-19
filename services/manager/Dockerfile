FROM ubuntu:latest

RUN apt-get update && apt-get install -y apt-utils

ENV INSTALL_PATH /manager

RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

ADD requirements-dev.txt requirements.txt

RUN apt-get update \
  && apt-get install -y --no-install-recommends python3-pip python3-dev python3-setuptools nano wget \
  && pip3 install --upgrade pip\
  && pip3 install -r requirements.txt

ADD . /manager

RUN wget -O /manager/api_manager/firestore/pubsub-firestore-development.json https://www.dropbox.com/s/jm7o4s8a0ekdn7d/pubsub-firestore-development.json?dl=1

WORKDIR $INSTALL_PATH
