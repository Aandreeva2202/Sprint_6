import allure

from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from locators.switch_yandex_locators import SwitchYandexLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Клик на вопрос')
    def click_to_question(self, num):
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        #self.scroll_to_element(MainPageLocators.QUESTION_LOCATOR_TO_SCROLL)
        self.find_element_with_wait(locator_q_formatted)
        self.click_to_element(locator_q_formatted)

    @allure.step('Получение ответа на вопрос')
    def get_answer_text(self, num):
        locator_a_formatted = self.format_locators(
            MainPageLocators.ANSWER_LOCATOR, num)
        self.find_element_with_wait(locator_a_formatted)
        return self.get_text_from_element(locator_a_formatted)

    @allure.step('Проверяем ответ')
    def check_answer(self, num, my_text):
        self.scroll_to_element(MainPageLocators.QUESTION_LOCATOR_TO_SCROLL)
        self.click_to_question(num)
        text = self.get_answer_text(num)
        return text == my_text
    
    @allure.step('Клик на кнопку заказа')
    def click_to_order(self):
        self.click_to_element(MainPageLocators.ORDER_BUTTON_UP)
        self.find_element_with_wait(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Клик на локатор самоката')
    def click_to_logo_scooter(self):
        self.click_to_element(MainPageLocators.LOGO_SCOOTER_LOCATOR)
        return self.get_text_from_element(MainPageLocators.HEADER_LOCATOR)

    @allure.step('Клик на локатор яндекса')
    def click_to_logo_yandex(self):
        self.click_to_element(MainPageLocators.LOGO_YANDEX_LOCATOR)
        self.swith_to_another_window()
        return self.find_element_with_wait(SwitchYandexLocators.SEARCH_INPUT_LOCATOR)
     