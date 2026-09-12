import allure

from urls import URL_MAIN_PAGE


@allure.title('Тест на проверку кнопки лого Самокат')
class TestSwitchScooter:
    def test_switch_scooter(self, main_page):
        main_page.go_to_url(URL_MAIN_PAGE)
        main_page.click_to_order()
        assert 'Самокат' in main_page.click_to_logo_scooter()
