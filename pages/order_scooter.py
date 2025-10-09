import allure
from locators.home_page_locators import HomePageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderScooter(BasePage):
    """
    Класс для автоматизации процесса заказа самоката
    """

    @allure.step("Нажать верхнюю кнопку заказа")
    def click_order_button_top(self):
        """
        Метод для клика по верхней кнопке заказа
        """
        self.click_on_element(HomePageLocators.ORDER_BUTTON_TOP)

    @allure.step("Нажать нижнюю кнопку заказа")
    def click_order_button_lower(self):
        """
        Метод для клика по нижней кнопке заказа
        Включает обработку cookie и прокрутку страницы
        """
        self.wait_for_element(HomePageLocators.COOKIE)
        self.click_on_element(HomePageLocators.COOKIE)
        self.scroll_to_element(HomePageLocators.ORDER_BUTTON_LOWER)
        self.wait_for_element(HomePageLocators.ORDER_BUTTON_LOWER)
        self.click_on_element(HomePageLocators.ORDER_BUTTON_LOWER)

    @allure.step("Заполнить первую страницу формы")
    def fill_first_order_form(self, name: str, surname: str, address: str, telephone: str):
        """
        Метод заполнения первой части формы заказа
        
        :param name: имя клиента
        :param surname: фамилия клиента
        :param address: адрес доставки
        :param telephone: номер телефона
        """
        self.send_keys_to_input(OrderPageLocators.NAME, name)
        self.send_keys_to_input(OrderPageLocators.SURNAME, surname)
        self.send_keys_to_input(OrderPageLocators.ADDRESS, address)
        self.send_keys_to_input(OrderPageLocators.TELEPHONE, telephone)

    @allure.step("Выбрать станцию метро")
    def choose_metro(self, station_name: str):
        """
        Метод выбора станции метро
        
        :param station_name: название станции метро
        """
        self.click_on_element(OrderPageLocators.BUTTON_METRO)
        self.send_keys_to_input(OrderPageLocators.BUTTON_METRO, station_name)
        self.click_on_element(OrderPageLocators.BUTTON_METRO_ENTER)

    @allure.step("Нажать кнопку 'Далее'")
    def click_button_further(self):
        """
        Метод клика по кнопке 'Далее'
        """
        self.click_on_element(OrderPageLocators.BUTTON_NEXT)

    @allure.step("Заполнить вторую страницу формы")
    def fill_second_order_form(self, date: str, comment: str):
        """
        Метод заполнения второй части формы заказа
        
        :param date: дата доставки
        :param comment: комментарий для курьера
        """
        self.send_keys_to_input(OrderPageLocators.WHEN_TO_BRING, date)
        self.send_keys_to_input(OrderPageLocators.COMMENT, comment)

    @allure.step("Выбрать срок аренды")
    def choose_rental_period(self):
        """
        Метод выбора срока аренды самоката
        """
        self.click_on_element(OrderPageLocators.RENTAL_PERIOD)
        self.click_on_element(OrderPageLocators.NUMBER_OF_DAYS)

    @allure.step("Выбрать цвет самоката")
    def choose_scooter_color(self):
        """
        Метод выбора цвета самоката
        """
        self.click_on_element(OrderPageLocators.SCOOTER_COLOR)

    @allure.step("Нажать кнопку 'Заказать'")
    def click_button_order(self):
        """
        Метод клика по кнопке 'Заказать'
        """
        self.click_on_element(OrderPageLocators.BUTTON_ORDER)
    
    @allure.step("Подтвердить заказ")
    def click_button_yes(self):
        """
        Метод для подтверждения заказа
        Выполняет клик по кнопке подтверждения
        """
        self.click_on_element(OrderPageLocators.PLACE_AN_ORDER)


    @allure.step("Посмотреть статус заказа")
    def click_button_view_status(self):
        """
        Метод для просмотра статуса заказа
        Выполняет клик по кнопке просмотра статуса
        """
        self.click_on_element(OrderPageLocators.VIEW_STATUS)


    @allure.step("Проверить создание заказа")
    def check_number_order(self):
        """
        Метод проверки успешного создания заказа
        Проверяет наличие номера заказа в URL страницы
        """
        order_number = self.get_text_on_element(OrderPageLocators.ORDER_CHECK)
        current_url = self.get_current_url()
        assert order_number in current_url, (
            f"Номер заказа {order_number} не найден в URL: {current_url}"
    )