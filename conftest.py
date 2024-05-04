import pytest
from selenium import webdriver
import random
from functions import login_fun
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import *


@pytest.fixture
def driver_register(): # запуск страницы регистрации
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")

    return driver

@pytest.fixture
def registration(driver_register, registration_login, registration_password): # регистрация нового пользователя
    login = registration_login
    password = registration_password
    driver = driver_register

    driver.find_elements(By.XPATH, Locators.LOCATOR_INPUT_REGISTRATION_AUTHORIZATION)[0].send_keys('AlenLisk')
    driver.find_elements(By.XPATH, Locators.LOCATOR_INPUT_REGISTRATION_AUTHORIZATION)[1].send_keys(login)
    driver.find_elements(By.XPATH, Locators.LOCATOR_INPUT_REGISTRATION_AUTHORIZATION)[2].send_keys(password)
    driver.find_element(By.XPATH, Locators.LOCATOR_BUTTON_REGISTRATION).click()
    WebDriverWait(driver_register, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.LOCATOR_LABEL_LOGIN)))

    return driver, login, password

@pytest.fixture
def login_fix(registration): # логин через страницу логин
    driver, login, password = registration
    login_fun(driver, login, password) # функция логина

    return driver, login

@pytest.fixture
def personal_account(login_fix): # переход в Личный кабинет с главной страницы
    driver, login = login_fix
    driver.find_element(By.XPATH, Locators.LOCATOR_BUTTON_PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, Locators.LOCATOR_BUTTON_PROFILE)))
    login_value = driver.find_elements(By.XPATH, Locators.LOCATOR_INPUT_PROFILE)[1].get_attribute('value')

    assert login in login_value

    return driver

@pytest.fixture
def registration_login(): # генерация логина
    name = 'ena'
    lastname = 'skovskaya'
    cohort_num = '8'
    domain = '@ya.ru'
    numbers = str(random.randint(100,999))

    email = name + '_' + lastname + '_' + cohort_num + '_' + numbers + domain

    return email

@pytest.fixture
def registration_password(): # генерация пароля от 6 до 10 символов
    symbols_list = [['ABCDEFGHIJKLMNOPQRSTUVWXYZ'], ['abcdefghijklmnopqrstuvwxyz'], ['0123456789'], ['/#@$*=+&%']]
    password = ''
    password_len = random.randint(6, 10)
    for i in range(password_len):
        symbols = symbols_list[random.randint(0, 3)][0]
        password += symbols[random.randint(0, len(symbols) - 1)]

    return password





