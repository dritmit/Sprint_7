import allure
import pytest
import data
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
        body = data.Data.NEW_ORDER_BODY_WITHOUT_COLOR
        body["color"] = color
        create_order_response = scooter_api.ScooterApi.create_order(body)
        assert create_order_response.status_code == 201 and create_order_response.json()['track'] > 0
