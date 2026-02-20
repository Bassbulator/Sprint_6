from __future__ import annotations

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    def accept_cookies_if_present(self) -> bool:
        return self.safe_click_if_present(MainPageLocators.COOKIE_ACCEPT)

    def click_order_button_from_header(self, entry_point="header"):
        self.click(MainPageLocators.ORDER_BUTTON_HEADER)

    def click_order_button_from_footer(self, entry_point="footer"):
        footer_button = self.find(MainPageLocators.ORDER_BUTTON_FOOTER)
        self.scroll_into_view(footer_button)
        self.click(footer_button)

    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)

    def wait_for_new_tab(self, original_window):
        self.switch_to_new_tab(original_window)
