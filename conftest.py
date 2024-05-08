import allure
import pytest
import data
import scooter_api
import helpers


@allure.step("Региструем рандомного нового курьера с системе, запоминаем его id,"
             "возвращаем его логин и пароль. Удаляем курьера по id.")
@pytest.fixture(scope='function')
def new_courier_creds():
    payload = helpers.register_new_courier_and_return_login_password()
    response = scooter_api.ScooterApi.courier_login(payload)
    courier_id = response.json()['id']

    yield payload

    scooter_api.ScooterApi.delete_courier(str(courier_id))


@allure.step("Генерируем данные для создания нового курьера, возвращаем данные."
             "Запрашиваем id курьера в ручке логина в систему. Удаляем курьера по id.")
@pytest.fixture(scope='function')
def valid_courier_data():
    payload = helpers.generate_new_courier_data()

    yield payload

    login_response = scooter_api.ScooterApi.courier_login(payload)
    courier_id = login_response.json()['id']
    scooter_api.ScooterApi.delete_courier(str(courier_id))


@allure.step("Региструем рандомного нового курьера с системе, запоминаем его id."
             "Создаем новый рандомный заказ, запоминаем его track"
             "Возвращаем track заказа и id курьера"
             "Удалем курьера и отменяем заказ")
@pytest.fixture(scope='function')
def accept_order():
    courier_login_body = helpers.register_new_courier_and_return_login_password()
    courier_login_response = scooter_api.ScooterApi.courier_login(courier_login_body)
    courier_id = courier_login_response.json()['id']
    result = {"courier_id": courier_id}
    create_order_response = scooter_api.ScooterApi.create_order(data.Data.NEW_ORDER_BODY)
    result["order_id"] = create_order_response.json()["track"]
    print(result)

    yield result

    scooter_api.ScooterApi.delete_courier(str(courier_id))
    scooter_api.ScooterApi.cancel_order({"track": result["order_id"]})


@allure.step("Создаем новый рандомный заказ, возвращаем его track"
             "Отменяем заказ")
@pytest.fixture(scope='function')
def new_order_track():
    create_order_response = scooter_api.ScooterApi.create_order(data.Data.NEW_ORDER_BODY)
    track = create_order_response.json()["track"]

    yield track

    scooter_api.ScooterApi.cancel_order({"track": track})
