import json

import flask
import pytest

import app as webapp
from models import Person
from models import db
from test.utils import assert_response_has_correct_fields


@pytest.fixture
def person(client):
    entity = Person(
        first_name='John',
        phone_number='+447363638787',
    )

    db.session.add(entity)
    db.session.commit()

    return entity


def test_post_person_creates_new_person_when_doesnt_exist(client):
    url = flask.url_for('person.post_person')
    first_name = 'John'
    phone_number = '+447356562323'

    json_data = json.dumps({
        'first_name': first_name,
        'phone_number': phone_number,
    })
    resp = client.post(
        url, content_type='application/json',
        data=json_data,
    )
    assert resp.status_code == 200

    entities = Person.query.all()
    assert len(entities) == 1
    entity = entities[0]
    assert entity.first_name == first_name
    assert entity.phone_number == phone_number

    assert_response_has_correct_fields(resp)


def test_post_person_does_not_create_when_exists(client, person):
    url = flask.url_for('person.post_person')

    json_data = json.dumps({
        'first_name': person.first_name,
        'phone_number': person.phone_number,
    })
    resp = client.post(
        url, content_type='application/json',data=json_data,
    )
    assert resp.status_code == 200

    entities = Person.query.all()
    assert len(entities) == 1

    assert_response_has_correct_fields(resp)
