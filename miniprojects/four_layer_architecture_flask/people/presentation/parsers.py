from flask import jsonify
from injector import inject

from common.request import Request
from people.presentation.schemas import PersonSchema


class PersonParser(object):
    @inject
    def __init__(self, person_schema: PersonSchema, request: Request):
        self.schema = person_schema
        self.request = request

    def parse(self) -> object:
        json = self.request.get_json()
        if not json:
            return jsonify({
                'message': 'Json data not received',
            }), 400
        json_data, errors = self.schema.load(json)
        if errors:
            return jsonify({
                'message': 'BadRequest',
                'errors': errors,
            }), 400

        return json_data
