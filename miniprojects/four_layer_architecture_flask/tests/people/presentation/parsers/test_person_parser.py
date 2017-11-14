from unittest import mock

import pytest

from people.presentation.parsers import PersonParser, ParserError


@pytest.fixture
def person_schema():
    return mock.MagicMock()


@pytest.fixture
def request():
    return mock.MagicMock()



def test_that_raises_exception_when_json_is_empty(person_schema, request):
    request.get_json.return_value = {}
    person_schema.load.return_value = None, 'Something wrong'

    parser = PersonParser(person_schema, request)

    with pytest.raises(ParserError):
        parser.parse()

    person_schema.load.assert_called_with({})


def test_that_returns_errors_when_json_contains_invalid_data(
        person_schema, request,
):
    json_data = ''
    errors = "Something wrong"
    person_schema.load.return_value = (json_data, errors)

    parser = PersonParser(person_schema, request)

    with pytest.raises(ParserError) as exception:
        parser.parse()

        assert exception.message == errors
