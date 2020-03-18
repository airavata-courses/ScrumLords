FROM node:latest

ENV INSTALL_PATH /user_interface

RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

ADD . /user_interface

RUN npm install

WORKDIR $INSTALL_PATH
