import sys

from modules import config, hdfbot, log, websetup


def setup():
    webdriverPath, matrixNumber, isFirstRun = config.getSettings()
    if isFirstRun:
        logger = log.newLogging("log.log")
        logger.error("Configuration file is not found")
        sys.exit(1)
    return websetup.open_hdf(webdriverPath), matrixNumber


def main(driver, matrixNumber):
    hdfbot.bot(driver, matrixNumber)


if __name__ == "__main__":
    driver, matrixNumber = setup()
    main(driver, matrixNumber)
