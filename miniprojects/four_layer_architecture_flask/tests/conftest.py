from uuid import uuid4

import pytest

from database import db
from dependency_injection.container import DIContainer


@pytest.fixture
def test_db(flask_app):
    uuid = str(uuid4())
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test-{}.db'.format(uuid)

    db.init_app(flask_app)
    with flask_app.app_context():
        db.create_all()

    return db


@pytest.yield_fixture(autouse=True)
def flask_app():
    app = DIContainer().app

    app.testing = True

    return app


@pytest.yield_fixture(autouse=True)
def app_context(flask_app):
    with flask_app.app_context() as context:
        yield context


@pytest.yield_fixture(autouse=True)
def request_context(app_context, flask_app):
    with flask_app.test_request_context():
        yield


@pytest.fixture
def flask_client(flask_app):
    return flask_app.test_client()
