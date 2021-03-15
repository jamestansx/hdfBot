import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class WebSetup:
    def __init__(self, driverPath):
        self.URL = "https://portal.utem.edu.my/ismp/saringan/frm_framesar.asp"
        self.driverPath = driverPath

    def setupSelenium(self):
        global driver
        path = self.driverPath
        chrome_option = Options()
        chrome_option.add_argument("--log-level=3")
        chrome_option.add_experimental_option("excludeSwitches", ["enable-logging"])
        chrome_option.add_argument("--headless")
        chrome_option.add_argument("--ignore-certificate-errors")
        chrome_option.add_argument("--ignore-ssl-errors")
        driver = webdriver.Chrome(executable_path=path, options=chrome_option)
        driver.implicitly_wait(5)
        return driver

    def open_webdriver(self):
        driver = self.setupSelenium()
        driver.get(self.URL)
        return driver


def open_hdf(webdriverPath):
    webHDF = WebSetup(webdriverPath)
    return webHDF.open_webdriver()


def close_webdriver():
    driver.quit()
