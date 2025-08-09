import pytest
from selenium import webdriver

from curl import *


@pytest.fixture(scope="function")
def driver():
    """
    Фиксатура для инициализации и управления веб-драйвером Firefox
    
    Выполняет:
    * Создание экземпляра драйвера
    * Максимизацию окна браузера
    * Переход на домашнюю страницу
    * Очистка ресурсов после использования
    """
    # Инициализация драйвера
    driver = webdriver.Firefox()
    
    # Настройка окна браузера
    driver.maximize_window()
    
    # Переход на целевую страницу
    driver.get(home_page)
    
    # Yield для использования драйвера в тестах
    yield driver
    
    # Очистка ресурсов
    driver.quit()
