from flask_sqlalchemy import SQLAlchemy

__all__ = ['DatabaseInterface', 'db']


class DatabaseInterface(object):
    pass


class SqlAlchemyInterface(SQLAlchemy, DatabaseInterface):
    pass


db = SqlAlchemyInterface()
