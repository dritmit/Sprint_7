import allure
import requests
import random
import string
import datetime
from faker import Faker


@allure.step("Регистрация нового рандомного курьера,"
             " если регистрация удалась возвращает словарь с логином и паролем,"
             "если регистрация не удалась возвращает пустой словарь")
def register_new_courier_and_return_login_password():

    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login_pass = {}

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    if response.status_code == 201:
        login_pass["login"] = login
        login_pass["password"] = password
        print(login_pass)

    return login_pass


@allure.step("Генерация данных для создания нового курьера")
def generate_new_courier_data():

    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    return payload


@allure.step("Генерация рандомных данных для создания заказа, без пераметра 'цвет самоката'")
def random_order_body_without_color():
    fake = Faker()

    return {
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "address": fake.address(),
        "metroStation": random.randint(1, 10),
        "phone": '79' + str(random.randint(100000000, 999999999)),
        "rentTime": random.randint(1, 7),
        "deliveryDate": datetime.datetime.now().strftime('%Y-%m-%d'),
        "comment": fake.text(max_nb_chars=20)
    }


@allure.step("Генерация рандомных данных для создания заказа")
def random_order_body():
    fake = Faker()
    color_list = [["BLACK"],
        ["GREY"],
        ["GREY", "BLACK"],
        []]

    return {
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "address": fake.address(),
        "metroStation": random.randint(1, 10),
        "phone": '79' + str(random.randint(100000000, 999999999)),
        "rentTime": random.randint(1, 7),
        "deliveryDate": datetime.datetime.now().strftime('%Y-%m-%d'),
        "comment": fake.text(max_nb_chars=20),
        "color": random.choice(color_list)
    }
