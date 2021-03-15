import os
import sys

import modules.jsonfile as jsonfile
import modules.setting as setting

appauthor = "jamestansx"
appname = "HDF_bot"


def isFirstRun():
    userData_json = get_userdata_dir()
    response = None
    if os.path.isfile(userData_json):
        response = isEditSetting()
    else:
        setupSetting(userData_json)

    if response:
        editSetting(userData_json)
    else:
        sys.exit(1)


def editSetting(userData_json):
    data = jsonfile.read_json(userData_json)
    choice = input("Select the setting to edit:\n1. chrome driver path\n2. matrix number\n[all]\n")
    if choice in {"1", "all"}:
        data["webdriverPath"] = input("Chrome driver path: ")
    if choice in {"2", "all"}:
        data["matrixNumber"] = input("Matrix number: ")
    jsonfile.update_json(userData_json, data)


def get_userdata_dir():
    dirs = setting.getDirs(appname, appauthor)
    userData_json = os.path.join(dirs["userData"], "userdata.json")
    return userData_json


def isEditSetting():
    while True:
        response = input("Setting is already existed\nDo you want to edit <y/n>: ")
        if response.strip().lower() in {"y", "yes"}:
            return True
        elif response.strip().lower() in {"n", "no"}:
            return False
        else:
            pass


def setupSetting(pathToFile):
    webdriverPath = input("Enter the path to Chrome driver: ")
    matrix_number = input("Enter your matrix number: ")
    data = {"webdriverPath": webdriverPath, "matrixNumber": matrix_number}
    jsonfile.write_json(pathToFile, writeSettings(data))


def writeSettings(pathDict):

    data = {}
    data["isFirstRun"] = True
    data["webdriverPath"] = pathDict["webdriverPath"]
    data["matrixNumber"] = pathDict["matrixNumber"]
    return data


def getSettings():
    pathToFile = get_userdata_dir()
    if os.path.isfile(pathToFile):
        data = jsonfile.read_json(pathToFile)
    else:
        pass
    webdriverPath = data["webdriverPath"]
    matrixNumber = data["matrixNumber"]
    return webdriverPath, matrixNumber, data["isFirstRun"]


def updateSetting():
    dirs = setting.getDirs(appname, appauthor)
    userData_json = os.path.join(dirs["userData"], "userdata.json")
    data = jsonfile.read_json(userData_json)
    data["isFirstRun"] = False
    jsonfile.update_json(userData_json, data)
