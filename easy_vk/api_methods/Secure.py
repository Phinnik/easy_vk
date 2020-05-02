from ApiMethod import ApiMethod


class Secure(ApiMethod):
    def __init__(self, access_token, v, session, calls_per_second):
        super(Secure, self).__init__(access_token, v, session, calls_per_second)
        self._base_method = 'secure.'

    def addAppEvent(self, user_id: str = None, activity_id: str = None, value: str = None) -> dict:
        """
        Добавляет информацию о достижениях пользователя в приложении.

        :param user_id: идентификатор пользователя, для которого нужно записать данные.
        :param activity_id: идентификатор достижения. Доступные значения:   1 — достигнут новый уровень, работает
            аналогично secure.setUserLevel;  2 — заработано новое число очков;  положительное число, отличное от 1 и
            2 — выполнена миссия с идентификатором activity_id.
        :param value: номер уровня или заработанное количество очков (соответственно, для activity_id=1 и
            activity_id=2).  Параметр игнорируется при значении activity_id, отличном от 1 и 2.  Если activity_id =
            1, то максимальное value 15000.  Если activity_id = 2, то максимальное value 10000000.

        :return
        """

        params = locals()
        method_name = self._base_method + 'addAppEvent'
        return self._call(method_name, params)

    def checkToken(self, token: str = None, ip: str = None) -> dict:
        """
        Позволяет проверять валидность пользователя в IFrame, VK Apps и Standalone-приложениях с помощью передаваемого
        в приложения параметра access_token.

        :param token: клиентский access_token
        :param ip: ip адрес пользователя. Обратите внимание, что пользователь может обращаться через ipv6, в этом
            случае обязательно передавать ipv6 адрес пользователя.  Если параметр не передан – ip адрес проверен не
            будет.

        :return: В случае успеха будет возвращен объект, содержащий следующие поля:   success = 1  user_id =
            идентификатор пользователя  date = unixtime дата, когда access_token был сгенерирован  expire = unixtime
            дата, когда access_token станет не валиде
        """

        params = locals()
        method_name = self._base_method + 'checkToken'
        return self._call(method_name, params)

    def getAppBalance(self) -> dict:
        """
        Возвращает платежный баланс (счет) приложения в сотых долях голоса.

        :return: Возвращает количество голосов (в сотых долях), которые есть на счете приложения.  Например, если
            метод возвращает 5000, это означает, что на балансе приложения 50 голосов
        """

        params = locals()
        method_name = self._base_method + 'getAppBalance'
        return self._call(method_name, params)

    def getSMSHistory(self, user_id: str = None, date_from: str = None, date_to: str = None, limit: str = None) -> dict:
        """
        Выводит список SMS-уведомлений, отосланных приложением с помощью метода secure.sendSMSNotification.

        :param user_id: фильтр по id пользователя, которому высылалось уведомление.
        :param date_from: фильтр по дате начала. Задается в виде UNIX-time.
        :param date_to: фильтр по дате окончания. Задается в виде UNIX-time.
        :param limit: количество возвращаемых записей. По умолчанию 1000.

        :return: Возвращает список SMS-уведомлений, отосланных приложением, отсортированных по убыванию даты и
            отфильтрованных с помощью параметров uid, date_from, date_to, limit
        """

        params = locals()
        method_name = self._base_method + 'getSMSHistory'
        return self._call(method_name, params)

    def getTransactionsHistory(self) -> dict:
        """
        Выводит историю транзакций по переводу голосов между пользователями и приложением.

        :return: Возвращает список транзакций, отсортированных по убыванию даты, и отфильтрованных с помощью
            параметров type, uid_from, uid_to, date_from, date_to, limit
        """

        params = locals()
        method_name = self._base_method + 'getTransactionsHistory'
        return self._call(method_name, params)

    def getUserLevel(self, user_ids: str = None) -> dict:
        """
        Возвращает ранее выставленный игровой уровень одного или нескольких пользователей в приложении.

        :param user_ids: идентификаторы пользователей, информацию об уровнях которых требуется получить.

        :return: Возвращает значения игровых уровней пользователей в приложении
        """

        params = locals()
        method_name = self._base_method + 'getUserLevel'
        return self._call(method_name, params)

    def giveEventSticker(self, user_ids: str = None, achievement_id: str = None) -> dict:
        """
        Выдает пользователю стикер и открывает игровое достижение.

        :param user_ids: список id пользователей которым нужно открыть достижение
        :param achievement_id: id игрового достижения на платформе игр

        :return: Возвращает список результатов выполнения в виде списка объектов:  {    "user_id": int,
              "status": string  }  status может принимать значения:  OK - операция успешна
            ERROR_ACHIEVEMENT_ALREADY_OPENED - стикер уже выдан пользователю  ERROR_UNKNOWN_ERROR - непредвиденная
            ошибк
        """

        params = locals()
        method_name = self._base_method + 'giveEventSticker'
        return self._call(method_name, params)

    def sendNotification(self, user_ids: str = None, user_id: str = None, message: str = None) -> dict:
        """
        Отправляет уведомление пользователю.

        :param user_ids: перечисленные через запятую идентификаторы пользователей, которым отправляется
            уведомление (максимум 100 штук).
        :param user_id: идентификатор пользователя.
        :param message: текст уведомления, который следует передавать в кодировке UTF-8 (максимум 254 символа).

        :return: Возвращает перечисленные через запятую ID пользователей, которым было успешно отправлено
            уведомление.  Обратите внимание, нельзя отправлять пользователю более 1 уведомления в час (3 в сутки).
            Кроме того, нельзя отправить одному пользователю два уведомления с одинаковым текстом подряд
        """

        params = locals()
        method_name = self._base_method + 'sendNotification'
        return self._call(method_name, params)

    def sendSMSNotification(self, user_id: str = None, message: str = None) -> dict:
        """
        Отправляет SMS-уведомление на мобильный телефон пользователя.

        :param user_id: id пользователя, которому отправляется SMS-уведомление. Пользователь должен разрешить
            приложению отсылать ему уведомления (getUserSettings, +1).
        :param message: текст SMS, который следует передавать в кодировке UTF-8. Допускаются только латинские
            буквы и цифры. Максимальный размер - 160 символов.

        :return: Возвращает 1 в случае успешной отсылки SMS.  Если номер пользователя еще не известен системе, то
            метод вернет ошибку 146 (The mobile number of the user is unknown). Для решения этой проблемы метод
            users.get возвращает поле has_mobile, которое позволяет определить, известен ли номер пользователя.  Если
            номер пользователя неизвестен, но Вы хотели бы иметь возможность высылать ему SMS-уведомления, необходимо
            предложить ему ввести номер мобильного телефона, не отвлекая от приложения
        """

        params = locals()
        method_name = self._base_method + 'sendSMSNotification'
        return self._call(method_name, params)

    def setCounter(self, counters: str = None, user_id: str = None, counter: str = None, increment: str = None) -> dict:
        """
        Устанавливает счетчик, который выводится пользователю жирным шрифтом в левом меню.

        :param counters: позволяет устанавливать счетчики нескольким пользователям за один запрос. Значение
            следует указывать в следующем формате: user_id1:counter1[:increment],user_id2:counter2[:increment],
            пример: 66748:6:1,6492:2. В случае, если указан этот параметр, параметры counter, user_id и increment не
            учитываются. Можно передать не более 200 значений за один запрос.
        :param user_id: идентификатор пользователя.
        :param counter: значение счетчика.
        :param increment: определяет, нужно ли заменить значение счетчика или прибавить новое значение к уже
            имеющемуся. 1 — прибавить counter к старому значению, 0 — заменить счетчик (по умолчанию).

        :return: Возвращает 1 в случае успешной установки счетчика.   Если пользователь не установил приложение в
            левое меню, метод вернет ошибку 148 (Access to the menu of the user denied). Избежать этой ошибки можно с
            помощью метода account.getAppPermissions.  Вы также можете обращаться к этому методу при стандартном
            взаимодействии с клиентской стороны, указывая setCounter вместо secure.setCounter в названии метода. В
            этом случае параметр uid передавать не нужно, счетчик установится для текущего пользователя.   Метод
            setCounter при стандартном, а не защищенном взаимодействии можно использовать для того, чтобы, например,
            сбрасывать счетчик при заходе пользователя в приложение
        """

        params = locals()
        method_name = self._base_method + 'setCounter'
        return self._call(method_name, params)

