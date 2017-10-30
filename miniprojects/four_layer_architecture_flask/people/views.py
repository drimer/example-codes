from injector import inject

from database import DatabaseInterface
from people.controllers import PersonService


@inject
def create_person(db: DatabaseInterface, person_service: PersonService):
    return person_service.find_by()
