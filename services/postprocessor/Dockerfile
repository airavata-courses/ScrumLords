FROM openjdk:8-jdk-alpine

ENV INSTALL_PATH /postprocessor

RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

ADD . /postprocessor

RUN apk update && apk add maven wget \
 && wget -O /postprocessor/deployment/pubsub-firestore-development.json https://www.dropbox.com/s/51l60y245m60nt1/pubsub-firestore-development.json?dl=1

WORKDIR $INSTALL_PATH
