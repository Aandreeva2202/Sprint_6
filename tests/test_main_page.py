import allure
import pytest

from data import ANSWERS_DATA
from urls import URL_MAIN_PAGE


@allure.title('Тесты на проверку вопросов')
#@allure. description('')
class TestMainPage:

    @pytest.mark.parametrize(
            'num',
            [0,1,2,3,4,5,6,7]
    )
    def test_check_heading1_text(self, num, main_page):
        main_page.go_to_url(URL_MAIN_PAGE)
        assert main_page.check_answer(num, ANSWERS_DATA[num])
