from conftest import *


class TestRegistration:

    # проверка регистрации - валидный пароль
    def test_registration_positive(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        login_value = Helper.registration_login()
        password_value = Helper.registration_password()

        driver.find_elements(By.XPATH, Locators.LOCATOR_INPUT_REGISTRATION_AUTHORIZATION)[0].send_keys('AlenLisk')
        driver.find_elements(By.XPATH, Locators.LOCATOR_INPUT_REGISTRATION_AUTHORIZATION)[1].send_keys(login_value)
        driver.find_elements(By.XPATH, Locators.LOCATOR_INPUT_REGISTRATION_AUTHORIZATION)[2].send_keys(password_value)
        driver.find_element(By.XPATH, Locators.LOCATOR_BUTTON_REGISTRATION).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.LOCATOR_BUTTON_LOGIN)))

        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_elements(By.XPATH, Locators.LOCATOR_INPUT_REGISTRATION_AUTHORIZATION)[0].send_keys('AlenLisk')
        driver.find_elements(By.XPATH, Locators.LOCATOR_INPUT_REGISTRATION_AUTHORIZATION)[1].send_keys(login_value)
        driver.find_elements(By.XPATH, Locators.LOCATOR_INPUT_REGISTRATION_AUTHORIZATION)[2].send_keys(password_value)
        driver.find_element(By.XPATH, Locators.LOCATOR_BUTTON_REGISTRATION).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.LOCATOR_ERROR_USER_ALREADY_EXISTS)))

        error_value = 'Такой пользователь уже существует'
        error_registration = driver.find_element(By.XPATH, Locators.LOCATOR_ERROR_USER_ALREADY_EXISTS).text

        assert error_registration == error_value

    # проверка регистрации - невалидный пароль
    def test_registration_negative(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")

        driver.find_elements(By.XPATH, Locators.LOCATOR_INPUT_REGISTRATION_AUTHORIZATION)[0].send_keys('AlenLisk')
        driver.find_elements(By.XPATH, Locators.LOCATOR_INPUT_REGISTRATION_AUTHORIZATION)[1].send_keys(Helper.registration_login())
        driver.find_elements(By.XPATH, Locators.LOCATOR_INPUT_REGISTRATION_AUTHORIZATION)[2].send_keys('12')
        driver.find_element(By.XPATH, Locators.LOCATOR_BUTTON_REGISTRATION).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.LOCATOR_ERROR_INCORRECT_PASSWORD)))

        error_value = 'Некорректный пароль'
        error_registration = driver.find_element(By.XPATH, Locators.LOCATOR_ERROR_INCORRECT_PASSWORD).text

        assert error_registration == error_value