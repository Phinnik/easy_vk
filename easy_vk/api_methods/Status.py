from .ApiMethod import ApiMethod


class Status(ApiMethod):
    def __init__(self, access_token, v, session, calls_per_second):
        super(Status, self).__init__(access_token, v, session, calls_per_second)
        self._base_method = 'status.'

    def get(self, user_id: str = None, group_id: str = None) -> dict:
        """
        Получает текст статуса пользователя или сообщества.

        :param user_id: идентификатор пользователя или сообщества, информацию о статусе которого нужно получить.
        :param group_id: идентификатор сообщества, статус которого необходимо получить.

        :return: В случае успеха возвращает объект, у которого в поле text содержится текст статуса пользователя
            или сообщества.  Если у пользователя включена трансляция играющей музыки в статус и в данный момент
            воспроизводится аудиозапись, то также будет возвращен объект audio
        """

        params = locals()
        method_name = self._base_method + 'get'
        return self._call(method_name, params)

    def set(self, text: str = None, group_id: str = None) -> dict:
        """
        Устанавливает новый статус текущему пользователю или сообществу.

        :param text: текст нового статуса.
        :param group_id: идентификатор сообщества, в котором будет установлен статус. По умолчанию статус
            устанавливается текущему пользователю.

        :return: В случае успешной установки или очистки статуса возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'set'
        return self._call(method_name, params)
