from unittest import mock

import pytest

from people.presentation.views import PeopleListOrCreateView


@pytest.fixture
def person_service():
    return mock.MagicMock()


@pytest.fixture
def person_serialiser():
    return mock.MagicMock()


@pytest.fixture
def person_parser():
    return mock.MagicMock()


@pytest.fixture
def request():
    return mock.MagicMock()


def test_get_returns_all_matches(
        person_service, person_serialiser, person_parser, request,
):
    existing_people = [1, 2, 3]
    serialised_people = ["1", "2", "3"]

    person_service.get_all.return_value = existing_people
    person_serialiser.serialise.return_value = serialised_people
    request.is_json.return_value = True

    view = PeopleListOrCreateView(person_service, person_serialiser, person_parser, request)
    result = view.get()

    person_serialiser.serialise.assert_called_once_with(view.schema, existing_people, many=True)
    assert result == serialised_people


def test_post_creates_new_person(
        person_service, person_serialiser, person_parser, request,
):
    parsed_person = ["one", "two", "three"]
    object_person = [1, 2, 3]
    serialised_person = ["1", "2", "3"]

    person_parser.parse.return_value = parsed_person
    person_service.create.return_value = object_person
    person_serialiser.serialise.return_value = serialised_person
    request.is_json.return_value = True

    view = PeopleListOrCreateView(person_service, person_serialiser, person_parser, request)
    result = view.post()

    person_parser.parse.assert_called_once_with(view.schema)
    person_service.create.assert_called_once_with(parsed_person)
    person_serialiser.serialise.assert_called_once_with(view.schema, object_person)
    assert result == (serialised_person, 201)
