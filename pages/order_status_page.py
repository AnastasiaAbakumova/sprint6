from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderStatusPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    CONFIRM_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and text()='Да']")
    STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")

    def confirm_order(self):
        confirm_btn = self.wait.until(EC.element_to_be_clickable(self.CONFIRM_BUTTON))
        confirm_btn.click()

    def click_status(self):
        status_btn = self.wait.until(EC.element_to_be_clickable(self.STATUS_BUTTON))
        status_btn.click()
