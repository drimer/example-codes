import json
from unittest import mock

import pytest

from people.presentation.parsers import PersonParser


@pytest.fixture
def person_schema():
    return mock.MagicMock()


@pytest.fixture
def request():
    return mock.MagicMock()


def test_that_returns_error_when_json_is_empty(person_schema, request):
    request.get_json.return_value = None

    parser = PersonParser(person_schema, request)
    response, status_code = parser.parse()

    assert status_code == 400

    data = json.loads(response.get_data().decode('utf8'))
    assert data['message'] == 'Json data not received'


def test_that_returns_errors_when_json_contains_invalid_data(
        person_schema, request,
):
    json_data = ''
    errors = {'field_1': 'Missing field'}
    person_schema.load.return_value = (json_data, errors)

    parser = PersonParser(person_schema, request)
    response, status_code = parser.parse()

    assert status_code == 400

    data = json.loads(response.get_data().decode('utf8'))
    assert data['errors'] == errors
