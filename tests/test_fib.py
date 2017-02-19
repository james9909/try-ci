import math
import json

def getFib(n):
    Phi = (1 + math.sqrt(5)) / 2.0
    phi = (1 - math.sqrt(5)) / 2.0
    answer = math.floor((math.pow(Phi, n) - math.pow(phi, n)) / math.sqrt(5))
    return answer

class TestFib():

    def test_fib(self, client):
        response = client.get("/fib", data={"n": 1})
        assert json.loads(response.data)["result"] == getFib(1)

        response = client.get("/fib", data={"n": 5})
        assert json.loads(response.data)["result"] == getFib(5)
