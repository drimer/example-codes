from schemas import PersonSchema


def test_required_fields():
    json_data = {'optional': '4'}
    data, errors = PersonSchema().load(json_data)

    assert errors == {
        'first_name': ['Missing data for required field.'],
        'phone_number': ['Missing data for required field.'],
    }
