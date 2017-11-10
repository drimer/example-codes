import injector
from flask.app import Flask
from flask_injector import FlaskInjector

from database import DatabaseInterface, db
from people.blueprint import BlueprintFactory as PeopleBluePrintFactory

__all__ = ['DIContainer']


class DatabaseModule(injector.Module):
    @injector.singleton
    @injector.provider
    def provide_db(self) -> DatabaseInterface:
        return db


class DIContainer(FlaskInjector):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            app = Flask(__name__)

            app.register_blueprint(PeopleBluePrintFactory.create())

            flask_injector = FlaskInjector(
                app=app,
                modules=[DatabaseModule(), ],
            )

            app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', False)
            db.init_app(app)

            with app.app_context():
                db.create_all()

            cls._instance = flask_injector

        return cls._instance
