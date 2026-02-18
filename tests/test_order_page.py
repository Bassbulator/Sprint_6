import pytest 
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from test_data_sets import ORDER_FROM_HEADER_BLACK, ORDER_FROM_FOOTER_GREY


class TestOrderPage:

    @allure.title("Оформление заказа самоката с черным цветом из хедера")
    @allure.description("Тест проверяет, что заказ можно оформить с входа из хедера с черным цветом")
    @allure.feature("Order")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_positive_order_flow_from_header_black_color(self, driver):
        order = OrderPage(driver)
        main = MainPage(driver)

        main.open()
        main.accept_cookies_if_present()

        main.click_order_button(ORDER_FROM_HEADER_BLACK["entry_point"])

        order.fill_step_one(
            first_name=ORDER_FROM_HEADER_BLACK["first_name"],
            last_name=ORDER_FROM_HEADER_BLACK["last_name"],
            address=ORDER_FROM_HEADER_BLACK["address"],
            metro_query=ORDER_FROM_HEADER_BLACK["metro_query"],
            phone=ORDER_FROM_HEADER_BLACK["phone"]
        )

        order.fill_step_two_black(
            rent_period_text=ORDER_FROM_HEADER_BLACK["rent_period"],
            comment=ORDER_FROM_HEADER_BLACK["comment"]
        )

        order.submit_order()

        assert order.yes_button_visible()

    @allure.title("Оформление заказа самоката с серым цветом из футера")
    @allure.description("Тест проверяет, что заказ можно оформить с входа из футера с серым цветом")
    @allure.feature("Order")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_positive_order_flow_from_footer_grey_color(self, driver):
        order = OrderPage(driver)
        main = MainPage(driver)

        main.open()
        main.accept_cookies_if_present()

        main.click_order_button(ORDER_FROM_FOOTER_GREY["entry_point"])

        order.fill_step_one(
            first_name=ORDER_FROM_FOOTER_GREY["first_name"],
            last_name=ORDER_FROM_FOOTER_GREY["last_name"],
            address=ORDER_FROM_FOOTER_GREY["address"],
            metro_query=ORDER_FROM_FOOTER_GREY["metro_query"],
            phone=ORDER_FROM_FOOTER_GREY["phone"]
        )

        order.fill_step_two_grey(
            rent_period_text=ORDER_FROM_FOOTER_GREY["rent_period"],
            comment=ORDER_FROM_FOOTER_GREY["comment"]
        )

        order.submit_order()

        assert order.yes_button_visible()