from ApiMethod import ApiMethod


class Utils(ApiMethod):
    def __init__(self, access_token, v, session, calls_per_second):
        super(Utils, self).__init__(access_token, v, session, calls_per_second)
        self._base_method = 'utils.'

    def checkLink(self, url: str = None) -> dict:
        """
        Возвращает информацию о том, является ли внешняя ссылка заблокированной на сайте ВКонтакте.

        :param url: внешняя ссылка, которую необходимо проверить.  Например, http://google.com

        :return: После успешного выполнения возвращает объект, который содержит следующие поля:    status
            (string) — статус ссылки. Возможные значения:   not_banned – ссылка не заблокирована;  banned – ссылка
            заблокирована;  processing – ссылка проверяется, необходимо выполнить повторный запрос через несколько
            секунд.   link (string) — исходная ссылка (url) либо полная ссылка (если в url была передана сокращенная
            ссылка)
        """

        params = locals()
        method_name = self._base_method + 'checkLink'
        return self._call(method_name, params)

    def deleteFromLastShortened(self, key: str = None) -> dict:
        """
        Удаляет сокращенную ссылку из списка пользователя.

        :param key: сокращенная ссылка (часть URL после "vk.cc/").

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'deleteFromLastShortened'
        return self._call(method_name, params)

    def getLastShortenedLinks(self, count: str = None, offset: str = None) -> dict:
        """
        Получает список сокращенных ссылок для текущего пользователя.

        :param count: количество ссылок, которые необходимо получить.
        :param offset: сдвиг для получения определенного подмножества ссылок.

        :return: Возвращает количество ссылок в поле count (integer) и массив объектов items, описывающих ссылки.
            Каждый из объектов содержит следующие поля:   timestamp (integer) — время создания ссылки в Unixtime;
            url (string) — URL ссылки до сокращения;  short_url (string) — сокращенный URL;  key (string) —
            содержательная часть (символы после "vk.cc");  views (integer) — число переходов;  access_key (string) —
            ключ доступа к приватной статистике
        """

        params = locals()
        method_name = self._base_method + 'getLastShortenedLinks'
        return self._call(method_name, params)

    def getLinkStats(self, key: str = None, source: str = None, access_key: str = None, interval: str = None,
                     intervals_count: str = None, extended: str = None) -> dict:
        """
        Возвращает статистику переходов по сокращенной ссылке.

        :param key: сокращенная ссылка (часть URL после "vk.cc/").
        :param source:
        :param access_key: ключ доступа к приватной статистике ссылки.
        :param interval: единица времени для подсчета статистики. Возможные значения:   hour — час;  day — день;
            week — неделя;  month — месяц;  forever — все время с момента создания ссылки.
        :param intervals_count: длительность периода для получения статистики в выбранных единицах (из параметра
            interval).
        :param extended: 1 — возвращать расширенную статистику (пол/возраст/страна/город), 0 — возвращать только
            количество переходов.

        :return: Возвращает объект, содержащий поле key с входным параметром key и массив stats с данными о
            статистике. Каждый объект в массиве stats содержит поле timestamp с указанием времени начала отсчета,
            общее число переходов views и массивы, описывающие половозрастную/геостатистику: sex_age, countries,
            cities.  Каждый объект в массиве sex_age содержит следующие поля:   age_range (string) — обозначение
            возраста;  female (integer) — число переходов пользователей женского пола;  male (integer) — число
            переходов пользователей мужского пола;   Каждый объект в массиве countries (cities) содержит следующие
            поля:   country_id (city_id) (integer) — идентификатор страны (города);  views (integer) — число
            переходов из этой страны (города)
        """

        params = locals()
        method_name = self._base_method + 'getLinkStats'
        return self._call(method_name, params)

    def getServerTime(self) -> dict:
        """
        Возвращает текущее время на сервере ВКонтакте в unixtime.

        :return: Возвращает число, соответствующее времени в unixtime
        """

        params = locals()
        method_name = self._base_method + 'getServerTime'
        return self._call(method_name, params)

    def getShortLink(self, url: str = None, private: str = None) -> dict:
        """
        Позволяет получить URL, сокращенный с помощью vk.cc.

        :param url: URL, для которого необходимо получить сокращенный вариант.
        :param private: 1 — статистика ссылки приватная. 0 — статистика ссылки общедоступная.

        :return: Возвращает объект, содержащий следующие поля:   short_url (string) — сокращённая ссылка.
            access_key (string) — ключ для доступа к приватной статистике ссылки;  key (string) — содержательная
            часть ссылки (после "vk.cc");  url (string) — оригинальный URL
        """

        params = locals()
        method_name = self._base_method + 'getShortLink'
        return self._call(method_name, params)

    def resolveScreenName(self, screen_name: str = None) -> dict:
        """
        Определяет тип объекта (пользователь, сообщество, приложение) и его идентификатор по короткому имени
        screen_name.

        :param screen_name: короткое имя пользователя, группы или приложения. Например, apiclub, andrew или
            rules_of_war.

        :return: После успешного выполнения возвращает объект, который содержит следующие поля:   type (string) —
            тип объекта. Возможные значения:   user — пользователь;  group — сообщество;  application — приложение.
            object_id (integer)— идентификатор объекта.   Если короткое имя screen_name не занято, то будет возвращён
            пустой объект
        """

        params = locals()
        method_name = self._base_method + 'resolveScreenName'
        return self._call(method_name, params)
