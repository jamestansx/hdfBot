import json
import logging


def write_json(pathToFile, data):
    with open(pathToFile, "w") as outFile:
        json.dump(data, outFile)
    logging.info(f"File is written to {pathToFile}")


def read_json(pathToFile):
    with open(pathToFile, "r") as readFile:
        data = json.load(readFile)
        logging.info(f"File is read from {pathToFile}")
        return data


def update_json(pathToFile, updataData):
    write_json(pathToFile, updataData)
