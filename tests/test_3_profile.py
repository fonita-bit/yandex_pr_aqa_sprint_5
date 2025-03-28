from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from urls import URLs
import pytest

class TestProfile:
    """Тесты для личного кабинета"""

    def test_navigate_to_profile(self, driver):
        """Тест перехода в личный кабинет"""
        driver.get(URLs.LOGIN_PAGE)

        driver.find_element(*Locators.EMAIL_INPUT).send_keys("svetlanabratchenko19123@yandex.ru")
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("password123")
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(URLs.MAIN_PAGE))

        driver.find_element(*Locators.PROFILE_BUTTON).click()
        assert "/account" in driver.current_url

    def test_logout(self, driver):
        """Тест выхода из аккаунта"""
        driver.get(URLs.LOGIN_PAGE)

        driver.find_element(*Locators.EMAIL_INPUT).send_keys("svetlanabratchenko19123@yandex.ru")
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("password123")
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(URLs.MAIN_PAGE))

        driver.find_element(*Locators.PROFILE_BUTTON).click()

        logout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.LOGOUT_BUTTON)
        )
        logout_button.click()

        WebDriverWait(driver, 10).until(EC.url_to_be(URLs.LOGIN_PAGE))
        assert driver.current_url == URLs.LOGIN_PAGE
