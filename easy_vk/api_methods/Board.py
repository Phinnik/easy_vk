from ApiMethod import ApiMethod


class Board(ApiMethod):
    def __init__(self, access_token, v, session, calls_per_second):
        super(Board, self).__init__(access_token, v, session, calls_per_second)
        self._base_method = 'board.'

    def addTopic(self, group_id: str = None, title: str = None, text: str = None, from_group: str = None,
                 attachments: str = None) -> dict:
        """
        Создает новую тему в списке обсуждений группы.

        :param group_id: идентификатор сообщества.
        :param title: название обсуждения.
        :param text: текст первого сообщения в обсуждении.
        :param from_group: 1 — тема будет создана от имени группы, 0 — тема будет создана от имени пользователя
            (по умолчанию).
        :param attachments: список объектов, приложенных к записи, в формате:
            <type><owner_id>_<media_id>,<type><owner_id>_<media_id>   <type> — тип медиа-приложения:   photo —
            фотография;  video — видеозапись ;  audio — аудиозапись;  doc — документ;   <owner_id> — идентификатор
            владельца медиа-приложения  <media_id> — идентификатор медиа-приложения.
            Например:photo100172_166443618,photo66748_265827614  Параметр является обязательным, если не задан
            параметр text.

        :return: В случае успеха возвращает идентификатор созданной темы
        """

        params = locals()
        method_name = self._base_method + 'addTopic'
        return self._call(method_name, params)

    def closeTopic(self, group_id: str = None, topic_id: str = None) -> dict:
        """
        Закрывает тему в списке обсуждений группы (в такой теме невозможно оставлять новые сообщения).

        :param group_id: идентификатор сообщества, в котором размещено обсуждение.
        :param topic_id: идентификатор обсуждения.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'closeTopic'
        return self._call(method_name, params)

    def createComment(self, group_id: str = None, topic_id: str = None, message: str = None, attachments: str = None,
                      from_group: str = None, sticker_id: str = None, guid: str = None) -> dict:
        """
        Добавляет новый комментарий в обсуждении.

        :param group_id: идентификатор сообщества, в котором находится обсуждение.
        :param topic_id: идентификатор темы, в которой необходимо оставить комментарий.
        :param message: текст комментария. Обязательный параметр, если не передано значение attachments.
        :param attachments: Список объектов, приложенных к комментарию и разделённых символом ",". Поле
            attachments представляется в формате: <type><owner_id>_<media_id>,<type><owner_id>_<media_id>  <type> —
            тип медиа-вложения: photo — фотография; video — видеозапись; audio — аудиозапись; doc — документ;
            <owner_id> — идентификатор владельца медиа-вложения; <media_id> — идентификатор медиа-вложения.
            Например: photo100172_166443618,photo66748_265827614
        :param from_group: 1 — сообщение будет опубликовано от имени группы, 0 — сообщение будет опубликовано от
            имени пользователя (по умолчанию).
        :param sticker_id: идентификатор стикера.
        :param guid: уникальный идентификатор, предназначенный для предотвращения повторной отправки одинакового
            комментария.

        :return: В случае успеха возвращает идентификатор созданного комментария
        """

        params = locals()
        method_name = self._base_method + 'createComment'
        return self._call(method_name, params)

    def deleteComment(self, group_id: str = None, topic_id: str = None, comment_id: str = None) -> dict:
        """
        Удаляет сообщение темы в обсуждениях сообщества.

        :param group_id: идентификатор сообщества.
        :param topic_id: идентификатор обсуждения.
        :param comment_id: идентификатор комментария в обсуждении.

        :return: После успешного выполнения, а также в том случае, если комментарий уже удален, возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'deleteComment'
        return self._call(method_name, params)

    def deleteTopic(self, group_id: str = None, topic_id: str = None) -> dict:
        """
        Удаляет тему в обсуждениях группы.

        :param group_id: идентификатор сообщества, в котором размещено обсуждение.
        :param topic_id: идентификатор обсуждения.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'deleteTopic'
        return self._call(method_name, params)

    def editComment(self, group_id: str = None, topic_id: str = None, comment_id: str = None, message: str = None,
                    attachments: str = None) -> dict:
        """
        Редактирует одно из сообщений в обсуждении сообщества.

        :param group_id: идентификатор сообщества, в котором размещено обсуждение.
        :param topic_id: идентификатор обсуждения.
        :param comment_id: идентификатор комментария в обсуждении.
        :param message: новый текст комментария (является обязательным, если не задан параметр attachments).
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

    def editTopic(self, group_id: str = None, topic_id: str = None, title: str = None) -> dict:
        """
        Изменяет заголовок темы в списке обсуждений группы.

        :param group_id: идентификатор сообщества, в котором размещено обсуждение.
        :param topic_id: идентификатор обсуждения.
        :param title: новое название обсуждения.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'editTopic'
        return self._call(method_name, params)

    def fixTopic(self, group_id: str = None, topic_id: str = None) -> dict:
        """
        Закрепляет тему в списке обсуждений группы (такая тема при любой сортировке выводится выше остальных).

        :param group_id: идентификатор сообщества, в котором размещено обсуждение.
        :param topic_id: идентификатор обсуждения.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'fixTopic'
        return self._call(method_name, params)

    def getComments(self, group_id: str = None, topic_id: str = None, need_likes: str = None,
                    start_comment_id: str = None, offset: str = None, count: str = None, extended: str = None,
                    sort: str = None) -> dict:
        """
        Возвращает список сообщений в указанной теме.

        :param group_id: идентификатор сообщества, информацию об обсуждениях которого нужно получить.
        :param topic_id: идентификатор обсуждения.
        :param need_likes: 1 — будет возвращено дополнительное поле likes. По умолчанию поле likes не
            возвращается.
        :param start_comment_id: идентификатор комментария, начиная с которого нужно вернуть список (подробности
            см. ниже).
        :param offset: смещение, необходимое для выборки определенного подмножества сообщений.
        :param count: количество сообщений, которое необходимо получить (но не более 100). По умолчанию — 20.
        :param extended: Если указать в качестве этого параметра 1, то будет возвращена информация о
            пользователях, являющихся авторами сообщений. По умолчанию 0.
        :param sort: порядок сортировки комментариев: asc — хронологический desc — антихронологический

        :return: В случае успеха возвращает объект, содержащий поле items, поле poll, если к теме прикреплен
            опрос, а также поле profiles (если был указан параметр extended).  Поле items представляет собой массив,
            содержащий объекты, описывающие комментарии.  Если к теме был прикреплен опрос, возвращается поле poll
            следующего вида:   owner_id — идентификатор владельца опроса  poll_id — идентификатор опроса;  created —
            время создания опроса в формате unixtime;  is_closed — 1, если опрос закрыт (в нем больше нельзя
            принимать участие) или 0 в противном случае;  question — текст вопроса для опроса;  votes — общее
            количество ответивших пользователей;  answer_id — идентификатор ответа текущего пользователя (если
            текущий пользователь еще не отвечал в данном опросе, то содержит 0);  answers — массив, содержащий
            объекты с вариантами ответа на вопрос в опросе:   id — идентификатор ответа на вопрос;  text — текст
            ответа на вопрос;  votes — количество пользователей, проголосовавших за данный вариант ответа;  rate —
            рейтинг данного варианта ответа, выраженный в процентах.    В случае передачи параметра extended равным
            1, поле profiles содержит массив объектов user с информацией о данных пользователей, являющихся авторами
            сообщений.  Если был передан параметр start_comment_id, будет также возвращено поле real_offset –
            итоговое смещение данного подмножества комментариев (оно может быть отрицательным, если был указан
            отрицательный offset)
        """

        params = locals()
        method_name = self._base_method + 'getComments'
        return self._call(method_name, params)

    def getTopics(self, group_id: str = None, topic_ids: str = None, order: str = None, offset: str = None,
                  count: str = None, extended: str = None, preview: str = None, preview_length: str = None) -> dict:
        """
        Возвращает список тем в обсуждениях указанной группы.

        :param group_id: идентификатор сообщества, информацию об обсуждениях которого необходимо получить. Если
            сообщество закрытое или частное, для вызова метода потребуется право доступа groups.
        :param topic_ids: список идентификаторов тем, которые необходимо получить (не более 100). По умолчанию
            возвращаются все темы. Если указан данный параметр, игнорируются параметры order, offset и count
            (возвращаются все запрошенные темы в указанном порядке).
        :param order: Порядок, в котором необходимо вернуть список тем. Возможные значения:   1 — по убыванию
            даты обновления;  2 — по убыванию даты создания;  -1 — по возрастанию даты обновления;  -2 — по
            возрастанию даты создания.  По умолчанию темы возвращаются в порядке, установленном администратором
            группы. "Прилепленные" темы при любой сортировке возвращаются первыми в списке.
        :param offset: смещение, необходимое для выборки определенного подмножества тем.
        :param count: количество тем, которое необходимо получить (но не более 100). По умолчанию — 40.
        :param extended: Если указать в качестве этого параметра 1, то будет возвращена информация о
            пользователях, являющихся создателями тем или оставившими в них последнее сообщение. По умолчанию 0.
        :param preview: Набор флагов, определяющий, необходимо ли вернуть вместе с информацией о темах текст
            первых и последних сообщений в них. Является суммой флагов:   1 — вернуть первое сообщение в каждой теме
            (поле first_comment);  2 — вернуть последнее сообщение в каждой теме (поле last_comment). По умолчанию —
            0 (не возвращать текст сообщений).
        :param preview_length: Количество символов, по которому нужно обрезать первое и последнее сообщение.
            Укажите 0, если Вы не хотите обрезать сообщение. (по умолчанию — 90).

        :return: После успешного выполнения возвращает объект, содержащий следующие поля:  count integer число
            результатов. items array массив объектов, описывающих обсуждения. default_order integer тип сортировки
            обсуждений в сообществе. Возможные значения:   1 — по убыванию даты обновления;  2 — по убыванию даты
            создания;  -1 — по возрастанию даты обновления;  -2 — по возрастанию даты создания. can_add_topics
            integer, [0,1] информация о том, может ли текущий пользователь создать обсуждение в сообществе. Возможные
            значения:   0 — не может;  1 — может. profiles array (только для extended = 1). Массив объектов,
            описывающих пользователей. Каждый из объектов содержит базовые поля, а также поля sex, photo_50,
            photo_100, online и type (= profile)
        """

        params = locals()
        method_name = self._base_method + 'getTopics'
        return self._call(method_name, params)

    def openTopic(self, group_id: str = None, topic_id: str = None) -> dict:
        """
        Открывает ранее закрытую тему (в ней станет возможно оставлять новые сообщения).

        :param group_id: идентификатор сообщества, в котором размещено обсуждение.
        :param topic_id: идентификатор обсуждения.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'openTopic'
        return self._call(method_name, params)

    def restoreComment(self, group_id: str = None, topic_id: str = None, comment_id: str = None) -> dict:
        """
        Восстанавливает удаленное сообщение темы в обсуждениях группы.

        :param group_id: идентификатор сообщества, в котором размещено обсуждение.
        :param topic_id: идентификатор обсуждения.
        :param comment_id: идентификатор комментария.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'restoreComment'
        return self._call(method_name, params)

    def unfixTopic(self, group_id: str = None, topic_id: str = None) -> dict:
        """
        Отменяет прикрепление темы в списке обсуждений группы (тема будет выводиться согласно выбранной сортировке).

        :param group_id: идентификатор сообщества, в котором размещено обсуждение.
        :param topic_id: идентификатор обсуждения.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'unfixTopic'
        return self._call(method_name, params)
