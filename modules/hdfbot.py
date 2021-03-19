from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

import modules.log as log
import modules.websetup as websetup


def bot(driver, matrix_number):
    logger = log.newLogging("log.log")

    click_pelajarSect(driver, logger)
    wait_for_loading(driver, logger)
    find_textbox(driver, logger)
    insert_textbox(driver, matrix_number, logger)
    wait_for_loading(driver, logger)
    click_ackno_tickbox(driver, logger)
    submit_button(driver, logger)
    skip_alert(driver)
    websetup.close_webdriver()


def skip_alert(driver):
    alert = driver.switch_to.alert
    alert.accept()


def submit_button(driver, logger):
    submit_button = driver.find_element_by_xpath("/html/body/form/input[1]")
    submit_button.click()
    logger.info("Form is submitted")


def click_ackno_tickbox(driver, logger):
    clickbox = driver.find_element_by_xpath("//*[@id='SahPel']")
    clickbox.click()
    logger.info("Acknowledgement button is clicked")


def insert_textbox(driver, matrix_number, logger):
    textbox = driver.find_element_by_xpath("//*[@id='txtNoMatrik']")
    textbox.send_keys(matrix_number)
    textbox.send_keys(Keys.ENTER)
    logger.info(f"Matrix number {matrix_number} is entered")


def find_textbox(driver, logger):
    textbox_source = driver.find_element_by_id("bd-iframe")
    driver.switch_to.frame(textbox_source)
    logger.info("driver's frame is switched to the form")


def click_pelajarSect(driver, logger):
    pelajar_button = driver.find_element_by_xpath("//*[@id='pelajar-btn']")
    pelajar_button.click()
    logger.info("pelajar catergory is clicked")


def wait_for_loading(driver, logger):
    attempts = 0
    while attempts < 3:
        try:
            WebDriverWait(driver, 15).until_not(
                lambda x: driver.find_element_by_xpath("//*[@id='pg-loader']")
            )
            logger.info("page is loaded")
            return True
        except TimeoutException:
            attempts += 1
    logger.critical("Error loading page after %d attempts", attempts)
    return False
