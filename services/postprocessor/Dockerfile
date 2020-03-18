FROM openjdk:8-jdk-slim

ENV INSTALL_PATH /postprocessor

RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

ADD . /postprocessor

WORKDIR $INSTALL_PATH
