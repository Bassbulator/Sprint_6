import pytest

from pages.main_page import MainPage


def test_yandex_logo_opens_dzen_in_new_window(driver, base_url):
    main = MainPage(driver).open(base_url)
    main.accept_cookies_if_present()

    old_handles = driver.window_handles
    main.click_yandex_logo()
    main.wait_for_new_window(old_handles)

    new_handle = [h for h in driver.window_handles if h not in old_handles][0]
    driver.switch_to.window(new_handle)

    main.url_contains("dzen")
    assert "dzen" in driver.current_url.lower()

