import requests
import json

host_url = "https://guarded-scrubland-59466.herokuapp.com/"

response = requests.get(host_url+"Ashok")
result = response.data.decode('utf-8')
assert result == 'Hello Ashok'