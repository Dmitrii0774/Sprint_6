from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Поля ввода
    NAME = (By.XPATH, '//input[@placeholder="* Имя"]')
    SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    TELEPHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    WHEN_TO_BRING = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    # Элементы управления метро
    BUTTON_METRO = (By.XPATH, ".//input[contains(@placeholder, 'метро')]")
    BUTTON_METRO_ENTER = (By.XPATH, ".//li[@class='select-search__row']")

    # Элементы выбора срока аренды
    RENTAL_PERIOD = (By.XPATH, ".//span[@class='Dropdown-arrow']")
    NUMBER_OF_DAYS = (By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']")

    # Цвет самоката
    SCOOTER_COLOR = (By.ID, 'black')

    # Кнопки
    BUTTON_NEXT = (By.XPATH, "//button[text()='Далее']")
    BUTTON_ORDER = (
        By.XPATH,
        "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']"
    )
    PLACE_AN_ORDER = (By.XPATH, "//button[text()='Да']")
    VIEW_STATUS = (By.XPATH, "//button[text()='Посмотреть статус']")

    # Проверка заказа
    ORDER_CHECK = (By.XPATH, "//div[@class='Input_InputContainer__3NykH']")