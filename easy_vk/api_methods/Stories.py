from .ApiMethod import ApiMethod


class Stories(ApiMethod):
    def __init__(self, access_token, v, session, calls_per_second):
        super(Stories, self).__init__(access_token, v, session, calls_per_second)
        self._base_method = 'stories.'

    def banOwner(self, owners_ids: str = None) -> dict:
        """
        Позволяет скрыть из ленты новостей истории от выбранных источников.

        :param owners_ids: список идентификаторов источников.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'banOwner'
        return self._call(method_name, params)

    def delete(self, owner_id: str = None, story_id: str = None) -> dict:
        """
        Удаляет историю.

        :param owner_id: идентификатор владельца истории.
        :param story_id: идентификатор истории.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'delete'
        return self._call(method_name, params)

    def get(self, owner_id: str = None, extended: str = None, fields: str = None) -> dict:
        """
        Возвращает истории, доступные для текущего пользователя.

        :param owner_id: идентификатор пользователя, истории которого необходимо получить.
        :param extended: 1 — возвращать в ответе дополнительную информацию о профилях пользователей.
        :param fields:

        :return: После успешного выполнения возвращает объект, содержащий число подборок в поле count и массив
            подборок историй в поле items. Каждая подборка — массив историй от одного владельца.  Если был задан
            параметр extended=1, дополнительно возвращает массив объектов пользователей в поле profiles (array) и
            сообществ в поле groups (array)
        """

        params = locals()
        method_name = self._base_method + 'get'
        return self._call(method_name, params)

    def getBanned(self, extended: str = None, fields: str = None) -> dict:
        """
        Возвращает список источников историй, скрытых из ленты текущего пользователя.

        :param extended: 1 — возвращать расширенную информацию о пользователях и сообществах.
        :param fields: дополнительные поля пользователей и сообществ, которые необходимо вернуть.

        :return: После успешного выполнения возвращает общее количество скрытых источников в поле count (integer)
            и их идентификаторы в массиве items. Если extended = 1, items содержит два поля:   profiles (array) —
            массив объектов, описывающих пользователей;  groups (array) — массив объектов, описывающих сообщества
        """

        params = locals()
        method_name = self._base_method + 'getBanned'
        return self._call(method_name, params)

    def getById(self, stories: str = None, extended: str = None, fields: str = None) -> dict:
        """
        Возвращает информацию об истории по её идентификатору.

        :param stories: перечисленные через запятую идентификаторы, которые представляют собой идущие через знак
            подчеркивания идентификаторы владельцев историй и идентификаторы самих историй.   Пример значения
            stories: 93388_21539,93388_20904
        :param extended: 1 — возвращать в ответе дополнительную информацию о пользователях.
        :param fields: дополнительные поля профилей и сообществ, которые необходимо вернуть в ответе.

        :return: После успешного выполнения возвращает объект, содержащий число историй в поле count и массив
            объектов историй в поле items.  Если был задан параметр extended = 1, дополнительно возвращает массив
            объектов пользователей в поле profiles и объектов сообществ в поле groups
        """

        params = locals()
        method_name = self._base_method + 'getById'
        return self._call(method_name, params)

    def getPhotoUploadServer(self, add_to_news: str = None, user_ids: str = None, reply_to_story: str = None,
                             link_text: str = None, link_url: str = None, group_id: str = None,
                             clickable_stickers: str = None) -> dict:
        """
        Позволяет получить адрес для загрузки истории с фотографией.

        :param add_to_news: 1 — разместить историю в новостях. Обязательно, если не указан user_ids
        :param user_ids: идентификаторы пользователей, которые будут видеть историю (для отправки в личном
            сообщении). Обязательно, если add_to_news не передан.
        :param reply_to_story: идентификатор истории, в ответ на которую создается новая.
        :param link_text: текст ссылки для перехода из истории (только для историй сообществ). Возможные
            значения:   to_store — «В магазин»;  vote — «Голосовать»;  more — «Ещё»;  book — «Забронировать»;  order
            — «Заказать»;  enroll — «Записаться»;  fill — «Заполнить»;  signup — «Зарегистрироваться»;  buy —
            «Купить»;  ticket — «Купить билет»;  write — «Написать»;  open — «Открыть»;  learn_more — «Подробнее» (по
            умолчанию);  view — «Посмотреть»;  go_to — «Перейти»;  contact — «Связаться»;  watch — «Смотреть»;  play
            — «Слушать»;  install — «Установить»;  read — «Читать».
        :param link_url: адрес ссылки для перехода из истории. Допустимы только внутренние ссылки https://vk.com.
        :param group_id: идентификатор сообщества, в которое должна быть загружена история (при работе с ключом
            доступа пользователя).  Обратите внимание — загрузка историй доступна только для верифицированных
            сообществ и для сообществ, отмеченных «огоньком».
        :param clickable_stickers: объект кликабельного стикера.

        :return: После успешного выполнения возвращает объект, содержащий следующие поля:   upload_url (string) —
            адрес сервера для загрузки файла;  user_ids (array) — идентификаторы пользователей, которые могут видеть
            историю
        """

        params = locals()
        method_name = self._base_method + 'getPhotoUploadServer'
        return self._call(method_name, params)

    def getReplies(self, owner_id: str = None, story_id: str = None, access_key: str = None, extended: str = None,
                   fields: str = None) -> dict:
        """
        Позволяет получить ответы на историю.

        :param owner_id: идентификатор владельца истории.
        :param story_id: идентификатор истории.
        :param access_key: ключ доступа для приватного объекта.
        :param extended: 1 — возвращать дополнительную информацию о профилях и сообществах.
        :param fields: дополнительные поля профилей и сообществ, которые необходимо вернуть в ответе.

        :return: После успешного выполнения возвращает объект, содержащий число подборок в поле count и массив
            подборок историй в поле items. Каждая подборка — массив историй от одного владельца.  Если был задан
            параметр extended=1, дополнительно возвращает массив объектов пользователей в поле profiles (array) и
            сообществ в поле groups (array)
        """

        params = locals()
        method_name = self._base_method + 'getReplies'
        return self._call(method_name, params)

    def getStats(self, owner_id: str = None, story_id: str = None) -> dict:
        """
        Возвращает статистику истории.

        :param owner_id: идентификатор владельца истории.
        :param story_id: идентификатор истории.

        :return: Возвращает объект, который содержит следующие поля:   views (object) — просмотры. Содержит поля:
            state (string) — доступность значения (on — доступно, off — недоступно);  count (integer) — значение
            счётчика;   replies (object) — ответы на историю. Содержит поля:   state (string) — доступность значения
            (on — доступно, off — недоступно);  count (integer) — значение счётчика;   answer (object) — показывает
            сколько раз ответили на эту историю сообщением через поле под историей. Не путать с ответами на историю.
            state (string) — доступность значения (on — доступно, off — недоступно);  count (integer) — значение
            счётчика;   shares (object) — расшаривания истории. Содержит поля:   state (string) — доступность
            значения (on — доступно, off — недоступно);  count (integer) — значение счётчика;   subscribers (object)
            — новые подписчики. Содержит поля:   state (string) — доступность значения (on — доступно, off —
            недоступно);  count (integer) — значение счётчика;   bans (object) — скрытия истории. Содержит поля:
            state (string) — доступность значения (on — доступно, off — недоступно);  count (integer) — значение
            счётчика;   open_link (object) — переходы по ссылке. Содержит поля:   state (string) — доступность
            значения (on — доступно, hidden — недоступно);  count (integer) — значение счётчика
        """

        params = locals()
        method_name = self._base_method + 'getStats'
        return self._call(method_name, params)

    def getVideoUploadServer(self, add_to_news: str = None, user_ids: str = None, reply_to_story: str = None,
                             link_text: str = None, link_url: str = None, group_id: str = None,
                             clickable_stickers: str = None) -> dict:
        """
        Позволяет получить адрес для загрузки видеозаписи в историю.

        :param add_to_news: 1 — разместить историю в новостях.
        :param user_ids: идентификаторы пользователей, которые будут видеть историю (для отправки в личном
            сообщении).
        :param reply_to_story: идентификатор истории, в ответ на которую создается новая.
        :param link_text: текст ссылки для перехода из истории (только для историй сообществ). Возможные
            значения:   to_store — «В магазин»;  vote — «Голосовать»;  more — «Ещё»;  book — «Забронировать»;  order
            — «Заказать»;  enroll — «Записаться»;  fill — «Заполнить»;  signup — «Зарегистрироваться»;  buy —
            «Купить»;  ticket — «Купить билет»;  write — «Написать»;  open — «Открыть»;  learn_more — «Подробнее» (по
            умолчанию);  view — «Посмотреть»;  go_to — «Перейти»;  contact — «Связаться»;  watch — «Смотреть»;  play
            — «Слушать»;  install — «Установить»;  read — «Читать»;  game — «Играть».
        :param link_url: адрес ссылки для перехода из истории.
        :param group_id: идентификатор сообщества, в которое должна быть загружена история (при работе с ключом
            доступа пользователя).  Обратите внимание — загрузка историй доступна только для верифицированных
            сообществ и для сообществ, отмеченных «огоньком».
        :param clickable_stickers: объект кликабельного стикера.

        :return: После успешного выполнения возвращает объект, содержащий следующие поля:   upload_url (string) —
            адрес сервера для загрузки файла;  user_ids (array) — идентификаторы пользователей, которые могут видеть
            историю
        """

        params = locals()
        method_name = self._base_method + 'getVideoUploadServer'
        return self._call(method_name, params)

    def getViewers(self, owner_id: str = None, story_id: str = None, count: str = None, offset: str = None,
                   extended: str = None) -> dict:
        """
        Возвращает список пользователей, просмотревших историю.

        :param owner_id: идентификатор владельца истории.
        :param story_id: идентификатор истории.
        :param count: максимальное число результатов в ответе.
        :param offset: сдвиг для получения определённого подмножества результатов.
        :param extended: 1 — возвращать в ответе расширенную информацию о пользователях.

        :return: После успешного выполнения возвращает объект, содержащий число результатов в поле count и
            идентификаторы пользователей в поле items (array). Если extended = 1, поле items (array) содержит массив
            объектов пользователей
        """

        params = locals()
        method_name = self._base_method + 'getViewers'
        return self._call(method_name, params)

    def hideAllReplies(self, owner_id: str = None, group_id: str = None) -> dict:
        """
        Скрывает все ответы автора за последние сутки на истории текущего пользователя.

        :param owner_id: идентификатор пользователя, ответы от которого нужно скрыть.
        :param group_id:

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'hideAllReplies'
        return self._call(method_name, params)

    def hideReply(self, owner_id: str = None, story_id: str = None) -> dict:
        """
        Скрывает ответ на историю.

        :param owner_id: идентификатор владельца истории (ответной).
        :param story_id: идентификатор истории (ответной).

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'hideReply'
        return self._call(method_name, params)

    def search(self, q: str = None, place_id: str = None, latitude: str = None, longitude: str = None,
               radius: str = None, mentioned_id: str = None, count: str = None, extended: str = None,
               fields: str = None) -> dict:
        """
        Возвращает результаты поиска по историям.

        :param q: поисковый запрос.
        :param place_id: идентификатор места.
        :param latitude: географическая широта точки, в радиусе которой необходимо производить поиск, заданная в
            градусах (от -90 до 90).
        :param longitude: географическая долгота точки, в радиусе которой необходимо производить поиск, заданная
            в градусах (от -180 до 180).
        :param radius: радиус зоны поиска в метрах.
        :param mentioned_id: идентификатор упомянутого в истории пользователя или сообщества.
        :param count: количество историй, информацию о которых необходимо вернуть.
        :param extended: параметр, определяющий необходимость возвращать расширенную информацию о владельце
            истории. Возможные значения:   0 — возвращаются только идентификаторы;  1 — будут дополнительно
            возвращены имя и фамилия.   По умолчанию: 0.
        :param fields: список дополнительных полей профилей, которые необходимо вернуть. См. подробное описание.

        :return: После успешного выполнения возвращает объект, содержащий число результатов в поле count и массив
            объектов историй в поле items.  Если был задан параметр extended=1, возвращает объекты profiles и groups,
            содержащие массивы объектов, описывающих пользователей и сообществ
        """

        params = locals()
        method_name = self._base_method + 'search'
        return self._call(method_name, params)

    def sendInteraction(self, access_key: str = None, message: str = None, is_broadcast: str = None,
                        is_anonymous: str = None) -> dict:
        """
        Отправляет фидбек на историю.

        :param access_key: ключ доступа пользователя, полученный при подписке. Возвращает событие
            VKWebAppSubscribeStoryApp.
        :param message: текст фидбека.
        :param is_broadcast: Возможные значения:   0 — фидбек виден только отправителю и автору истории;  1 —
            фидбек виден всем зрителям истории и автору.
        :param is_anonymous: Возможные значения:   0 — автор фидбека не анонимный;  1 — автор фидбека анонимный.

        :return
        """

        params = locals()
        method_name = self._base_method + 'sendInteraction'
        return self._call(method_name, params)

    def unbanOwner(self, owners_ids: str = None) -> dict:
        """
        Позволяет вернуть пользователя или сообщество в список отображаемых историй в ленте.

        :param owners_ids: список идентификаторов владельцев историй, разделённых запятой.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'unbanOwner'
        return self._call(method_name, params)
