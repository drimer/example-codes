from datetime import datetime

from injector import inject

from database import DatabaseInterface
from people.db.models import Person


class PersonService(object):
    @inject
    def __init__(self, db: DatabaseInterface):
        self.db = db

    def find_by_id(self, id):
        return 'found'

    def create(self, data):
        qry = Person.query.filter_by(phone_number=data['phone_number'])
        if qry.count():
            return None

        entity = Person(
            first_name=data['first_name'],
            phone_number=data['phone_number'],
            created=datetime.utcnow(),
        )

        self.db.session.add(entity)
        self.db.session.commit()

        return entity
