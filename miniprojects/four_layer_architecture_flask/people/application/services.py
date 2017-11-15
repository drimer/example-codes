from datetime import datetime

from injector import inject

from database import DatabaseInterface
from people.application.repositories import PersonRepository


class PersonService(object):
    class AlreadyExists(Exception):
        pass

    @inject
    def __init__(self, db: DatabaseInterface, repository: PersonRepository):
        self.db = db
        self.repository = repository

    def create(self, data):
        if self.repository.get_count(phone_number=data['phone_number']):
            raise PersonService.AlreadyExists()

        entity = self.repository.create(
            first_name=data['first_name'],
            phone_number=data['phone_number'],
            created=datetime.utcnow(),
        )

        self.db.add(entity)
        self.db.commit()

        return entity

    def get_all(self):
        return self.repository.get_all()
