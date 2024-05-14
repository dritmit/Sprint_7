import allure
import pytest
import scooter_api
import helpers


@allure.step("Региструем рандомного нового курьера с системе, запоминаем его id,"
             "возвращаем его логин и пароль. Удаляем курьера по id.")
@pytest.fixture(scope='function')
def new_courier_creds():
    courier_data = helpers.generate_new_courier_data()
    payload = helpers.register_new_courier_and_return_login_password(courier_data)
    response = scooter_api.ScooterApi.courier_login(payload)
    courier_id = response.json()['id']
    yield payload
    scooter_api.ScooterApi.delete_courier(str(courier_id))


@allure.step("Генерируем данные для создания нового курьера, возвращаем данные.")
@pytest.fixture(scope='function')
def valid_courier_data():
    payload = helpers.generate_new_courier_data()
    yield payload


@allure.step("Региструем рандомного нового курьера с системе, вызываем ручку логина в системе, возвращаем его id."
             " Удаляем курьера.")
@pytest.fixture(scope='function')
def new_courier_id():
    courier_data = helpers.generate_new_courier_data()
    courier_login_body = helpers.register_new_courier_and_return_login_password(courier_data)
    courier_login_response = scooter_api.ScooterApi.courier_login(courier_login_body)
    courier_id = courier_login_response.json()['id']
    yield courier_id
    scooter_api.ScooterApi.delete_courier(str(courier_id))


@allure.step("Создаем новый рандомный заказ, получаем информацию по заказу, возвращаем его id. Отменяем заказ")
@pytest.fixture(scope='function')
def new_order_id():
    create_order_response = scooter_api.ScooterApi.create_order(helpers.random_order_body())
    track = create_order_response.json()["track"]
    get_order_response = scooter_api.ScooterApi.get_order(track)
    order_id = get_order_response.json()["order"]["id"]
    yield order_id
    scooter_api.ScooterApi.cancel_order({"track": track})


@allure.step("Создаем новый рандомный заказ, возвращаем его track. Отменяем заказ")
@pytest.fixture(scope='function')
def new_order_track():
    create_order_response = scooter_api.ScooterApi.create_order(helpers.random_order_body())
    track = create_order_response.json()["track"]
    yield track
    scooter_api.ScooterApi.cancel_order({"track": track})
