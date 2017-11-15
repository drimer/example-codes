from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from injector import provider, inject

from people.presentation.views import create_person


class App(Flask):
    pass


class DatabaseInterface(SQLAlchemy):
    pass


@inject
@provider
def create_app(db: DatabaseInterface) -> App:
    api = App('api')

    blueprints = [create_person]
    for blueprint in blueprints:
        api.register_blueprint(blueprint)

    db.init_app(api)

    with api.app_context():
        db.create_all()

    return api
