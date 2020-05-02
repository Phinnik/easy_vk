from ApiMethod import ApiMethod


class Stats(ApiMethod):
    def __init__(self, access_token, v, session, calls_per_second):
        super(Stats, self).__init__(access_token, v, session, calls_per_second)
        self._base_method = 'stats.'

    def get(self, group_id: str = None, app_id: str = None, timestamp_from: str = None, timestamp_to: str = None,
            interval: str = None, intervals_count: str = None, filters: str = None, stats_groups: str = None,
            extended: str = None) -> dict:
        """
        Возвращает статистику сообщества или приложения.

        :param group_id: идентификатор сообщества.
        :param app_id: идентификатор приложения.
        :param timestamp_from: начало периода статистики в Unixtime.
        :param timestamp_to: окончание периода статистики в Unixtime.
        :param interval: временные интервалы. Возможные значения: day, week, month, year, all. По умолчанию: day.
        :param intervals_count: количество интервалов времени.
        :param filters:
        :param stats_groups: фильтр для получения данных по конкретному блоку статистики сообщества. Возможные
            значения: visitors, reach, activity.
        :param extended: 1 — возвращать дополнительно агрегированные данные в результатах.

        :return: После успешного выполнения возвращает объект с данными статистики
        """

        params = locals()
        method_name = self._base_method + 'get'
        return self._call(method_name, params)

    def getPostReach(self, owner_id: str = None, post_ids: str = None) -> dict:
        """
        Возвращает статистику для записи на стене.

        :param owner_id: идентификатор сообщества — владельца записи. Указывается со знаком «минус».
        :param post_ids:

        :return: После успешного выполнения возвращает данные о статистике записи в виде объекта, который
            содержит следующие поля:  reach_subscribers  integerохват подписчиков. reach_total  integerсуммарный
            охват. reach_ads  integerрекламный охват (если запись продвигалась с помощью таргетированной рекламы).
            reach_viral  integerвиральный охват (если запись продвигалась с помощью таргетированной рекламы).. links
            integerпереходы по ссылке. to_group  integerпереходы в сообщество. join_group  integerвступления в
            сообщество. report  integerколичество жалоб на запись. hide  integerколичество скрывших запись.
            unsubscribe  integerколичество отписавшихся участников
        """

        params = locals()
        method_name = self._base_method + 'getPostReach'
        return self._call(method_name, params)

    def trackVisitor(self) -> dict:
        """
        Добавляет данные о текущем сеансе в статистику посещаемости приложения.

        :return: В случае успешной обработки данных метод вернет 1
        """

        params = locals()
        method_name = self._base_method + 'trackVisitor'
        return self._call(method_name, params)
