from modules import config, hdfbot, websetup


def setup():
    webdriverPath,matrixNumber, isFirstRun = config.isFirstRun()
    return websetup.open_hdf(webdriverPath), matrixNumber, isFirstRun

def main(driver, matrixNumber, isFirstRun):
    hdfbot.bot(driver, matrixNumber)
    if isFirstRun is True:
        config.updateSetting()

if __name__ == '__main__':
    driver, matrixNumber, isFirstRun = setup()
    main(driver, matrixNumber, isFirstRun)
