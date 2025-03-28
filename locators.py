from selenium.webdriver.common.by import By

class Locators:
    """Локаторы для страниц Stellar Burgers"""

    # Локаторы страницы регистрации
    NAME_INPUT = (By.XPATH, "//input[@name='name']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='Email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    #ERROR_MESSAGE = (By.XPATH, "//p[@class='input__error']")
    # Локатор для сообщения об ошибке при некорректном пароле
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'input__error') and contains(text(), 'Некорректный пароль')]")

    # Локаторы страницы входа
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")

    # Локаторы личного кабинета
    PROFILE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход') and contains(@class, 'Account_button__14Yp3')]")

    # Локаторы конструктора
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")

    # Локатор для активной вкладки
    ACTIVE_TAB = (By.CSS_SELECTOR, "div.tab_tab_type_current__2BEPc")
