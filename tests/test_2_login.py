from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

def test_login_via_main_button(driver):
    """Тест входа"""
    driver.get("https://stellarburgers.nomoreparties.site/login")

    driver.find_element(*Locators.EMAIL_INPUT).send_keys("svetlanabratchenko19123@yandex.ru")
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys("password123")
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    # Добавляем ожидание успешного редиректа
    WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"