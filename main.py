import requests
import pprint
import json
import shlex

variables = []
history = []
responses = []
errors = []
selectedBaseUrl = ""
headers = {"Accept":"application/json"}

def handleGetRequest(userInp):
    try:
        url = userInp.split(',')[1]
        if ("$base" in url):
            url = selectedBaseUrl
        resp = requests.get(url, headers=headers)
        pprint.pprint(resp)
        responses.append(resp)
    except Exception as e:
        print(e)
        errors.append(e)
def handlePostRequest(userInp):
    try:
        _, data = userInp.split('{')
        url = _.split(',')[1]
        if ("$base" in url):
            url = selectedBaseUrl
        data = "{" + data
        resp = requests.post(url, json=json.loads(data), headers=headers)
        pprint.pprint(resp.json())
        responses.append(resp)
    except Exception as e:
        print(e)
        errors.append(e)
def handlePatchRequest(userInp):
    try:
        url = userInp.split(',')[1]
        resp = requests.patch(url, headers=headers)
        pprint.pprint(resp.json())
        responses.append(resp)
    except Exception as e:
        print(e)
        errors.append(e)

def handleDeleteRequest(userInp):
    try:
        url = userInp.split(',')[1]
        resp = requests.delete(url, headers=headers)
        pprint.pprint(resp.json())
        responses.append(resp)
    except Exception as e:
        print(e)
        errors.append(e)

def handleNewVariableCreation(userInp):
    propName, propValue = userInp.split('=')
    variables.append({propName: propValue})

def getStoredVariableValue(var):
    for v in variables:
        for key,val in v.items():
            if key == var:
                return val
def getInfoAboutLastResponse():
    response = responses.pop()
    print('[Code]: ', response.status_code)
    print('[Headers]: ', response.headers)
    if ("json" in response.headers['Content-Type']):
        print('[Json]: ', response.json())
def addNewHeader(userInp):
    _, key, value = shlex.split(userInp)
    headers[key] = value
def removeHeader(userInp):
    _, key = userInp.split(' ')
    headers.pop(key, None)
def showHeaders():
    print(headers)
while(True):
    userInp = input("[SRCE]:")
    if (userInp == "q"):
        break
    if (userInp == "last"):
        userInp = history.pop()
    if ("$base" in userInp):
        userInp = userInp.replace("$base", selectedBaseUrl)
    if ("base" in userInp):
        selectedBaseUrl = userInp.split(' ')[1]
    history.append(userInp)
    if ("get" in userInp):
        handleGetRequest(userInp)
    if ("post" in userInp):
        handlePostRequest(userInp)
    if ("patch" in userInp):
        handlePatchRequest(userInp)
    if ("delete" in userInp):
        handleDeleteRequest(userInp)
    if ("=" in userInp):
        handleNewVariableCreation(userInp)
    if ("resp" in userInp):
        getInfoAboutLastResponse()
    if ("addh" in userInp):
        addNewHeader(userInp)
    if ("delh" in userInp):
        removeHeader(userInp)
    if("showh" in userInp):
        showHeaders()