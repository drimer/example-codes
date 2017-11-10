import pytest

from dependency_injection.container import DIContainer


@pytest.yield_fixture(autouse=True)
def test_flask_app():
    return DIContainer().app


@pytest.yield_fixture(autouse=True)
def test_app_context(test_flask_app):
    with test_flask_app.app_context() as context:
        yield context


@pytest.yield_fixture(autouse=True)
def test_request_context(test_app_context, test_flask_app):
    with test_flask_app.test_request_context():
        yield
