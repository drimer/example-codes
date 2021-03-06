import json
from datetime import datetime

import pytest

from people.db.models import Person


@pytest.fixture
def people(test_db):
    person_1 = Person(
        id=3,
        first_name='John',
        phone_number='1',
        created=datetime(year=2017, month=2, day=1, hour=13, minute=15, second=9)
    )
    person_2 = Person(
        id=4,
        first_name='Mike',
        phone_number='2',
        created=datetime(year=2015, month=5, day=4, hour=12, minute=30, second=40)
    )
    people = [person_1, person_2]

    test_db.session.add_all(people)
    test_db.session.commit()

    return people


def test_create_new_person(flask_client, people):
    post_data = {
        'first_name': 'Hermione',
        'phone_number': '07598765432',
    }
    response = flask_client.post(
        '/person',
        data=json.dumps(post_data),
        content_type='application/json',
    )

    assert response.status_code == 201
    data = json.loads(response.get_data().decode('utf8'))
    assert data['first_name'] == post_data['first_name']
    assert data['phone_number'] == post_data['phone_number']
    assert 'id' in data
    assert 'created' in data


def test_create_endpoint_only_takes_json_requests(flask_client):
    response = flask_client.post('/person', data={})
    assert response.status_code == 415


def test_create_endpoint_returns_400_when_request_is_incorrect(flask_client):
    post_data = {'incorrect_field': 'incorrect data'}
    response = flask_client.post(
        '/person',
        data=post_data,
        content_type='application/json',
    )

    data = json.loads(response.get_data().decode('utf8'))
    assert 'errors' in data


def test_create_endpoint_returns_409_when_person_already_exists(flask_client, people):
    post_data = {
        'first_name': people[0].first_name,
        'phone_number': people[0].phone_number,
    }
    response = flask_client.post(
        '/person',
        data=json.dumps(post_data),
        content_type='application/json',
    )

    assert response.status_code == 409
