from conftest import *


class TestPersonalAccount:

    # проверка перехода в Личный кабинет по кнопке Личный кабинет на главной странице
    def test_personal_account_button(self, driver, registration, login):
        login_value = registration[0]
        driver.find_element(By.XPATH, Locators.LOCATOR_BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, Locators.LOCATOR_BUTTON_PROFILE)))
        profile_login_value = driver.find_elements(By.XPATH, Locators.LOCATOR_INPUT_PROFILE)[1].get_attribute('value')

        assert login_value == profile_login_value

