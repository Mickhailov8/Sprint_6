from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from data import Data


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # Ожидания появления элемента
    def find_element_with_wait(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    # Нажатие на элемент
    def click_to_element(self, locator):
        self.find_element_with_wait(locator).click()

    # Ввод текста
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    # Получения текста
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    # Скролл до элемента
    def scroll_to_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find_element_with_wait(locator))

    # Форматирования локатора
    def format_locators(self, locator_1, num):
        method,  locator = locator_1
        locator = locator.format(num)
        return (method, locator)

    # Ожидание загрузки сайта
    def wait_loading_site(self, url):
        WebDriverWait(self.driver,10).until(expected_conditions.url_to_be(url))

    # Получения текущего URL
    def get_current_url(self):
        return self.driver.current_url

    # Переключения на новую вкладку
    def switch_tab(self):
        return self.driver.switch_to.window(self.driver.window_handles[-1])