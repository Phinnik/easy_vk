from ApiMethod import ApiMethod


class Storage(ApiMethod):
    def __init__(self, access_token, v, session, calls_per_second):
        super(Storage, self).__init__(access_token, v, session, calls_per_second)
        self._base_method = 'storage.'

    def get(self, key: str = None, keys: str = None, user_id: str = None) -> dict:
        """
        Возвращает значение переменной, название которой передано в параметре key.

        :param key: название переменной.
        :param keys: список названий переменных, разделённых запятыми. Если указан этот параметр, то параметр key
            не учитывается.
        :param user_id: id пользователя, переменная которого устанавливается, в случае если данные запрашиваются
            серверным методом.

        :return: Возвращает значение одной или нескольких переменных. Если переменная на сервере отсутствует, то
            будет возвращена пустая строка
        """

        params = locals()
        method_name = self._base_method + 'get'
        return self._call(method_name, params)

    def getKeys(self, user_id: str = None, offset: str = None, count: str = None) -> dict:
        """
        Возвращает названия всех переменных.

        :param user_id: id пользователя, названия переменных которого получаются, в случае если данные
            запрашиваются серверным методом.
        :param offset: смещение, необходимое для выборки определенного подмножества названий переменных. По
            умолчанию 0.
        :param count: количество названий переменных, информацию о которых необходимо получить.

        :return: Возвращает массив названий переменных
        """

        params = locals()
        method_name = self._base_method + 'getKeys'
        return self._call(method_name, params)

    def set(self, key: str = None, value: str = None, user_id: str = None) -> dict:
        """
        Сохраняет значение переменной, название которой передано в параметре key.

        :param key: название переменной. Может содержать символы латинского алфавита, цифры, знак тире, нижнее
            подчёркивание [a-zA-Z_\-0-9].
        :param value: значение переменной, сохраняются только первые 4096 байта.
        :param user_id: id пользователя, переменная которого устанавливается, в случае если данные запрашиваются
            серверным методом.

        :return: Возвращает 1 в случае удачного сохранения переменной.  Для удаления переменной необходимо
            передать пустое значение в параметре value
        """

        params = locals()
        method_name = self._base_method + 'set'
        return self._call(method_name, params)
