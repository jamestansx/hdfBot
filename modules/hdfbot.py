import logging
import os.path

from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

import modules.config as config
import modules.log as log
import modules.setting as setting
import modules.websetup as websetup


def bot(driver, matrix_number):
    logger = newLogging()
    pelajar_button = driver.find_element_by_xpath("//*[@id='pelajar-btn']")
    pelajar_button.click()
    logger.info("pelajar catergory is clicked")
    wait_for_loading(driver, logger)
    textbox_source = driver.find_element_by_id("bd-iframe")
    frame = driver.switch_to.frame(textbox_source)
    logger.info(f"driver's frame is switched to the form: {frame}")
    textbox = driver.find_element_by_xpath("//*[@id='txtNoMatrik']")
    textbox.send_keys(matrix_number)
    textbox.send_keys(Keys.ENTER)
    logger.info(f"Matrix number {matrix_number} is entered")
    wait_for_loading(driver, logger)
    clickbox = driver.find_element_by_xpath("//*[@id='SahPel']")
    clickbox.click()
    logger.info("Acknowledgement button is clicked")
    submit_button = driver.find_element_by_xpath("/html/body/form/input[1]")
    submit_button.click()
    logger.info("Form is submitted")
    alert = driver.switch_to.alert
    alert.accept()
    websetup.close_webdriver()


def newLogging():
    logger = logging.getLogger()
    dirs = setting.getDirs(config.appname, config.appauthor)
    logDir = os.path.join(dirs["userLog"], "log.log")
    log.log(logger, logging.INFO, logDir)
    return logger


def wait_for_loading(driver, logger):
    attempts = 0
    while attempts < 3:
        try:
            WebDriverWait(driver, 15).until_not(
                lambda x: driver.find_element_by_xpath("//*[@id='pg-loader']")
            )
            logger.info("page is loaded")
            break
        except TimeoutException:
            attempts += 1
