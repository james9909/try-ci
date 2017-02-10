from app import app as test_app
import pytest

@pytest.fixture(scope="session")
def app(request):
    app = test_app
    app.config["TESTING"] = True

    ctx = app.test_request_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app

@pytest.fixture(scope="session")
def client(app):
    return app.test_client()
