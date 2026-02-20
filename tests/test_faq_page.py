import pytest  # type: ignore[import]
import allure

from locators.faq_page_locators import FaqPageLocators
from pages.faq_page import FaqPage
from pages.main_page import MainPage
from constants import FaqAnswers

class TestFaqPage:
    
    @allure.title("Проверка открывающегося ответа на вопрос в FAQ")
    @allure.description("Тест проверяет, что при клике на вопрос в разделе FAQ открывается правильный ответ")
    @allure.feature("FAQ")
    @allure.severity(allure.severity_level.NORMAL)

    @pytest.mark.parametrize(
        "question_locator,answer_locator,expected",
        [
            (
                FaqPageLocators.HOW_MUCH,
                FaqPageLocators.HOW_MUCH_TEXT,
                FaqAnswers.HOW_MUCH_ANSWER
            ),
            (
                FaqPageLocators.WANT_FEW_SCOOTERS,
                FaqPageLocators.WANT_FEW_SCOOTERS_TEXT,
                FaqAnswers.WANT_FEW_SCOOTERS_ANSWER
            ),
            (
                FaqPageLocators.CALCULATING_RENTTIME,
                FaqPageLocators.CALCULATING_RENTTIME_TEXT,
                FaqAnswers.CALCULATING_RENTTIME_ANSWER
            ),
            (
                FaqPageLocators.ORDER_FOR_TODAY,
                FaqPageLocators.ORDER_FOR_TODAY_TEXT,
                FaqAnswers.ORDER_FOR_TODAY_ANSWER
            ),
            (
                FaqPageLocators.RETURN_SCOOTER_EARLY,
                FaqPageLocators.RETURN_SCOOTER_EARLY_TEXT,
                FaqAnswers.RETURN_SCOOTER_EARLY_ANSWER
            ),
            (
                FaqPageLocators.CHARGER_FOR_SCOOTER,
                FaqPageLocators.CHARGER_FOR_SCOOTER_TEXT,
                FaqAnswers.CHARGER_FOR_SCOOTER_ANSWER
            ),
            (
                FaqPageLocators.CANCEL_ORDER,
                FaqPageLocators.CANCEL_ORDER_TEXT,
                FaqAnswers.CANCEL_ORDER_ANSWER
            ),
            (
                FaqPageLocators.OUTSIDE_MKAD_DELIVERY,
                FaqPageLocators.OUTSIDE_MKAD_DELIVERY_TEXT,
                FaqAnswers.OUTSIDE_MKAD_DELIVERY_ANSWER
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
    def test_faq_answer_opens(self, driver, base_url, question_locator, answer_locator, expected):
        main = MainPage(driver)
        faq = FaqPage(driver)

        main.open(base_url)
        main.accept_cookies_if_present()
        actual = faq.open_question_and_get_answer(question_locator, answer_locator)
        assert actual == expected
