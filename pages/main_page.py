from __future__ import annotations

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    def accept_cookies_if_present(self) -> bool:
        return self.safe_click_if_present(MainPageLocators.COOKIE_ACCEPT)

    def click_order_button(self, entry_point: str):
        if entry_point == "header":
            self.click(MainPageLocators.ORDER_BUTTON_HEADER)
        elif entry_point == "footer":
            footer_button = self.find(MainPageLocators.ORDER_BUTTON_FOOTER)
            self.scroll_into_view(footer_button)
            self.click(footer_button)
        else:
            raise ValueError(f"Unknown entry_point: {entry_point}")

    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)
