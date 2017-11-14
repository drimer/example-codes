import json
from datetime import datetime

import pytest

from people.db.models import Person


@pytest.fixture
def people(test_db):
    person_1 = Person(
        id=1,
        first_name='John',
        phone_number='07512341234',
        created=datetime(year=2017, month=2, day=1, hour=13, minute=15, second=9)
    )
    person_2 = Person(
        id=2,
        first_name='Mike',
        phone_number='07556785678',
        created=datetime(year=2015, month=5, day=4, hour=12, minute=30, second=40)
    )
    people = [person_1, person_2]

    test_db.session.add_all(people)
    test_db.session.commit()

    return people


def test_get_person_returns_all_people(flask_client, people):
    response = flask_client.get('/person')

    expected_data = sorted(
        [
            {
                'id': 1,
                'created': '2017-02-01T13:15:09+00:00',
                'first_name': 'John',
                'phone_number': '07512341234',
            },
            {
                'id': 2,
                'created': '2015-05-04T12:30:40+00:00',
                'first_name': 'Mike',
                'phone_number': '07556785678',
            }
        ],
        key=lambda d: d['id']
    )
    actual_data = sorted(
        json.loads(response.get_data().decode('utf8')),
        key=lambda d: d['id']
    )

    assert actual_data == expected_data


def test_get_person_returns_empty_list_when_no_records(test_db, flask_client):
    del test_db

    response = flask_client.get('/person')

    actual_data = json.loads(response.get_data().decode('utf8'))

    assert actual_data == []
