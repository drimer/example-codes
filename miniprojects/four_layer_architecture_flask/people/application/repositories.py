from people.db.models import Person


class PersonRepository:
    def get_all(self, **filter) -> list:
        if not filter:
            return Person.query.all()

        return Person.query.filter_by(**filter)

    def get_count(self, **filter) -> int:
        return self.get_all(**filter).count()

    def create(self, **attributes) -> Person:
        return Person(
            **attributes
        )