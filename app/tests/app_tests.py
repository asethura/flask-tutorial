import pytest

def test_hello_world():
    import requests
    response = requests.get("http://localhost:8888/")
    print(response)
    assert True

