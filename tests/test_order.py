import time
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.order_status_page import OrderStatusPage

@pytest.mark.parametrize("order_button_method", ["click_order_top", "click_order_bottom"])
@pytest.mark.parametrize("user_data", [
    {"name": "Иван", "surname": "Иванов", "address": "Улица Пушкина, дом Колотушкина", "metro": "Черкизовская", "phone": "+79991234567"},
    {"name": "Петр", "surname": "Петров", "address": "Проспект Мира, 10", "metro": "Китай-город", "phone": "+79997654321"},
])
def test_order_positive_first_page(driver, order_button_method, user_data):
    main_page = MainPage(driver)
    order_page = OrderPage(driver)
    status_page = OrderStatusPage(driver)

    # Открываем главную
    main_page.open()
    main_page.accept_cookies()

    # Нажимаем кнопку Заказать (сверху или снизу)
    getattr(main_page, order_button_method)()

    # Заполняем форму с личными данными
    order_page.fill_personal_data(
        user_data["name"], 
        user_data["surname"], 
        user_data["address"], 
        user_data["metro"], 
        user_data["phone"]
    )

    # Переходим далее
    order_page.click_next()

    # Дополнительные данные
    order_page.select_date("26")
    order_page.select_rent_period("сутки")
    order_page.select_black_color()
    order_page.fill_comment("Пожалуйста, позвоните перед приездом")

    # Кнопка Заказать
    order_page.click_order()

    # Подтверждение заказа
    status_page.confirm_order()

    # Нажать кнопку "Посмотреть статус"
    status_page.click_status()

    # Проверка перехода на главную по логотипу
    main_page.click_scooter_logo()
    time.sleep(2)
    assert driver.current_url == MainPage.URL

    # Проверка открытия Дзена через Яндекс лого
    main_page.click_yandex_logo()
    time.sleep(2)

    windows = driver.window_handles
    assert len(windows) > 1
    driver.switch_to.window(windows[-1])
    assert "dzen.ru" in driver.current_url

    driver.close()
    driver.switch_to.window(windows[0])
