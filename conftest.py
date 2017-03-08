from app import app as test_app

import os
import pytest

from utils import initialize

@pytest.fixture(scope="session")
def app(request):
    app = test_app

    ctx = app.test_request_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app

@pytest.fixture(scope="session")
def client(app):
    return app.test_client()

@pytest.fixture(scope="class")
def db(request):
    DATABASE = "database.db"

    db = initialize.initialize_tables()

    def teardown():
        db.close()
        os.remove(DATABASE)

    request.addfinalizer(teardown)

    return db
