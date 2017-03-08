from flask import url_for

import pytest

from test_general import USER

@pytest.mark.usefixtures("db")
class TestUsers():

    # Test that user registration works
    def test_register(self, client):
        VALID_USER = {
            "username": USER["username"],
            "password": USER["password"],
            "pwd": USER["password"]
        }

        INVALID_USER = {
            "username": "user1",
            "password": "password",
            "pwd": ""
        }

        response = client.post("/register", data=INVALID_USER)
        assert "Passwords do not match" in response.data

        response = client.post("/register", data=VALID_USER)
        assert "User registered" in response.data

        response = client.post("/register", data=VALID_USER)
        assert "Username taken" in response.data

    # Test that user logins work
    def test_login(self, client):
        VALID_USER = {
            "username": USER["username"],
            "password": USER["password"]
        }

        INVALID_USER = {
            "username": "user2",
            "password": ""
        }

        response = client.post("/login", data=INVALID_USER)
        assert "User does not exist" in response.data

        INVALID_USER["username"] = VALID_USER["username"]
        response = client.post("/login", data=INVALID_USER)
        assert "Invalid credentials" in response.data

        response = client.post("/login", data=VALID_USER)
        assert response.status_code == 302
        assert response.location == url_for("index", _external=True)
