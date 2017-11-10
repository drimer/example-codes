from flask_sqlalchemy import SQLAlchemy

__all__ = ['DatabaseInterface', 'db']


class DatabaseInterface(object):
    def add(self, entity: object):
        raise NotImplementedError

    def commit(self):
        raise NotImplementedError


class SqlAlchemyInterface(SQLAlchemy, DatabaseInterface):
    def add(self, entity: object):
        self.session.add(entity)

    def commit(self):
        self.session.commit()


db = SqlAlchemyInterface()
