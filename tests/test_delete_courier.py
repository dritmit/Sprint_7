import allure
import helpers
import scooter_api


class TestDeleteCourier:

    @allure.title("Проверка успешного удаления курьера")
    @allure.description("Проверка статуса ответа и тела ответа")
    def test_delete_courier_success(self):
        courier_data = helpers.generate_new_courier_data()
        courier_login_body = helpers.register_new_courier_and_return_login_password(courier_data)
        courier_login_response = scooter_api.ScooterApi.courier_login(courier_login_body)
        courier_id = courier_login_response.json()['id']
        courier_delete_response = scooter_api.ScooterApi.delete_courier(str(courier_id))
        assert courier_delete_response.status_code == 200 and courier_delete_response.json() == {"ok": True}


    @allure.title("Проверка ошибки при попытке удаления курьера без указания id курьера")
    @allure.description("Проверка статуса ответа и тела ответа")
    def test_delete_courier_without_id(self):
        courier_delete_response = scooter_api.ScooterApi.delete_courier('')
        assert courier_delete_response.status_code == 404 and \
               courier_delete_response.json()["message"] == 'Not Found.'


    @allure.title("Проверка ошибки при попытке удаления курьера c указанием несуществующего id курьера")
    @allure.description("Проверка статуса ответа и тела ответа")
    def test_delete_courier_wrong_id(self):
        courier_delete_response = scooter_api.ScooterApi.delete_courier('0')
        assert courier_delete_response.status_code == 404 and \
               courier_delete_response.json()["message"] == 'Курьера с таким id нет.'
