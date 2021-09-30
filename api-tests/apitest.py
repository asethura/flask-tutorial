import requests
import json

host_url = "https://guarded-scrubland-59466.herokuapp.com/"


def test_hello_name():
    response = requests.get(host_url+"Ashok")

    print(response.text)

    result = response.text

    assert result == 'Hello Ashok'