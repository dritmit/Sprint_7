import allure
import requests
import urls


class ScooterApi:
    @staticmethod
    @allure.step("Запрос на создание курьера")
    def create_courier(body):
        return requests.post(urls.BASE_URL + urls.CREATE_COURIER_ENDPOINT,
                             json=body)


    @staticmethod
    @allure.step("Запрос на удаление курьера")
    def delete_courier(courier_id):
        return requests.delete(urls.BASE_URL+urls.CREATE_COURIER_ENDPOINT+'/'+courier_id)


    @staticmethod
    @allure.step("Запрос логина курьера в системе")
    def courier_login(body):
        return requests.post(urls.BASE_URL+urls.COURIER_LOGIN_ENDPOINT, json=body)


    @staticmethod
    @allure.step("Запрос создания заказа")
    def create_order(body):
        return requests.post(urls.BASE_URL+urls.ORDERS_ENDPOINT, json=body)


    @staticmethod
    @allure.step("Запрос получения списка заказов")
    def orders_list():
        return requests.get(urls.BASE_URL+urls.ORDERS_ENDPOINT)


    @staticmethod
    @allure.step("Запрос подтверждения заказа")
    def accept_order(order, courier_id):
        return requests.put(urls.BASE_URL + urls.ACCEPT_ORDER_ENDPOINT
                            + '/' + str(order) + '?courierId=' + str(courier_id))


    @staticmethod
    @allure.step("Запрос отмены заказа")
    def cancel_order(body):
        return requests.put(urls.BASE_URL + urls.CANCEL_ORDER_ENDPOINT, json=body)

    @staticmethod
    @allure.step("Запрос получения информации по заказу")
    def get_order(track):
        return requests.get(urls.BASE_URL + urls.GET_ORDER_ENDPOINT + '?t=' + str(track))