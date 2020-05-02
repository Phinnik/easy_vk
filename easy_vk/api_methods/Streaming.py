from .ApiMethod import ApiMethod


class Streaming(ApiMethod):
    def __init__(self, access_token, v, session, calls_per_second):
        super(Streaming, self).__init__(access_token, v, session, calls_per_second)
        self._base_method = 'streaming.'

    def getServerUrl(self) -> dict:
        """
        Позволяет получить данные для подключения к Streaming API.

        :return: Возвращает объект, который содержит следующие поля:   endpoint (string) — хост для подключения к
            серверу;  key (string) — ключ доступа. Ключ бессрочный и прекращает действовать только после получения
            нового ключа
        """

        params = locals()
        method_name = self._base_method + 'getServerUrl'
        return self._call(method_name, params)

    def getSettings(self) -> dict:
        """
        Позволяет получить значение порога для Streaming API.

        :return: Возвращает объект с единственным полем monthly_limit (string), которое содержит значение
            tier_1-tier_6 или unlimited и соответствует установленному порогу для приложения
        """

        params = locals()
        method_name = self._base_method + 'getSettings'
        return self._call(method_name, params)

    def getStats(self, type: str = None, interval: str = None, start_time: str = None, end_time: str = None) -> dict:
        """
        Позволяет получить статистику для подготовленных и доставленных событий Streaming API.

        :param type: тип статистики. Возможные значения:   received — события, полученные приложением;  prepared
            — события, сгенерированные со стороны ВКонтакте.
        :param interval: интервалы статистики. Возможные значения:   5m — пять минут. Максимальный период — 3 дня
            между start_time и end_time;  1h — один час. Максимальный период — 7 дней между start_time и end_time;
            24h — сутки. Максимальный период — 31 день между start_time и end_time.
        :param start_time: время начала отсчёта в Unixtime. По умолчанию: end_time минус сутки.
        :param end_time: время окончания отсчёта в Unixtime. По умолчанию: текущее время.

        :return: Возвращает массив объектов, каждый из которых содержит поля:   event_type (string) — тип
            событий. Возможные значения:   post — записи на стене;  comment — комментарии;  share — репосты.   stats
            (array) — значения статистики. Массив объектов, каждый из которых содержит оля:   timestamp (integer) —
            время, соответствующее значению;  value (integer) — значение
        """

        params = locals()
        method_name = self._base_method + 'getStats'
        return self._call(method_name, params)

    def getStem(self, word: str = None) -> dict:
        """
        Позволяет получить основу слова.

        :param word: слово, основу которого мы собираемся получить

        :return
        """

        params = locals()
        method_name = self._base_method + 'getStem'
        return self._call(method_name, params)

    def setSettings(self, monthly_tier: str = None) -> dict:
        """
        Позволяет задать значение порога для Streaming API.

        :param monthly_tier: значение порога в месяц. Возможные значения:   tier_1;  tier_2;  tier_3;  tier_4;
            tier_5;  tier_6;  unlimited.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'setSettings'
        return self._call(method_name, params)

