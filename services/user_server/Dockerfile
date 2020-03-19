FROM node:latest

ENV INSTALL_PATH /user_server

RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

ADD . /user_server

RUN npm install

WORKDIR $INSTALL_PATH
