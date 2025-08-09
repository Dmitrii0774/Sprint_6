import allure
from pages.order_scooter import OrderScooter
import data  # Импорт модуля с тестовыми данными


class TestOrderScooter:
    """
    Класс для тестирования процесса заказа самоката
    Содержит тесты для проверки различных сценариев оформления заказа
    """

    @allure.step("Тест успешного заказа самоката через верхнюю кнопку 'Заказать'")
    def test_success_ful_order_first(self, driver):
        """
        Тест полного цикла заказа самоката через верхнюю кнопку
        Проверяет:
        * Открытие формы заказа
        * Заполнение всех полей
        * Выбор параметров
        * Подтверждение заказа
        * Проверку статуса
        """
        # Создание экземпляра класса для работы с формой заказа
        order_scooter = OrderScooter(driver)
        
        # Открытие формы заказа через верхнюю кнопку
        order_scooter.click_order_button_top()
        
        # Заполнение первой части формы заказа
        order_scooter.fill_first_order_form(
            data.OrderScooterFirst.name,
            data.OrderScooterFirst.surname,
            data.OrderScooterFirst.address,
            data.OrderScooterFirst.telephone
        )
        
        # Выбор станции метро
        order_scooter.choose_metro(data.OrderScooterFirst.station_name)
        
        # Переход к следующему этапу
        order_scooter.click_button_further()
        
        # Заполнение второй части формы
        order_scooter.fill_second_order_form(
            data.OrderScooterFirst.date,
            data.OrderScooterFirst.comment
        )
        
        # Выбор срока аренды
        order_scooter.choose_rental_period()
        
        # Выбор цвета самоката
        order_scooter.choose_scooter_color()
        
        # Оформление заказа
        order_scooter.click_button_order()
        
        # Подтверждение заказа
        order_scooter.click_button_yes()
        
        # Просмотр статуса
        order_scooter.click_button_view_status()
        
        # Проверка создания заказа
        order_scooter.check_number_order()

    @allure.step("Тест успешного заказа самоката через нижнюю кнопку 'Заказать'")
    def test_success_ful_order_second(self, driver):
        """
        Тест полного цикла заказа самоката через нижнюю кнопку
        Проверяет:
        * Открытие формы заказа
        * Заполнение всех полей
        * Выбор параметров
        * Подтверждение заказа
        * Проверку статуса
        """
        # Создание экземпляра класса для работы с формой заказа
        order_scooter = OrderScooter(driver)
        
        # Открытие формы заказа через нижнюю кнопку
        order_scooter.click_order_button_lower()
        
        # Заполнение первой части формы заказа
        order_scooter.fill_first_order_form(
            data.OrderScooterSecond.name,
            data.OrderScooterSecond.surname,
            data.OrderScooterSecond.address,
            data.OrderScooterSecond.telephone
        )
        
        # Выбор станции метро
        order_scooter.choose_metro(data.OrderScooterSecond.station_name)
        
        # Переход к следующему этапу
        order_scooter.click_button_further()
        
        # Заполнение второй части формы
        order_scooter.fill_second_order_form(
            data.OrderScooterSecond.date,
            data.OrderScooterSecond.comment
        )
        
        # Выбор срока аренды
        order_scooter.choose_rental_period()
        
        # Выбор цвета самоката
        order_scooter.choose_scooter_color()
        
        # Оформление заказа
        order_scooter.click_button_order()
        
        # Подтверждение заказа
        order_scooter.click_button_yes()
        
        # Просмотр статуса
        order_scooter.click_button_view_status()
        
        # Проверка создания заказа
        order_scooter.check_number_order()