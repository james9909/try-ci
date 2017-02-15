class TestGeneral():
    def test_sanity(self):
        assert True

    def test_register(self, client):
        responce = client.post("/register", data={
            "username":"y",
            "password":"y",
            "pwd":"y"
            })
        assert "register failed" in responce.data
        responce = client.post("/register", data={
            "username":"x",
            "password":"x",
            "pwd":"x"
            })
        assert "register successful" in responce.data
