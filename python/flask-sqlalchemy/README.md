Flask + SQLAlchemy
===============

Notes
-----

This is a very simple example of a webapp that provides an API to create and
get people's details, by using Flask and SQLAlchemy.


Setting it up
-------------

> mkvirtualenv -p $(which python3) flask-sqlalchemy
> pip install -r dev-requirements.txt


Running the tests
-----------------

Run the following command:
> py.test


Running the app
----------------

Run the following command:
> FLASK_APP=app.py flask run


Testing the app manually
------------------------

In order to create a new person, replacing {{first_name}} and
{{phone_number}}:

> curl -X POST -H "Content-Type: application/json" -d '{"first_name": "{{first_name}}", "phone_number": "{{phone_number}}"}' http://localhost:5000/person/

This should get a response like the following:

    {
      "id": 1,
      "created": "2017-02-02T12:25:14.751471+00:00",
      "first_name": "{{first_name}}",
      "phone_number": "{{phone_number}}"
    }

If we take the id and place it in a GET request:

> curl -X GET -H "Accept: application/json" http://localhost:5000/person/{{id}}

We get a response like the following:

    {
      "id": 1,
      "created": "2017-02-02T12:25:14.751471+00:00",
      "first_name": "{{first_name}}",
      "phone_number": "{{phone_number}}"
    }
