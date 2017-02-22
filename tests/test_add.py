import json

class TestAdd():

    def test_add(self, client):
        response = client.get("/fib", data={"a": 1,"b": 2})
        assert json.loads(response.data)["result"] == 3
