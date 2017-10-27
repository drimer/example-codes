from dependency_injector import providers
from flask_sqlalchemy import SQLAlchemy

from flask_app import create_app
from people.blueprint import BlueprintFactory


class DIContainer(object):
    main_app = providers.Callable(
        create_app,
        SQLAlchemy(),
        (
            BlueprintFactory.create(),
        )
    )
