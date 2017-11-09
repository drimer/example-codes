from injector import inject

from people.application.services import PersonService
from people.presentation.parsers import PersonParser
from people.presentation.serialisers import PersonSerialiser


@inject
def create_person(person_service: PersonService, serialiser: PersonSerialiser,
                  parser: PersonParser):
    person_json = parser.parse()
    new_person = person_service.create(person_json)
    return serialiser.serialise(new_person)


@inject
def get_person(person_service: PersonService, serialiser: PersonSerialiser, pk: int):
    person = person_service.find_by_id(pk)
    return serialiser.serialise(person)