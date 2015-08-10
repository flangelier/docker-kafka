[![dockeri.co](http://dockeri.co/image/flangelier/kafka)](https://registry.hub.docker.com/u/flangelier/kafka/)

[![stars](https://img.shields.io/github/stars/apache/kafka.svg) ![forks](https://img.shields.io/github/forks/apache/kafka.svg) ![issues](https://img.shields.io/github/issues/apache/kafka.svg) ](https://github.com/apache/kafka)

# Supported tags and respective `Dockerfile` links
- [`0.8.2.1`,`latest`(0.8.2.1/broker/Dockerfile)](https://github.com/flangelier/docker-kafka/0.8.2.1/broker/Dockerfile)

# What is Kafka?
Apache Kafka is publish-subscribe messaging rethought as a distributed commit log.
## Fast
A single Kafka broker can handle hundreds of megabytes of reads and writes per second from thousands of clients.
## Scalable
Kafka is designed to allow a single cluster to serve as the central data backbone for a large organization. It can be elastically and transparently expanded without downtime. Data streams are partitioned and spread over a cluster of machines to allow data streams larger than the capability of any single machine and to allow clusters of co-ordinated consumers
## Durable
Messages are persisted on disk and replicated within the cluster to prevent data loss. Each broker can handle terabytes of messages without performance impact.
Distributed by Design
Kafka has a modern cluster-centric design that offers strong durability and fault-tolerance guarantees.

# How to use this image?
### Zookeeper
This image need a zookeeper server to run. Although, you could use any zookeeper, we suggest you to use this docker image [wurstmeister/zookeeper:latest](https://hub.docker.com/r/wurstmeister/zookeeper/).

    docker run -d -p 2181:2181 -P --name zookeeper wurstmeister/zookeeper:latest

### Suggested way to use the image
If you want to use the image the way it was meant to be, you chould pull those images

    docker pull busybox:latest
    docker pull flangelier/configure
    docker pull flangelier/kafka

Then you should execute those lines for launching a broker

    export CURRENT_BROKER_ID=1

    docker run -d -v /kafka --name kafka-data-$CURRENT_BROKER_ID busybox:latest
    docker run --rm --volumes-from kafka-data-$CURRENT_BROKER_ID flangelier/configure broker.id=$CURRENT_BROKER_ID
    docker run -d --volumes-from kafka-data-$CURRENT_BROKER_ID --link zookeeper:zk -P --name kafka-broker-$CURRENT_BROKER_ID flangelier/kafka

If you want more brokers, just rerun the same lines as many time as you want, just don't forget to change the CURRENT_BROKER_ID value everytime you want a new broker

# License

No license selected yet.

# Supported Docker versions

This image is officially supported on Docker version 1.7.1.

Support for older versions (down to 1.0) is provided on a best-effort basis.

# User Feedback

## Documentation

This is the only documentation available at the moment.

## Issues

If you have any problems with or questions about this image, please contact us through a [GitHub issue](https://github.com/flangelier/docker-kafka/issues).

## Contributing

You are invited to contribute new features, fixes, or updates, large or small; we are always thrilled to receive pull requests, and do our best to process them as fast as we can.

Before you start to code, we recommend discussing your plans through a [GitHub issue](https://github.com/flangelier/docker-kafka/issues), especially for more ambitious contributions. This gives other contributors a chance to point you in the right direction, give you feedback on your design, and help you find out if someone else is working on the same thing.
