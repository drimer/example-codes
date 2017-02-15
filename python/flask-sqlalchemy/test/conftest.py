import pytest

import app as webapp


@pytest.yield_fixture
def client():
    app = webapp.create_app()
    with app.test_request_context() as ctx:
        ctx.push()
        yield app.test_client()
        ctx.pop()
