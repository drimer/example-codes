from flask.json import jsonify
from flask.views import MethodView
from injector import inject

from common.request import Request
from people.application.services import PersonService
from people.presentation.parsers import PersonParser
from people.presentation.serialisers import PersonSerialiser


class PeopleListOrCreateView(MethodView):
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

    def dispatch_request(self, *args, **kwargs):
        if not self.request.is_json():
            return jsonify({
                'message': 'Invalid request. Make sure your content type is application/json',
            }), 415

        return super().dispatch_request(*args, **kwargs)

    def get(self):
        person_results = self.person_service.get_all()
        return self.person_serialiser.serialise(person_results, many=True)

    def post(self):
        person_json = self.person_parser.parse()
        new_person = self.person_service.create(person_json)
        return self.person_serialiser.serialise(new_person)
