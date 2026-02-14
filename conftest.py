import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


BASE_URL = "https://qa-scooter.praktikum-services.ru/"


@pytest.fixture
def base_url() -> str:
    return BASE_URL


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
