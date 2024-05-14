import allure
import scooter_api
from conftest import new_order_track


class TestGetOrder:

    @allure.title("Проверка успешного получения данных заказа по номеру")
    @allure.description("Проверка статуса ответа и номера заказа в тела ответа")
    def test_get_order_success(self, new_order_track):
        get_order_response = scooter_api.ScooterApi.get_order(new_order_track)
        assert get_order_response.status_code == 200 and\
               get_order_response.json()["order"]["track"] == new_order_track


    @allure.title("Проверка ошибки при попытке получения данных заказа без указания номера заказа")
    @allure.description("Проверка статуса ответа и тела ответа")
    def test_get_order_without_number(self):
        get_order_response = scooter_api.ScooterApi.get_order('')
        assert get_order_response.status_code == 400 and\
               get_order_response.json()["message"] == 'Недостаточно данных для поиска'


    @allure.title("Проверка ошибки при попытке получения данных заказа с указанием несуществующего номера заказа")
    @allure.description("Проверка статуса ответа и тела ответа")
    def test_get_order_wrong_number(self):
        get_order_response = scooter_api.ScooterApi.get_order('0')
        assert get_order_response.status_code == 404 and \
               get_order_response.json()["message"] == 'Заказ не найден'
