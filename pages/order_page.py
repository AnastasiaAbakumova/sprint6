from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Локаторы
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.CLASS_NAME, "select-search__input")
    METRO_OPTION_TEMPLATE = "//div[contains(text(), '{}')]"
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.CSS_SELECTOR, "button.Button_Button__ra12g.Button_Middle__1CSJM")  # кнопка "Далее"

    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DATE_TO_SELECT_TEMPLATE = "//div[contains(@class,'react-datepicker__day') and text()='{}']"

    RENT_DROPDOWN = (By.CLASS_NAME, "Dropdown-placeholder")
    RENT_OPTION_TEMPLATE = "//div[@class='Dropdown-option' and text()='{}']"

    BLACK_CHECKBOX = (By.ID, "black")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and contains(text(),'Заказать')]")

    # Методы
    def fill_personal_data(self, name, surname, address, metro_text, phone):
        self.wait.until(EC.visibility_of_element_located(self.NAME_INPUT)).send_keys(name)
        self.driver.find_element(*self.SURNAME_INPUT).send_keys(surname)
        self.driver.find_element(*self.ADDRESS_INPUT).send_keys(address)

        metro = self.driver.find_element(*self.METRO_INPUT)
        metro.click()
        metro.send_keys(metro_text)

        metro_option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.METRO_OPTION_TEMPLATE.format(metro_text)))
        )
        metro_option.click()

        self.driver.find_element(*self.PHONE_INPUT).send_keys(phone)

    def click_next(self):
        next_btn = self.wait.until(EC.element_to_be_clickable(self.NEXT_BUTTON))
        next_btn.click()

    def select_date(self, day):
        self.wait.until(EC.element_to_be_clickable(self.DATE_INPUT)).click()
        date_elem = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.DATE_TO_SELECT_TEMPLATE.format(day)))
        )
        date_elem.click()

    def select_rent_period(self, period):
        rent_dropdown = self.wait.until(EC.element_to_be_clickable(self.RENT_DROPDOWN))
        rent_dropdown.click()
        rent_option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.RENT_OPTION_TEMPLATE.format(period)))
        )
        rent_option.click()

    def select_black_color(self):
        self.driver.find_element(*self.BLACK_CHECKBOX).click()

    def fill_comment(self, comment):
        self.driver.find_element(*self.COMMENT_INPUT).send_keys(comment)

    def click_order(self):
        order_btn = self.wait.until(EC.element_to_be_clickable(self.ORDER_BUTTON))
        order_btn.click()
