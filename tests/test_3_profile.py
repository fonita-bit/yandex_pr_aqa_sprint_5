from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

def test_navigate_to_profile(driver):
    """Тест перехода в личный кабинет"""
    driver.get("https://stellarburgers.nomoreparties.site/login")

    driver.find_element(*Locators.EMAIL_INPUT).send_keys("svetlanabratchenko19123@yandex.ru")
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys("password123")
    driver.find_element(*Locators.LOGIN_BUTTON).click()

    # Ждем успешного редиректа на главную страницу
    WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

    driver.find_element(*Locators.PROFILE_BUTTON).click()
    assert "/account" in driver.current_url

def test_logout(driver):
    """Тест выхода из аккаунта"""
    driver.get("https://stellarburgers.nomoreparties.site/login")

    driver.find_element(*Locators.EMAIL_INPUT).send_keys("svetlanabratchenko19123@yandex.ru")
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys("password123")
    driver.find_element(*Locators.LOGIN_BUTTON).click()

    # Ждем успешного редиректа на главную страницу
    WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

    # Переход к профилю
    driver.find_element(*Locators.PROFILE_BUTTON).click()

    # Ожидание загрузки элемента "Выход"
    logout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Выход')]"))
    )

    # Нажимаем кнопку выхода
    logout_button.click()
    # Ожидаем, что URL изменится на страницу логина
    WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))

    # Проверяем редирект на страницу логина
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"