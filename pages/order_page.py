import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OrderPage(BasePage):
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.CLASS_NAME, "select-search__input")
    METRO_OPTION_TEMPLATE = "//div[contains(text(), '{}')]"
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.CSS_SELECTOR, "button.Button_Button__ra12g.Button_Middle__1CSJM")
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DATE_TO_SELECT_TEMPLATE = "//div[contains(@class,'react-datepicker__day') and text()='{}']"
    RENT_DROPDOWN = (By.CLASS_NAME, "Dropdown-placeholder")
    RENT_OPTION_TEMPLATE = "//div[@class='Dropdown-option' and text()='{}']"
    BLACK_CHECKBOX = (By.ID, "black")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and contains(text(),'Заказать')]")

    @allure.step("Заполнить персональные данные: имя={name}, фамилия={surname}, адрес={address}, метро={metro_text}, телефон={phone}")
    def fill_personal_data(self, name, surname, address, metro_text, phone):
        self.send_keys(self.NAME_INPUT, name)
        self.send_keys(self.SURNAME_INPUT, surname)
        self.send_keys(self.ADDRESS_INPUT, address)
        self.click(self.METRO_INPUT)
        self.send_keys(self.METRO_INPUT, metro_text)
        self.click((By.XPATH, self.METRO_OPTION_TEMPLATE.format(metro_text)))
        self.send_keys(self.PHONE_INPUT, phone)

    @allure.step("Нажать кнопку 'Далее'")
    def click_next(self):
        self.click(self.NEXT_BUTTON)

    @allure.step("Выбрать дату доставки: {day}")
    def select_date(self, day):
        self.click(self.DATE_INPUT)
        self.click((By.XPATH, self.DATE_TO_SELECT_TEMPLATE.format(day)))

    @allure.step("Выбрать срок аренды: {period}")
    def select_rent_period(self, period):
        self.click(self.RENT_DROPDOWN)
        self.click((By.XPATH, self.RENT_OPTION_TEMPLATE.format(period)))

    @allure.step("Выбрать цвет самоката: черный")
    def select_black_color(self):
        self.click(self.BLACK_CHECKBOX)

    @allure.step("Заполнить комментарий для курьера: {comment}")
    def fill_comment(self, comment):
        self.send_keys(self.COMMENT_INPUT, comment)

    @allure.step("Нажать кнопку 'Заказать'")
    def click_order(self):
        self.click(self.ORDER_BUTTON)
