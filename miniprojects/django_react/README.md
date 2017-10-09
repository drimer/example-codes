ReactJS - Django app
====================

This is an example of how to use ReactJS, Django and Docker to build a web app.

Set up
======

This app uses docker-compose, which can be used as a management command.

Steps to set it up:

- Install Docker and docker-compose: https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/

- Build all necessary infrastructure with:

```
$ docker-compose build
```

- Kick off your dev environment with:

```
$ docker-compose up
```

Now you have the web up and running on http://localhost/


Alternatively to the last step, you can run the app in the backgroun and check the logs only when
necessary as follows:

```
$ docker-compose up -d  # to run in the background
$ docker-compose logs -f  # to check the logs
```

Updating frontend libraries
===========================

If you need to edit any dependencies for the UI, you'll need to re-created the
`node_modules/` folder and commit those changes too. You can do this with the
following steps.

- Build the docker images with:

```
$ docker-compose build
```

- Re-build the UI's dependencies from the Docker image with:

```
$ docker run -tid djangoreact_web_frontend bash
$ pushd web_frontend
$ docker cp $(docker ps | grep djangoreact_web_frontend | cut -f1 -d' '):/src/node_modules .
$ popd
$ docker kill $(docker ps | grep djangoreact_web_frontend | cut -f1 -d' ')
```
