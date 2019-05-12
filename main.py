from utils.headerController import HeaderController
from utils.requestController import RequestController

variables = []
history = []
selectedBaseUrl = ""

headerController = HeaderController()
requestController = RequestController(headerController.getHeaders())

def handleNewVariableCreation(userInp):
    propName, propValue = userInp.split('=')
    variables.append({propName: propValue})

def getStoredVariableValue(var):
    for v in variables:
        for key,val in v.items():
            if key == var:
                return val

while(True):
    userInp = input("[SRCE]:")
    if (userInp == "q"):
        print("Thank you for using SERC.")
        break
    if (userInp == "last"):
        userInp = history.pop()
    if ("$base" in userInp):
        userInp = userInp.replace("$base", selectedBaseUrl)
    if ("base" in userInp):
        selectedBaseUrl = userInp.split(' ')[1]
    history.append(userInp)

    if ("get" in userInp):
        requestController.handleGetRequest(userInp)
    if ("post" in userInp):
        requestController.handlePostRequest(userInp)
    if ("patch" in userInp):
        requestController.handlePatchRequest(userInp)
    if ("delete" in userInp):
        requestControllerhandleDeleteRequest(userInp)
    if ("=" in userInp):
        handleNewVariableCreation(userInp)
    if ("resp" in userInp):
        requestController.getInfoAboutLastResponse()
    if ("addh" in userInp):
        headerController.addNewHeader(userInp)
    if ("delh" in userInp):
        headerController.removeHeader(userInp)
    if("showh" in userInp):
        headerController.showHeaders()