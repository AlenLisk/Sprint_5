from conftest import *


class TestConstructorSection:

    # проверка перехода к разделау Булки на странице Конструктор
    def test_section_buns(self, driver, login, scroll):
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.LOCATOR_CONSTRUCTOR_SECTION)))
        driver.find_elements(By.XPATH, Locators.LOCATOR_CONSTRUCTOR_SECTION)[0].click()

        section_name = 'Булки'
        section = driver.find_element(By.XPATH, Locators.LOCATOR_SECTION_BUNS).text

        assert section_name == section

    # проверка перехода к разделу Соусы на странице Конструктор
    def test_section_sauces(self, driver, login, scroll):
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.LOCATOR_CONSTRUCTOR_SECTION)))
        driver.find_elements(By.XPATH, Locators.LOCATOR_CONSTRUCTOR_SECTION)[1].click()

        section_name = 'Соусы'
        section = driver.find_element(By.XPATH, Locators.LOCATOR_SECTION_SAUCES).text

        assert section_name == section

    # проверка перехода к разделу Начинки на странице Конструктор
    def test_section_stuffing(self, driver, login):
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.LOCATOR_CONSTRUCTOR_SECTION)))
        driver.find_elements(By.XPATH, Locators.LOCATOR_CONSTRUCTOR_SECTION)[2].click()

        section_name = 'Начинки'
        section = driver.find_element(By.XPATH, Locators.LOCATOR_SECTION_STUFFING).text

        assert section_name == section

