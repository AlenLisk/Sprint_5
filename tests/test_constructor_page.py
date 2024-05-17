from conftest import *


class TestConstructor:

    # проверка перехода на страницу Конструктор по кнопке Конструктор на странице Личный кабинет
    def test_constructor_button(self, driver, personal_account):
        driver.find_element(By.XPATH, Locators.LOCATOR_BUTTON_CONSTRUCTOR).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.LOCATOR_LABEL_ASSEMBLE_A_BURGER)))

        title_value = 'Соберите бургер'
        title = driver.find_element(By.XPATH, Locators.LOCATOR_LABEL_ASSEMBLE_A_BURGER).text

        assert title_value == title

    # проверка перехода на страницу Конструктор по логотипу Stellar Burgers на странице Личный кабинет
    def test_logo_button(self, driver, personal_account):
        driver.find_element(By.XPATH, Locators.LOCATOR_LOGO_STELLAR_BURGERS).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.LOCATOR_LABEL_ASSEMBLE_A_BURGER)))

        title_value = 'Соберите бургер'
        title = driver.find_element(By.XPATH, Locators.LOCATOR_LABEL_ASSEMBLE_A_BURGER).text

        assert title_value == title
