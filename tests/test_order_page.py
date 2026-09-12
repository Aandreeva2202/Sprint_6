import allure
import pytest

from locators.main_page_locators import MainPageLocators
from data import *
from urls import URL_MAIN_PAGE


@allure.title('Тесты на проверку заказа самоката')
@allure. description('Проверяем заказ самоката с двумя наборами данных')
class TestOrderPage:

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
        order_page.go_to_url(URL_MAIN_PAGE)
        order_page.scroll_to_element(locator)
        order_page.click_to_element(locator)
        order_page.set_order(order_data)
        assert 'Заказ оформлен' in order_page.check_order()
        