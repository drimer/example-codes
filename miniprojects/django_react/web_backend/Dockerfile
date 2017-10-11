# This image relies on having the whole project mounted on /src
# Use -v option for mounting.

FROM ubuntu:trusty

ADD . /src
WORKDIR /src

RUN apt-get update
RUN apt-get install -y python-pip
RUN pip install -r /src/requirements.txt

EXPOSE 80

ENV DOMAIN "localhost"

CMD python manage.py runserver 0.0.0.0:80