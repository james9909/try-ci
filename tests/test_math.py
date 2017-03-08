import json

class TestMath():

    def test_add(self, client):
        tests = [
            {
                "a": 0,
                "b": 0,
                "expected": 0
            },
            {
                "a": 1,
                "b": 1,
                "expected": 2
            },
            {
                "a": 5,
                "b": 0,
                "expected": 5
            },
            {
                "a": 1,
                "b": -1,
                "expected": 0
            },
            {
                "a": -1,
                "b": -1,
                "expected": -2
            },
            {
                "a": -1,
                "b": 2,
                "expected": 1
            },
        ]
        for test in tests:
            data = {
                "a": test["a"],
                "b": test["b"]
            }
            response = client.get("/add", data=data)
            assert json.loads(response.data)["result"] == test["expected"]
