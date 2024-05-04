from conftest import *


class TestLogout:

    # проверка Logout на странице Личный кабинет
    def test_logout_button(self, personal_account):
        driver = personal_account
        driver.find_element(By.XPATH, Locators.LOCATOR_BUTTON_LOGOUT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.LOCATOR_LABEL_LOGIN)))

        driver.quit()
