# Тесты для проверки успешной регистрации
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

def test_switch_to_buns(driver):
    """Тест переключения на вкладку 'Булки'"""
    # Сначала переключаемся на вкладку 'Соусы'
    driver.find_element(*Locators.SAUCES_TAB).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.SAUCES_TAB))  # Ждем, пока отобразится контент вкладки "Соусы"

    # Теперь возвращаемся на вкладку 'Булки'
    driver.find_element(*Locators.BUNS_TAB).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.BUNS_TAB))  # Ждем, пока отобразится контент вкладки "Булки"

    # Проверяем, что на странице есть контент, связанный с "Булками"
    assert "Булки" in driver.page_source

def test_switch_to_sauces(driver):
    """Тест переключения на вкладку 'Соусы'"""
    driver.find_element(*Locators.SAUCES_TAB).click()
    assert "Соусы" in driver.page_source

def test_switch_to_fillings(driver):
    """Тест переключения на вкладку 'Начинки'"""
    driver.find_element(*Locators.FILLINGS_TAB).click()
    assert "Начинки" in driver.page_source