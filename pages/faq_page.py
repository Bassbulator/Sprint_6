from locators.faq_page_locators import FaqPageLocators

from pages.base_page import BasePage


class FaqPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_question_and_get_answer(self, question_locator, answer_locator) -> str:
        self.scroll_into_view(self.find(question_locator))
        self.click(question_locator)
        return self.find_visible(answer_locator).text
