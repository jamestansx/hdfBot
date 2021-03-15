from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

import modules.websetup as websetup


def bot(driver, matrix_number):
    pelajar_button = driver.find_element_by_xpath("//*[@id='pelajar-btn']")
    pelajar_button.click()
    wait_for_loading(driver)
    textbox_source = driver.find_element_by_id("bd-iframe")
    driver.switch_to.frame(textbox_source)
    textbox = driver.find_element_by_xpath("//*[@id='txtNoMatrik']")
    textbox.send_keys(matrix_number)
    textbox.send_keys(Keys.ENTER)
    wait_for_loading(driver)
    clickbox = driver.find_element_by_xpath("//*[@id='SahPel']")
    clickbox.click()

    submit_button = driver.find_element_by_xpath("/html/body/form/input[1]")
    print(submit_button)
    submit_button.click()
    websetup.close_webdriver()


def wait_for_loading(driver):
    attempts = 0
    while attempts < 3:
        try:
            WebDriverWait(driver, 15).until_not(
                lambda x: driver.find_element_by_xpath("//*[@id='pg-loader']")
            )
            print("loaded")
            break
        except TimeoutException:
            attempts += 1
