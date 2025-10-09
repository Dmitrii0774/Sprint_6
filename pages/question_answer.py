import allure
from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators


class QuestionAnswer(BasePage):
    """
    Класс для работы с разделом вопросов и ответов (FAQ) на главной странице
    """

    @allure.step("Нажать на вопрос с индексом {index}")
    def click_question(self, index: int):
        """
        Метод для открытия ответа на вопрос по указанному индексу
        
        :param index: индекс вопроса в списке FAQ
        """
        locator = HomePageLocators.FAQ_QUESTIONS_ITEMS[index]
        self.wait_for_element(HomePageLocators.COOKIE)
        self.click_on_element(HomePageLocators.COOKIE)
        self.scroll_to_element(locator)
        self.wait_for_element(locator)
        self.click_on_element(locator)

    @allure.step("Получить текст ответа для вопроса {index}")
    def get_answer_text(self, index: int) -> str:
        """
        Метод получения текста ответа на вопрос по указанному индексу
        
        :param index: индекс вопроса в списке FAQ
        :return: текст ответа
        """
        locator = HomePageLocators.FAQ_ANSWERS_ITEMS[index]
        return self.get_text_on_element(locator)

