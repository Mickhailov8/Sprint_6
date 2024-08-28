import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    @allure.step('Заполнение всех полей формы "Для кого самокат" и нажатие на кнопку "Далее"')
    def set_who_is_the_scooter_for(self,  name, surname, address, subway_station, phone):
        self.add_text_to_element(OrderPageLocators.FIELD_NAME, name)
        self.add_text_to_element(OrderPageLocators.FIELD_SURNAME, surname)
        self.add_text_to_element(OrderPageLocators.FIELD_ADDRESS, address)
        self.click_to_element(OrderPageLocators.KEY_SUBWAY)
        self.add_text_to_element(OrderPageLocators.FIELD_SUBWAY, subway_station)
        self.click_to_element(OrderPageLocators.DROPDOWN_STATION)
        self.add_text_to_element(OrderPageLocators.FIELD_PHONE, phone)
        self.click_to_element(OrderPageLocators.BUTTON_NEXT)

    @allure.step('Проверка загрузки страницы "Оформление аренды"')
    def check_title_about_rent(self):
        return self.find_element_with_wait(OrderPageLocators.TITLE_ABOUT_RENT)

    @allure.step('Заполнение полей формы "Когда привезти самокат"')
    def set_when_to_bring_scooter(self, date):
        self.add_text_to_element(OrderPageLocators.FIELD_DATE, date)
        self.click_to_element(OrderPageLocators.TITLE_ABOUT_RENT)

    @allure.step('Выбор срока аренды "Сутки"')
    def choose_period_one_day(self):
        self.click_to_element(OrderPageLocators.LIST_PERIOD)
        self.click_to_element(OrderPageLocators.CHECK_DAY_PERIOD)

    @allure.step('Выбор срока аренды "Двое суток"')
    def choose_period_two_days(self):
        self.click_to_element(OrderPageLocators.LIST_PERIOD)
        self.click_to_element(OrderPageLocators.CHECK_TWO_DAYS_PERIOD)

    @allure.step('Выбор цвета самоката "Серая безысходность"')
    def choose_color_scooter_grey(self):
        self.click_to_element(OrderPageLocators.CHECK_COLOR_GREY)

    @allure.step('Добавление комментария к заказу')
    def add_comment_to_order(self, comment):
        self.add_text_to_element(OrderPageLocators.FIELD_COMMENT, comment)

    @allure.step('Нажатие на кнопку "Заказать"')
    def click_to_order_button(self):
        self.click_to_element(OrderPageLocators.BUTTON_ORDER)

    @allure.step('Проверка появление попапа подтверждения заказа')
    def check_popup_confirmation(self):
        return self.find_element_with_wait(OrderPageLocators.POPUP_CONFIRM)

    @allure.step('Нажатие на кнопку "Да" в попапе подтверждения заказа')
    def click_to_yes_button(self):
        self.click_to_element(OrderPageLocators.POPUP_BUTTON_YES)

    @allure.step('Проверка попапа офрмления заказа')
    def check_order_confirmation(self):
        return self.get_text_from_element(OrderPageLocators.POPUP_ORDER_COMPLETE)
