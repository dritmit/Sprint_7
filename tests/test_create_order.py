import allure
import pytest
import helpers
import scooter_api


class TestCreateOrder:

    @allure.title("Проверка создания возмоожности заказа со всевозможными комбинациями в выборе цвета самоката")
    @allure.description("Проверка статуса ответа и тела ответа")
    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"],
        ["GREY", "BLACK"],
        []
    ])
    def test_create_order_various_color(self, color):
        body = helpers.random_order_body_without_color()
        body["color"] = color
        create_order_response = scooter_api.ScooterApi.create_order(body)
        assert create_order_response.status_code == 201 and create_order_response.json()['track'] > 0
