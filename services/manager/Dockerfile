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

WORKDIR $INSTALL_PATH
