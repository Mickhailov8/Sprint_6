from selenium.webdriver.common.by import By
from data import DataForForms


class OrderPageLocators:

    TITLE_WHO_IS_THE_SCOOTER = By.XPATH, "//div[@class='Order_Header__BZXOb']"  # заголовок страницы "Для кого самокат"
    FIELD_NAME = By.XPATH, "//input[@placeholder='* Имя']"  # поле ввода "Имя"
    FIELD_SURNAME = By.XPATH, "//input[@placeholder='* Фамилия']"  # поле ввода "Фамилия"
    FIELD_ADDRESS = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"  # поле ввода "Адрес"
    FIELD_PHONE = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"  # поле ввода "Телефон"
    KEY_SUBWAY = By.XPATH, "//input[@placeholder='* Станция метро']/parent::div[@class='select-search__value']"  # поле "Станция метро"
    FIELD_SUBWAY = By.XPATH, "//input[@placeholder='* Станция метро']"  # поле ввода "Станция метро"
    DROPDOWN_STATION = By.XPATH, ("//input[@placeholder='* Станция метро']/" "parent::div[@class='select-search__value']/" "following::*[contains(text(), '") + DataForForms.METRO_STATION + "')]"  # выпадающий список станций метро
    BUTTON_NEXT = By.XPATH, "//button[text()='Далее']"  # кнопка "Далее"
    TITLE_ABOUT_RENT = By.XPATH, "//div[text()='Про аренду']"  # заголовок страницы "Про аренду"
    FIELD_DATE = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"  # поле "Когда привезти самокат"
    DROPDOWN_TODAY = By.XPATH, "//div[contains(@class, 'react-datepicker__day--today')]"  # сегодняшний день в выпадающем календаре
    LIST_PERIOD = By.XPATH, "//div[text()='* Срок аренды']"  # выпадающий список "Срок аренды"
    CHECK_DAY_PERIOD = By.XPATH, "//*[@class='Dropdown-option' and contains(text(), 'сутки')]"  # элемент "Сутки" выпадающего списка "Срок аренды"
    CHECK_TWO_DAYS_PERIOD = By.XPATH, "//*[@class='Dropdown-option' and contains(text(), 'двое суток')]"  # элемент "двое сутки" выпадающего списка "Срок аренды"
    CHECK_COLOR_BLACK = By.XPATH, "//label[@for='black']"  # чек-бокс "Черный жемчуг"
    CHECK_COLOR_GREY = By.XPATH, "//label[@for='grey']"  # чек-бокс "Серая безысходность"
    FIELD_COMMENT = By.XPATH, "//input[@placeholder='Комментарий для курьера']"  # поле "Комментарий для курьера"
    BUTTON_ORDER = By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']"  # кнопка "Заказать"
    POPUP_CONFIRM = By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']"  # всплывающее окно "Хотите оформить заказ?"
    POPUP_BUTTON_YES = By.XPATH, "//button[text()='Да']"  # кнопка "Да" в всплывающем окне "Хотите оформить заказ?"
    POPUP_ORDER_COMPLETE = By.XPATH, "//div[text()='Заказ оформлен']"  # надпись в всплывающем окне "Заказ оформлен"
    BUTTON_CHECK_STATUS = By.XPATH, "//button[text()='Посмотреть статус']"  # кнопка "Посмотреть статус" в всплывающем окне "Заказ оформлен"

