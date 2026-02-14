from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def type_first_name(self, first_name):
        self.find(OrderPageLocators.INPUT_NAME).send_keys(first_name)

    def type_last_name(self, last_name):
        self.find(OrderPageLocators.INPUT_LAST_NAME).send_keys(last_name)

    def type_address(self, address):
        self.find(OrderPageLocators.INPUT_ADDRESS).send_keys(address)

    def type_phone_number(self, phone):
        self.find(OrderPageLocators.INPUT_PHONE_NUMBER).send_keys(phone)

    def choose_subway_station(self, query: str):
        el = self.find(OrderPageLocators.SUBWAY_STATION_INPUT)
        el.send_keys(query)
        self.wait_visible(OrderPageLocators.SUBWAY_STATION_FIRST_OPTION).click()

    def click_next_button(self):
        self.wait_visible(OrderPageLocators.NEXT_BUTTON)
        self.click(OrderPageLocators.NEXT_BUTTON)

    def fill_step_one(self, first_name, last_name, address, metro_query, phone):
        self.type_first_name(first_name)
        self.type_last_name(last_name)
        self.type_address(address)
        self.choose_subway_station(metro_query)
        self.type_phone_number(phone)
        self.click_next_button()

#    def type_date(self, date_str: str):
#        el = self.find(OrderPageLocators.DATE_INPUT)
#        el.send_keys(date_str)
#        el.send_keys(Keys.ENTER)

    def type_date(self):
        self.wait_visible(OrderPageLocators.DATE_INPUT)
        self.click(OrderPageLocators.DATE_INPUT)
        self.wait_visible(OrderPageLocators.CALENDAR)
        self.click(OrderPageLocators.CALENDDAR_SELECT)

    def choose_rent_period(self, rent_period_text: str):
        self.wait_visible(OrderPageLocators.RENT_PERIOD_DROPDOWN).click()
        # build locator for the option with provided text
        locator = (
            OrderPageLocators.RENT_PERIOD_OPTION_BY_TEXT[0],
            OrderPageLocators.RENT_PERIOD_OPTION_BY_TEXT[1].format(text=rent_period_text),
        )
        self.wait_visible(locator).click()

    def choose_color(self, color: str):
        if color.lower() == "black":
            self.find(OrderPageLocators.COLOR_BLACK).click()
        else:
            self.find(OrderPageLocators.COLOR_GREY).click()

    def type_comment(self, comment: str):
        self.find(OrderPageLocators.COMMENT_FIELD).send_keys(comment)

    def fill_step_two(self, rent_period_text, color, comment):
        self.type_date()
        self.choose_rent_period(rent_period_text)
        self.choose_color(color)
        self.type_comment(comment)

    def submit_order(self):
        order_btn = self.wait_visible(OrderPageLocators.ORDER_BUTTON)
        order_btn.click()

    def yes_button_visible(self):
        return WebDriverWait(self.driver).until(
            EC.visibility_of_element_located(OrderPageLocators.CONFIRM_YES_BUTTON)
            )

    def wait_success_modal(self):
        return WebDriverWait(self.driver, max(20, self.timeout * 2)).until(
            EC.visibility_of_element_located(OrderPageLocators.SUCCESS_MODAL_TEXT)
        )
