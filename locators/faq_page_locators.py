from selenium.webdriver.common.by import By


class FaqPageLocators:
    HOW_MUCH = (By.ID, "accordion__heading-24")
    HOW_MUCH_TEXT = (By.CSS_SELECTOR, "div.accordion__item > div#accordion__panel-24 p")
    WANT_FEW_SCOOTERS = (By.ID, "accordion__heading-25")
    WANT_FEW_SCOOTERS_TEXT = (By.CSS_SELECTOR, "div.accordion__item > div#accordion__panel-25 p")
    CALCULATING_RENTTIME = (By.ID, "accordion__heading-26")
    CALCULATING_RENTTIME_TEXT = (By.CSS_SELECTOR, "div.accordion__item > div#accordion__panel-26 p")
    ORDER_FOR_TODAY = (By.ID, "accordion__heading-27")
    ORDER_FOR_TODAY_TEXT = (By.CSS_SELECTOR, "div.accordion__item > div#accordion__panel-27 p")
    RETURN_SCOOTER_EARLY = (By.ID, "accordion__heading-28")
    RETURN_SCOOTER_EARLY_TEXT = (By.CSS_SELECTOR, "div.accordion__item > div#accordion__panel-28 p")
    CHARGER_FOR_SCOOTER = (By.ID, "accordion__heading-29")
    CHARGER_FOR_SCOOTER_TEXT = (By.CSS_SELECTOR, "div.accordion__item > div#accordion__panel-29 p")
    CANCEL_ORDER = (By.ID, "accordion__heading-30")
    CANCEL_ORDER_TEXT = (By.CSS_SELECTOR, "div.accordion__item > div#accordion__panel-30 p")
    OUTSIDE_MKAD_DELIVERY = (By.ID, "accordion__heading-31")
    OUTSIDE_MKAD_DELIVERY_TEXT = (By.CSS_SELECTOR, "div.accordion__item > div#accordion__panel-31 p")