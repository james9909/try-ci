import pytest
class testFib():
    def getFib(n):
        if n <= 1:
            return 1
        return getFib(n-1) + getFib(n-2)


    def test_register(self, client):
        response = client.post("/fib", {"n": 1})
        assert "1" in response.data

        response = client.post("/fib", {"n": 5})
        assert "8" in response.data

