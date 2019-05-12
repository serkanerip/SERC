import requests
import pprint
import json

class RequestController:
    def __init__(self, headers):
        self.responses = []
        self.errors = []
        self.headers = headers
    def handleGetRequest(self, userInp):
        try:
            url = userInp.split(',')[1]
            resp = requests.get(url, headers=self.headers)
            pprint.pprint(resp)
            self.responses.append(resp)
        except Exception as e:
            print(e)
            self.errors.append(e)

    def handlePostRequest(self, userInp):
        try:
            _, data = userInp.split('{')
            url = _.split(',')[1]
            data = "{" + data
            resp = requests.post(url, json=json.loads(data), headers=self.headers)
            pprint.pprint(resp.json())
            self.responses.append(resp)
        except Exception as e:
            print(e)
            self.errors.append(e)

    def handlePatchRequest(self, userInp):
        try:
            url = userInp.split(',')[1]
            resp = requests.patch(url, headers=self.headers)
            pprint.pprint(resp.json())
            self.responses.append(resp)
        except Exception as e:
            print(e)
            self.errors.append(e)

    def handleDeleteRequest(self, userInp):
        try:
            url = userInp.split(',')[1]
            resp = requests.delete(url, headers=self.headers)
            pprint.pprint(resp.json())
            self.responses.append(resp)
        except Exception as e:
            print(e)
            self.errors.append(e)

    def getInfoAboutLastResponse(self):
        response = self.responses.pop()
        print('[Code]: ', response.status_code)
        print('[Headers]: ', response.headers)
        if ("json" in response.headers['Content-Type']):
            print('[Json]: ', response.json())
