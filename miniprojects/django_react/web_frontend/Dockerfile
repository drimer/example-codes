# This image generates a node_modules/ folder with necessary JS libraries.
# Before running a container with a volume overriding /src, you should copy
# nodule_modules using `docker cp container:/src/node_modules .`

FROM ubuntu:xenial

ADD . /src
RUN rm -rf /src/node_modules
WORKDIR /src

RUN apt-get update
RUN apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get install -y nodejs

RUN npm install
# RUN npm run build

EXPOSE 3000

ENV BASE_URL "http://localhost"

CMD npm run start