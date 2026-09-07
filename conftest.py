import pytest
import geckodriver_autoinstaller

from pages.main_page import MainPage
#from pages.order_page import OrderPage
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    geckodriver_autoinstaller.install()
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def main_page(driver):
    page = MainPage(driver)
    page.timeout = 10
    return page

#@pytest.fixture(scope="function")
#def order_page(driver):
    page = OrderPage(driver)
    page.timeout = 10
    return page
