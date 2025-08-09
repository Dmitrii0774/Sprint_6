import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as Wait


class BasePage:
    """Базовый класс для всех страниц приложения"""

    def __init__(self, driver):
        """
        Инициализация страницы
        :param driver: объект веб-драйвера Selenium
        """
        self.driver = driver

    @allure.step("Подождать видимости элемента")
    def wait_for_element(self, locator, timeout=20):
        """
        Ожидает появления элемента на странице
        :param locator: локатор элемента
        :param timeout: время ожидания (сек)
        :return: найденный элемент
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator, timeout=20):
        """
        Прокручивает страницу до указанного элемента
        :param locator: локатор элемента
        :param timeout: время ожидания (сек)
        """
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator):
        """
        Выполняет клик по элементу
        :param locator: локатор элемента
        """
        element = self.wait_for_element(locator)
        element.click()

    @allure.step("Ввести текст в поле ввода")
    def send_keys_to_input(self, locator, keys, timeout=10):
        """
        Очищает поле ввода и вводит текст
        :param locator: локатор поля ввода
        :param keys: текст для ввода
        :param timeout: время ожидания (сек)
        """
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step("Найти элемент")
    def find_element(self, locator, timeout=10):
        """
        Находит элемент на странице
        :param locator: локатор элемента
        :param timeout: время ожидания (сек)
        :return: найденный элемент
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator, timeout=10):
        """
        Получает текст элемента
        :param locator: локатор элемента
        :param timeout: время ожидания (сек)
        :return: текст элемента
        """
        element = self.wait_for_element(locator, timeout)
        return element.text

    @allure.step("Подождать и проверить, что атрибут элемента содержит текст")
    def wait_for_attribute(self, locator, attribute, value, timeout=10):
        """
        Ожидает появления определенного текста в атрибуте элемента
        :param locator: локатор элемента
        :param attribute: имя атрибута
        :param value: ожидаемое значение
        :param timeout: время ожидания (сек)
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element_attribute(locator, attribute, value)
        )

    @allure.step("Получить текущий URL страницы")
    def get_current_url(self):
        """
        Возвращает текущий URL страницы
        :return: URL страницы
        """
        return self.driver.current_url

    @allure.step("Ожидание появления части URL в адресной строке")
    def wait_url_contains(self, url):
        """
        Ожидает появления указанной части URL
        :param url: часть URL для проверки
        """
        Wait(self.driver, 10).until(EC.url_contains(url))

    @allure.step("Переключение на следующую вкладку браузера")
    def switch_to_window_next_tab(self):
        """
        Переключает драйвер Selenium на вторую открытую вкладку браузера
        (индекс 1 в списке всех вкладок)
        """
        self.driver.switch_to.window(self.driver.window_handles[1])