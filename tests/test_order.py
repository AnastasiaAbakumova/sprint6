import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.order_status_page import OrderStatusPage
from data.data_1 import user_order_data, order_buttons

@allure.feature("Заказ самоката")
class TestOrder:
    
    @pytest.mark.parametrize("order_button_method", order_buttons)
    @pytest.mark.parametrize("user_data", user_order_data)
    @allure.story("Позитивный сценарий оформления заказа - первый этап")
    def test_order_positive_first_page(self, driver, order_button_method, user_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        status_page = OrderStatusPage(driver)

        with allure.step("Открыть главную страницу и принять куки"):
            main_page.open_main()
            main_page.accept_cookies()

        with allure.step(f"Нажать кнопку Заказать ({order_button_method})"):
            getattr(main_page, order_button_method)()

        with allure.step("Заполнить личные данные"):
            order_page.fill_personal_data(
                user_data["name"],
                user_data["surname"],
                user_data["address"],
                user_data["metro"],
                user_data["phone"]
            )

        with allure.step("Перейти к следующему шагу"):
            order_page.click_next()

        with allure.step("Заполнить данные аренды"):
            order_page.select_date("26")
            order_page.select_rent_period("сутки")
            order_page.select_black_color()
            order_page.fill_comment("Пожалуйста, позвоните перед приездом")

        with allure.step("Оформить заказ"):
            order_page.click_order()

        with allure.step("Подтвердить заказ и проверить статус"):
            status_page.confirm_order()
            status_page.click_status()

        with allure.step("Проверить переход по логотипу самоката"):
            main_page.click_scooter_logo()
            main_page.wait_for_url_contains("qa-scooter")
            assert main_page.get_current_url() == MainPage.URL

        with allure.step("Проверить переход по логотипу Яндекса и закрыть вкладку"):
            main_page.click_yandex_logo()
            main_page.wait_for_new_window()
            handles = main_page.get_window_handles()
            main_page.switch_to_window(handles[-1])
            main_page.wait_for_url_contains("dzen.ru")
            assert "dzen.ru" in main_page.get_current_url()
            main_page.close_current_window()
            main_page.switch_to_window(handles[0])
