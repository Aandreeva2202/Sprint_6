from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_LOCATOR = By.XPATH, ".//input[@placeholder='* Имя']"
    LAST_NAME_LOCATOR = By.XPATH, ".//input[@placeholder='* Фамилия']"
    ADDRESS_LOCATOR = By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"
    METRO_LOCATOR = By.XPATH, ".//div[@class='select-search']"
    METRO_INPUT = By.XPATH, ".//input[@class='select-search__input']"
    #METRO_SELECT = By.XPATH, ".//div[@class='select-search__option']"
    METRO_SELECT = By.CSS_SELECTOR, ".select-search__option"
    PHONE_LOCATOR = By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"

    NEXT_BUTTON = By.XPATH, ".//button[text()='Далее']"

    DATE_LOCATOR = By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"
    PERIOD_LOCATOR = By.XPATH, ".//div[text()='* Срок аренды']"
    PERIOD_INPUT = By.XPATH, "//div[@class='Dropdown-option']"
    BLACK_CHECKBOX_LOCATOR = By.XPATH, ".//input[@id='black']"
    GREY_CHECKBOX_LOCATOR = By.XPATH, ".//input[@id='grey']"
    COMMENT_LOCATOR = By.XPATH, ".//input[@placeholder='Комментарий для курьера']"

    ORDER_BUTTON = By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"

    ORDER_MODAL = By.XPATH, ".//div[@class='Order_ModalHeader__3FDaJ' and text() = 'Хотите оформить заказ?']"
    YES_BUTTON = By.XPATH, ".//button[text()='Да']"
    ORDER_CREATION_SUCCESS = By.XPATH, ".//div[@class='Order_ModalHeader__3FDaJ' and text() = 'Заказ оформлен']"
