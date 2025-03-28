import pytest
from selenium import webdriver
from faker import Faker
from urls import URLs  # Импортируем урлы

fake = Faker()

@pytest.fixture(scope="function")
def driver():
    """Инициализация браузера перед тестом, закрытие после"""
    driver = webdriver.Chrome()
    driver.get(URLs.BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def generate_email():
    """Генерация случайного email"""
    return fake.email()

@pytest.fixture
def generate_password():
    """Генерация случайного пароля (8 символов)"""
    return fake.password(length=8, special_chars=False)
