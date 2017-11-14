from injector import inject
from marshmallow.schema import Schema

from common.request import Request


class JsonParser:
    @inject
    def __init__(self, request: Request):
        self.request = request

    def parse(self, schema: Schema) -> object:
        json = self.request.get_json()
        json_data, errors = schema.load(json)

        if errors:
            raise ParserError(str(errors))

        return json_data


class ParserError(Exception):
    def __init__(self, message, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.message = message
