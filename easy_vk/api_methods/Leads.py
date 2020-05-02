from .ApiMethod import ApiMethod


class Leads(ApiMethod):
    def __init__(self, access_token, v, session, calls_per_second):
        super(Leads, self).__init__(access_token, v, session, calls_per_second)
        self._base_method = 'leads.'

    def checkUser(self, lead_id: str = None, test_result: str = None, test_mode: str = None, auto_start: str = None,
                  age: str = None, country: str = None) -> dict:
        """
        Проверяет, доступна ли рекламная акция пользователю.

        :param lead_id: Идентификатор рекламной акции
        :param test_result: При использовании тестового режима функция вернёт result, соответствующий значению
            этого параметра.
        :param test_mode: 1 -- включить тестовый режим;  0 -- включить боевой режим.
        :param auto_start: Автоматический старт акции при успешной проверке. Доступно по согласованию с
            администрацией.
        :param age: Возраст пользователя.
        :param country: Двухбуквенный код страны пользователя (ISO 3166-1 alpha-2, также известный как ISO2).

        :return: Возвращает объект, содержащий поля:   result — признак того, может ли пользователь начать акцию
            (true/false), а также, в случае auto_start=1, признак успешного старта акции,  reason — в случае
            result=false, описание причины, по которой пользователь не может начать акцию,  start_link — в случае
            result=true и auto_start=0, ссылка, по которой должен перейти пользователь для начала акции.  sid — в
            случае result=true и auto_start=1, идентификатор сессии начатой акции
        """

        params = locals()
        method_name = self._base_method + 'checkUser'
        return self._call(method_name, params)

    def complete(self, vk_sid: str = None, secret: str = None, comment: str = None) -> dict:
        """
        Завершает начатую пользователем рекламную акцию, используя сессию и секретный ключ.

        :param vk_sid: cессия, полученная GET параметром при старте акции.
        :param secret: секретный ключ, доступный в интерфейсе тестирования рекламной акции.
        :param comment: комментарий

        :return: При успешном завершении оффера будет возвращен объект, содержащий следующие поля:   limit —
            ограничение, установленное у текущего оффера;  spent — количество потраченных на акцию голосов;  cost —
            стоимость одной выполненной акции;  test_mode — режим транзакции (1 — тестовый, 0 — реальный);  success —
            результат выполнения транзакции (всегда равно 1)
        """

        params = locals()
        method_name = self._base_method + 'complete'
        return self._call(method_name, params)

    def getStats(self, lead_id: str = None, secret: str = None, date_start: str = None, date_end: str = None) -> dict:
        """
        Возвращает статистику по рекламной акции.

        :param lead_id: идентификатор рекламной акции, доступный в интерфейсе тестирования рекламных акций.
        :param secret: секретный ключ, доступный в интерфейсе тестирования рекламной акции.
        :param date_start: идентификатор дня, начиная с которого необходимо вернуть статистику в формате Y-m-d
            (8-и значное число). Например, 2011-09-17.
        :param date_end: идентификатор дня, до которого необходимо вернуть статистику в формате Y-m-d (8-и
            значное число). Например, 2011-09-19.

        :return: При успешном завершении оффера будет возвращен объект, содержащий следующие поля:   limit —
            ограничения в голосах на текущую рекламную акцию;  spent — количество голосов, уже потраченных на
            рекламную акцию;  cost — стоимость (в голосах) одного прохождения;  impressions — количество показов
            акций;  started — количество начатых акций;  completed — количество пройденных акций;  days — данное поле
            возвращается, только если переданы входные параметры date_start и date_end.    Параметр days Объект days
            содержит следующие поля:   impressions — показы;  started — начатые акции;  completed — законченные
            акции;  spent — потрачено голосов
        """

        params = locals()
        method_name = self._base_method + 'getStats'
        return self._call(method_name, params)

    def getUsers(self, offer_id: str = None, secret: str = None, offset: str = None, count: str = None,
                 status: str = None, reverse: str = None) -> dict:
        """
        Возвращает список последних действий пользователей по рекламной акции.

        :param offer_id: идентификатор рекламной акции.
        :param secret: секретный ключ, доступный в интерфейсе редактирования рекламной акции.
        :param offset: смещение необходимое для выборки определенного подмножества действий.
        :param count: количество действий, которые необходимо вернуть.
        :param status: тип действия:   0 — начало действия;  1 — завершения действия;  2 — действия по
            блокированию пользователей;  4 — начало действия в тестовом режиме;  5 — завершения действия в тестовом
            режиме.  Если параметр не задан, возвращаются все действия.
        :param reverse:   0 — сортировка в обратном хронологическом порядке;  1 — сортировка в прямом
            хронологическом порядке.  Если параметр не задан, то значение по умолчанию 0

        :return: После успешного выполнения возвращает массив объектов entry, каждый из которых содержит поля:
            uid — идентификатор пользователя;  aid — идентификатор приложения, из которого было выполнено действие;
            sid — идентификатор сессии;  date — время действия в формате unixtime;  start_date — время начала
            действия в формате unixtime для status = 1;  status — 0 - начало действия, 1 - завершение действия, 2 -
            блокирование пользователя;  test_mode — 0 - рабочий режим, 1 - тестовый режим;  comment — текст
            комментария
        """

        params = locals()
        method_name = self._base_method + 'getUsers'
        return self._call(method_name, params)

    def metricHit(self, data: str = None) -> dict:
        """
        Засчитывает событие метрики.

        :param data: Данные метрики, полученные в личном кабинете рекламной акции.

        :return: Возвращает объект, содержащий поля:   result - равен true в случае успеха, и false в обратном
            случае,  redirect_link - возвращается в случае, когда пользователя нужно перенаправить по указанной
            ссылке
        """

        params = locals()
        method_name = self._base_method + 'metricHit'
        return self._call(method_name, params)

    def start(self, lead_id: str = None, secret: str = None, uid: str = None, aid: str = None, test_mode: str = None,
              force: str = None) -> dict:
        """
        Создаёт новую сессию для прохождения рекламной акции для пользователя.

        :param lead_id: идентификатор рекламной акции, доступный в интерфейсе тестирования рекламных акций.
        :param secret: секретный ключ, доступный в интерфейсе редактирования рекламных акций.
        :param uid: идентификатор пользователя, для которого необходимо получить сессию рекламной акции.
        :param aid: идентификатор приложения, на счет которого будут зачислены голоса. Если 0, при завершении
            рекламной акции голоса будут зачислены на счет пользователя.
        :param test_mode: 1 - запустить рекламную акцию в тестовом режиме;  0 - запустить рекламную акцию в
            боевом режиме (рекламная акция должна быть одобрена).
        :param force: 1 - запустить рекламную акцию без проверок пользователя на фрод. Рекомендуется использовать
            только при выполнении оффлайн-офферов.

        :return: При успешном старте рекламной акции будет возвращен объект содержащий следующие поля:
            test_mode — режим транзакции (1 — тестовый, 0 — реальный);  vk_sid — сессия рекламной акции
        """

        params = locals()
        method_name = self._base_method + 'start'
        return self._call(method_name, params)

