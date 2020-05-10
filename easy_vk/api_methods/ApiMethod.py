from typing import List, Dict, Optional, Union
import time


class VKExceptions:
    class ErrorUnknown(Exception):
        def __str__(self):
            return 'Произошла неизвестная ошибка. Попробуйте повторить запрос позже'

    class AppOffline(Exception):
        def __str__(self):
            return 'Приложение выключено. \n' \
                   'Необходимо включить приложение в настройках https://vk.com/editapp?id={Ваш API_ID} \n' \
                   ' или использовать тестовый режим (test_mode=1)'

    class MethodUnknown(Exception):
        def __str__(self):
            return 'Передан неизвестный метод.\n' \
                   'Проверьте, правильно ли указано название вызываемого метода: https://vk.com/dev/methods.'

    class SignUnknown(Exception):
        def __str__(self):
            return 'Неверная подпись.'

    class AuthorisationError(Exception):
        def __str__(self):
            return 'Авторизация пользователя не удалась.\n' \
                   'Убедитесь, что Вы используете верную схему авторизации.'

    class TooManyRequests(Exception):
        def __str__(self):
            return 'Слишком много запросов в секунду.\n' \
                   'Задайте больший интервал между вызовами или используйте метод execute.\n' \
                   'Подробнее об ограничениях на частоту вызовов см. на странице https://vk.com/dev/api_requests.'

    class PermissionError(Exception):
        def __str__(self):
            return 'Нет прав для выполнения этого действия.\n' \
                   'Проверьте, получены ли нужные права доступа при авторизации.\n' \
                   'Это можно сделать с помощью метода account.getAppPermissions.'

    class RequestInvalid(Exception):
        def __str__(self):
            return 'Неверный запрос.\n' \
                   'Проверьте синтаксис запроса и список используемых параметров\n' \
                   '(его можно найти на странице с описанием метода)'

    class SameTypeActions(Exception):
        def __str__(self):
            return 'Слишком много однотипных действий.\n' \
                   'Нужно сократить число однотипных обращений.\n' \
                   'Для более эффективной работы Вы можете использовать execute.'

    class ServerError(Exception):
        def __str__(self):
            return 'Произошла внутренняя ошибка сервера.\n Попробуйте повторить запрос позже.'

    class CaptchaError(Exception):
        def __str__(self):
            return 'Требуется ввод кода с картинки (Captcha). \n' \
                   'Процесс обработки этой ошибки подробно описан на отдельной странице.\n' \
                   'https://vk.com/dev/captcha_error'

    class AccessDenied(Exception):
        def __str__(self):
            return 'Доступ запрещён.\n' \
                   'Убедитесь, что Вы используете верные идентификаторы,\n' \
                   'и доступ к контенту для текущего пользователя есть в полной версии сайта.'


class ApiMethod:
    def __init__(self, access_token, v, session, calls_per_second):
        self._session = session
        self._calls_per_second = calls_per_second
        self._required_params = {
            'v': v,
            'access_token': access_token
        }

    def _call(self, method_name: str, params: dict) -> Union[dict, int, list]:
        url = 'https://api.vk.com/method/{}'.format(method_name)
        params.update(self._required_params)
        params.pop('self')
        params = {p: params[p] for p in params if params[p]}
        time_start = time.time()
        r = self._session.post(url, params=params)
        delay = 1 / (self._calls_per_second - 0.2) - (time.time() - time_start)
        if delay > 0:
            time.sleep(delay)
        try:
            r = r.json()['response']
        except Exception as e:
            print(r.json())
            raise e
        return r

