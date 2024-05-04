from conftest import *
import time

class TestConstructorSection:

    # проверка перехода  к разделам Начинки, Соусы, Булки на странице Конструктор
    def test_constructor_section(self, login_fix):
        driver = login_fix[0]
        driver.find_elements(By.XPATH, Locators.LOCATOR_CONSTRUCTOR_SECTION)[2].click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.LOCATOR_SECTION_STUFFING)))
        time.sleep(1)
        driver.find_elements(By.XPATH, Locators.LOCATOR_CONSTRUCTOR_SECTION)[1].click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.LOCATOR_SECTION_SAUCES)))
        time.sleep(1)
        driver.find_elements(By.XPATH, Locators.LOCATOR_CONSTRUCTOR_SECTION)[0].click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.LOCATOR_SECTION_BUNS)))
        time.sleep(1)

        driver.quit()
