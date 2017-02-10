class TestGeneral():
    def test_sanity(self):
        assert True

    def test_index(self, client):
        response = client.get("/")
        assert response.status_code == 200
        assert response.data == "Hi"
