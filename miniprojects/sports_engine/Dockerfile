FROM ubuntu:xenial

RUN apt-get update
RUN apt-get install -y --allow-unauthenticated nginx software-properties-common
RUN add-apt-repository -y ppa:ondrej/php
RUN apt-get install -y --allow-unauthenticated php5.6-cli php5.6-fpm

ADD src:/src