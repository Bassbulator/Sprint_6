from selenium.webdriver.common.by import By


class FaqPageLocators:
    HOW_MUCH = (By.ID, "accordion__heading-0")
    HOW_MUCH_TEXT = (By.CSS_SELECTOR, "div.accordion__item > div#accordion__panel-0 p")
    WANT_FEW_SCOOTERS = (By.ID, "accordion__heading-1")
    WANT_FEW_SCOOTERS_TEXT = (By.CSS_SELECTOR, "div.accordion__item > div#accordion__panel-1 p")
    CALCULATING_RENTTIME = (By.ID, "accordion__heading-2")
    CALCULATING_RENTTIME_TEXT = (By.CSS_SELECTOR, "div.accordion__item > div#accordion__panel-2 p")
    ORDER_FOR_TODAY = (By.ID, "accordion__heading-3")
    ORDER_FOR_TODAY_TEXT = (By.CSS_SELECTOR, "div.accordion__item > div#accordion__panel-3 p")
    RETURN_SCOOTER_EARLY = (By.ID, "accordion__heading-4")
    RETURN_SCOOTER_EARLY_TEXT = (By.CSS_SELECTOR, "div.accordion__item > div#accordion__panel-4 p")
    CHARGER_FOR_SCOOTER = (By.ID, "accordion__heading-5")
    CHARGER_FOR_SCOOTER_TEXT = (By.CSS_SELECTOR, "div.accordion__item > div#accordion__panel-5 p")
    CANCEL_ORDER = (By.ID, "accordion__heading-6")
    CANCEL_ORDER_TEXT = (By.CSS_SELECTOR, "div.accordion__item > div#accordion__panel-6 p")
    OUTSIDE_MKAD_DELIVERY = (By.ID, "accordion__heading-7")
    OUTSIDE_MKAD_DELIVERY_TEXT = (By.CSS_SELECTOR, "div.accordion__item > div#accordion__panel-7 p")