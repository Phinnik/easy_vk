from .ApiMethod import ApiMethod


class Pages(ApiMethod):
    def __init__(self, access_token, v, session, calls_per_second):
        super(Pages, self).__init__(access_token, v, session, calls_per_second)
        self._base_method = 'pages.'

    def clearCache(self, url: str = None) -> dict:
        """
        Позволяет очистить кеш отдельных внешних страниц, которые могут быть прикреплены к записям ВКонтакте. После
        очистки кеша при последующем прикреплении ссылки к записи, данные о странице будут обновлены.

        :param url: Адрес страницы, закешированную версию которой необходимо очистить

        :return: При удачной очистке кеша – метод возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'clearCache'
        return self._call(method_name, params)

    def get(self, owner_id: str = None, page_id: str = None, site_preview: str = None,
            title: str = None, need_source: str = None, need_html: str = None) -> dict:
        # global: str = None,
        """
        Возвращает информацию о вики-странице.

        :param owner_id: идентификатор владельца вики-страницы.
        :param page_id: идентификатор вики-страницы.
        :param global: 1 — требуется получить информацию о глобальной вики-странице.
        :param site_preview: 1 — получаемая wiki страница является предпросмотром для прикрепленной ссылки.
        :param title: название страницы.
        :param need_source: 1 — требуется вернуть содержимое страницы в вики-формате.
        :param need_html: 1 — требуется вернуть html-представление страницы.

        :return: Возвращает информацию о вики-странице в виде объекта page.  Если был задан параметр need_source
            равный 1, дополнительно будет возвращено поле source.  Если был задан параметр need_html равный 1,
            дополнительно будет возвращено поле html
        """

        params = locals()
        method_name = self._base_method + 'get'
        return self._call(method_name, params)

    def getHistory(self, page_id: str = None, group_id: str = None, user_id: str = None) -> dict:
        """
        Возвращает список всех старых версий вики-страницы.

        :param page_id: идентификатор вики-страницы.
        :param group_id: идентификатор сообщества, которому принадлежит вики-страница.
        :param user_id: идентификатор пользователя, создавшего вики-страницу.

        :return: Возвращает массив объектов page_version, имеющих следующую структуру:   id — идентификатор
            версии страницы;  length длина версии страницы в байтах;  edited — дата редактирования страницы;
            editor_id — идентификатор редактора;  editor_name — имя редактора
        """

        params = locals()
        method_name = self._base_method + 'getHistory'
        return self._call(method_name, params)

    def getTitles(self, group_id: str = None) -> dict:
        """
        Возвращает список вики-страниц в группе.

        :param group_id: идентификатор сообщества, которому принадлежит вики-страница.

        :return: Возвращает массив объектов вики-страниц
        """

        params = locals()
        method_name = self._base_method + 'getTitles'
        return self._call(method_name, params)

    def getVersion(self, version_id: str = None, group_id: str = None, user_id: str = None,
                   need_html: str = None) -> dict:
        """
        Возвращает текст одной из старых версий страницы.

        :param version_id: идентификатор версии.
        :param group_id: идентификатор сообщества, которому принадлежит вики-страница.
        :param user_id: идентификатор пользователя, который создал страницу.
        :param need_html: определяет, требуется ли в ответе html-представление вики-страницы.

        :return: Возвращает объект вики-страницы
        """

        params = locals()
        method_name = self._base_method + 'getVersion'
        return self._call(method_name, params)

    def parseWiki(self, text: str = None, group_id: str = None) -> dict:
        """
        Возвращает html-представление вики-разметки.

        :param text: текст в вики-формате.
        :param group_id: идентификатор группы, в контексте которой интерпретируется данная страница.

        :return: В случае успеха возвращает экранированный html, соответствующий вики-разметке
        """

        params = locals()
        method_name = self._base_method + 'parseWiki'
        return self._call(method_name, params)

    def save(self, text: str = None, page_id: str = None, group_id: str = None, user_id: str = None,
             title: str = None) -> dict:
        """
        Сохраняет текст вики-страницы.

        :param text: новый текст страницы в вики-формате.
        :param page_id: идентификатор вики-страницы. Вместо page_id может быть передан параметр title.
        :param group_id: идентификатор сообщества, которому принадлежит вики-страница.
        :param user_id: идентификатор пользователя, создавшего вики-страницу.
        :param title: название вики-страницы.

        :return: В случае успеха возвращает id созданной страницы
        """

        params = locals()
        method_name = self._base_method + 'save'
        return self._call(method_name, params)

    def saveAccess(self, page_id: str = None, group_id: str = None, user_id: str = None, view: str = None,
                   edit: str = None) -> dict:
        """
        Сохраняет новые настройки доступа на чтение и редактирование вики-страницы.

        :param page_id: идентификатор вики-страницы.
        :param group_id: идентификатор сообщества, которому принадлежит вики-страница.
        :param user_id: идентификатор пользователя, создавшего вики-страницу.
        :param view: значение настройки доступа на чтение. Возможные значения:   2 — просматривать страницу могут
            все;  1 — только участники сообщества;  0 — только руководители сообщества.
        :param edit: значение настройки доступа на редактирование. Возможные значения:   2 — редактировать
            страницу могут все;  1 — только участники сообщества;  0 — только руководители сообщества.

        :return: В случае успеха возвращает id страницы, доступ к которой был отредактирован
        """

        params = locals()
        method_name = self._base_method + 'saveAccess'
        return self._call(method_name, params)

