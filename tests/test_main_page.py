import pytest
import allure

from pages.main_page import MainPage
from pages.base_page import BasePage


class TestMainPage:

    @allure.title("Проверка редиректа на страницу Дзена")
    @allure.description("Тест проверяет, что при клике на логотип Яндекса происходит редирект на страницу Дзена")
    @allure.feature("Main Page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_click_on_yandex_logo_opens_dzen(self, driver, base_url):
        main = MainPage(driver)
        base = BasePage(driver)

        base.open(base_url)
        main.accept_cookies_if_present()

        main.click_yandex_logo()

        # Сохраняем идентификатор текущей вкладки
        original_window = driver.current_window_handle

        main.click_yandex_logo()
        main.wait_for_new_tab(original_window)

        assert "dzen.ru" in driver.current_url


    @allure.title("Проверка перехода на главную страницу заказа Самоката")
    @allure.description("Тест проверяет, что после нажатия на логотип Самоката происходит переход на главную страницу заказа")
    @allure.feature("Main Page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_click_on_scooter_logo_opens_main_page(self, driver, base_url):
        main = MainPage(driver)
        base = BasePage(driver)

        base.open(base_url)
        main.accept_cookies_if_present()

        main.click_order_button("header")
        main.click_scooter_logo()

        assert base_url in base.get_current_url()
