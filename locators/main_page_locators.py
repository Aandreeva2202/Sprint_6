from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION_LOCATOR = [By.ID, 'accordion__heading-{}']

    ANSWER_LOCATOR = By.XPATH, '//*[@id="accordion__panel-{}"]/p'

    QUESTION_LOCATOR_TO_SCROLL = [By.ID, 'accordion__heading-7']

    LOGO_YANDEX_LOCATOR = By.XPATH, ".//img[@alt='Yandex']"

    LOGO_SCOOTER_LOCATOR = By.XPATH, ".//img[@alt='Scooter']"

    ORDER_BUTTON_UP = By.XPATH, ".//button[@class='Button_Button__ra12g']"

    ORDER_BUTTON_DOWN = By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"

    HEADER_LOCATOR = By.XPATH, ".//div[@class='Home_Header__iJKdX']"
