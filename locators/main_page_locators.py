from selenium.webdriver.common.by import By


class MainPageLocators:

    LOGO_YANDEX = By.XPATH, "//a[@href='//yandex.ru']"  # логотип "Яндекс" в хедере
    LOGO_SAMOKAT = By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']"  # логотип "Самокат" в хедере
    BUTTON_ORDER_HEADER = By.XPATH, "//button[@class='Button_Button__ra12g']"  # кнопка "Заказать" в хедере
    BUTTON_ORDER_DOWN = By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/child::button"  # кнопка "Заказать" внизу экрана
    QUESTIONS_LIST = By.XPATH, "//div[text()='Вопросы о важном']/parent::div"  # раздел "Вопросы о важном"
    ACCORDION_QUESTION = By.XPATH, "//div[@aria-controls='accordion__panel-{}']"  # поле с вопросами
    ACCORDION_ANSWER = By.ID, "accordion__panel-{}"  # поле с ответами
    HEADING_TEXT = By.CLASS_NAME, "Home_Header__iJKdX"  # заголовок страницы "Самокат на пару дней"
    BUTTON_COOKE_ACCEPT = By.XPATH, "//button[text()='да все привыкли']"  # кнопка "да все привыкли"

