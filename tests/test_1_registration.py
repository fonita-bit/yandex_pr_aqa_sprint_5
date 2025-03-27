# Тесты для проверки успешной регистрации
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


def test_successful_registration(driver, generate_email, generate_password):
    """Тест успешной регистрации"""
    driver.get("https://stellarburgers.nomoreparties.site/register")

    driver.find_element(*Locators.NAME_INPUT).send_keys("Тест Пользователь")
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(generate_email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(generate_password)
    driver.find_element(*Locators.REGISTER_BUTTON).click()

    # Добавляем ожидание успешного редиректа
    WebDriverWait(driver, 10).until(EC.url_contains("login"))

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"


def test_invalid_password_registration(driver, generate_email):
    """Тест ошибки при вводе короткого пароля"""
    driver.get("https://stellarburgers.nomoreparties.site/register")

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@name='Пароль']")))

    driver.find_element(*Locators.NAME_INPUT).send_keys("Тест Пользователь")
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(generate_email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys("123")  # Недостаточно символов
    driver.find_element(*Locators.REGISTER_BUTTON).click()

    # Ожидаем появления сообщения об ошибке
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//p[@class='input__error text_type_main-default']"))
    )

    # Проверяем, что сообщение об ошибке отображается
    error_message = driver.find_element(By.XPATH, "//p[@class='input__error text_type_main-default']")
    assert error_message.is_displayed(), "Ошибка не появилась"