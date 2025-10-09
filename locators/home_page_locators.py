from selenium.webdriver.common.by import By


class HomePageLocators:
    # Логотипы
    LOGO_YANDEX = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    LOGO_SCOOTER = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")

    # Кнопки заказа
    ORDER_BUTTON_TOP = (
        By.XPATH,
        ".//div[starts-with(@class, 'Header')]/button[text()='Заказать']"
    )
    ORDER_BUTTON_LOWER = (
        By.XPATH,
        ".//div[starts-with(@class, 'Home')]/button[text()='Заказать']"
    )

    # Куки
    COOKIE = (By.XPATH, "//button[text()='да все привыкли']")

    # Вопросы FAQ
    FAQ_QUESTIONS_ITEMS = {
        0: (By.ID, "accordion__heading-0"),
        1: (By.ID, "accordion__heading-1"),
        2: (By.ID, "accordion__heading-2"),
        3: (By.ID, "accordion__heading-3"),
        4: (By.ID, "accordion__heading-4"),
        5: (By.ID, "accordion__heading-5"),
        6: (By.ID, "accordion__heading-6"),
        7: (By.ID, "accordion__heading-7"),
    }

    # Ответы FAQ
    FAQ_ANSWERS_ITEMS = {
        0: (By.ID, "accordion__panel-0"),
        1: (By.ID, "accordion__panel-1"),
        2: (By.ID, "accordion__panel-2"),
        3: (By.ID, "accordion__panel-3"),
        4: (By.ID, "accordion__panel-4"),
        5: (By.ID, "accordion__panel-5"),
        6: (By.ID, "accordion__panel-6"),
        7: (By.ID, "accordion__panel-7"),
    }