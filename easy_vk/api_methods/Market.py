from ApiMethod import ApiMethod


class Market(ApiMethod):
    def __init__(self, access_token, v, session, calls_per_second):
        super(Market, self).__init__(access_token, v, session, calls_per_second)
        self._base_method = 'market.'

    def add(self, owner_id: str = None, name: str = None, description: str = None, category_id: str = None,
            price: str = None, old_price: str = None, deleted: str = None, main_photo_id: str = None,
            photo_ids: str = None, url: str = None) -> dict:
        """
        Добавляет новый товар.

        :param owner_id: идентификатор владельца товара.  Обратите внимание, идентификатор сообщества в параметре
            owner_id необходимо указывать со знаком "-" — например, owner_id=-1 соответствует идентификатору
            сообщества ВКонтакте API (club1)
        :param name: название товара. Ограничение по длине считается в кодировке cp1251.
        :param description: описание товара.
        :param category_id: идентификатор категории товара.
        :param price: цена товара.
        :param old_price: старая цена товара.
        :param deleted: статус товара (1 — товар удален, 0 — товар не удален).
        :param main_photo_id: идентификатор фотографии обложки товара.  Фотография должна быть загружена с
            помощью метода photos.getMarketUploadServer, передав параметр main_photo. См. подробную информацию о
            загрузке фотографии товаров
        :param photo_ids: идентификаторы дополнительных фотографий товара.  Фотография должна быть загружена с
            помощью метода photos.getMarketUploadServer. См. подробную информацию о загрузке фотографии товаров
        :param url: ссылка на сайт товара.

        :return: После успешного выполнения возвращает идентификатор добавленного товара
        """

        params = locals()
        method_name = self._base_method + 'add'
        return self._call(method_name, params)

    def addAlbum(self, owner_id: str = None, title: str = None, photo_id: str = None, main_album: str = None) -> dict:
        """
        Добавляет новую подборку с товарами.

        :param owner_id: идентификатор владельца подборки.  Обратите внимание, идентификатор сообщества в
            параметре owner_id необходимо указывать со знаком "-" — например, owner_id=-1 соответствует
            идентификатору сообщества ВКонтакте API (club1)
        :param title: название подборки.
        :param photo_id: идентификатор фотографии-обложки подборки.  Фотография должна быть загружена с помощью
            метода photos.getMarketAlbumUploadServer. См. подробную информацию о загрузке фотографии товаров.
        :param main_album: назначить подборку основной (1 — назначить, 0 — нет).

        :return: После успешного выполнения возвращает идентификатор созданной подборки
        """

        params = locals()
        method_name = self._base_method + 'addAlbum'
        return self._call(method_name, params)

    def addToAlbum(self, owner_id: str = None, item_id: str = None, album_ids: str = None) -> dict:
        """
        Добавляет товар в одну или несколько выбранных подборок.

        :param owner_id: идентификатор владельца товара.  Обратите внимание, идентификатор сообщества в параметре
            owner_id необходимо указывать со знаком "-" — например, owner_id=-1 соответствует идентификатору
            сообщества ВКонтакте API (club1)
        :param item_id: идентификатор товара.
        :param album_ids: идентификаторы подборок, в которые нужно добавить товар.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'addToAlbum'
        return self._call(method_name, params)

    def createComment(self, owner_id: str = None, item_id: str = None, message: str = None, attachments: str = None,
                      from_group: str = None, reply_to_comment: str = None, sticker_id: str = None,
                      guid: str = None) -> dict:
        """
        Создает новый комментарий к товару.

        :param owner_id: идентификатор владельца товара. Обратите внимание, идентификатор сообщества в параметре
            owner_id необходимо указывать со знаком "-" — например, owner_id=-1 соответствует идентификатору
            сообщества ВКонтакте API (club1)
        :param item_id: идентификатор товара.
        :param message: текст комментария (является обязательным, если не задан параметр attachments).
        :param attachments: список объектов, приложенных к комментарию и разделённых символом ",". Поле
            attachments представляется в формате: <type><owner_id>_<media_id>,<type><owner_id>_<media_id> <type> —
            тип медиа-вложения: photo — фотография  video — видеозапись  audio — аудиозапись  doc — документ
            <owner_id> — идентификатор владельца медиа-вложения  <media_id> — идентификатор медиа-вложения.
            Например: photo100172_166443618,photo66748_265827614 Параметр является обязательным, если не задан
            параметр message.
        :param from_group: 1 — комментарий будет опубликован от имени группы, 0 — комментарий будет опубликован
            от имени пользователя (по умолчанию).
        :param reply_to_comment: идентификатор комментария, в ответ на который должен быть добавлен новый
            комментарий.
        :param sticker_id: идентификатор стикера.
        :param guid: уникальный идентификатор, предназначенный для предотвращения повторной отправки одинакового
            комментария.

        :return: После успешного выполнения возвращает идентификатор созданного комментария
        """

        params = locals()
        method_name = self._base_method + 'createComment'
        return self._call(method_name, params)

    def delete(self, owner_id: str = None, item_id: str = None) -> dict:
        """
        Удаляет товар.

        :param owner_id: идентификатор владельца товара.  Обратите внимание, идентификатор сообщества в параметре
            owner_id необходимо указывать со знаком "-" — например, owner_id=-1 соответствует идентификатору
            сообщества ВКонтакте API (club1)
        :param item_id: идентификатор товара.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'delete'
        return self._call(method_name, params)

    def deleteAlbum(self, owner_id: str = None, album_id: str = None) -> dict:
        """
        Удаляет подборку с товарами.

        :param owner_id: идентификатор владельца подборки.  Обратите внимание, идентификатор сообщества в
            параметре owner_id необходимо указывать со знаком "-" — например, owner_id=-1 соответствует
            идентификатору сообщества ВКонтакте API (club1)
        :param album_id: идентификатор подборки.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'deleteAlbum'
        return self._call(method_name, params)

    def deleteComment(self, owner_id: str = None, comment_id: str = None) -> dict:
        """
        Удаляет комментарий к товару.

        :param owner_id: идентификатор владельца товара.  Обратите внимание, идентификатор сообщества в параметре
            owner_id необходимо указывать со знаком "-" — например, owner_id=-1 соответствует идентификатору
            сообщества ВКонтакте API (club1)
        :param comment_id: идентификатор комментария.

        :return: После успешного выполнения возвращает 1 (0, если комментарий не найден)
        """

        params = locals()
        method_name = self._base_method + 'deleteComment'
        return self._call(method_name, params)

    def edit(self, owner_id: str = None, item_id: str = None, name: str = None, description: str = None,
             category_id: str = None, price: str = None, old_price: str = None, deleted: str = None,
             main_photo_id: str = None, photo_ids: str = None, url: str = None) -> dict:
        """
        Редактирует товар.

        :param owner_id: идентификатор владельца товара.  Обратите внимание, идентификатор сообщества в параметре
            owner_id необходимо указывать со знаком "-" — например, owner_id=-1 соответствует идентификатору
            сообщества ВКонтакте API (club1)
        :param item_id: идентификатор товара.
        :param name: новое название товара.
        :param description: новое описание товара.
        :param category_id: идентификатор категории товара.
        :param price: цена товара.
        :param old_price: старая цена.
        :param deleted: статус товара (1 — товар удален, 0 — товар не удален).
        :param main_photo_id: идентификатор фотографии для обложки товара.  Фотография может быть загружена с
            помощью метода photos.getMarketUploadServer (параметр main_photo). См. подробную информацию о загрузке
            фотографии товаров.  Идентификатор фотографии может быть также получен методами market.get или
            market.getById (если Вы хотите использовать существующую фотографию товара).
        :param photo_ids: идентификаторы дополнительных фотографией товара.  Фотография должна быть загружена с
            помощью метода photos.getMarketUploadServer. См. подробную информацию о загрузке фотографии товаров.
        :param url: ссылка на сайт товара.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'edit'
        return self._call(method_name, params)

    def editAlbum(self, owner_id: str = None, album_id: str = None, title: str = None, photo_id: str = None,
                  main_album: str = None) -> dict:
        """
        Редактирует подборку с товарами.

        :param owner_id: идентификатор владельца подборки.  Обратите внимание, идентификатор сообщества в
            параметре owner_id необходимо указывать со знаком "-" — например, owner_id=-1 соответствует
            идентификатору сообщества ВКонтакте API (club1)
        :param album_id: идентификатор подборки.
        :param title: название подборки.
        :param photo_id: идентификатор фотографии-обложки подборки.  Фотография должна быть загружена с помощью
            метода photos.getMarkeAlbumUploadServer. См. подробную информацию о загрузке фотографии товаров.
        :param main_album: назначить подборку основной (1 — назначить, 0 — нет).

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'editAlbum'
        return self._call(method_name, params)

    def editComment(self, owner_id: str = None, comment_id: str = None, message: str = None,
                    attachments: str = None) -> dict:
        """
        Изменяет текст комментария к товару.

        :param owner_id: идентификатор владельца товара.  Обратите внимание, идентификатор сообщества в параметре
            owner_id необходимо указывать со знаком "-" — например, owner_id=-1 соответствует идентификатору
            сообщества ВКонтакте API (club1)
        :param comment_id: идентификатор комментария.
        :param message: новый текст комментария (является обязательным, если не задан параметр attachments).
            Максимальное количество символов: 2048.
        :param attachments: новый список объектов, приложенных к комментарию и разделённых символом ",". Поле
            attachments представляется в формате: <type><owner_id>_<media_id>,<type><owner_id>_<media_id> <type> —
            тип медиа-вложения: photo — фотография  video — видеозапись  audio — аудиозапись  doc — документ
            <owner_id> — идентификатор владельца медиа-вложения  <media_id> — идентификатор медиа-вложения.
            Например: photo100172_166443618,photo66748_265827614 Параметр является обязательным, если не задан
            параметр message.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'editComment'
        return self._call(method_name, params)

    def get(self, owner_id: str = None, album_id: str = None, count: str = None, offset: str = None,
            extended: str = None) -> dict:
        """
        Возвращает список товаров в сообществе.

        :param owner_id: идентификатор владельца товаров.  Обратите внимание, идентификатор сообщества в
            параметре owner_id необходимо указывать со знаком "-" — например, owner_id=-1 соответствует
            идентификатору сообщества ВКонтакте API (club1)
        :param album_id: идентификатор подборки, товары из которой нужно вернуть.
        :param count: количество возвращаемых товаров.
        :param offset: смещение относительно первого найденного товара для выборки определенного подмножества.
        :param extended: 1 — будут возвращены дополнительные поля likes, can_comment, can_repost, photos,
            views_count. По умолчанию эти поля не возвращается.

        :return: После успешного выполнения возвращает объект, содержащий число результатов в поле count и массив
            объектов товаров в поле items
        """

        params = locals()
        method_name = self._base_method + 'get'
        return self._call(method_name, params)

    def getAlbumById(self, owner_id: str = None, album_ids: str = None) -> dict:
        """
        Возвращает данные подборки с товарами.

        :param owner_id: идентификатор владельца подборки.  Обратите внимание, идентификатор сообщества в
            параметре owner_id необходимо указывать со знаком "-" — например, owner_id=-1 соответствует
            идентификатору сообщества ВКонтакте API (club1)
        :param album_ids: идентификаторы подборок, данные о которых нужно получить.

        :return: После успешного выполнения возвращает объект, содержащий число результатов в поле count и массив
            объектов подборок в поле items
        """

        params = locals()
        method_name = self._base_method + 'getAlbumById'
        return self._call(method_name, params)

    def getAlbums(self, owner_id: str = None, offset: str = None, count: str = None) -> dict:
        """
        Возвращает список подборок с товарами.

        :param owner_id: идентификатор владельца товаров.  Обратите внимание, идентификатор сообщества в
            параметре owner_id необходимо указывать со знаком "-" — например, owner_id=-1 соответствует
            идентификатору сообщества ВКонтакте API (club1)
        :param offset: смещение относительно первой найденной подборки для выборки определенного подмножества.
        :param count: количество возвращаемых подборок.

        :return: После успешного выполнения возвращает объект, содержащий число результатов в поле count и массив
            объектов подборок в поле items
        """

        params = locals()
        method_name = self._base_method + 'getAlbums'
        return self._call(method_name, params)

    def getById(self, item_ids: str = None, extended: str = None) -> dict:
        """
        Возвращает информацию о товарах по идентификаторам.

        :param item_ids: перечисленные через запятую идентификаторы — идущие через знак подчеркивания id
            владельцев товаров и id самих товаров. Если товар принадлежит сообществу, то в качестве первого параметра
            используется -id сообщества. Пример значения item_ids:  -4363_136089719,13245770_137352259
        :param extended: 1 — будут возвращены дополнительные поля likes, can_comment, can_repost, photos,
            views_count. По умолчанию: 0.

        :return: После успешного выполнения возвращает объект, содержащий число результатов в поле count и массив
            объектов товаров в поле items
        """

        params = locals()
        method_name = self._base_method + 'getById'
        return self._call(method_name, params)

    def getCategories(self, count: str = None, offset: str = None) -> dict:
        """
        Возвращает список категорий для товаров.

        :param count: количество категорий, информацию о которых необходимо вернуть.
        :param offset: смещение, необходимое для выборки определенного подмножества категорий.

        :return: После успешного выполнения возвращает список объектов category.  Объект category — категория
            товара.  id   (integer) идентификатор категории. name   (string) название метки. section   (object)
            секция. Объект, содержащий поля:   id (integer) — идентификатор секции;  name (string) — название секции
        """

        params = locals()
        method_name = self._base_method + 'getCategories'
        return self._call(method_name, params)

    def getComments(self, owner_id: str = None, item_id: str = None, need_likes: str = None,
                    start_comment_id: str = None, offset: str = None, count: str = None, sort: str = None,
                    extended: str = None, fields: str = None) -> dict:
        """
        Возвращает список комментариев к товару.

        :param owner_id: идентификатор владельца товара.  Обратите внимание, идентификатор сообщества в параметре
            owner_id необходимо указывать со знаком "-" — например, owner_id=-1 соответствует идентификатору
            сообщества ВКонтакте API (club1)
        :param item_id: идентификатор товара.
        :param need_likes: 1 — возвращать информацию о лайках.
        :param start_comment_id: идентификатор комментария, начиная с которого нужно вернуть список (подробности
            см. ниже).
        :param offset: сдвиг, необходимый для получения конкретной выборки результатов.
        :param count: число комментариев, которые необходимо получить.
        :param sort: порядок сортировки комментариев (asc — от старых к новым, desc - от новых к старым)
        :param extended: 1 — комментарии в ответе будут возвращены в виде пронумерованных объектов, дополнительно
            будут возвращены списки объектов profiles, groups.
        :param fields: список дополнительных полей профилей, которые необходимо вернуть. См. подробное описание.
            Доступные значения: sex, bdate, city, country, photo_50, photo_100, photo_200_orig, photo_200,
            photo_400_orig, photo_max, photo_max_orig, photo_id, online, online_mobile, domain, has_mobile, contacts,
            connections, site, education, universities, schools, can_post, can_see_all_posts, can_see_audio,
            can_write_private_message, status, last_seen, common_count, relation, relatives, counters, screen_name,
            maiden_name, timezone, occupation,activities, interests, music, movies, tv, books, games, about, quotes,
            personal, friend_status, military, career

        :return: После успешного выполнения возвращает объект, содержащий число результатов в поле count и массив
            объектов комментариев в поле items
        """

        params = locals()
        method_name = self._base_method + 'getComments'
        return self._call(method_name, params)

    def removeFromAlbum(self, owner_id: str = None, item_id: str = None, album_ids: str = None) -> dict:
        """
        Удаляет товар из одной или нескольких выбранных подборок.

        :param owner_id: идентификатор владельца товара.  Обратите внимание, идентификатор сообщества в параметре
            owner_id необходимо указывать со знаком "-" — например, owner_id=-1 соответствует идентификатору
            сообщества ВКонтакте API (club1)
        :param item_id: идентификатор товара.
        :param album_ids: идентификаторы подборок, из которых нужно удалить товар.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'removeFromAlbum'
        return self._call(method_name, params)

    def reorderAlbums(self, owner_id: str = None, album_id: str = None, before: str = None, after: str = None) -> dict:
        """
        Изменяет положение подборки с товарами в списке.

        :param owner_id: идентификатор владельца альбома.  Обратите внимание, идентификатор сообщества в
            параметре owner_id необходимо указывать со знаком "-" — например, owner_id=-1 соответствует
            идентификатору сообщества ВКонтакте API (club1)
        :param album_id: идентификатор подборки.
        :param before: идентификатор подборки, перед которой следует поместить текущую.
        :param after: идентификатор подборки, после которой следует поместить текущую.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'reorderAlbums'
        return self._call(method_name, params)

    def reorderItems(self, owner_id: str = None, album_id: str = None, item_id: str = None, before: str = None,
                     after: str = None) -> dict:
        """
        Изменяет положение товара в подборке.

        :param owner_id: идентификатор владельца товара.  Обратите внимание, идентификатор сообщества в параметре
            owner_id необходимо указывать со знаком "-" — например, owner_id=-1 соответствует идентификатору
            сообщества ВКонтакте API (club1)
        :param album_id: идентификатор подборки, в которой находится товар. 0 — для сортировки общего списка
            товаров.
        :param item_id: идентификатор товара.
        :param before: идентификатор товара, перед которым следует поместить текущий.
        :param after: идентификатор товара, после которого следует поместить текущий.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'reorderItems'
        return self._call(method_name, params)

    def report(self, owner_id: str = None, item_id: str = None, reason: str = None) -> dict:
        """
        Позволяет отправить жалобу на товар.

        :param owner_id: идентификатор владельца товаров.  Обратите внимание, идентификатор сообщества в
            параметре owner_id необходимо указывать со знаком "-" — например, owner_id=-1 соответствует
            идентификатору сообщества ВКонтакте API (club1)
        :param item_id: идентификатор товара
        :param reason: причина жалобы:   0 — спам;  1 — детская порнография;  2 — экстремизм;  3 — насилие;  4 —
            пропаганда наркотиков;  5 — материал для взрослых;  6 — оскорбление.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'report'
        return self._call(method_name, params)

    def reportComment(self, owner_id: str = None, comment_id: str = None, reason: str = None) -> dict:
        """
        Позволяет оставить жалобу на комментарий к товару.

        :param owner_id: идентификатор владельца товара.  Обратите внимание, идентификатор сообщества в параметре
            owner_id необходимо указывать со знаком "-" — например, owner_id=-1 соответствует идентификатору
            сообщества ВКонтакте API (club1)
        :param comment_id: идентификатор комментария.
        :param reason: причина жалобы:   0 — спам;  1 — детская порнография;  2 — экстремизм;  3 — насилие;  4 —
            пропаганда наркотиков;  5 — материал для взрослых;  6 — оскорбление.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'reportComment'
        return self._call(method_name, params)

    def restore(self, owner_id: str = None, item_id: str = None) -> dict:
        """
        Восстанавливает удаленный товар.

        :param owner_id: идентификатор владельца товара.  Обратите внимание, идентификатор сообщества в параметре
            owner_id необходимо указывать со знаком "-" — например, owner_id=-1 соответствует идентификатору
            сообщества ВКонтакте API (club1)
        :param item_id: идентификатор товара.

        :return: После успешного выполнения возвращает 1 (0, если товар не найден среди удаленных)
        """

        params = locals()
        method_name = self._base_method + 'restore'
        return self._call(method_name, params)

    def restoreComment(self, owner_id: str = None, comment_id: str = None) -> dict:
        """
        Восстанавливает удаленный комментарий к товару.

        :param owner_id: идентификатор владельца товара.  Обратите внимание, идентификатор сообщества в параметре
            owner_id необходимо указывать со знаком "-" — например, owner_id=-1 соответствует идентификатору
            сообщества ВКонтакте API (club1)
        :param comment_id: идентификатор удаленного комментария.

        :return: После успешного выполнения возвращает 1 (0, если комментарий с таким идентификатором не является
            удаленным)
        """

        params = locals()
        method_name = self._base_method + 'restoreComment'
        return self._call(method_name, params)

    def search(self, owner_id: str = None, album_id: str = None, q: str = None, price_from: str = None,
               price_to: str = None, tags: str = None, sort: str = None, rev: str = None, offset: str = None,
               count: str = None, extended: str = None, status: str = None) -> dict:
        """
        Ищет товары в каталоге сообщества.

        :param owner_id: идентификатор сообщества, которому принадлежат товары.
        :param album_id: идентификатор подборки, товары из которой нужно вернуть.
        :param q:  поискового запроса. Например, зеленые тапочки.
        :param price_from: минимальное значение цены товаров в сотых долях единицы валюты. Например, 100000.
        :param price_to: максимальное значение цены товаров в сотых долях единицы валюты. Например, 1410000.
        :param tags: перечисленные через запятую идентификаторы меток.
        :param sort: вид сортировки. 0 — пользовательская расстановка, 1 — по дате добавления товара, 2 — по
            цене, 3 — по популярности.
        :param rev: 0 — не использовать обратный порядок, 1 — использовать обратный порядок.
        :param offset: смещение относительно первого найденного товара для выборки определенного подмножества.
        :param count: количество возвращаемых товаров.
        :param extended: 1 — будут возвращены дополнительные поля likes, can_comment, can_repost, photos,
            views_count. По умолчанию эти поля не возвращается.
        :param status:

        :return: После успешного выполнения возвращает объект, содержащий число результатов в поле count и массив
            объектов товаров в поле items
        """

        params = locals()
        method_name = self._base_method + 'search'
        return self._call(method_name, params)
