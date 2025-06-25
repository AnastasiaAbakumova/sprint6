import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Firefox()  # <-- поменял на Firefox
    yield driver
    driver.quit()

@pytest.fixture
def faq_page(driver):
    from pages.faq_page import FAQPage

    driver.get("https://qa-scooter.praktikum-services.ru/")
    page = FAQPage(driver)
    page.accept_cookies()
    return page