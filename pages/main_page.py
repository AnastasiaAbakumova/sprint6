from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    URL = "https://qa-scooter.praktikum-services.ru/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Локаторы
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    ORDER_BUTTON_TOP = (By.XPATH, "//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.CSS_SELECTOR, "button.Button_Button__ra12g.Button_Middle__1CSJM")
    SCOOTER_LOGO = (By.CSS_SELECTOR, 'img[alt="Scooter"]')
    YANDEX_LOGO = (By.CSS_SELECTOR, 'img[alt="Yandex"]')

    # Методы
    def open(self):
        self.driver.get(self.URL)

    def accept_cookies(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.COOKIE_BUTTON))
        btn.click()

    def click_order_top(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.ORDER_BUTTON_TOP))
        btn.click()

    def click_order_bottom(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.ORDER_BUTTON_BOTTOM))
        btn.click()

    def click_scooter_logo(self):
        logo = self.wait.until(EC.element_to_be_clickable(self.SCOOTER_LOGO))
        logo.click()

    def click_yandex_logo(self):
        logo = self.wait.until(EC.element_to_be_clickable(self.YANDEX_LOGO))
        logo.click()
