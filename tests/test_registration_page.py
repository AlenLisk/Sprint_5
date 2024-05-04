from conftest import *


class TestRegistration:

    # проверка регистрации - валидный пароль
    def test_registration_positive(self, driver_register, registration_login, registration_password):
        driver_register.find_elements(By.XPATH, Locators.LOCATOR_INPUT_REGISTRATION_AUTHORIZATION)[0].send_keys('AlenLisk')
        driver_register.find_elements(By.XPATH, Locators.LOCATOR_INPUT_REGISTRATION_AUTHORIZATION)[1].send_keys(registration_login)
        driver_register.find_elements(By.XPATH, Locators.LOCATOR_INPUT_REGISTRATION_AUTHORIZATION)[2].send_keys(registration_password)
        driver_register.find_element(By.XPATH, Locators.LOCATOR_BUTTON_REGISTRATION).click()
        WebDriverWait(driver_register, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.LOCATOR_BUTTON_REGISTRATION)))

        driver_register.quit()

    # проверка регистрации - невалидный пароль
    def test_registration_negative(self, driver_register, registration_login, registration_password):
        driver_register.find_elements(By.XPATH, Locators.LOCATOR_INPUT_REGISTRATION_AUTHORIZATION)[0].send_keys('AlenLisk')
        driver_register.find_elements(By.XPATH, Locators.LOCATOR_INPUT_REGISTRATION_AUTHORIZATION)[1].send_keys(registration_login)
        driver_register.find_elements(By.XPATH, Locators.LOCATOR_INPUT_REGISTRATION_AUTHORIZATION)[2].send_keys('12')
        driver_register.find_element(By.XPATH, Locators.LOCATOR_BUTTON_REGISTRATION).click()
        WebDriverWait(driver_register, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.LOCATOR_ERROR_INCORRECT_PASSWORD)))

        driver_register.quit()
