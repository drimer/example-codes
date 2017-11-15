from marshmallow import Schema, fields


def phone_number_validator(phone_number) -> bool:
    """
    Validation for phone numbers. Dull function that just serves as an
    example. It should return False if the value isn't a valid phone number.
    """
    del phone_number
    return True


class PersonSchema(Schema):
    first_name = fields.String(required=True)
    phone_number = fields.String(required=True, validate=phone_number_validator)

    class Meta:
        fields = ['id', 'created', 'first_name', 'phone_number']
