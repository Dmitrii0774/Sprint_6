import allure

from pages.check_logo import CheckLogoScooter, CheckLogoYandex
from curl import *


class TestCheckLogoScooter:
    """
    Класс для тестирования работы логотипов на главной странице
    """

    @allure.step("Тест проверки логотипа Самокат")
    def test_check_logo_scooter(self, driver):
        """
        Тест проверки функциональности логотипа Самоката
        
        Проверяет:
        * Нажатие кнопки заказа
        * Кликабельность логотипа
        * Корректность перехода на главную страницу
        """
        check_logo = CheckLogoScooter(driver)
        check_logo.click_order_button_top()
        check_logo.click_scooter_logo()
        check_logo.check_current_url_is_home_page(home_page)

    @allure.step("Тест проверки логотипа Яндекс")
    def test_check_logo_yandex(self, driver):
        """
        Тест проверки функциональности логотипа Яндекса
        
        Проверяет:
        * Нажатие на логотип Яндекса
        * Открытие новой вкладки
        * Корректность перехода на Дзен
        """
        check_logo = CheckLogoYandex(driver)
        check_logo.click_yandex_logo()
        check_logo.switch_to_window_next_tab()
        check_logo.wait_url_contains(page_dzen)

        expected_url = 'https://dzen.ru/?yredirect=true'
        current_url = check_logo.get_current_url()
        assert current_url == expected_url, (
            f"Неверное значение URL. "
            f"Ожидалось: {expected_url}, "
            f"фактически: {current_url}"
        )