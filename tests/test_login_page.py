from conftest import *


class TestLogin:

    # проверка логина по кнопке Войти в аккаунт на главной странице
    def test_login_button(self, driver, registration):
        login_value, password_value = registration
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(By.XPATH, Locators.LOCATOR_BUTTON_LOGIN_TO_ACCOUNT).click()

        driver.find_elements(By.XPATH, Locators.LOCATOR_INPUT_REGISTRATION_AUTHORIZATION)[0].send_keys(login_value)
        driver.find_elements(By.XPATH, Locators.LOCATOR_INPUT_REGISTRATION_AUTHORIZATION)[1].send_keys(password_value)
        driver.find_element(By.XPATH, Locators.LOCATOR_BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.LOCATOR_BUTTON_PLACE_AN_ORDER)))

        driver.find_element(By.XPATH, Locators.LOCATOR_BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, Locators.LOCATOR_BUTTON_PROFILE)))
        profile_login_value = driver.find_elements(By.XPATH, Locators.LOCATOR_INPUT_PROFILE)[1].get_attribute('value')

        assert login_value == profile_login_value

    # проверка логина по кнопке Личный кабинет на главной странице
    def test_personal_account_button(self, driver, registration):
        login_value, password_value = registration
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(By.XPATH, Locators.LOCATOR_BUTTON_PERSONAL_ACCOUNT).click()

        driver.find_elements(By.XPATH, Locators.LOCATOR_INPUT_REGISTRATION_AUTHORIZATION)[0].send_keys(login_value)
        driver.find_elements(By.XPATH, Locators.LOCATOR_INPUT_REGISTRATION_AUTHORIZATION)[1].send_keys(password_value)
        driver.find_element(By.XPATH, Locators.LOCATOR_BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.LOCATOR_BUTTON_PLACE_AN_ORDER)))

        driver.find_element(By.XPATH, Locators.LOCATOR_BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, Locators.LOCATOR_BUTTON_PROFILE)))
        profile_login_value = driver.find_elements(By.XPATH, Locators.LOCATOR_INPUT_PROFILE)[1].get_attribute('value')

        assert login_value == profile_login_value

    # проверка логина по кнопке Войти на форме регистрации
    def test_login_button_on_the_registration_form(self, driver, registration):
        login_value, password_value = registration
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(By.LINK_TEXT, Locators.LOCATOR_LINK_LOGIN).click()

        driver.find_elements(By.XPATH, Locators.LOCATOR_INPUT_REGISTRATION_AUTHORIZATION)[0].send_keys(login_value)
        driver.find_elements(By.XPATH, Locators.LOCATOR_INPUT_REGISTRATION_AUTHORIZATION)[1].send_keys(password_value)
        driver.find_element(By.XPATH, Locators.LOCATOR_BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.LOCATOR_BUTTON_PLACE_AN_ORDER)))

        driver.find_element(By.XPATH, Locators.LOCATOR_BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, Locators.LOCATOR_BUTTON_PROFILE)))
        profile_login_value = driver.find_elements(By.XPATH, Locators.LOCATOR_INPUT_PROFILE)[1].get_attribute('value')

        assert login_value == profile_login_value

    # проверка логина по кнопке Войти на форме восстановления пароля
    def test_login_button_on_the_password_recovery_form(self, driver, registration):
        login_value, password_value = registration
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        driver.find_element(By.LINK_TEXT, Locators.LOCATOR_LINK_LOGIN).click()

        driver.find_elements(By.XPATH, Locators.LOCATOR_INPUT_REGISTRATION_AUTHORIZATION)[0].send_keys(login_value)
        driver.find_elements(By.XPATH, Locators.LOCATOR_INPUT_REGISTRATION_AUTHORIZATION)[1].send_keys(password_value)
        driver.find_element(By.XPATH, Locators.LOCATOR_BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.LOCATOR_BUTTON_PLACE_AN_ORDER)))

        driver.find_element(By.XPATH, Locators.LOCATOR_BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, Locators.LOCATOR_BUTTON_PROFILE)))
        profile_login_value = driver.find_elements(By.XPATH, Locators.LOCATOR_INPUT_PROFILE)[1].get_attribute('value')

        assert login_value == profile_login_value
