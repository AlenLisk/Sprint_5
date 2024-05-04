from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import *


def login_fun(driver, login, password):
    driver.find_elements(By.XPATH, Locators.LOCATOR_INPUT_REGISTRATION_AUTHORIZATION)[0].send_keys(login)
    driver.find_elements(By.XPATH, Locators.LOCATOR_INPUT_REGISTRATION_AUTHORIZATION)[1].send_keys(password)
    driver.find_element(By.XPATH, Locators.LOCATOR_BUTTON_LOGIN).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.LOCATOR_BUTTON_PLACE_AN_ORDER)))
