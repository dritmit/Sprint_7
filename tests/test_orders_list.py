import allure
import scooter_api


class TestOrdersList:

    @allure.title("Проверка успешного получения списка заказов")
    @allure.description("Проверка статуса ответа и тела ответа")
    def test_orders_list_success(self):
        orders_list_response = scooter_api.ScooterApi.orders_list()
        assert orders_list_response.status_code == 200 and len(orders_list_response.json()["orders"]) > 0
