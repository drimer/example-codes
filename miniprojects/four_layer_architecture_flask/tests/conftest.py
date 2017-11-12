import pytest
from flask_sqlalchemy import SQLAlchemy

from dependency_injection.container import DIContainer


@pytest.fixture
def test_db():
    return SQLAlchemy()


@pytest.yield_fixture(autouse=True)
def flask_app(test_db):
    app = DIContainer().app

    app.config['DATABASE'] = test_db
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
