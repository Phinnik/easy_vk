from .ApiMethod import ApiMethod


class Auth(ApiMethod):
    def __init__(self, access_token, v, session, calls_per_second):
        super(Auth, self).__init__(access_token, v, session, calls_per_second)
        self._base_method = 'auth.'

    def checkPhone(self, phone: str = None, client_id: str = None, client_secret: str = None,
                   auth_by_phone: str = None) -> dict:
        """
        Проверяет правильность введённого номера (возможность его использования для регистрации или авторизации).

        :param phone: номер телефона регистрируемого пользователя.
        :param client_id: идентификатор Вашего приложения.
        :param client_secret: секретный ключ приложения, доступный в разделе редактирования приложения.
        :param auth_by_phone: 1 — проверить правильность номера для авторизации, а не для регистрации нового
            аккаунта. По умолчанию: 0.

        :return: В случае, если номер пользователя является корректным, будет возвращён 1
        """

        params = locals()
        method_name = self._base_method + 'checkPhone'
        return self._call(method_name, params)

    def restore(self, phone: str = None, last_name: str = None) -> dict:
        """
        Позволяет восстановить доступ к аккаунту, используя код, полученный через SMS.  Данный метод доступен только
        приложениям, имеющим доступ к Прямой авторизации.

        :param phone: номер телефона пользователя.
        :param last_name: фамилия пользователя.

        :return: В случае успеха метод возвращает объект содержащий следующие поля:  success – 1;  sid – параметр
            необходимый для получения доступа по коду.  Для завершения восстановления доступа необходимо обратиться
            по адресу: https://oauth.vk.com/token?grant_type=restore_code&client_id={Идентификатор
            приложения}&client_secret={Секретный_ключ}&username={Номер телефона}&scope={Список прав
            доступа}&sid={Параметр, получаемый в данном методе}&code={Код полученный через SMS}  Список параметров:
            grant_type – необходимо передать значение: restore_code;  client_id – Идентификатор приложения;
            client_secret – Секретный ключ;  username – Номер телефона по которому был восстановлен пароль;  scope –
            список прав доступа, разделенных через запятую;  sid – идентификатор сессии, полученный в результате
            выполнения этого метода;  code – код, полученный через SMS.  В результате авторизации через restore_code
            OAuth вернет данные аналогичные обычной авторизации, с дополнительным параметром change_password_hash
            необходимым для метода account.changePassword
        """

        params = locals()
        method_name = self._base_method + 'restore'
        return self._call(method_name, params)
