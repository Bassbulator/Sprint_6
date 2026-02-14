import pytest  # type: ignore[import]

from locators.faq_page_locators import FaqPageLocators
from pages.faq_page import FaqPage
from pages.main_page import MainPage


@pytest.mark.parametrize(
    "question_locator,answer_locator,expected",
    [
        (
            FaqPageLocators.HOW_MUCH,
            FaqPageLocators.HOW_MUCH_TEXT,
            "Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
        ),
        (
            FaqPageLocators.WANT_FEW_SCOOTERS,
            FaqPageLocators.WANT_FEW_SCOOTERS_TEXT,
            "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.",
        ),
        (
            FaqPageLocators.CALCULATING_RENTTIME,
            FaqPageLocators.CALCULATING_RENTTIME_TEXT,
            "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.",
        ),
        (
            FaqPageLocators.ORDER_FOR_TODAY,
            FaqPageLocators.ORDER_FOR_TODAY_TEXT,
            "Только начиная с завтрашнего дня. Но скоро станем расторопнее.",
        ),
        (
            FaqPageLocators.RETURN_SCOOTER_EARLY,
            FaqPageLocators.RETURN_SCOOTER_EARLY_TEXT,
            "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.",
        ),
        (
            FaqPageLocators.CHARGER_FOR_SCOOTER,
            FaqPageLocators.CHARGER_FOR_SCOOTER_TEXT,
            "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.",
        ),
        (
            FaqPageLocators.CANCEL_ORDER,
            FaqPageLocators.CANCEL_ORDER_TEXT,
            "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.",
        ),
        (
            FaqPageLocators.OUTSIDE_MKAD_DELIVERY,
            FaqPageLocators.OUTSIDE_MKAD_DELIVERY_TEXT,
            "Да, обязательно. Всем самокатов! И Москве, и Московской области.",
        ),
    ],
    ids=[
        "faq_how_much",
        "faq_few_scooters",
        "faq_rent_time",
        "faq_order_today",
        "faq_return_early",
        "faq_charger",
        "faq_cancel",
        "faq_outside_mkad",
    ],
)
def test_faq_answer_opens(driver, base_url, question_locator, answer_locator, expected):
    MainPage(driver).open(base_url).accept_cookies_if_present()
    faq = FaqPage(driver)
    actual = faq.open_question_and_get_answer(question_locator, answer_locator)
    assert actual == expected

