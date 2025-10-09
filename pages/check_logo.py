import allure
from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators


class CheckLogoScooter(BasePage):
    """
    Класс для проверки функционала логотипа Самоката и связанных элементов
    """

    @allure.step("Нажать верхнюю кнопку заказа")
    def click_order_button_top(self):
        """
        Метод для клика по верхней кнопке заказа на главной странице
        """
        self.click_on_element(HomePageLocators.ORDER_BUTTON_TOP)

    @allure.step("Нажать на логотип Самоката")
    def click_scooter_logo(self):
        """
        Метод для клика по логотипу Самоката
        Ожидает появления элемента и выполняет клик
        """
        self.wait_for_element(HomePageLocators.LOGO_SCOOTER)
        self.click_on_element(HomePageLocators.LOGO_SCOOTER)

    @allure.step("Проверить URL главной страницы Самоката")
    def check_current_url_is_home_page(self, home_url: str):
        """
        Метод проверки текущего URL на соответствие ожидаемому
        
        :param home_url: ожидаемый URL главной страницы
        """
        current_url = self.get_current_url()
        assert current_url == home_url, (
            f"Неверное значение URL. "
            f"Ожидалось: {home_url}, "
            f"фактически: {current_url}"
        )


class CheckLogoYandex(BasePage):
    """
    Класс для проверки функционала логотипа Яндекса
    """

    @allure.step("Нажать на логотип Яндекса")
    def click_yandex_logo(self):
        """
        Метод для клика по логотипу Яндекса
        Ожидает появления элемента и выполняет клик
        """
        self.wait_for_element(HomePageLocators.LOGO_YANDEX)
        self.click_on_element(HomePageLocators.LOGO_YANDEX)

    @allure.step("Проверить URL целевой страницы")
    def check_current_url_is_home_page(self, home_url: str):
        """
        Метод проверки текущего URL на соответствие ожидаемому
        
        :param home_url: ожидаемый URL целевой страницы
        """
        current_url = self.get_current_url()
        assert current_url == home_url, (
            f"Неверное значение URL. "
            f"Ожидалось: {home_url}, "
            f"фактически: {current_url}"
        )