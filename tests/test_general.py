class TestGeneral():
    def test_sanity(self):
        assert True

    def test_register(self, client, db):
        response = client.post("/register", data={
            "username":"y",
            "password":"y",
            "pwd":"y"
        })
        assert "register successful" in response.data

        response = client.post("/register", data={
            "username":"x",
            "password":"password",
            "pwd":"password2"
            })
        assert "register failed" in response.data
