from ApiMethod import ApiMethod


class Notes(ApiMethod):
    def __init__(self, access_token, v, session, calls_per_second):
        super(Notes, self).__init__(access_token, v, session, calls_per_second)
        self._base_method = 'notes.'

    def add(self, title: str = None, text: str = None, privacy_view: str = None, privacy_comment: str = None) -> dict:
        """
        Создает новую заметку у текущего пользователя.

        :param title: заголовок заметки.
        :param text: текст заметки.
        :param privacy_view: настройки приватности просмотра заметки в специальном формате.
        :param privacy_comment: настройки приватности комментирования заметки в специальном формате.

        :return: После успешного выполнения возвращает идентификатор созданной заметки (nid)
        """

        params = locals()
        method_name = self._base_method + 'add'
        return self._call(method_name, params)

    def createComment(self, note_id: str = None, owner_id: str = None, reply_to: str = None, message: str = None,
                      guid: str = None) -> dict:
        """
        Добавляет новый комментарий к заметке.

        :param note_id: идентификатор заметки.
        :param owner_id: идентификатор владельца заметки.
        :param reply_to: идентификатор пользователя, ответом на комментарий которого является добавляемый
            комментарий (не передаётся, если комментарий не является ответом).
        :param message: текст комментария.
        :param guid: уникальный идентификатор, предназначенный для предотвращения повторной отправки одинакового
            комментария.

        :return: После успешного выполнения возвращает идентификатор созданного комментария (cid)
        """

        params = locals()
        method_name = self._base_method + 'createComment'
        return self._call(method_name, params)

    def delete(self, note_id: str = None) -> dict:
        """
        Удаляет заметку текущего пользователя.

        :param note_id: идентификатор заметки.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'delete'
        return self._call(method_name, params)

    def deleteComment(self, comment_id: str = None, owner_id: str = None) -> dict:
        """
        Удаляет комментарий к заметке.

        :param comment_id: идентификатор комментария.
        :param owner_id: идентификатор владельца заметки.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'deleteComment'
        return self._call(method_name, params)

    def edit(self, note_id: str = None, title: str = None, text: str = None, privacy_view: str = None,
             privacy_comment: str = None) -> dict:
        """
        Редактирует заметку текущего пользователя.

        :param note_id: идентификатор заметки.
        :param title: заголовок заметки.
        :param text: текст заметки.
        :param privacy_view: настройки приватности просмотра заметки в специальном формате.
        :param privacy_comment: настройки приватности комментирования заметки в специальном формате.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'edit'
        return self._call(method_name, params)

    def editComment(self, comment_id: str = None, owner_id: str = None, message: str = None) -> dict:
        """
        Редактирует указанный комментарий у заметки.

        :param comment_id: идентификатор комментария.
        :param owner_id: идентификатор владельца заметки.
        :param message: новый текст комментария.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'editComment'
        return self._call(method_name, params)

    def get(self, note_ids: str = None, user_id: str = None, offset: str = None, count: str = None,
            sort: str = None) -> dict:
        """
        Возвращает список заметок, созданных пользователем.

        :param note_ids: идентификаторы заметок, информацию о которых необходимо получить.
        :param user_id: идентификатор пользователя, информацию о заметках которого требуется получить.
        :param offset: смещение, необходимое для выборки определенного подмножества заметок.
        :param count: количество заметок, информацию о которых необходимо получить.
        :param sort: сортировка результатов (0 — по дате создания в порядке убывания, 1 - по дате создания в
            порядке возрастания).

        :return: После успешного выполнения возвращает список объектов заметок
        """

        params = locals()
        method_name = self._base_method + 'get'
        return self._call(method_name, params)

    def getById(self, note_id: str = None, owner_id: str = None, need_wiki: str = None) -> dict:
        """
        Возвращает заметку по её id.

        :param note_id: идентификатор заметки.
        :param owner_id: идентификатор владельца заметки.
        :param need_wiki: определяет, требуется ли в ответе wiki-представление заметки (работает, только если
            запрашиваются заметки текущего пользователя).

        :return: После успешного выполнения возвращает список объектов заметок с дополнительными полями:
            privacy — уровень доступа к заметке (0 — все пользователи, 1 — только друзья, 2 — друзья и друзья друзей,
            3 — только пользователь);  comment_privacy — уровень доступа к комментированию заметки (0 — все
            пользователи, 1 — только друзья, 2 — друзья и друзья друзей, 3 — только пользователь);  can_comment —
            может ли текущий пользователь комментировать заметку (1 — может, 0 — не может)
        """

        params = locals()
        method_name = self._base_method + 'getById'
        return self._call(method_name, params)

    def getComments(self, note_id: str = None, owner_id: str = None, sort: str = None, offset: str = None,
                    count: str = None) -> dict:
        """
        Возвращает список комментариев к заметке.

        :param note_id: идентификатор заметки.
        :param owner_id: идентификатор владельца заметки.
        :param sort: сортировка результатов (0 — по дате добавления в порядке возрастания, 1 — по дате добавления
            в порядке убывания).
        :param offset: смещение, необходимое для выборки определенного подмножества комментариев.
        :param count: количество комментариев, которое необходимо получить.

        :return: Возвращает массив объектов comment, каждый из которых содержит следующие поля:   id —
            идентификатор комментария;  uid — идентификатор автора комментария;  nid — идентификатор заметки;  oid —
            идентификатор владельца заметки;  date — дата добавления комментария в формате unixtime;  message — текст
            комментария;  reply_to — идентификатор пользователя, в ответ на комментарий которого был оставлен текущий
            комментарий (если доступно)
        """

        params = locals()
        method_name = self._base_method + 'getComments'
        return self._call(method_name, params)

    def restoreComment(self, comment_id: str = None, owner_id: str = None) -> dict:
        """
        Восстанавливает удалённый комментарий.

        :param comment_id: идентификатор удаленного комментария.
        :param owner_id: идентификатор владельца заметки.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'restoreComment'
        return self._call(method_name, params)

