import allure
import scooter_api
from conftest import new_order_id
from conftest import new_courier_id


class TestAcceptOrder:

    @allure.title("Проверка успешности приема заказа")
    @allure.description("Проверка статуса ответа и тела ответа")
    def test_accept_order_success(self, new_order_id, new_courier_id):
        accept_order_response = scooter_api.ScooterApi.accept_order(new_order_id, new_courier_id)
        assert accept_order_response.status_code == 200 and\
               accept_order_response.json() == {"ok": True}


    @allure.title("Проверка ошибки при приема заказа без указания id курьера")
    @allure.description("Проверка статуса ответа и тела ответа")
    def test_accept_order_without_courier_id(self, new_order_id):
        accept_order_response = scooter_api.ScooterApi.accept_order(new_order_id, '')
        assert accept_order_response.status_code == 400 and\
               accept_order_response.json()["message"] == 'Недостаточно данных для поиска'


    @allure.title("Проверка ошибки при приема заказа c указанием несуществующего id курьера")
    @allure.description("Проверка статуса ответа и тела ответа")
    def test_accept_order_wrong_courier_id(self, new_order_id):
        accept_order_response = scooter_api.ScooterApi.accept_order(new_order_id, '0')
        assert accept_order_response.status_code == 404 and\
               accept_order_response.json()["message"] == 'Курьера с таким id не существует'


    @allure.title("Проверка ошибки при приема заказа без указания id заказа")
    @allure.description("Проверка статуса ответа и тела ответа")
    def test_accept_order_without_order_id(self, new_courier_id):
        accept_order_response = scooter_api.ScooterApi.accept_order('', new_courier_id)
        assert accept_order_response.status_code == 404 and\
               accept_order_response.json()["message"] == 'Not Found.'


    @allure.title("Проверка ошибки при приема заказа c указанием несуществующего id заказа")
    @allure.description("Проверка статуса ответа и тела ответа")
    def test_accept_order_wrong_order_id(self, new_courier_id):
        accept_order_response = scooter_api.ScooterApi.accept_order('0', new_courier_id)
        assert accept_order_response.status_code == 404 and\
               accept_order_response.json()["message"] == 'Заказа с таким id не существует'
