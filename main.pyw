import logging
import os.path
import sys

from modules import config, hdfbot, log, setting, websetup


def setup():
    webdriverPath, matrixNumber, isFirstRun = config.getSettings()
    if isFirstRun:
        logger = newLog()
        logger.error("Configuration file is not found")
        sys.exit(1)
    return websetup.open_hdf(webdriverPath), matrixNumber


def newLog():
    logger = logging.getLogger(__name__)
    dirs = setting.getDirs(config.appname, config.appauthor)
    logDir = os.path.join(dirs["userLog"], "log.log")
    log.log(logger, logging.ERROR, logDir)
    return logger


def main(driver, matrixNumber):
    hdfbot.bot(driver, matrixNumber)


if __name__ == "__main__":
    driver, matrixNumber = setup()
    main(driver, matrixNumber)
    sys.exit()
