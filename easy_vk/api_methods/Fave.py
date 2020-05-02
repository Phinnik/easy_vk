from .ApiMethod import ApiMethod


class Fave(ApiMethod):
    def __init__(self, access_token, v, session, calls_per_second):
        super(Fave, self).__init__(access_token, v, session, calls_per_second)
        self._base_method = 'fave.'

    def addArticle(self, url: str = None) -> dict:
        """
        Добавляет статью в закладки.

        :param url: ссылка на добавляемую статью.

        :return: В случае успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'addArticle'
        return self._call(method_name, params)

    def addLink(self, link: str = None) -> dict:
        """
        Добавляет ссылку в закладки.

        :param link: адрес добавляемой ссылки. Поддерживаются только внутренние ссылки на vk.com.

        :return: В случае успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'addLink'
        return self._call(method_name, params)

    def addPage(self, user_id: str = None, group_id: str = None) -> dict:
        """
        Добавляет сообщество или пользователя в закладки.

        :param user_id: идентификатор пользователя, которого нужно добавить в закладки.
        :param group_id: идентификатор сообщества, которое нужно добавить в закладки.

        :return: В случае успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'addPage'
        return self._call(method_name, params)

    def addPost(self, owner_id: str = None, id: str = None, access_key: str = None, ref: str = None,
                track_code: str = None, source: str = None) -> dict:
        """
        Добавляет запись со стены пользователя или сообщества в закладки.

        :param owner_id: идентификатор пользователя или сообщества, чью запись со стены требуется добавить в
            закладки. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком
            "-" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)
        :param id: идентификатор записи, которую необходимо добавить в закладки.
        :param access_key: специальный код доступа для приватных постов.
        :param ref:
        :param track_code:
        :param source:

        :return: В случае успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'addPost'
        return self._call(method_name, params)

    def addProduct(self, owner_id: str = None, id: str = None, access_key: str = None) -> dict:
        """
        Добавляет товар в закладки.

        :param owner_id: идентификатор пользователя или сообщества, чей товар требуется добавить в закладки.
            Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком "-" —
            например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)
        :param id: идентификатор товара.
        :param access_key: специальный код доступа для приватных товаров.

        :return: В случае успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'addProduct'
        return self._call(method_name, params)

    def addTag(self, name: str = None, position: str = None) -> dict:
        """
        Создает метку закладок.

        :param name: название метки.
        :param position: положение метки.  Возможные значения:   front - начало списка,  back - конец списка.

        :return: В случае успешного выполнения возвращает объект метки с полями name - названием метки и id -
            идентификатором созданной метки
        """

        params = locals()
        method_name = self._base_method + 'addTag'
        return self._call(method_name, params)

    def addVideo(self, owner_id: str = None, id: str = None, access_key: str = None, ref: str = None) -> dict:
        """
        Добавляет видеозапись в закладки.

        :param owner_id: идентификатор пользователя или сообщества, владельца видеозаписи, которую требуется
            добавить в закладки. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо
            указывать со знаком "-" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API
            (club1)
        :param id: идентификатор видеозаписи.
        :param access_key: специальный код доступа для приватных видеозаписей.
        :param ref:

        :return: В случае успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'addVideo'
        return self._call(method_name, params)

    def editTag(self, id: str = None, name: str = None) -> dict:
        """
        Редактирует метку.

        :param id: идентификатор метки.
        :param name: новое название метки.

        :return: В случае успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'editTag'
        return self._call(method_name, params)

    def get(self, extended: str = None, item_type: str = None, tag_id: str = None, offset: str = None,
            count: str = None, fields: str = None, is_from_snackbar: str = None) -> dict:
        """
        Возвращает объекты, добавленные в закладки пользователя.

        :param extended: 1, если необходимо получить информацию о пользователе. По умолчанию: 0.
        :param item_type: Типы объектов, которые необходимо вернуть. Возможные значения:   post — записи;  video
            — видеозаписи;  product — товары;  article — статьи;  link — ссылки.
        :param tag_id: идентификатор метки, закладки отмеченные которой требуется вернуть.
        :param offset: смещение относительно первого объекта в закладках пользователя для выборки определенного
            подмножества.
        :param count: количество возвращаемых закладок.
        :param fields: список дополнительных полей профилей, которые необходимо вернуть. См. подробное описание.
        :param is_from_snackbar:

        :return: После успешного выполнения возвращает объект, содержащий число результатов в поле count и массив
            объектов, добавленных в закладки, в поле items.  Каждый из объектов содержит следующие поля:  type
            stringтип объекта, добавленного в закладки. Возможные значения:   post — запись на стене;  video —
            видеозапись;  product — товар;  article — статья;  link — ссылки. seen  booleanявляется ли закладка
            просмотренной. added_date  integerдата добавления объекта в закладки в формате Unixtime. tags
            arrayмассив меток объекта в списке закладок. {object_type}  objectобъект, добавленный в закладки.  Если
            был задан параметр extended=1, возвращает число результатов в поле count, отдельно массив объектов
            пользователей в поле profiles и сообществ в поле groups
        """

        params = locals()
        method_name = self._base_method + 'get'
        return self._call(method_name, params)

    def getPages(self, offset: str = None, count: str = None, type: str = None, fields: str = None,
                 tag_id: str = None) -> dict:
        """
        Возвращает страницы пользователей и сообществ, добавленных в закладки.

        :param offset: смещение относительно первого объекта в закладках пользователя для выборки определенного
            подмножества.
        :param count: количество возвращаемых закладок.
        :param type: Типы объектов, которые необходимо вернуть. Возможные значения:   users — вернуть только
            пользователей;  groups — вернуть только сообщества;  hints — топ сообществ и пользователей.   Если
            параметр не указан — вернутся объекты пользователей и сообществ, добавленных в закладки, в порядке
            добавления.
        :param fields: список дополнительных полей для объектов user и group, которые необходимо вернуть.
        :param tag_id: идентификатор метки, закладки отмеченные которой требуется вернуть.

        :return
        """

        params = locals()
        method_name = self._base_method + 'getPages'
        return self._call(method_name, params)

    def getTags(self) -> dict:
        """
        Возвращает список меток в закладках.

        :return: После успешного выполнения возвращает объект, содержащий число результатов в поле count и массив
            объектов меток в поле items.  Поля, описывающие объект метки: id - идентификатор метки и name - название
        """

        params = locals()
        method_name = self._base_method + 'getTags'
        return self._call(method_name, params)

    def markSeen(self) -> dict:
        """
        Отмечает закладки как просмотренные.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'markSeen'
        return self._call(method_name, params)

    def removeArticle(self, owner_id: str = None, article_id: str = None, ref: str = None) -> dict:
        """
        Удаляет статью из закладок.

        :param owner_id: идентификатор владельца статьи.
        :param article_id: идентификатор статьи.
        :param ref:

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'removeArticle'
        return self._call(method_name, params)

    def removeLink(self, link_id: str = None) -> dict:
        """
        Удаляет ссылку из списка закладок пользователя.

        :param link_id: идентификатор ссылки.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'removeLink'
        return self._call(method_name, params)

    def removePage(self, user_id: str = None, group_id: str = None) -> dict:
        """
        Удаляет из закладок сообщество или страницу пользователя.

        :param user_id: идентификатор пользователя, которого следует удалить из закладок.
        :param group_id: идентификатор сообщества, которое следует удалить из закладок.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'removePage'
        return self._call(method_name, params)

    def removePost(self, owner_id: str = None, id: str = None) -> dict:
        """
        Удаляет из закладок запись на стене пользователя или сообщества.

        :param owner_id: идентификатор владельца записи. Обратите внимание, идентификатор сообщества в параметре
            owner_id необходимо указывать со знаком "-" — например, owner_id=-1 соответствует идентификатору
            сообщества ВКонтакте API (club1)
        :param id: идентификатор записи на стене.

        :return: В случае успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'removePost'
        return self._call(method_name, params)

    def removeProduct(self, owner_id: str = None, id: str = None) -> dict:
        """
        Удаляет товар из закладок.

        :param owner_id: идентификатор пользователя или сообщества, чей товар требуется удалить из закладок.
            Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком "-" —
            например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)
        :param id: идентификатор товара.

        :return: В случае успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'removeProduct'
        return self._call(method_name, params)

    def removeTag(self, id: str = None) -> dict:
        """
        Удаляет метку закладок.

        :param id: идентификатор метки.

        :return: В случае успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'removeTag'
        return self._call(method_name, params)

    def removeVideo(self, owner_id: str = None, id: str = None) -> dict:
        """
        Удаляет видеозапись из списка закладок.

        :param owner_id: идентификатор пользователя или сообщества, владельца видеозаписи, которую требуется
            удалить из закладок. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо
            указывать со знаком "-" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API
            (club1)
        :param id: идентификатор видеозаписи.

        :return: В случае успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'removeVideo'
        return self._call(method_name, params)

    def reorderTags(self, ids: str = None) -> dict:
        """
        Меняет порядок меток закладок в списке.

        :param ids: перечисленные через запятую все идентификаторы меток пользователя в том порядке, в котором их
            требуется отображать.

        :return: В случае успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'reorderTags'
        return self._call(method_name, params)

    def setPageTags(self, user_id: str = None, group_id: str = None, tag_ids: str = None) -> dict:
        """
        Устанавливает метку странице пользователя или сообщества.

        :param user_id: идентификатор пользователя, которому требуется проставить метку в закладках. Обязательный
            параметр, если не задан параметр group_id.
        :param group_id: идентификатор сообщества, которому требуется проставить метку в закладках. Обязательный
            параметр, если не задан параметр user_id.
        :param tag_ids: перечисленные через запятую идентификаторы тегов, которые требуется присвоить странице.

        :return: В случае успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'setPageTags'
        return self._call(method_name, params)

    def setTags(self, item_type: str = None, item_owner_id: str = None, item_id: str = None, tag_ids: str = None,
                link_id: str = None, link_url: str = None) -> dict:
        """
        Устанавливает метку выбранному объекту в списке закладок.

        :param item_type: Тип объекта, которому необходимо присвоить метку. Возможные значения:   post — запись
            на стене;  video — видеозапись;  product — товар;  article — статья;  link — ссылка.   Для работы с
            объектами пользователя или сообщества используйте метод fave.setPageTags
        :param item_owner_id: идентификатор владельца объекта, которому требуется присвоить метку. Обратите
            внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком "-" — например,
            owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)
        :param item_id: идентификатор объекта.
        :param tag_ids: идентификатор метки, которую требуется присвоить объекту.
        :param link_id: идентификатор ссылки, которой требуется присвоить метку.
        :param link_url:

        :return: В случае успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'setTags'
        return self._call(method_name, params)

    def trackPageInteraction(self, user_id: str = None, group_id: str = None) -> dict:
        """
        Устанавливает страницу пользователя или сообщества в топ закладок.

        :param user_id: идентификатор пользователя, которому требуется проставить метку в закладках. Обязательный
            параметр, если не задан параметр group_id.
        :param group_id: идентификатор сообщества, которому требуется проставить метку в закладках. Обязательный
            параметр, если не задан параметр user_id.

        :return: В случае успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'trackPageInteraction'
        return self._call(method_name, params)
