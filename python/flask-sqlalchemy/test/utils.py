import json


def assert_response_has_correct_fields(response):
    data = json.loads(response.data.decode('utf-8'))
    assert 'created' in data
    assert 'id' in data
    assert 'first_name' in data
    assert 'phone_number' in data
