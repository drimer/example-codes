Steps to set up
===============

- Install Python 3
- (optional) Make a virtual environment: `mkvirtualenv -p $(which python3) django-di`
- `pip install -r requirements.txt`

Running the app
===============

`python manage.py runserver <port>`

Running the tests
=================

- `python manage.py test`

How to use the app
==================

One the app is running, you can hit the endpoint /person to perform different actions:

1. Create a person
URL: /person
Request type: POST
Request parameters: name (string), phone_number (string)

2. Edit person
URL: /person/<id>
Request type: PATCH
Request parameters: name (string, optional), phone_number (string, optional)

3. Delete person
URL: /person/<id>
Request type: DELETE
Request parameters: none

4. List people
URL: /person
Request type: GET
Request parameters: none

5. Get Person
URL: /person/<id>
Request type: GET
Request parameters: none
