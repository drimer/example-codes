from injector import inject

from common.request import Request
from people.presentation.schemas import PersonSchema


class ParserError(Exception):
    def __init__(self, message, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.message = message


class PersonParser(object):
    @inject
    def __init__(self, person_schema: PersonSchema, request: Request):
        self.schema = person_schema
        self.request = request

    def parse(self) -> object:
        json = self.request.get_json()
        json_data, errors = self.schema.load(json)

        if errors:
            raise ParserError(str(errors))

        return json_data
