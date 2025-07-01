import pytest
import allure
from data.data_1 import questions_data

@allure.feature("FAQ")
class TestFAQ:

    @pytest.mark.parametrize("index, expected_text", questions_data)
    @allure.story("Проверка вопросов и ответов в FAQ")
    def test_faq_questions(self, faq_page, index, expected_text):
        with allure.step(f"Нажать на вопрос с индексом {index}"):
            faq_page.click_question(index)
        with allure.step("Получить текст ответа"):
            answer = faq_page.get_answer_text(index)
        with allure.step("Проверить, что ответ содержит ожидаемый текст"):
            assert expected_text in answer