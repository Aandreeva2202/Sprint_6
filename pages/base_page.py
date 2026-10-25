import random

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver): 
        self.driver = driver
        self.timeout = 15
        self.wait = WebDriverWait(self.driver, self.timeout)

    def go_to_url(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_to_element(self, some):
        self.wait.until(expected_conditions.element_to_be_clickable(some))
        self.driver.find_element(*some).click()

    def click_to_enter(self, locator):
        element = self.wait.until(expected_conditions.element_to_be_clickable(locator))
        element.send_keys(Keys.ENTER)

    def scroll_to_element(self, locator):
        scroll_element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll_element)

    #добавить текст на элемент
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    #получение текста с элемента
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return method, locator

    #переход на другое окно
    def swith_to_another_window(self):
        windows_list = self.driver.window_handles
        self.driver.switch_to.window(windows_list[-1]) 

    def select_option_click(self, locator):
        # Ждём появления опций в выпадающем списке
        options = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_all_elements_located((locator)))
        # Кликаем по нужной опции (первая подходящая)
        for option in options:
            if "Сокол" in option.text:
                option.click()
                break

    def select_random(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_all_elements_located((locator)))
        elements =  self.driver.find_elements(*locator)
        random_option = random.choice(elements)
        random_option.click()
