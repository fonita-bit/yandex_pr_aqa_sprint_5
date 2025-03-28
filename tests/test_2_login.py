from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from urls import URLs
import pytest

class TestLogin:
    """Тесты для страницы входа"""

    def test_login_via_main_button(self, driver):
        """Тест входа"""
        driver.get(URLs.LOGIN_PAGE)

        driver.find_element(*Locators.EMAIL_INPUT).send_keys("svetlanabratchenko19123@yandex.ru")
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("password123")
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        # Ожидание успешного редиректа
        WebDriverWait(driver, 10).until(EC.url_to_be(URLs.MAIN_PAGE))

        assert driver.current_url == URLs.MAIN_PAGE

