import pytest
from selenium import webdriver
from data.data_1 import BASE_URL
from pages.faq_page import FAQPage

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture
def faq_page(driver):
    driver.get(BASE_URL)
    page = FAQPage(driver)
    page.accept_cookies()
    return page