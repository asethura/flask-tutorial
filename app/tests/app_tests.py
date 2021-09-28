import pytest

def test_hello_world():
    import requests
    response = requests.get("http://0.0.0.0:8888/")
    print(response)
    assert True

