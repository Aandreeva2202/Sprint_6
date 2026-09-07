import pytest

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data import *
from urls import BASE_URL


class TestOrderPage(BasePage):

    @pytest.mark.parametrize(
        'locator, order_data',
        [
            (MainPageLocators.ORDER_BUTTON_UP,
             ORDER_DATA_1),
            (MainPageLocators.ORDER_BUTTON_DOWN,
             ORDER_DATA_2)
        ] 
    )
    def test_create_order(self, order_page, locator, order_data):
        order_page.go_to_url(BASE_URL)
        order_page.scroll_to_element(locator)
        order_page.click_to_element(locator)
        order_page.set_order(order_data)
        assert order_page.get_text_from_element(locator) == 'text'
        