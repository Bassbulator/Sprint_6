import pytest
import allure

from pages.main_page import MainPage
from constants import BasePageLocators

class TestMainPage:

    @allure.title("Проверка редиректа на страницу Дзена")
    @allure.description("Тест проверяет, что при клике на логотип Яндекса происходит редирект на страницу Дзена")
    @allure.feature("Main Page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_click_on_yandex_logo_opens_dzen(self, driver):
        main = MainPage(driver)

        main.open()
        main.accept_cookies_if_present()

        main.click_yandex_logo()

        # Сохраняем идентификатор текущей вкладки
        original_window = main.get_new_tab(driver)

        main.click_yandex_logo()
        main.wait_for_new_tab(original_window)

        assert main.get_current_url() == BasePageLocators.DZEN_URL



    @allure.title("Проверка перехода на главную страницу заказа Самоката")
    @allure.description("Тест проверяет, что после нажатия на логотип Самоката происходит переход на главную страницу заказа")
    @allure.feature("Main Page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_click_on_scooter_logo_opens_main_page(self, driver):
        main = MainPage(driver)

        main.open()
        main.accept_cookies_if_present()

        main.click_order_button("header")
        main.click_scooter_logo()

        assert main.get_current_url() == BasePageLocators.BASE_URL
