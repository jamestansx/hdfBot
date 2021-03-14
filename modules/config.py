import logging
import os

import modules.jsonfile as jsonfile
import modules.setting as setting

appauthor = "jamestansx"
appname = "HDF_bot"


def isFirstRun():
    dirs = setting.getDirs(appname, appauthor)
    userData_json = os.path.join(dirs["userData"], "userdata.json")
    if os.path.isfile(userData_json):
        return getSettings(userData_json)
    else:
        return setupSetting(userData_json)


def setupSetting(pathToFile):
    webdriverPath = input("Enter the path to Chrome driver: ")
    logging.info("paths is entered")
    matrix_number = input("Enter your matrix number: ")
    data = {"webdriverPath": webdriverPath, "matrixNumber": matrix_number}
    jsonfile.write_json(pathToFile, writeSettings(data))
    return webdriverPath, matrix_number, True


def writeSettings(pathDict):

    data = {}
    data["isFirstRun"] = True
    data["webdriverPath"] = pathDict["webdriverPath"]
    data["matrixNumber"] = pathDict["matrixNumber"]
    return data


def getSettings(pathToFile):
    data = jsonfile.read_json(pathToFile)
    try:
        if data["isFirstRun"] is True:
            logging.warning("Setup is not yet been done with isFirstRun: " + data["isFirstRun"])
            return setupSetting(pathToFile)
    except Exception as e:
        logging.error(e)
    webdriverPath = data["webdriverPath"]
    matrixNumber = data["matrixNumber"]
    logging.info("Path(s) are successfully extracted")
    return webdriverPath, matrixNumber, data["isFirstRun"]


def updateSetting():
    dirs = setting.getDirs(appname, appauthor)
    userData_json = os.path.join(dirs["userData"], "userdata.json")
    data = jsonfile.read_json(userData_json)
    data["isFirstRun"] = False
    jsonfile.update_json(userData_json, data)
