from selenium.webdriver.common.by import By


class MainPageLocators:
    COOKIE_ACCEPT = (By.ID, "rcc-confirm-button")

    ORDER_BUTTON_HEADER = (By.CSS_SELECTOR, "div.Header_Nav__AGCXC button.Button_Button__ra12g")
    ORDER_BUTTON_FOOTER = (By.CSS_SELECTOR, "div.Home_FinishButton__1_cWm button.Button_Button__ra12g")

    SCOOTER_LOGO = (By.CSS_SELECTOR, "a[class*='Header_LogoScooter']")
    YANDEX_LOGO = (By.CSS_SELECTOR, "a[class*='Header_LogoYandex']")
