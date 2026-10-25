import allure

from urls import URL_MAIN_PAGE


@allure.title('Тест на проверку кнопки лого Яндекс')
class TestSwitchYandex:
    def test_switch_yandex(self, main_page):
        main_page.go_to_url(URL_MAIN_PAGE)
        assert main_page.click_to_logo_yandex()
