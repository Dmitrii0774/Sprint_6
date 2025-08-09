import allure
import pytest
import data  # Импорт модуля с тестовыми данными

from pages.question_answer import QuestionAnswer  # Импорт класса для работы с FAQ


class TestQuestionAnswer:
    """
    Класс для тестирования раздела вопросов и ответов (FAQ)
    Содержит тесты для проверки корректности отображения ответов
    """

    @allure.step("Проверка ответа на вопрос №{index}")
    @pytest.mark.parametrize(
        "index, expected_answer", data.Data.ACCORDION_DATA
    )  # Параметризация теста
    def test_faq_answers(
        self, driver, index: int, expected_answer: str
    ):
        """
        Тест проверки корректности отображения ответов в FAQ

        Параметры:
        driver - веб-драйвер для взаимодействия с браузером
        index - индекс вопроса в списке FAQ
        expected_answer - ожидаемый текст ответа

        Проверяет:
        * Открытие вопроса по индексу
        * Соответствие отображенного ответа ожидаемому
        """
        # Создание экземпляра класса для работы с FAQ
        question_answer = QuestionAnswer(driver)
        
        # Открытие вопроса по указанному индексу
        question_answer.click_question(index)
        
        # Получение текста ответа
        answer_text = question_answer.get_answer_text(index)
        
        # Проверка соответствия полученного ответа ожидаемому
        assert (
            answer_text == expected_answer
        ), f"Текст ответа не соответствует ожидаемому. " \
           f"Ожидалось: {expected_answer}, " \
           f"получено: {answer_text}"