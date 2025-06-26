import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OrderStatusPage(BasePage):
    CONFIRM_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and text()='Да']")
    STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.click(self.CONFIRM_BUTTON)

    @allure.step("Нажать кнопку 'Посмотреть статус'")
    def click_status(self):
        self.click(self.STATUS_BUTTON)
