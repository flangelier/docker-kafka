FROM java:openjdk-8-jre

MAINTAINER Francois Langelier <f.langelier@gmail.com>

ENV DEBIAN_FRONTEND noninteractive
ENV SCALA_VERSION 2.11
ENV KAFKA_VERSION 0.8.2.1
ENV KAFKA_BASE_HOME /opt
ENV KAFKA_HOME "$KAFKA_BASE_HOME"/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION"

EXPOSE 9092

VOLUME /kafka

RUN apt-get update && apt-get install -y \
    wget \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

RUN wget -q http://mirror.sdunix.com/apache/kafka/"$KAFKA_VERSION"/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz -O "$KAFKA_HOME".tgz \
    && tar xfz "$KAFKA_HOME".tgz -C "$KAFKA_BASE_HOME" \
    && rm "$KAFKA_HOME".tgz \
    && cp "$KAFKA_HOME"/config/server.properties /kafka/server.properties

CMD "$KAFKA_HOME"/bin/kafka-server-start.sh /kafka/server.properties"$BROKER_ID"
