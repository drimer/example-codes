from flask.json import jsonify
from flask.views import MethodView
from injector import inject

from common.request import Request
from common.views import JsonViewMixin
from people.application.services import PersonService
from people.presentation.parsers import PersonParser, ParserError
from people.presentation.serialisers import PersonSerialiser


class PeopleListOrCreateView(JsonViewMixin, MethodView):
    @inject
    def __init__(
            self,
            person_service: PersonService,
            person_serialiser: PersonSerialiser,
            person_parser: PersonParser,
            request: Request,
    ):
        self.person_service = person_service
        self.person_serialiser = person_serialiser
        self.person_parser = person_parser
        self.request = request

    def get(self):
        person_results = self.person_service.get_all()
        return self.person_serialiser.serialise(person_results, many=True)

    def post(self):
        try:
            person_json = self.person_parser.parse()
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

        return self.person_serialiser.serialise(new_person), 201
