FROM openjdk:8

ENV INSTALL_PATH /postprocessor

RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

ADD . /postprocessor

RUN apk update && apk add maven wget \
 && wget -O /postprocessor/src/main/resources/pubsub-firestore-development.json https://www.dropbox.com/s/jm7o4s8a0ekdn7d/pubsub-firestore-development.json?dl=1

WORKDIR $INSTALL_PATH
