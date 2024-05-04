from conftest import *
import time


class TestLogin:

    # проверка логина по кнопке Войти в аккаунт на главной странице
    def test_login_button(self, registration):
        driver, login, password = registration
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(By.XPATH, Locators.LOCATOR_BUTTON_LOGIN_TO_ACCOUNT).click()
        login_fun(driver, login, password) # логин

        driver.quit()

    # проверка логина по кнопке Личный кабинет на главной странице
    def test_personal_account_button(self, registration):
        driver, login, password=registration
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(By.XPATH, Locators.LOCATOR_BUTTON_PERSONAL_ACCOUNT).click()
        login_fun(driver, login, password) # логин

        driver.quit()

    # проверка логина по кнопке Войти на форме регистрации
    def test_login_button_on_the_registration_form(self, registration):
        driver, login, password = registration
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(By.LINK_TEXT, Locators.LOCATOR_LINK_LOGIN).click()
        login_fun(driver, login, password) # логин

        driver.quit()

    # проверка логина по кнопке Войти на форме восстановления пароля
    def test_login_button_on_the_password_recovery_form(self, registration):
        driver, login, password = registration
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        driver.find_element(By.LINK_TEXT, Locators.LOCATOR_LINK_LOGIN).click()
        login_fun(driver, login, password) # логин

        driver.quit()
