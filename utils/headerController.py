import shlex

class HeaderController:
    def __init__(self):
        self.headers =  { "Accept":"application/json" }

    def addNewHeader(self, userInp):
        _, key, value = shlex.split(userInp)
        self.headers[key] = value
        
    def removeHeader(self, userInp):
        _, key = userInp.split(' ')
        self.headers.pop(key, None)

    def showHeaders(self):
        print(self.headers)

    def getHeaders(self):
        return self.headers