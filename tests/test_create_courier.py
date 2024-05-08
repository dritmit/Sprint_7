import allure
from conftest import valid_courier_data
import data
import scooter_api


class TestCreateCourier:

    @allure.title("Проверка успешного создания курьера с валидными данными")
    @allure.description("Проверка статуса ответа и тела ответа")
    def test_create_courier_success(self, valid_courier_data):
        create_courier_response = scooter_api.ScooterApi.create_courier(valid_courier_data)
        assert create_courier_response.status_code == 201 and create_courier_response.json() == {"ok": True}


    @allure.title("Проверка ошибки создания курьера с существующими данными")
    @allure.description("Проверка статуса ответа и тела ответа")
    def test_create_courier_duplicate(self, valid_courier_data):
        scooter_api.ScooterApi.create_courier(valid_courier_data)
        create_courier_duplicate_response = scooter_api.ScooterApi.create_courier(valid_courier_data)
        assert create_courier_duplicate_response.status_code == 409 and \
               create_courier_duplicate_response.json()["message"] == 'Этот логин уже используется. Попробуйте другой.'


    @allure.title("Проверка ошибки создания курьера без указания логина")
    @allure.description("Проверка статуса ответа и тела ответа")
    def test_create_courier_without_login(self):
        body = data.Data.NEW_COURIER_BODY
        del body["login"]
        create_courier_response = scooter_api.ScooterApi.create_courier(body)
        assert create_courier_response.status_code == 400 and \
               create_courier_response.json()["message"] == 'Недостаточно данных для создания учетной записи'


    @allure.title("Проверка ошибки создания курьера без указания пароля")
    @allure.description("Проверка статуса ответа и тела ответа")
    def test_create_courier_without_password(self):
        body = data.Data.NEW_COURIER_BODY
        del body["password"]
        create_courier_response = scooter_api.ScooterApi.create_courier(body)
        assert create_courier_response.status_code == 400 and \
               create_courier_response.json()["message"] == 'Недостаточно данных для создания учетной записи'
