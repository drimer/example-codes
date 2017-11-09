from flask_sqlalchemy import SQLAlchemy


class DatabaseInterface(object):
    pass


class SqlAlchemyInterface(SQLAlchemy, DatabaseInterface):
    pass
