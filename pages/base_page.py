from __future__ import annotations
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from constants import BasePageLocators



class BasePage:
    def __init__(self, driver: WebDriver, timeout = 10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def open(self):
        self.driver.get(BasePageLocators.BASE_URL)
    
    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_visible(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
    )
    
    def click(self, locator, timeout=3):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
    )
        element.click()

    def safe_click_if_present(self, locator, timeout=3) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)).click()
            return True
        except TimeoutException:
            return False
        except Exception:
            return False

    def get_text(self, locator):
        return self.find(locator).text

    def type(self, locator, text, clear=True):
        el = self.find_visible(locator)
        if clear:
            el.clear()
        el.send_keys(text)

    def scroll_into_view(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center', inline:'nearest'});", element
        )

    def get_current_url(self):
        return self.driver.current_url
    
    def get_new_tab(self, driver):
        return driver.current_window_handle
    
    def switch_to_new_tab(self, original_window):
        try:
            self.wait.until(lambda d: len(d.window_handles) > 1)
            for window_handle in self.driver.window_handles:
                if window_handle != original_window:
                    self.driver.switch_to.window(window_handle)
                    break
        except Exception as e:
            return False
