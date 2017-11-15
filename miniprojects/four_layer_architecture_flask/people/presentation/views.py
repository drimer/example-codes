from flask.json import jsonify
from flask.views import MethodView
from injector import inject

from common.parsers import ParserError, JsonParser
from common.request import Request
from common.views import JsonViewMixin
from people.application.services import PersonService
from people.presentation.schemas import PersonSchema
from common.serialisers import JsonSerialiser


class PeopleListOrCreateView(JsonViewMixin, MethodView):
    schema = PersonSchema()

    @inject
    def __init__(
            self,
            person_service: PersonService,
            json_serialiser: JsonSerialiser,
            json_parser: JsonParser,
            request: Request,
    ):
        self.person_service = person_service
        self.json_serialiser = json_serialiser
        self.json_parser = json_parser
        self.request = request

    def get(self):
        person_results = self.person_service.get_all()
        return self.json_serialiser.serialise(self.schema, person_results, many=True)

    def post(self):
        try:
            person_json = self.json_parser.parse(self.schema)
        except ParserError as exc:
            return jsonify({
                'message': 'Error occurred while parsing data received.',
                'errors': [exc.message],
            }), 400

        try:
            new_person = self.person_service.create(person_json)
        except PersonService.AlreadyExists:
            return jsonify({
                'message': 'Person already exists',
            }), 409

        return self.json_serialiser.serialise(self.schema, new_person), 201
