import time
from pprint import pprint
import sys

request_keys_default = ["url", "method", "data", "timeout", "headers"]
methods_default = ["GET", "POST", "PUT", "DELETE", "AUTH", "HEAD", "PATCH"]


def processing_error_auth(func):
    def excepted(request_data, time_sleep=0.5, check_request_keys=True, check_methods=True,
                 request_keys=request_keys_default, methods=methods_default):

        if len(request_data) == 0:
            print("Возникла ошибка")
            time.sleep(.2)
            raise KeyError('Подан пустой словарь')

        if check_request_keys:
            if len(request_data) < 5:
                print("Отсутсвуют элементы с ключем:")
                for i in request_keys:
                    if request_data.get(i, None):
                        pass
                    else:
                        print(i)
        else:
            print("Проверка ключа отключена")

        if check_methods:
            try:
                if request_data["method"] not in methods:
                    request_data_except = request_data["method"]
                    raise NonExistentMethod(error=request_data_except)
            except KeyError:
                pass
        else:
            print("Проверка метода отключена")

        result = func(request_data)

        return result

    return excepted


###########################################################################
request_from_user1 = {
    "url": "localhost/home/",
    "method": "GET",
    "data": {"попытка входа": 1},
    "timeout": 3000,
    "headers": {
        "Authorization": 'Bearer admin qwerty12345',
    },
}

request_from_user2 = {
    "url": "localhost/",
    "method": "POST",
    "data": {"попытка входа": 1},
    "timeout": 3000,
    "headers": {},
}

user_input_login_and_password = request_from_user1["headers"]["Authorization"]
correct_login_and_password = request_from_user1["headers"]["Authorization"]
incorrect_login_and_password = False


class AuthError(Exception):
    def __init__(self, exteption_text: str):
        self.exteption_text = exteption_text

    def return_error(self):
        return f'ATTENTION! AN ERROR HAS OCCURRED : {self.exteption_text}'


def check_user_request():
    try:
        if user_input_login_and_password == correct_login_and_password:
            pass
        else:
            raise AuthError(exteption_text="incorrect login")
        return 'Successfully!'
    except AuthError as error:
        error = error.return_error()
        print(error)


print(check_user_request())


################################################################################

class NonExistentMethod(Exception):

    def __init__(self, error, ):
        self.message = f"Метод '{error}' не существует"

        super().__init__(self.message)
