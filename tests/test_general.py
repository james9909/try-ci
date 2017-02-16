class TestGeneral():
    def test_sanity(self):
        assert True

    def test_register(self, client, db):
        USER = {
            "username": "user1",
            "password": "password",
            "pwd": "hi"
        }

        response = client.post("/register", data=USER)
        assert "Passwords do not match" in response.data

        USER["pwd"] = USER["password"]
        response = client.post("/register", data=USER)
        assert "User registered" in response.data

        response = client.post("/register", data=USER)
        assert "Username taken" in response.data

    def test_login(self, client):
        response = client.post("/login", data={
            "username": "user2",
            "password": "password"
            })
        assert "User does not exist" in response.data

        response = client.post("/login", data={
            "username": "user1",
            "password": "hi"
        })
        assert "Invalid credentials" in response.data

        response = client.post("/login", data={
            "username": "user1",
            "password": "password"
        })
        assert "Redirecting..." in response.data
