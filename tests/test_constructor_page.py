from conftest import *


class TestConstructor:

    # проверка перехода на страницу Конструктор по кнопке Конструктор на странице Личный кабинет
    def test_constructor_button(self, personal_account):
        driver = personal_account
        driver.find_element(By.XPATH, Locators.LOCATOR_BUTTON_CONSTRUCTOR).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.LOCATOR_LABEL_ASSEMBLE_A_BURGER)))

        driver.quit()

    # проверка перехода на страницу Конструктор по логотипу Stellar Burgers на странице Личный кабинет
    def test_logo_button(self, personal_account):
        driver = personal_account
        driver.find_element(By.XPATH, Locators.LOCATOR_LOGO_STELLAR_BURGERS).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.LOCATOR_LABEL_ASSEMBLE_A_BURGER)))

        driver.quit()
