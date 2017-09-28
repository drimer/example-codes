ReactJS - Django app
====================

This is an example of how to use ReactJS, Django and Docker to build a web app.

Set up
======

This app uses docker-compose, which can be used as a management command.

Steps to set it up:

- Install docker-compose.

- Build the docker images with: `$ docker-compose build`

- Take the UI's dependencies from the Docker image with:

```
$ docker run -tid djangoreact_web_frontend bash
$ pushd web_frontend
$ docker cp $(docker ps | grep djangoreact_web_frontend | cut -f1 -d' '):/src/node_modules .
$ popd
$ docker kill $(docker ps | grep djangoreact_web_frontend | cut -f1 -d' ')
```

- Create a new file called `env_variables.env` copied from `env_variables.env.template`
and adjust according to the environment you're setting up.

- Kick off the app: `$ docker-compose up`
