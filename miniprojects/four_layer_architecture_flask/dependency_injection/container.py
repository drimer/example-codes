from flask.app import Flask
from flask_injector import FlaskInjector
from injector import Binder, Module, provider, singleton

from database import DatabaseInterface
from people.blueprint import BlueprintFactory as PeopleBluePrintFactory
from people.controllers import PersonService


class PeopleModule(Module):
    @singleton
    @provider
    def provide_person_service(self) -> PersonService:
        return PersonService()


def configure(binder: Binder):
    binder.bind(
        DatabaseInterface,
        to=DatabaseInterface(),
    )


class DIContainer(FlaskInjector):
    @classmethod
    def create_app(cls):
        app = Flask(__name__)

        app.register_blueprint(PeopleBluePrintFactory.create())

        FlaskInjector(
            app=app,
            modules=[configure, PeopleModule],
        )

        return app
