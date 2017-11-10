from datetime import datetime
from unittest import mock

import pytest

from people.application.services import PersonService


@pytest.fixture
def db_interface():
    return mock.MagicMock()


@pytest.fixture
def person_repository():
    return mock.MagicMock()


def test_that_get_all_returns_everything(
        db_interface, person_repository,
):
    existing_people = (
        {'name': 'John'},
        {'name': 'Smith'},
    )
    person_repository.get_all.return_value = existing_people

    service = PersonService(db_interface, person_repository)
    results = service.get_all()

    assert results == existing_people


def test_that_create_creates_new_person(
        db_interface, person_repository,
):
    new_person_data = {
        'phone_number': '07512341234',
        'first_name': 'John',
        'last_name': 'Smith',
        'created': datetime.utcnow(),
    }
    new_db_entity = 'db_entity'

    person_repository.get_count.return_value = 0
    person_repository.create.return_value = new_db_entity

    service = PersonService(db_interface, person_repository)
    result = service.create(new_person_data)

    db_interface.add.assert_called_once_with(new_db_entity)
    db_interface.commit.assert_called_once_with()

    assert result == new_db_entity


def test_that_create_does_not_create_peson_when_phone_is_taken(
        db_interface, person_repository,
):
    new_person_data = {
        'phone_number': '07512341234',
    }

    person_repository.get_count.return_value = 1

    service = PersonService(db_interface, person_repository)
    result = service.create(new_person_data)

    assert result is None
