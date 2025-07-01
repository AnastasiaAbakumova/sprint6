import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from data.data_1 import BASE_URL

class MainPage(BasePage):
    URL = BASE_URL

    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    ORDER_BUTTON_TOP = (By.XPATH, "//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.CSS_SELECTOR, "button.Button_Button__ra12g.Button_Middle__1CSJM")
    SCOOTER_LOGO = (By.CSS_SELECTOR, 'img[alt="Scooter"]')
    YANDEX_LOGO = (By.CSS_SELECTOR, 'img[alt="Yandex"]')

    @allure.step("Открыть главную страницу")
    def open_main(self):
        self.open(self.URL)

    @allure.step("Принять cookie")
    def accept_cookies(self):
        self.click(self.COOKIE_BUTTON)

    @allure.step("Нажать кнопку 'Заказать' сверху")
    def click_order_top(self):
        self.click(self.ORDER_BUTTON_TOP)

    @allure.step("Нажать кнопку 'Заказать' снизу")
    def click_order_bottom(self):
        self.click(self.ORDER_BUTTON_BOTTOM)

    @allure.step("Кликнуть на логотип самоката")
    def click_scooter_logo(self):
        self.click(self.SCOOTER_LOGO)

    @allure.step("Кликнуть на логотип Яндекса")
    def click_yandex_logo(self):
        self.click(self.YANDEX_LOGO)
        