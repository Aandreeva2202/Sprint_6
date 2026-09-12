import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from data import *


class OrderPage(BasePage):

    @allure.step("Заполняем первую часть данных заказа")
    def set_fields_first_part(self, data):
        self.add_text_to_element(OrderPageLocators.NAME_LOCATOR, data['name'])
        self.add_text_to_element(OrderPageLocators.LAST_NAME_LOCATOR, data['last_name'])
        self.add_text_to_element(OrderPageLocators.ADDRESS_LOCATOR, data['adress'])
        self.click_to_element(OrderPageLocators.METRO_LOCATOR)
        self.add_text_to_element(OrderPageLocators.METRO_INPUT, data['metro'])
        self.select_option_click(OrderPageLocators.METRO_SELECT)
        self.add_text_to_element(OrderPageLocators.PHONE_LOCATOR, data['phone'])

    @allure.step("Заполняем вторую часть данных заказа")
    def set_fields_second_part(self, data):
        self.add_text_to_element(OrderPageLocators.DATE_LOCATOR, data['date'])
        self.click_to_enter(OrderPageLocators.DATE_LOCATOR)
        self.click_to_element(OrderPageLocators.PERIOD_LOCATOR)
        self.select_random(OrderPageLocators.PERIOD_INPUT)
        self.click_to_element(OrderPageLocators.BLACK_CHECKBOX_LOCATOR)
        self.add_text_to_element(OrderPageLocators.COMMENT_LOCATOR, data['comment'])

    @allure.step("Оформляем заказ")
    def set_order(self, data):
        self.set_fields_first_part(data=data)
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)
        self.set_fields_second_part(data=data)
        self.click_to_element(OrderPageLocators.ORDER_BUTTON)
        self.click_to_element(OrderPageLocators.YES_BUTTON)

    @allure.step("Проверяем заказ")
    def check_order(self):
        text = self.get_text_from_element(OrderPageLocators.ORDER_CREATION_SUCCESS)
        return text
    