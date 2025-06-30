import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Клик по элементу с локатором: {locator}")
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("Ввод текста '{text}' в элемент с локатором: {locator}")
    def send_keys(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    @allure.step("Получение текста из элемента с локатором: {locator}")
    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    @allure.step("Открытие страницы по URL: {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Поиск элемента с локатором: {locator}")
    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def is_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def get_current_url(self):
        return self.driver.current_url

    def get_window_handles(self):
        return self.driver.window_handles

    def switch_to_window(self, handle):
        self.driver.switch_to.window(handle)

    def close_current_window(self):
        self.driver.close()

    def wait_for_url_contains(self, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(text))

    def wait_for_new_window(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(lambda d: len(d.window_handles) > 1)

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url    
    
    @allure.step("Получить список всех открытых вкладок")
    def get_window_handles(self):
        return self.driver.window_handles
    
    @allure.step("Переключиться на вкладку {handle}")
    def switch_to_window(self, handle):
        self.driver.switch_to.window(handle)

    @allure.step("Закрыть текущую вкладку браузера")
    def close_current_window(self):
        self.driver.close()

