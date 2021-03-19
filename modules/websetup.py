import sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import modules.log as log


class WebSetup:
    def __init__(self, driverPath):
        self.URL = "https://portal.utem.edu.my/ismp/saringan/frm_framesar.asp"
        self.driverPath = driverPath

    def setupSelenium(self):
        global driver
        path = self.driverPath
        chrome_option = Options()
        chrome_option.add_experimental_option("excludeSwitches", ["enable-logging"])
        chrome_option.add_argument("--headless")
        chrome_option.add_argument("--ignore-certificate-errors")
        chrome_option.add_argument("--ignore-ssl-errors")
        chrome_option.add_argument("--no-sandbox")
        driver = webdriver.Chrome(executable_path=path, options=chrome_option)
        driver.implicitly_wait(5)
        return driver

    def open_webdriver(self):
        logger = log.newLogging("log.log")
        driver = self.setupSelenium()
        try:
            driver.get(self.URL)
        except Exception as e:
            logger.critical(f"Couldn't access webpage.\n------\nDetails:\n{e}")
            sys.exit(1)
        return driver


def open_hdf(webdriverPath):
    webHDF = WebSetup(webdriverPath)
    return webHDF.open_webdriver()


def close_webdriver():
    driver.quit()
