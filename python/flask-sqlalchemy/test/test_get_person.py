import flask
import pytest

from models import Person, db
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


def test_get_existing_person_returns_200(client, person):
    url = flask.url_for('person.get_person', id=person.id)
    resp = client.get(url)

    assert resp.status_code == 200
    assert Person.query.count() == 1

    assert_response_has_correct_fields(resp)


def test_get_nonexistent_url_returns_404(client):
    url = flask.url_for('person.get_person', id=5656)
    resp = client.get(url)

    assert resp.status_code == 404
