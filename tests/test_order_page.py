import pytest 

from datetime import datetime, timedelta
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.base_page import BasePage


def _tomorrow_date() -> str:
    return (datetime.now() + timedelta(days=1)).strftime("%d.%m.%Y")

@pytest.mark.parametrize(
    "entry_point,order_data",
    [
        (
            "header",
            {
                "first_name": "Иван",
                "last_name": "Иванов",
                "address": "Москва, Красная площадь, 1",
                "metro_query": "Чер",
                "phone": "+79999999999",
                "rent_period": "сутки",
                "color": "black",
                "comment": "Test1",
            },
        ),
        (
            "footer",
            {
                "first_name": "Мария",
                "last_name": "Петрова",
                "address": "Москва, Тверская, 1",
                "metro_query": "Сок",
                "phone": "+79990000000",
                "rent_period": "двое суток",
                "color": "grey",
                "comment": "Test2",
            },
        ),
    ],
    ids=["order_from_header", "order_from_footer"],
)
def test_positive_order_flow_two_datasets(driver, base_url, order_data, entry_point):
    base_page = BasePage(driver)
    order = OrderPage(driver)
    main = MainPage(driver)

    base_page.open(base_url)
    main.accept_cookies_if_present()

    main.click_order_button(entry_point)

    order.fill_step_one(
        first_name=order_data["first_name"],
        last_name=order_data["last_name"],
        address=order_data["address"],
        metro_query=order_data["metro_query"],
        phone=order_data["phone"]
    )
    
    order.click_next_button()

    order.fill_step_two(
        rent_period_text=order_data["rent_period"],
        color=order_data["color"],
        comment=order_data["comment"]
    )

    order.submit_order()

    expected_text = order.wait_success_modal()
    yes_button_is_visible = order.yes_button_visible()
    assert expected_text == "Хотите оформить заказ?"
    assert yes_button_is_visible == True