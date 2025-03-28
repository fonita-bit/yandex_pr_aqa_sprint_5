from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from urls import URLs
import pytest


class TestConstructor:
    """Тесты для конструктора бургеров"""

    def test_switch_to_buns(self, driver):
        """Тест переключения на вкладку 'Булки'"""
        driver.get(URLs.MAIN_PAGE)

        # Переключаемся на вкладку 'Соусы'
        driver.find_element(*Locators.SAUCES_TAB).click()

        # Ожидаем, что вкладка 'Соусы' стала активной
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.ACTIVE_TAB))
        active_tab = driver.find_element(*Locators.ACTIVE_TAB)
        assert "Соусы" in active_tab.text, "Вкладка 'Соусы' не активна"

        # Теперь возвращаемся на вкладку 'Булки'
        driver.find_element(*Locators.BUNS_TAB).click()

        # Ожидаем, что вкладка 'Булки' стала активной
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.ACTIVE_TAB))
        active_tab = driver.find_element(*Locators.ACTIVE_TAB)
        assert "Булки" in active_tab.text, "Вкладка 'Булки' не активна"

    def test_switch_to_sauces(self, driver):
        """Тест переключения на вкладку 'Соусы'"""
        driver.get(URLs.MAIN_PAGE)

        driver.find_element(*Locators.SAUCES_TAB).click()

        # Ожидаем, что вкладка 'Соусы' стала активной
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.ACTIVE_TAB))
        active_tab = driver.find_element(*Locators.ACTIVE_TAB)
        assert "Соусы" in active_tab.text, "Вкладка 'Соусы' не активна"

    def test_switch_to_fillings(self, driver):
        """Тест переключения на вкладку 'Начинки'"""
        driver.get(URLs.MAIN_PAGE)

        driver.find_element(*Locators.FILLINGS_TAB).click()

        # Ожидаем, что вкладка 'Начинки' стала активной
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.ACTIVE_TAB))
        active_tab = driver.find_element(*Locators.ACTIVE_TAB)
        assert "Начинки" in active_tab.text, "Вкладка 'Начинки' не активна"
