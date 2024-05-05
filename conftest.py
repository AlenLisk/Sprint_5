import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from helper import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import *


@pytest.fixture(scope="function")
def driver(request): # создание экземпляра класса webdriver
    driver = webdriver.Chrome()

    def fin():
        print('\ndriver_quit')
        driver.quit()

    request.addfinalizer(fin)
    return driver

@pytest.fixture
def registration(driver): # регистрация нового пользователя
    login_value = Helper.registration_login()
    password_value = Helper.registration_password()
    driver.get("https://stellarburgers.nomoreparties.site/register")

    driver.find_elements(By.XPATH, Locators.LOCATOR_INPUT_REGISTRATION_AUTHORIZATION)[0].send_keys('AlenLisk')
    driver.find_elements(By.XPATH, Locators.LOCATOR_INPUT_REGISTRATION_AUTHORIZATION)[1].send_keys(login_value)
    driver.find_elements(By.XPATH, Locators.LOCATOR_INPUT_REGISTRATION_AUTHORIZATION)[2].send_keys(password_value)
    driver.find_element(By.XPATH, Locators.LOCATOR_BUTTON_REGISTRATION).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.LOCATOR_LABEL_LOGIN)))

    return login_value, password_value

@pytest.fixture
def login(driver, registration): # логин через страницу логин
    login_value, password_value = registration

    driver.find_elements(By.XPATH, Locators.LOCATOR_INPUT_REGISTRATION_AUTHORIZATION)[0].send_keys(login_value)
    driver.find_elements(By.XPATH, Locators.LOCATOR_INPUT_REGISTRATION_AUTHORIZATION)[1].send_keys(password_value)
    driver.find_element(By.XPATH, Locators.LOCATOR_BUTTON_LOGIN).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.LOCATOR_BUTTON_PLACE_AN_ORDER)))

    return login_value
@pytest.fixture
def personal_account(driver, login): # переход в Личный кабинет с главной страницы
    driver.find_element(By.XPATH, Locators.LOCATOR_BUTTON_PERSONAL_ACCOUNT).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, Locators.LOCATOR_BUTTON_PROFILE)))

@pytest.fixture
def scroll(driver): # прокрутка до конца конструктора
    element = driver.find_element(By.XPATH, Locators.LOCATOR_STUFFING_CHEESE)
    driver.execute_script("arguments[0].scrollIntoView();", element)
