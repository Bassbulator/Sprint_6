from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Step 1
    INPUT_NAME = (By.CSS_SELECTOR, "input[placeholder='* Имя']")
    INPUT_LAST_NAME = (By.CSS_SELECTOR, "input[placeholder='* Фамилия']")
    INPUT_ADDRESS = (By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']")
    INPUT_PHONE_NUMBER = (By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']")
    SUBWAY_STATION_INPUT = (By.CLASS_NAME, "select-search__input")
    SUBWAY_STATION_FIRST_OPTION = (
        By.CSS_SELECTOR,
        ".select-search__select .select-search__row button",
    )
    NEXT_BUTTON = (By.CSS_SELECTOR, "button.Button_Button__ra12g.Button_Middle__1CSJM")

    # Step 2
    DATE_INPUT = (By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']")
    CALENDAR = (By.XPATH, "//div[@class='react-datepicker-popper']")
    CALENDDAR_SELECT = (By.XPATH, "//div[@class='react-datepicker-popper']//div[@class='react-datepicker__day react-datepicker__day--017']")
    RENT_PERIOD_DROPDOWN = (By.CSS_SELECTOR, "span.Dropdown-arrow")
    RENT_PERIOD_OPTION_BY_TEXT = (
        By.XPATH,
        "//div[contains(@class,'Dropdown-menu')]//div[contains(@class,'Dropdown-option') and normalize-space(text())='{text}']",
    )
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT_FIELD = (By.CSS_SELECTOR, "input[placeholder='Комментарий для курьера']")

    ORDER_BUTTON = (By.XPATH, "//div[contains(@class,'Order_Buttons')]//button[normalize-space(text())='Заказать']")
    CONFIRM_YES_BUTTON = (By.XPATH, "//div[contains(@class,'Order_Modal')]//button[normalize-space(text())='Да']")

    SUCCESS_MODAL_TEXT = (
        By.XPATH,
        "//div[contains(@class,'Order_Modal')]//div[contains(text(),'Хотите оформить заказ?')]",
    )

#.//div[@class='select-search__select']/ul/li[@class='select-search__row'][1]/button subway selector