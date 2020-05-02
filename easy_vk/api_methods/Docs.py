from .ApiMethod import ApiMethod


class Docs(ApiMethod):
    def __init__(self, access_token, v, session, calls_per_second):
        super(Docs, self).__init__(access_token, v, session, calls_per_second)
        self._base_method = 'docs.'


    def add(self, owner_id: str = None, doc_id: str = None, access_key: str = None) -> dict:
        """
        Копирует документ в документы текущего пользователя.

        :param owner_id: идентификатор пользователя или сообщества, которому принадлежит документ.  Обратите
            внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком "-" — например,
            owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)
        :param doc_id: идентификатор документа.
        :param access_key: ключ доступа документа. Этот параметр следует передать, если вместе с остальными
            данными о документе было возвращено поле access_key.

        :return: После успешного выполнения возвращает идентификатор созданного документа
        """

        params = locals()
        method_name = self._base_method + 'add'
        return self._call(method_name, params)

    def delete(self, owner_id: str = None, doc_id: str = None) -> dict:
        """
        Удаляет документ пользователя или группы.

        :param owner_id: идентификатор пользователя или сообщества, которому принадлежит документ.  Обратите
            внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком "-" — например,
            owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)
        :param doc_id: идентификатор документа.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'delete'
        return self._call(method_name, params)

    def edit(self, owner_id: str = None, doc_id: str = None, title: str = None, tags: str = None) -> dict:
        """
        Редактирует документ пользователя или группы.

        :param owner_id: идентификатор пользователя или сообщества, которому принадлежит документ.  Обратите
            внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком "-" — например,
            owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)
        :param doc_id: идентификатор документа.
        :param title: название документа.
        :param tags: метки для поиска.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'edit'
        return self._call(method_name, params)

    def get(self, count: str = None, offset: str = None, type: str = None, owner_id: str = None,
            return_tags: str = None) -> dict:
        """
        Возвращает расширенную информацию о документах пользователя или сообщества.

        :param count: количество документов, информацию о которых нужно вернуть.  По умолчанию: все документы.
            Максимальное количество документов, которое можно получить: 2000.
        :param offset: смещение, необходимое для выборки определенного подмножества документов. Максимальное
            значение: 1999.
        :param type: фильтр по типу документа.  Возможные варианты:   1 — текстовые документы;  2 — архивы;  3 —
            gif;  4 — изображения;  5 — аудио;  6 — видео;  7 — электронные книги;  8 — неизвестно.
        :param owner_id: идентификатор пользователя или сообщества, которому принадлежат документы.  Обратите
            внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком "-" — например,
            owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)
        :param return_tags:

        :return: После успешного выполнения возвращает объект, содержащий число результатов в поле count и массив
            объектов документов в поле items
        """

        params = locals()
        method_name = self._base_method + 'get'
        return self._call(method_name, params)

    def getById(self, docs: str = None, return_tags: str = None) -> dict:
        """
        Возвращает информацию о документах по их идентификаторам.

        :param docs: идентификаторы документов, информацию о которых нужно вернуть. Пример значения docs:
            66748_91488,66748_91455.  Метод поддерживает передачу access_key.
        :param return_tags:

        :return: После успешного выполнения возвращает объект, содержащий число результатов в поле count и массив
            объектов документов в поле items
        """

        params = locals()
        method_name = self._base_method + 'getById'
        return self._call(method_name, params)

    def getMessagesUploadServer(self, type: str = None, peer_id: str = None) -> dict:
        """
        Получает адрес сервера для загрузки документа в личное сообщение.

        :param type: тип документа. Возможные значения:   doc — обычный документ;  audio_message — голосовое
            сообщение;  graffiti — граффити.
        :param peer_id: идентификатор назначения.  Для пользователя:  id пользователя.   Для групповой беседы:
            2000000000 + id беседы.   Для сообщества:  -id сообщества.

        :return: Возвращает объект с единственным полем upload_url (string), содержащим адрес сервера для
            загрузки документа
        """

        params = locals()
        method_name = self._base_method + 'getMessagesUploadServer'
        return self._call(method_name, params)

    def getTypes(self, owner_id: str = None) -> dict:
        """
        Возвращает доступные для пользователя типы документов.

        :param owner_id: идентификатор пользователя или сообщества, которому принадлежат документы.

        :return: После успешного выполнения возвращает список объектов type с полями, описанными ниже:  id
            integer идентификатор типа. name  string название типа. count   integer число документов
        """

        params = locals()
        method_name = self._base_method + 'getTypes'
        return self._call(method_name, params)

    def getUploadServer(self, group_id: str = None) -> dict:
        """
        Возвращает адрес сервера для загрузки документов.

        :param group_id: идентификатор сообщества (если необходимо загрузить документ в список документов
            сообщества). Если документ нужно загрузить в список пользователя, метод вызывается без дополнительных
            параметров.

        :return: Возвращает объект с полем upload_url, содержащим адрес для загрузки файла. После успешной
            загрузки документа необходимо воспользоваться методом docs.save
        """

        params = locals()
        method_name = self._base_method + 'getUploadServer'
        return self._call(method_name, params)

    def getWallUploadServer(self, group_id: str = None) -> dict:
        """
        Возвращает адрес сервера для загрузки документов в папку Отправленные, для последующей отправки документа на
        стену или личным сообщением.

        :param group_id: идентификатор сообщества, в которое нужно загрузить документ.

        :return: Возвращает объект с полем upload_url. После успешной загрузки документа необходимо
            воспользоваться методом docs.save
        """

        params = locals()
        method_name = self._base_method + 'getWallUploadServer'
        return self._call(method_name, params)

    def save(self, file: str = None, title: str = None, tags: str = None, return_tags: str = None) -> dict:
        """
        Сохраняет документ после его успешной загрузки на сервер.

        :param file: параметр, возвращаемый в результате загрузки файла на сервер.
        :param title: название документа.
        :param tags: метки для поиска.
        :param return_tags:

        :return: После успешного выполнения возвращает массив объектов, описывающих загруженные документы. Каждый
            объект массива содержит поле type (string) с возможными значениями graffiti, audio_message, doc, и
            одноименный объект, описывающий загруженный документ.  Для type = graffiti объект graffiti, описывающий
            граффити.  Для type = audio_message объект audio_message, описывающий голосовое сообщение.  Для type =
            doc объект doc, описывающий другие типы документов
        """

        params = locals()
        method_name = self._base_method + 'save'
        return self._call(method_name, params)

    def search(self, q: str = None, search_own: str = None, count: str = None, offset: str = None,
               return_tags: str = None) -> dict:
        """
        Возвращает результаты поиска по документам.

        :param q: строка поискового запроса. Например, зеленые тапочки.
        :param search_own: 1 — искать среди собственных документов пользователя.
        :param count: количество документов, информацию о которых нужно вернуть. Обратите внимание — даже при
            использовании параметра offset для получения информации доступны только первые 1000 результатов.
        :param offset: смещение, необходимое для выборки определенного подмножества документов.
        :param return_tags:

        :return: После успешного выполнения возвращает список объектов документов.  Если установлен флаг
            search_own, в поле local дополнительно вернется список документов из локального поиска
        """

        params = locals()
        method_name = self._base_method + 'search'
        return self._call(method_name, params)

