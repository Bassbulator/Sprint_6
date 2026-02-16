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

    def wait_for_new_tab(self, original_window):
        try:
            self.wait.until(lambda d: len(d.window_handles) > 1)
            for window_handle in self.driver.window_handles:
                if window_handle != original_window:
                    self.driver.switch_to.window(window_handle)
                    break
        except Exception as e:
            print("Не удалось пройти капчу")
            return False