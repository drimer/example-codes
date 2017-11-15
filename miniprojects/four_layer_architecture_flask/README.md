Steps to set up
===============

- Install Python 3
- (optional) Make a virtual environment: `mkvirtualenv -p $(which python3) four-layer-architecture-flask`
- `pip install -r requirements.txt`

Running the app
===============

`FLASK_APP=app.py flask run`

Running the tests
=================

- `PYTHONPATH=.:$PYTHONPATH pytest`

How to use the app
==================

Once the app is running, you can hit the endpoint /person to perform different actions:

1. Create a person
URL: /person
Request type: POST
Request parameters: first_name (string), phone_number (string)

1. Get Person
URL: /person/<id>
Request type: GET
Request parameters: none