from urllib.parse import urlencode
import json


def call(client, path, params=''):
    if (params != ''):
        url = path + '?' + urlencode(params)
    else:
        url = path
    response = client.get(url)
    return response.data.decode('utf-8')

def postCall(client, path, myobj):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    response = client.post(path, data=json.dumps(myobj), headers=headers)
    return response.data.decode('utf-8')

def test_hello_world(client):
    result = call(client, '/')
    assert result == 'Hello World - 2!'

def test_hello_name(client):
    result = call(client, '/Ashok')
    assert result == 'Hello Ashok'


def test_list_todo_empty(client):
    result = call(client, '/todo')
    jResult = json.loads(result)
    assert len(jResult) == False


def test_create_todo_(client):
    myobj = {'Title': 'Second Todo', 'Description': 'asdad'}
    updateResult = postCall(client, '/todo', myobj)
    result = call(client, '/todo')
    jResult = json.loads(result)
    print(jResult)
    assert len(jResult) == 1