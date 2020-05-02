from .ApiMethod import ApiMethod


class Polls(ApiMethod):
    def __init__(self, access_token, v, session, calls_per_second):
        super(Polls, self).__init__(access_token, v, session, calls_per_second)
        self._base_method = 'polls.'

    def addVote(self, owner_id: str = None, poll_id: str = None, answer_ids: str = None, is_board: str = None) -> dict:
        """
        Отдает голос текущего пользователя за выбранный вариант ответа в указанном опросе.

        :param owner_id: идентификатор пользователя или сообщества, которому принадлежит опрос.
        :param poll_id: идентификатор опроса.
        :param answer_ids: список идентификаторов ответа (для опроса с мультивыбором).
        :param is_board: 1 – опрос находится в обсуждении, 0 – опрос прикреплен к стене.

        :return: После успешного выполнения возвращает одно из следующих значений:   1 — если голос текущего
            пользователя был отдан за выбранный вариант ответа;  0 — если текущий пользователь уже голосовал в
            указанном опрос
        """

        params = locals()
        method_name = self._base_method + 'addVote'
        return self._call(method_name, params)

    def create(self, question: str = None, is_anonymous: str = None, is_multiple: str = None, end_date: str = None,
               owner_id: str = None, add_answers: str = None, photo_id: str = None, background_id: str = None) -> dict:
        """
        Позволяет создавать опросы, которые впоследствии можно прикреплять к записям на странице пользователя или
        сообщества.

        :param question: текст вопроса
        :param is_anonymous: 1 – анонимный опрос, список проголосовавших недоступен;  0 – опрос публичный, список
            проголосовавших доступен;  По умолчанию – 0.
        :param is_multiple: 1 — для создания опроса с мультивыбором.
        :param end_date: дата завершения опроса в Unixtime.
        :param owner_id: Если опрос будет добавлен в группу, необходимо передать отрицательный идентификатор
            группы. По умолчанию текущий пользователь.
        :param add_answers: список вариантов ответов, например: ["yes", "no", "maybe"]  Может быть не менее 1 и
            не более 10 вариантов ответа.
        :param photo_id: идентификатор фотографии для использования в качестве фона сниппета.
        :param background_id: идентификатор стандартного фона для сниппета.

        :return: В случае успешного создания опроса в качестве результата возвращается объект опроса
        """

        params = locals()
        method_name = self._base_method + 'create'
        return self._call(method_name, params)

    def deleteVote(self, owner_id: str = None, poll_id: str = None, answer_id: str = None,
                   is_board: str = None) -> dict:
        """
        Снимает голос текущего пользователя с выбранного варианта ответа в указанном опросе.

        :param owner_id: идентификатор пользователя или сообщества, которому принадлежит опрос.
        :param poll_id: идентификатор опроса.
        :param answer_id: идентификатор варианта ответа.
        :param is_board: 1 – опрос находится в обсуждении, 0 – опрос прикреплен к стене.

        :return: После успешного выполнения возвращает одно из следующих значений:   1 — если голос текущего
            пользователя был снят с выбранного варианта ответа  0 — если текущий пользователь еще не голосовал в
            указанном опросе или указан не выбранный им вариант ответ
        """

        params = locals()
        method_name = self._base_method + 'deleteVote'
        return self._call(method_name, params)

    def edit(self, owner_id: str = None, poll_id: str = None, question: str = None, add_answers: str = None,
             edit_answers: str = None, delete_answers: str = None, end_date: str = None, photo_id: str = None,
             background_id: str = None) -> dict:
        """
        Позволяет редактировать созданные опросы.

        :param owner_id: идентификатор владельца опроса
        :param poll_id: идентификатор редактируемого опроса
        :param question: новый текст редактируемого опроса
        :param add_answers: список вариантов ответов, например: ["yes", "no", "maybe"]
        :param edit_answers: объект, содержащий варианты ответов, которые необходимо отредактировать;  ключ –
            идентификатор ответа, значение – новый текст ответа  Пример: {"382967099":"option1",
            "382967103":"option2"}
        :param delete_answers: список идентификаторов ответов, которые необходимо удалить, например: [382967099,
            382967103]
        :param end_date: дата завершения опроса в Unixtime.
        :param photo_id: идентификатор фотографии для сниппета.
        :param background_id: идентификатор стандартного фона для сниппета.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'edit'
        return self._call(method_name, params)

    def getBackgrounds(self) -> dict:
        """
        Возвращает варианты фонового изображения для опросов.

        :return: Возвращает массив объектов, описывающих фоновое изображение опроса. Каждый из объектов содержит
            поля:   type (string) — тип фона. Возможные значения: gradient или tile.  angle (string) — (для type =
            gradient) угол градиента по оси X.  color (string) — HEX-код замещающего цвета (без #).  width (integer)
            — (для type = tile) ширина плитки паттерна.  height (integer) — (для type = tile) высота плитки паттерна.
            points (array) — (для type = gradient) точки градиента. Массив объектов, каждый из которых содержит поля
            position (number) — положение точки — и color (string) — HEX-код цвета точки.  id (integer) —
            идентификатор фона
        """

        params = locals()
        method_name = self._base_method + 'getBackgrounds'
        return self._call(method_name, params)

    def getById(self, owner_id: str = None, is_board: str = None, poll_id: str = None, extended: str = None,
                friends_count: str = None, fields: str = None, name_case: str = None) -> dict:
        """
        Возвращает детальную информацию об опросе по его идентификатору.

        :param owner_id: идентификатор пользователя или сообщества, которому принадлежит опрос.
        :param is_board: 1 — опрос находится в обсуждении, 0 — опрос прикреплен к стене.  По умолчанию — 0.
        :param poll_id: идентификатор опроса.
        :param extended: 1 — возвращать дополнительную информацию о профилях пользователей.
        :param friends_count: число идентификаторов проголосовавших друзей, которые необходимо вернуть в ответе.
        :param fields: список дополнительных полей профилей. См. список возможных значений
        :param name_case: падеж для склонения имени и фамилии пользователя. Возможные значения: именительный –
            nom, родительный – gen, дательный – dat, винительный – acc, творительный – ins, предложный – abl. По
            умолчанию nom.

        :return: После успешного выполнения возвращает объект опроса
        """

        params = locals()
        method_name = self._base_method + 'getById'
        return self._call(method_name, params)

    def getPhotoUploadServer(self, owner_id: str = None) -> dict:
        """
        Возвращает адрес сервера для загрузки фоновой фотографии в опрос.

        :param owner_id: идентификатор владельца опроса.

        :return: Возвращает объект с единственным полем upload_url (string), содержащим URL для загрузки
            фотографии
        """

        params = locals()
        method_name = self._base_method + 'getPhotoUploadServer'
        return self._call(method_name, params)

    def getVoters(self, owner_id: str = None, poll_id: str = None, answer_ids: str = None, is_board: str = None,
                  friends_only: str = None, offset: str = None, count: str = None, fields: str = None,
                  name_case: str = None) -> dict:
        """
        Получает список идентификаторов пользователей, которые выбрали определенные варианты ответа в опросе.

        :param owner_id: идентификатор пользователя или сообщества, которому принадлежит опрос.
        :param poll_id: идентификатор опроса.
        :param answer_ids: идентификаторы вариантов ответа.
        :param is_board: 1 – опрос находится в обсуждении, 0 – опрос прикреплен к стене.
        :param friends_only: указывает, необходимо ли возвращать только пользователей, которые являются друзьями
            текущего пользователя. Параметр может принимать следующие значения: 0 — возвращать всех пользователей в
            порядке убывания времени голосования; 1 — возвращать только друзей текущего пользователя в порядке
            убывания времени голосования.  Если параметр не был задан, то считается, что он равен 0.
        :param offset: смещение относительно начала списка, для выборки определенного подмножества. Если параметр
            не задан, то считается, что он равен 0.
        :param count: количество возвращаемых идентификаторов пользователей. Если параметр не задан, то
            считается, что он равен 100, если не задан параметр friends_only, в противном случае 10. Максимальное
            значение параметра 1000, если не задан параметр friends_only, в противном случае 100.
        :param fields: перечисленные через запятую поля анкет, необходимые для получения. Доступные значения:
            nickname, screen_name, sex, bdate (birthdate), city, country, timezone, photo, photo_medium, photo_big,
            has_mobile, rate, contacts, education, online, counters.
        :param name_case: падеж для склонения имени и фамилии пользователя. Возможные значения: именительный –
            nom, родительный – gen, дательный – dat, винительный – acc, творительный – ins, предложный – abl. По
            умолчанию nom.

        :return: После успешного выполнения для каждого варианта ответа возвращает объект со следующими полями:
            answer_id — идентификатор варианта ответа;  users — список идентификаторов пользователей с учетом
            параметров offset и count, которые проголосовали за данный вариант. Первый элемент списка - общее
            количество пользователей, проголосовавших за данный вариант.   При использовании параметра fields массив
            users будет состоять из объектов user, каждый из которых содержит набор полей, определенных в этом
            параметре. Значения uid, first_name и last_name возвращаются всегда, вне зависимости от выбранных полей и
            их количества.  см. Описание полей параметра user
        """

        params = locals()
        method_name = self._base_method + 'getVoters'
        return self._call(method_name, params)

    def savePhoto(self, photo: str = None, hash: str = None) -> dict:
        """
        Сохраняет фотографию, загруженную в опрос.

        :param photo: параметр, полученный в результате загрузки фотографии.
        :param hash: параметр, полученный в результате загрузки фотографии.

        :return: Возвращает идентификатор загруженной фотографии
        """

        params = locals()
        method_name = self._base_method + 'savePhoto'
        return self._call(method_name, params)

