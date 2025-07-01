import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class FAQPage(BasePage):
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    @allure.step("Принять cookie")
    def accept_cookies(self):
        self.click(self.COOKIE_BUTTON)

    @allure.step("Получить локатор заголовка ис индексом {index}")
    def question_heading_locator(self, index):
        return (By.ID, f"accordion__heading-{index}")
    
    @allure.step("Получить локатор панели с индексом {index}")
    def answer_panel_locator(self, index):
        return (By.ID, f"accordion__panel-{index}")

    @allure.step("Кликнуть на вопрос с индексом {index}")
    def click_question(self, index):
        self.click(self.question_heading_locator(index))

    @allure.step("Получить текст ответа на вопрос с индексом {index}")
    def get_answer_text(self, index):
        return self.get_text(self.answer_panel_locator(index))
