from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from urls import URLs
import pytest

class TestRegistration:
    """Тесты для страницы регистрации"""

    def test_successful_registration(self, driver, generate_email, generate_password):
        """Тест успешной регистрации"""
        driver.get(URLs.REGISTRATION_PAGE)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.NAME_INPUT))
        driver.find_element(*Locators.NAME_INPUT).send_keys("Тест Пользователь")
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(generate_email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(generate_password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        # Добавляем ожидание успешного редиректа
        WebDriverWait(driver, 10).until(EC.url_contains(URLs.LOGIN_PAGE))
        assert driver.current_url == URLs.LOGIN_PAGE

    def test_invalid_password_registration(self, driver, generate_email):
        """Тест ошибки при вводе короткого пароля"""
        driver.get(URLs.REGISTRATION_PAGE)

        WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.PASSWORD_INPUT))
        driver.find_element(*Locators.NAME_INPUT).send_keys("Тест Пользователь")
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(generate_email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("123")  # Недостаточно символов
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        # Ожидаем появления сообщения об ошибке
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(Locators.ERROR_MESSAGE)
        )

        # Проверяем, что сообщение об ошибке отображается
        error_message = driver.find_element(*Locators.ERROR_MESSAGE)
        assert error_message.is_displayed(), "Ошибка не появилась"
