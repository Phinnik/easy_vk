from ApiMethod import ApiMethod


class Video(ApiMethod):
    def __init__(self, access_token, v, session, calls_per_second):
        super(Video, self).__init__(access_token, v, session, calls_per_second)
        self._base_method = 'video.'

    def add(self, target_id: str = None, video_id: str = None, owner_id: str = None) -> dict:
        """
        Добавляет видеозапись в список пользователя.

        :param target_id: идентификатор пользователя или сообщества, в которое нужно добавить видео.  Обратите
            внимание, идентификатор сообщества в параметре target_id необходимо указывать со знаком "-" — например,
            target_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)
        :param video_id: идентификатор видеозаписи.
        :param owner_id: идентификатор пользователя или сообщества, которому принадлежит видеозапись. Обратите
            внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком "-" — например,
            owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'add'
        return self._call(method_name, params)

    def addAlbum(self, group_id: str = None, title: str = None, privacy: str = None) -> dict:
        """
        Создает пустой альбом видеозаписей.

        :param group_id: идентификатор сообщества (если необходимо создать альбом в сообществе).
        :param title: название альбома.
        :param privacy: настройки доступа к альбому в специальном формате.  Приватность доступна для альбомов с
            видео в профиле пользователя.

        :return: После успешного выполнения возвращает идентификатор созданного альбома в поле album_id
        """

        params = locals()
        method_name = self._base_method + 'addAlbum'
        return self._call(method_name, params)

    def addToAlbum(self, target_id: str = None, album_id: str = None, album_ids: str = None, owner_id: str = None,
                   video_id: str = None) -> dict:
        """
        Позволяет добавить видеозапись в альбом.

        :param target_id: идентификатор владельца альбома, в который нужно добавить видео.  Обратите внимание,
            идентификатор сообщества в параметре target_id необходимо указывать со знаком "-" — например,
            target_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)
        :param album_id: идентификатор альбома, в который нужно добавить видео.  Для добавления видео в общий
            альбом «Добавленные» передавайте -2.
        :param album_ids: идентификаторы альбомов, в которые нужно добавить видео.
        :param owner_id: идентификатор владельца видеозаписи.  Обратите внимание, идентификатор сообщества в
            параметре owner_id необходимо указывать со знаком "-" — например, owner_id=-1 соответствует
            идентификатору сообщества ВКонтакте API (club1)
        :param video_id: идентификатор видеозаписи.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'addToAlbum'
        return self._call(method_name, params)

    def createComment(self, owner_id: str = None, video_id: str = None, message: str = None, attachments: str = None,
                      from_group: str = None, reply_to_comment: str = None, sticker_id: str = None,
                      guid: str = None) -> dict:
        """
        Cоздает новый комментарий к видеозаписи

        :param owner_id: идентификатор пользователя или сообщества, которому принадлежит видеозапись. Обратите
            внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком "-" — например,
            owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)
        :param video_id: идентификатор видеозаписи.
        :param message: текст комментария. Обязательный параметр, если не задан параметр attachments.
        :param attachments: список объектов, приложенных к комментарию и разделённых символом ",". Поле
            attachments представляется в формате: <type><owner_id>_<media_id>,<type><owner_id>_<media_id> <type> —
            тип медиа-вложения: photo — фотография  video — видеозапись  audio — аудиозапись  doc — документ
            <owner_id> — идентификатор владельца медиа-вложения  <media_id> — идентификатор медиа-вложения.
            Например: photo100172_166443618,photo66748_265827614 Параметр является обязательным, если не задан
            параметр message.
        :param from_group: этот параметр учитывается, если owner_id < 0 (комментарий к видеозаписи группы). 1 —
            комментарий будет опубликован от имени группы, 0 — комментарий будет опубликован от имени пользователя.
            по умолчанию: 0.
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

    def delete(self, video_id: str = None, owner_id: str = None, target_id: str = None) -> dict:
        """
        Удаляет видеозапись со страницы пользователя.

        :param video_id: идентификатор видеозаписи.
        :param owner_id: идентификатор пользователя или сообщества, которому принадлежит видеозапись. Обратите
            внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком "-" — например,
            owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)
        :param target_id: идентификатор пользователя или сообщества, для которого нужно удалить видеозапись.
            Обратите внимание, идентификатор сообщества в параметре target_id необходимо указывать со знаком "-" —
            например, target_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'delete'
        return self._call(method_name, params)

    def deleteAlbum(self, group_id: str = None, album_id: str = None) -> dict:
        """
        Удаляет альбом видеозаписей.

        :param group_id: идентификатор сообщества (если альбом, который необходимо удалить, принадлежит
            сообществу).
        :param album_id: идентификатор альбома.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'deleteAlbum'
        return self._call(method_name, params)

    def deleteComment(self, owner_id: str = None, comment_id: str = None) -> dict:
        """
        Удаляет комментарий к видеозаписи.

        :param owner_id: идентификатор пользователя или сообщества, которому принадлежит видеозапись.
        :param comment_id: идентификатор комментария.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'deleteComment'
        return self._call(method_name, params)

    def edit(self, owner_id: str = None, video_id: str = None, name: str = None, desc: str = None,
             privacy_view: str = None, privacy_comment: str = None, no_comments: str = None,
             repeat: str = None) -> dict:
        """
        Редактирует данные видеозаписи.

        :param owner_id: идентификатор пользователя или сообщества, которому принадлежит видеозапись. Обратите
            внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком "-" — например,
            owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)
        :param video_id: идентификатор видеозаписи.
        :param name: новое название для видеозаписи.
        :param desc: новое описание для видеозаписи.
        :param privacy_view: настройки приватности просмотра видеозаписи в специальном формате. Приватность
            доступна для видеозаписей, которые пользователь загрузил в профиль.
        :param privacy_comment: настройки приватности комментирования видеозаписи в специальном формате.
            Приватность доступна для видеозаписей, которые пользователь загрузил в профиль.
        :param no_comments: закрыть комментарии (для видео из сообществ).
        :param repeat: зацикливание воспроизведения видеозаписи.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'edit'
        return self._call(method_name, params)

    def editAlbum(self, group_id: str = None, album_id: str = None, title: str = None, privacy: str = None) -> dict:
        """
        Редактирует альбом с видео.

        :param group_id: идентификатор сообщества (если нужно отредактировать альбом, принадлежащий сообществу).
        :param album_id: идентификатор альбома.
        :param title: новое название для альбома.
        :param privacy: уровень доступа к альбому в специальном формате.  Приватность доступна для альбомов с
            видео в профиле пользователя.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'editAlbum'
        return self._call(method_name, params)

    def editComment(self, owner_id: str = None, comment_id: str = None, message: str = None,
                    attachments: str = None) -> dict:
        """
        Изменяет текст комментария к видеозаписи.

        :param owner_id: идентификатор пользователя или сообщества, которому принадлежит видеозапись. Обратите
            внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком "-" — например,
            owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)
        :param comment_id: идентификатор комментария.
        :param message: новый текст комментария. Обязательный параметр, если не задан параметр attachments.
        :param attachments: новый список объектов, приложенных к комментарию и разделённых символом ",". Поле
            attachments представляется в формате: <type><owner_id>_<media_id>,<type><owner_id>_<media_id> <type> —
            тип медиа-вложения: photo — фотография  video — видеозапись  audio — аудиозапись  doc — документ
            <owner_id> — идентификатор владельца медиа-вложения  <media_id> — идентификатор медиа-вложения.
            Например: photo100172_166443618,photo66748_265827614 Обязательный параметр, если не задан параметр
            message.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'editComment'
        return self._call(method_name, params)

    def get(self, owner_id: str = None, videos: str = None, album_id: str = None, count: str = None, offset: str = None,
            extended: str = None) -> dict:
        """
        Возвращает информацию о видеозаписях.

        :param owner_id: идентификатор пользователя или сообщества, которому принадлежат видеозаписи. Обратите
            внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком "-" — например,
            owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)
        :param videos: перечисленные через запятую идентификаторы — идущие через знак подчеркивания id
            пользователей, которым принадлежат видеозаписи, и id самих видеозаписей. Если видеозапись принадлежит
            сообществу, то в качестве первого параметра используется -id сообщества. Пример значения videos:
            -4363_136089719,13245770_137352259  Некоторые видеозаписи, идентификаторы которых могут быть получены
            через API, закрыты приватностью, и не будут получены. В этом случае следует использовать ключ доступа
            access_key в её идентификаторе. Пример значения videos:   1_129207899_220df2876123d3542f,
            6492_135055734_e0a9bcc31144f67fbd  Поле access_key будет возвращено вместе с остальными данными
            видеозаписи в методах, которые возвращают видеозаписи, закрытые приватностью, но доступные в данном
            контексте. Например, данное поле имеют видеозаписи, возвращаемые методом messages.get.
        :param album_id: идентификатор альбома, видеозаписи из которого нужно вернуть.
        :param count: количество возвращаемых видеозаписей.
        :param offset: смещение относительно первой найденной видеозаписи для выборки определенного подмножества.
        :param extended: определяет, возвращать ли информацию о настройках приватности видео для текущего
            пользователя.

        :return: После успешного выполнения возвращает объект, содержащий число результатов в поле count и массив
            объектов видеозаписей с дополнительным полем comments, содержащим число комментариев у видеозаписи, в
            поле items.  Если был задан параметр extended=1, возвращаются дополнительные поля:   privacy_view —
            настройки приватности в формате настроек приватности; (приходит только для текущего пользователя)
            privacy_comment — настройки приватности в формате настроек приватности; (приходит только для текущего
            пользователя)  can_comment — может ли текущий пользователь оставлять комментарии к ролику (1 — может, 0 —
            не может);  can_repost — может ли текущий пользователь скопировать ролик с помощью функции «Рассказать
            друзьям» (1 — может, 0 — не может);  likes — информация об отметках «Мне нравится»:   user_likes — есть
            ли отметка «Мне нравится» от текущего пользователя;  count — число отметок «Мне нравится»;   repeat —
            зацикливание воспроизведения видеозаписи (1 — зацикливается, 0 — не зацикливается).   Если в Вашем
            приложении используется прямая авторизация, возвращается дополнительное поле files, содержащее ссылку на
            файл с видео (если ролик размещен на сервере ВКонтакте) или ссылку на внешний ресурс (если ролик встроен
            с какого-либо видеохостинга)
        """

        params = locals()
        method_name = self._base_method + 'get'
        return self._call(method_name, params)

    def getAlbumById(self, owner_id: str = None, album_id: str = None) -> dict:
        """
        Позволяет получить информацию об альбоме с видео.

        :param owner_id: идентификатор пользователя или сообщества, которому принадлежит альбом.
        :param album_id: идентификатор альбома.

        :return: После успешного выполнения возвращает объект, который содержит следующие поля:   id —
            идентификатор альбома;  owner_id — идентификатор владельца альбома;  title — название альбома;  count —
            число видеозаписей в альбоме;  photo_320 — url обложки альбома с шириной 320px;  photo_160 — url обложки
            альбома с шириной 160px;  updated_time — время последнего обновления в формате unixtime
        """

        params = locals()
        method_name = self._base_method + 'getAlbumById'
        return self._call(method_name, params)

    def getAlbums(self, owner_id: str = None, offset: str = None, count: str = None, extended: str = None,
                  need_system: str = None) -> dict:
        """
        Возвращает список альбомов видеозаписей пользователя или сообщества.

        :param owner_id: идентификатор владельца альбомов (пользователь или сообщество). По умолчанию —
            идентификатор текущего пользователя.
        :param offset: смещение, необходимое для выборки определенного подмножества альбомов. По умолчанию: 0.
        :param count: количество альбомов, информацию о которых нужно вернуть. По умолчанию: не больше 50,
            максимальное значение: 100.
        :param extended: 1— возвращать дополнительные поля count, photo_320, photo_160 и updated_time для каждого
            альбома. Если альбом пустой, то поля photo_320 и photo_160 возвращены не будут. По умолчанию: 0.
        :param need_system: 1 — возвращать системные альбомы.

        :return: После успешного выполнения возвращает объект, содержащий число результатов в поле count и массив
            объектов альбомов в поле items. Каждый из объектов, описывающих альбом, содержит следующие поля:   id —
            идентификатор альбома;  owner_id — идентификатор владельца альбома;  title — название альбома
        """

        params = locals()
        method_name = self._base_method + 'getAlbums'
        return self._call(method_name, params)

    def getAlbumsByVideo(self, target_id: str = None, owner_id: str = None, video_id: str = None,
                         extended: str = None) -> dict:
        """
        Возвращает список альбомов, в которых находится видеозапись.

        :param target_id: идентификатор пользователя или сообщества, для которого нужно получить список альбомов,
            содержащих видеозапись.  Обратите внимание, идентификатор сообщества в параметре target_id необходимо
            указывать со знаком "-" — например, target_id=-1 соответствует идентификатору сообщества ВКонтакте API
            (club1)
        :param owner_id: идентификатор владельца видеозаписи.  Обратите внимание, идентификатор сообщества в
            параметре owner_id необходимо указывать со знаком "-" — например, owner_id=-1 соответствует
            идентификатору сообщества ВКонтакте API (club1)
        :param video_id: идентификатор видеозаписи.
        :param extended: 1 — возвращать расширенную информацию об альбомах.

        :return: Возвращает список идентификаторов альбомов, в которых видеозапись находится у пользователя или
            сообщества с идентификатором target_id. Если был передан параметр extended=1, возвращается список
            объектов альбомов с дополнительной информацией о каждом из них
        """

        params = locals()
        method_name = self._base_method + 'getAlbumsByVideo'
        return self._call(method_name, params)

    def getComments(self, owner_id: str = None, video_id: str = None, need_likes: str = None,
                    start_comment_id: str = None, offset: str = None, count: str = None, sort: str = None,
                    extended: str = None, fields: str = None) -> dict:
        """
        Возвращает список комментариев к видеозаписи.

        :param owner_id: идентификатор пользователя или сообщества, которому принадлежит видеозапись. Обратите
            внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком "-" — например,
            owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)
        :param video_id: идентификатор видеозаписи.
        :param need_likes: 1 — будет возвращено дополнительное поле likes. По умолчанию поле likes не
            возвращается.
        :param start_comment_id: идентификатор комментария, начиная с которого нужно вернуть список (подробности
            см. ниже).
        :param offset: смещение, необходимое для выборки определенного подмножества комментариев. По умолчанию:
            0.
        :param count: количество комментариев, информацию о которых необходимо вернуть.
        :param sort: порядок сортировки комментариев. Возможные значения:   asc — от старых к новым;  desc — от
            новых к старым.
        :param extended: 1 — в ответе будут возвращены дополнительные поля profiles и groups, содержащие
            информацию о пользователях и сообществах. По умолчанию: 0.
        :param fields:

        :return: После успешного выполнения возвращает объект, содержащий число результатов в поле count и массив
            объектов комментариев в поле items. Каждый объект, описывающий комментарий, содержит следующие поля:   id
            — идентификатор комментария;  from_id — идентификатор автора комментария;  date — дата добавления
            комментария в формате unixtime;  text — текст комментария;  likes — информация об отметках «Мне нравится»
            текущего комментария (если был задан параметр need_likes), объект с полями:   count — число
            пользователей, которым понравился комментарий,  user_likes — наличие отметки «Мне нравится» от текущего
            пользователя  (1 — есть, 0 — нет),  can_like — информация о том, может ли текущий пользователь поставить
            отметку «Мне нравится»  (1 — может, 0 — не может).    Если был задан параметр extended=1, возвращает
            число результатов в поле count, отдельно массив объектов комментариев в поле items, пользователей в поле
            profiles и сообществ в поле groups.  Если был передан параметр start_comment_id, будет также возвращено
            поле real_offset – итоговое смещение данного подмножества комментариев (оно может быть отрицательным,
            если был указан отрицательный offset)
        """

        params = locals()
        method_name = self._base_method + 'getComments'
        return self._call(method_name, params)

    def removeFromAlbum(self, target_id: str = None, album_id: str = None, album_ids: str = None, owner_id: str = None,
                        video_id: str = None) -> dict:
        """
        Позволяет убрать видеозапись из альбома.

        :param target_id: идентификатор владельца альбома. Обратите внимание, идентификатор сообщества в
            параметре target_id необходимо указывать со знаком "-" — например, target_id=-1 соответствует
            идентификатору сообщества ВКонтакте API (club1)
        :param album_id: идентификатор альбома, из которого нужно убрать видео.
        :param album_ids: идентификаторы альбомов, из которых нужно убрать видео.
        :param owner_id: идентификатор владельца видеозаписи. Обратите внимание, идентификатор сообщества в
            параметре owner_id необходимо указывать со знаком "-" — например, owner_id=-1 соответствует
            идентификатору сообщества ВКонтакте API (club1)
        :param video_id: идентификатор видеозаписи.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'removeFromAlbum'
        return self._call(method_name, params)

    def reorderAlbums(self, owner_id: str = None, album_id: str = None, before: str = None, after: str = None) -> dict:
        """
        Позволяет изменить порядок альбомов с видео.

        :param owner_id: идентификатор пользователя или сообщества, которому принадлежит альбом. Обратите
            внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком "-" — например,
            owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)
        :param album_id: идентификатор альбома, который нужно переместить.
        :param before: идентификатор альбома, перед которым нужно поместить текущий.
        :param after: идентификатор альбома, после которого нужно поместить текущий.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'reorderAlbums'
        return self._call(method_name, params)

    def reorderVideos(self, target_id: str = None, album_id: str = None, owner_id: str = None, video_id: str = None,
                      before_owner_id: str = None, before_video_id: str = None, after_owner_id: str = None,
                      after_video_id: str = None) -> dict:
        """
        Позволяет переместить видеозапись в альбоме.

        :param target_id: идентификатор пользователя или сообщества, в чьем альбоме нужно переместить видео.
            Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком "-" —
            например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)
        :param album_id: идентификатор альбома с видеозаписью, которую нужно переместить.
        :param owner_id: идентификатор владельца видеозаписи, которую нужно переместить (пользователь или
            сообщество).
        :param video_id: идентификатор видеозаписи, которую нужно переместить.
        :param before_owner_id: идентификатор владельца видеозаписи, перед которой следует поместить текущую
            (пользователь или сообщество).
        :param before_video_id: идентификатор видеозаписи, перед которой следует поместить текущую.
        :param after_owner_id: идентификатор владельца видеозаписи, после которой следует поместить текущую
            (пользователь или сообщество).
        :param after_video_id: идентификатор видеозаписи, после которой следует поместить текущую.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'reorderVideos'
        return self._call(method_name, params)

    def report(self, owner_id: str = None, video_id: str = None, reason: str = None, comment: str = None,
               search_query: str = None) -> dict:
        """
        Позволяет пожаловаться на видеозапись.

        :param owner_id: идентификатор пользователя или сообщества, которому принадлежит видеозапись.
        :param video_id: идентификатор видеозаписи.
        :param reason: тип жалобы. Возможные значения:   0 — это спам;  1 — детская порнография;  2 — экстремизм;
            3 — насилие;  4 — пропаганда наркотиков;  5 — материал для взрослых;  6 — оскорбление.
        :param comment: комментарий для жалобы.
        :param search_query: поисковой запрос, если видеозапись была найдена через поиск.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'report'
        return self._call(method_name, params)

    def reportComment(self, owner_id: str = None, comment_id: str = None, reason: str = None) -> dict:
        """
        Позволяет пожаловаться на комментарий к видеозаписи.

        :param owner_id: идентификатор владельца видеозаписи, к которой оставлен комментарий.
        :param comment_id: идентификатор комментария.
        :param reason: тип жалобы. Возможные значения:   0 — это спам;  1 — детская порнография;  2 — экстремизм;
            3 — насилие;  4 — пропаганда наркотиков;  5 — материал для взрослых;  6 — оскорбление.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'reportComment'
        return self._call(method_name, params)

    def restore(self, video_id: str = None, owner_id: str = None) -> dict:
        """
        Восстанавливает удаленную видеозапись.

        :param video_id: идентификатор видеозаписи.
        :param owner_id: идентификатор владельца видеозаписи (пользователь или сообщество). Обратите внимание,
            идентификатор сообщества в параметре owner_id необходимо указывать со знаком "-" — например, owner_id=-1
            соответствует идентификатору сообщества ВКонтакте API (club1)

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'restore'
        return self._call(method_name, params)

    def restoreComment(self, owner_id: str = None, comment_id: str = None) -> dict:
        """
        Восстанавливает удаленный комментарий к видеозаписи.

        :param owner_id: идентификатор пользователя или сообщества, которому принадлежит видеозапись. Обратите
            внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком "-" — например,
            owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)
        :param comment_id: идентификатор удаленного комментария.

        :return: После успешного выполнения возвращает 1 (0, если комментарий с таким идентификатором не является
            удаленным)
        """

        params = locals()
        method_name = self._base_method + 'restoreComment'
        return self._call(method_name, params)

    def save(self, name: str = None, description: str = None, is_private: str = None, wallpost: str = None,
             link: str = None, group_id: str = None, album_id: str = None, privacy_view: str = None,
             privacy_comment: str = None, no_comments: str = None, repeat: str = None, compression: str = None) -> dict:
        """
        Возвращает адрес сервера, необходимый для загрузки, и данные видеозаписи.

        :param name: название видеофайла.
        :param description: описание видеофайла.
        :param is_private: указывается 1, если видео загружается для отправки личным сообщением. После загрузки с
            этим параметром видеозапись не будет отображаться в списке видеозаписей пользователя и не будет доступна
            другим пользователям по ее идентификатору. По умолчанию: 0.
        :param wallpost: требуется ли после сохранения опубликовать запись с видео на стене (1 — требуется, 0 —
            не требуется).  Обратите внимание, для публикации записи на стене приложение должно иметь права wall.
        :param link: url для встраивания видео с внешнего сайта, например, с Youtube. В этом случае нужно вызвать
            полученный upload_url, не прикрепляя файл, достаточно просто обратиться по этому адресу.
        :param group_id: идентификатор сообщества, в которое будет сохранен видеофайл. По умолчанию файл
            сохраняется на страницу текущего пользователя.
        :param album_id: идентификатор альбома, в который будет загружен видео файл.
        :param privacy_view: настройки приватности просмотра видеозаписи в специальном формате. Приватность
            доступна для видеозаписей, которые пользователь загрузил в профиль.
        :param privacy_comment: настройки приватности комментирования видеозаписи в специальном формате.
            Приватность доступна для видеозаписей, которые пользователь загрузил в профиль.
        :param no_comments: 1 — закрыть комментарии (для видео из сообществ). По умолчанию: 0.
        :param repeat: зацикливание воспроизведения видеозаписи.
        :param compression:

        :return: Возвращает объект, который имеет поля upload_url, video_id, title, description, owner_id.  Метод
            может быть вызван не более 5000 раз в сутки для одного сервиса
        """

        params = locals()
        method_name = self._base_method + 'save'
        return self._call(method_name, params)

    def search(self, q: str = None, sort: str = None, hd: str = None, adult: str = None, filters: str = None,
               search_own: str = None, offset: str = None, longer: str = None, shorter: str = None, count: str = None,
               extended: str = None) -> dict:
        """
        Возвращает список видеозаписей в соответствии с заданным критерием поиска.

        :param q: строка поискового запроса. Например, The Beatles.
        :param sort: сортировка результатов. Возможные значения:   0 — по дате добавления видеозаписи;  1 — по
            длительности;  2 — по релевантности.
        :param hd: если не равен нулю, то поиск производится только по видеозаписям высокого качества.
        :param adult: фильтр «Безопасный поиск». Возможные значения:   1 — выключен;  0 — включен.
        :param filters: список критериев, по которым требуется отфильтровать видео:   mp4 — искать только видео в
            формате mp4 (воспроизводимое на iOS);  youtube — возвращать только youtube видео;  vimeo — возвращать
            только vimeo видео;  short — возвращать только короткие видеозаписи;  long — возвращать только длинные
            видеозаписи.
        :param search_own: 1 — искать по видеозаписям пользователя, 0 — не искать по видеозаписям пользователя.
            По умолчанию: 0.
        :param offset: смещение относительно первой найденной видеозаписи для выборки определенного подмножества.
        :param longer: количество секунд, видеозаписи длиннее которого необходимо вернуть.
        :param shorter: количество секунд, видеозаписи короче которого необходимо вернуть.
        :param count: количество возвращаемых видеозаписей. Обратите внимание — даже при использовании параметра
            offset для получения информации доступны только первые 1000 результатов.
        :param extended: 1 — в ответе будут возвращены дополнительные поля profiles и groups, содержащие
            информацию о пользователях и сообществах. По умолчанию: 0.

        :return: После успешного выполнения возвращает объект, содержащий число результатов в поле count и массив
            объектов видеозаписей в поле items.  Если был задан параметр extended=1, возвращает число результатов в
            поле count, отдельно массив объектов видеозаписей в поле items, пользователей в поле profiles и сообществ
            в поле groups.  Если в Вашем приложении используется прямая авторизация, возвращается дополнительное поле
            files, содержащее ссылку на файл с видео (если ролик размещен на сервере ВКонтакте) или ссылку на внешний
            ресурс (если ролик встроен с какого-либо видеохостинга)
        """

        params = locals()
        method_name = self._base_method + 'search'
        return self._call(method_name, params)
