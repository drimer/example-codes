from flask.views import MethodView
from injector import inject

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
    ):
        self.person_service = person_service
        self.person_serialiser = person_serialiser
        self.person_parser = person_parser

    def get(self):
        person_results = self.person_service.get_all()
        return self.person_serialiser.serialise(person_results, many=True)

    def post(self):
        person_json = self.person_parser.parse()
        new_person = self.person_service.create(person_json)
        return self.person_serialiser.serialise(new_person)
