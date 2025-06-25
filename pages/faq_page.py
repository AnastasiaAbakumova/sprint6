from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FAQPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    # Метод для принятия cookie
    def accept_cookies(self):
        cookie_btn = self.wait.until(EC.element_to_be_clickable(self.COOKIE_BUTTON))
        cookie_btn.click()

    # Возвращает локатор заголовка вопроса по индексу
    def question_heading_locator(self, index):
        return (By.ID, f"accordion__heading-{index}")

    # Возвращает локатор панели с ответом по индексу
    def answer_panel_locator(self, index):
        return (By.ID, f"accordion__panel-{index}")

    # Нажать на вопрос по индексу
    def click_question(self, index):
        heading = self.wait.until(EC.element_to_be_clickable(self.question_heading_locator(index)))
        heading.click()

    # Получить текст ответа по индексу
    def get_answer_text(self, index):
        panel = self.wait.until(EC.visibility_of_element_located(self.answer_panel_locator(index)))
        return panel.text
