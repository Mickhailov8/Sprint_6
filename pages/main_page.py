import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from data import Data


class MainPage(BasePage):

    @allure.step('Проскроллить страницу до вопросов')
    def scroll_to_question(self):
        self.scroll_to_element(MainPageLocators.QUESTIONS_LIST)

    @allure.step('Получение текста ответа нажатием на вопрос')
    def get_answer_text(self, num):
        locator_question_format = self.format_locators(MainPageLocators.ACCORDION_QUESTION, num)
        locator_answer_format = self.format_locators(MainPageLocators.ACCORDION_ANSWER, num)
        self.click_to_element(locator_question_format)
        return self.get_text_from_element(locator_answer_format)

    @allure.step('Проскроллить до кнопки "Заказать" внизу экрана и нажать ее')
    def scroll_and_click_to_down_order_button(self):
        self.scroll_to_element(MainPageLocators.BUTTON_ORDER_DOWN)
        self.click_to_element(MainPageLocators.BUTTON_ORDER_DOWN)

    @allure.step('Получить заголовок страницы "Самокат на пару дней"')
    def get_heading_text(self):
        return self.get_text_from_element(MainPageLocators.HEADING_TEXT)

    @allure.step('Нажать на кнопку "да все привыкли"')
    def click_to_cooke_accept(self):
        self.click_to_element(MainPageLocators.BUTTON_COOKE_ACCEPT)

    @allure.step('Нажать на логотип "Яндекс" в хедере')
    def click_to_yandex_logo(self):
        self.click_to_element(MainPageLocators.LOGO_YANDEX)

    @allure.step('Нажать на логотип "Самокат" в хедере')
    def click_to_samokat_logo(self):
        self.click_to_element(MainPageLocators.LOGO_SAMOKAT)

    @allure.step('Нажать на кнопку "Заказать" в хедере')
    def click_to_order_button_on_header(self):
        self.click_to_element(MainPageLocators.BUTTON_ORDER_HEADER)

    @allure.step('Переключиться на новую вкладку')
    def switch_tab_on_browserer(self):
        return self.switch_tab()

    @allure.step('Получить текущий URL')
    def get_url_dzen(self):
        return self.get_current_url()

    @allure.step('Ожидание загрузки сайта')
    def wait_loading_site_Dzen(self):
        self.wait_loading_site(Data.URL_DZEN)