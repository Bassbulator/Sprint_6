from locators.faq_page_locators import FaqPageLocators

from pages.base_page import BasePage


class FaqPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_question_and_get_answer(self, question_locator, answer_locator) -> str:
        self.scroll_into_view(self.find(question_locator))
        self.click(question_locator)
        answer_element = self.wait_visible(answer_locator)
        answer_text = answer_element.text
        return answer_text
