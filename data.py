import helpers


class Data:
    NEW_COURIER_BODY = helpers.generate_new_courier_data()
    COURIER_LOGIN_REQUEST_BODY = helpers.register_new_courier_and_return_login_password()
    NEW_ORDER_BODY_WITHOUT_COLOR = helpers.random_order_body_without_color()
    NEW_ORDER_BODY = helpers.random_order_body()
