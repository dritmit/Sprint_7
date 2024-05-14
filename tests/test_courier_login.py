import allure
from conftest import new_courier_creds
import scooter_api


class TestCourierLogin:

    @allure.title("Проверка успешного логина в системе курьера в системе")
    @allure.description("Проверка статуса ответа и тела ответа")
    def test_courier_login_success(self, new_courier_creds):
        courier_login_response = scooter_api.ScooterApi.courier_login(new_courier_creds)
        assert courier_login_response.status_code == 200 and courier_login_response.json()['id'] > 0


    @allure.title("Проверка ошибки логина в системе курьера без указания логина курьера")
    @allure.description("Проверка статуса ответа и тела ответа")
    def test_courier_login_body_without_login(self, new_courier_creds):
        del new_courier_creds["login"]
        courier_login_response = scooter_api.ScooterApi.courier_login(new_courier_creds)
        assert courier_login_response.status_code == 400 and\
               courier_login_response.json()["message"] == "Недостаточно данных для входа"


    @allure.title("Проверка ошибки логина в системе курьера без указания пароля курьера")
    @allure.description("Проверка статуса ответа и тела ответа")
    def test_courier_login_body_without_password(self, new_courier_creds):
        del new_courier_creds["password"]
        courier_login_response = scooter_api.ScooterApi.courier_login(new_courier_creds)
        assert courier_login_response.status_code == 504


    @allure.title("Проверка ошибки логина в системе курьера с указанием несуществующего логина курьера")
    @allure.description("Проверка статуса ответа и тела ответа")
    def test_courier_login_wrong_login(self, new_courier_creds):
        new_courier_creds["login"] = "0"
        courier_login_response = scooter_api.ScooterApi.courier_login(new_courier_creds)
        assert courier_login_response.status_code == 404 and \
               courier_login_response.json()["message"] == "Учетная запись не найдена"


    @allure.title("Проверка ошибки логина в системе курьера с указанием несуществующего пароля курьера")
    @allure.description("Проверка статуса ответа и тела ответа")
    def test_courier_login_wrong_password(self, new_courier_creds):
        new_courier_creds["password"] = '0'
        courier_login_response = scooter_api.ScooterApi.courier_login(new_courier_creds)
        assert courier_login_response.status_code == 404 and \
               courier_login_response.json()["message"] == "Учетная запись не найдена"
