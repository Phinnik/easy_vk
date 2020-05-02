from ApiMethod import ApiMethod

class Account(ApiMethod):
    def __init__(self, access_token, v, session, calls_per_second):
        super(Account, self).__init__(access_token, v, session, calls_per_second)
        self._base_method = 'account.'

    def ban(self, owner_id: str = None) -> dict:
        """
        Добавляет пользователя или группу в черный список.

        :param owner_id: идентификатор пользователя или сообщества, которое будет добавлено в черный список.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'ban'
        return self._call(method_name, params)

    def changePassword(self, restore_sid: str = None, change_password_hash: str = None, old_password: str = None,
                       new_password: str = None) -> dict:
        """
        Позволяет сменить пароль пользователя после успешного восстановления доступа к аккаунту через СМС, используя
        метод auth.restore.

        :param restore_sid: идентификатор сессии, полученный при восстановлении доступа используя метод
            auth.restore. (В случае если пароль меняется сразу после восстановления доступа)
        :param change_password_hash: хэш, полученный при успешной OAuth авторизации по коду полученному по СМС (В
            случае если пароль меняется сразу после восстановления доступа)
        :param old_password: текущий пароль пользователя.
        :param new_password: новый пароль, который будет установлен в качестве текущего.

        :return: Возвращает объект с единственным полем token, содержащим новый токен
        """

        params = locals()
        method_name = self._base_method + 'changePassword'
        return self._call(method_name, params)

    def getActiveOffers(self, offset: str = None, count: str = None) -> dict:
        """
        Возвращает список активных рекламных предложений (офферов), выполнив которые пользователь сможет получить
        соответствующее количество голосов на свой счёт внутри приложения.

        :param offset: смещение, необходимое для выборки определенного подмножества офферов.
        :param count: количество офферов, которое необходимо получить

        :return: Возвращает массив, состоящий из общего количества старгетированных на текущего пользователя
            специальных предложений (первый элемент), и списка объектов с информацией о предложениях.  В случае, если
            на пользователя не старгетировано ни одного специального предложения, массив будет содержать элемент 0
            (количество специальных предложений)
        """

        params = locals()
        method_name = self._base_method + 'getActiveOffers'
        return self._call(method_name, params)

    def getAppPermissions(self, user_id: str = None) -> dict:
        """
        Получает настройки текущего пользователя в данном приложении.

        :param user_id: идентификатор пользователя, информацию о настройках которого необходимо получить. По
            умолчанию — текущий пользователь.

        :return: После успешного выполнения возвращает битовую маску настроек текущего пользователя в данном
            приложении.   Пример Если Вы хотите получить права на Доступ к друзьям и Доступ к статусам пользователя,
            то Ваша битовая маска будет равна: 2 + 1024 = 1026.  Если, имея битовую маску 1026, Вы хотите проверить,
            имеет ли она доступ к друзьям — Вы можете сделать 1026 & 2. Например alert(1026 & 2);  см. Список
            возможных настроек прав доступ
        """

        params = locals()
        method_name = self._base_method + 'getAppPermissions'
        return self._call(method_name, params)

    def getBanned(self, offset: str = None, count: str = None) -> dict:
        """
        Возвращает список пользователей, находящихся в черном списке.

        :param offset: смещение, необходимое для выборки определенного подмножества черного списка.
        :param count: количество объектов, информацию о которых необходимо вернуть.

        :return: После успешного выполнения возвращает объект, содержащий число результатов в поле count и массив
            объектов, описывающих пользователей в поле items
        """

        params = locals()
        method_name = self._base_method + 'getBanned'
        return self._call(method_name, params)

    def getCounters(self, filter: str = None) -> dict:
        """
        Возвращает ненулевые значения счетчиков пользователя.

        :param filter: счетчики, информацию о которых нужно вернуть. Может включать следующие значения:   friends
            — новые заявки в друзья;  friends_suggestions — предлагаемые друзья;  messages — новые сообщения;  photos
            — новые отметки на фотографиях;  videos — новые отметки на видеозаписях;  gifts — подарки;  events —
            события;  groups — сообщества;  notifications — ответы;  sdk — запросы в мобильных играх;  app_requests —
            уведомления от приложений.  friends_recommendations — рекомендации друзей.

        :return: Возвращает объект, который может содержать поля friends, messages, photos, videos, notes, gifts,
            events, groups, notifications, sdk, app_requests, friends_recommendations со значением счетчиков
            (integer)
        """

        params = locals()
        method_name = self._base_method + 'getCounters'
        return self._call(method_name, params)

    def getInfo(self, fields: str = None) -> dict:
        """
        Возвращает информацию о текущем аккаунте.

        :param fields: список полей, которые необходимо вернуть. Возможные значения:   country  https_required
            own_posts_default  no_wall_replies  intro  lang  По умолчанию будут возвращены все поля.

        :return: Метод возвращает объект, содержащий следующие поля:  country  stringстроковой код страны,
            определенный по IP адресу, с которого сделан запрос. https_required  integer, [0,1]информация о том,
            включено ли безопасное соединение для аккаунта. 1 — включено, 0 — не включено. 2fa_required  integer,
            [0,1]информация о том, включена ли двухфакторная аутентификация для аккаунта. 1 — включена, 0 — не
            включена. own_posts_default  integer, [0,1]информация о том, показываются ли по умолчанию на стене только
            записи пользователя. 1 — да, 0 — нет. no_wall_replies  integer, [0,1]информация о том, отключено ли
            комментирование записей на стене. 1 — да, 0 — нет. intro  integer, [0,1]информация о том, прошел ли
            пользователь обучение по использованию приложения. lang  integerидентификатор текущего языка
            пользователя
        """

        params = locals()
        method_name = self._base_method + 'getInfo'
        return self._call(method_name, params)

    def getProfileInfo(self) -> dict:
        """
        Возвращает информацию о текущем профиле.



        :return: Метод возвращает объект, описывающий профиль пользователя, со следующими полями:  first_name
            string имя пользователя. last_name string фамилия пользователя. maiden_name stringдевичья фамилия
            пользователя (только для женского пола). screen_name stringкороткое имя пользователя (если есть). sex
            integerпол. Возможные значения:   1 — женский;  2 — мужской;  0 — пол не указан. relation integerсемейное
            положение. Возможные значения:   1 — не женат/не замужем;  2 — есть друг/есть подруга;  3 —
            помолвлен/помолвлена;  4 — женат/замужем;  5 — всё сложно;  6 — в активном поиске;  7 — влюблён/влюблена;
            8 — в гражданском браке;  0 — не указано. relation_partner objectобъект пользователя, с которым связано
            семейное положение (если есть). relation_pending  integerпередается 1, если пользователь, указанный в
            relation_partner, не подтвердил отношения. relation_requests arrayсписок объектов пользователей, которые
            указали, что состоят в отношениях с данным пользователем (если есть). bdate stringдата рождения
            пользователя, возвращается в формате D.M.YYYY. bdate_visibility integerвидимость даты рождения. Возможные
            значения:   1 — показывать дату рождения;  2 — показывать только месяц и день;  0 — не показывать дату
            рождения. home_town  stringназвание родного города. country objectстрана. Объект, содержащий поля:   id
            (integer) — идентификатор страны;  title (string) — название страны. city  objectгород. Объект,
            содержащий поля:   id (integer) — идентификатор города;  title (string) — название города. name_request
            objectинформация о заявке на смену имени, если она была подана. Объект, содержащий поля:   id (integer) –
            идентификатор заявки, необходимый для её отмены (только если status равен processing);  status (string) –
            статус заявки. Возможные значения:   processing – заявка рассматривается;  declined – заявка отклонена;
            first_name (string) – имя пользователя, указанное в заявке;  last_name (string) – фамилия пользователя,
            указанная в заявке. status  stringстатус пользователя. phone  stringномер телефона
        """

        params = locals()
        method_name = self._base_method + 'getProfileInfo'
        return self._call(method_name, params)

    def getPushSettings(self, device_id: str = None) -> dict:
        """
        Позволяет получать настройки Push-уведомлений.

        :param device_id: уникальный идентификатор устройства.

        :return: Возвращает объект, содержащий поля:   disabled — отключены ли уведомления.  disabled_until —
            unixtime-значение времени, до которого временно отключены уведомления.  conversations — список,
            содержащий настройки конкретных диалогов, и их количество первым элементом.  settings — объект с
            настройками Push-уведомлений в специальном формате
        """

        params = locals()
        method_name = self._base_method + 'getPushSettings'
        return self._call(method_name, params)

    def registerDevice(self, token: str = None, device_model: str = None, device_year: str = None,
                       device_id: str = None, system_version: str = None, settings: str = None,
                       sandbox: str = None) -> dict:
        """
        Подписывает устройство на базе iOS, Android, Windows Phone или Mac на получение Push-уведомлений.

        :param token: идентификатор устройства, используемый для отправки уведомлений. (для mpns идентификатор
            должен представлять из себя URL для отправки уведомлений).
        :param device_model: cтроковое название модели устройства.
        :param device_year: год устройства.
        :param device_id: уникальный идентификатор устройства.
        :param system_version: строковая версия операционной системы устройства.
        :param settings: сериализованный JSON-объект, описывающий настройки уведомлений в специальном формате.
        :param sandbox: флаг предназначен для iOS устройств. 1 — использовать sandbox сервер для отправки push-
            уведомлений, 0 — не использовать.

        :return: После успешного выполнения возвращает 1.  На iOS и Windows Phone push-уведомления будут
            отображены без какой либо обработки.  На Android будут приходить события в следующем формате
        """

        params = locals()
        method_name = self._base_method + 'registerDevice'
        return self._call(method_name, params)

    def saveProfileInfo(self, first_name: str = None, last_name: str = None, maiden_name: str = None,
                        screen_name: str = None, cancel_request_id: str = None, sex: str = None, relation: str = None,
                        relation_partner_id: str = None, bdate: str = None, bdate_visibility: str = None,
                        home_town: str = None, country_id: str = None, city_id: str = None, status: str = None) -> dict:
        """
        Редактирует информацию текущего профиля.

        :param first_name: имя пользователя. Обязательно с большой буквы.
        :param last_name: фамилия пользователя. Обязательно с большой буквы.
        :param maiden_name: девичья фамилия пользователя (только для женского пола).
        :param screen_name: короткое имя страницы.
        :param cancel_request_id: идентификатор заявки на смену имени, которую необходимо отменить.  Если передан
            этот параметр, все остальные параметры игнорируются.
        :param sex: пол пользователя. Возможные значения:   1 — женский;  2 — мужской.
        :param relation: семейное положение пользователя. Возможные значения:   1 — не женат/не замужем;  2 —
            есть друг/есть подруга;  3 — помолвлен/помолвлена;  4 — женат/замужем;  5 — всё сложно;  6 — в активном
            поиске;  7 — влюблён/влюблена;  8 — в гражданском браке;  0 — не указано.
        :param relation_partner_id: идентификатор пользователя, с которым связано семейное положение.
        :param bdate: дата рождения пользователя в формате DD.MM.YYYY, например "15.11.1984".
        :param bdate_visibility: видимость даты рождения. Возможные значения:   1 — показывать дату рождения;  2
            — показывать только месяц и день;  0 — не показывать дату рождения.
        :param home_town: родной город пользователя.
        :param country_id: идентификатор страны пользователя.
        :param city_id: идентификатор города пользователя.
        :param status: статус пользователя, который также может быть изменен методом status.set

        :return: Метод возвращает объект, содержащий следующие поля:   changed – возвращает 1 — если информация
            была сохранена, 0 — если ни одно из полей не было сохранено.  Если в параметрах передавалось имя или
            фамилия пользователя, в объекте также будет возвращено поле name_request – объект, содержащий информацию
            о заявке на смену имени, со следующими полями:   id – идентификатор заявки, необходимый для её отмены
            (только если status равен processing). Для отмены заявки необходимо вызвать метод account.saveProfileInfo
            с параметром cancel_request_id;  status – статус заявки, возвращаемые значения:   success – имя было
            успешно изменено;  processing – заявка рассматривается;  declined – заявка отклонена;  was_accepted –
            недавно уже была одобрена заявка, повторную заявку можно подать не раньше даты, указанной в поле
            repeat_date;  was_declined – предыдущая заявка была отклонена, повторную заявку можно подать не раньше
            даты, указанной в поле repeat_date;   first_name – имя пользователя, указанное в заявке;  last_name –
            фамилия пользователя, указанная в заявке
        """

        params = locals()
        method_name = self._base_method + 'saveProfileInfo'
        return self._call(method_name, params)

    def setInfo(self, name: str = None, value: str = None) -> dict:
        """
        Позволяет редактировать информацию о текущем аккаунте.

        :param name: имя настройки
        :param value: значение настройки

        :return: В результате успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'setInfo'
        return self._call(method_name, params)

    def setNameInMenu(self, user_id: str = None, name: str = None) -> dict:
        """
        Устанавливает короткое название приложения (до 17 символов), которое выводится пользователю в левом меню.

        :param user_id: идентификатор пользователя.
        :param name: короткое название приложения.

        :return: Возвращает 1 в случае успешной установки короткого названия.  Если пользователь не установил
            приложение в левое меню, метод вернет ошибку 148 (Access to the menu of the user denied). Избежать этой
            ошибки можно с помощью метода account.getAppPermissions
        """

        params = locals()
        method_name = self._base_method + 'setNameInMenu'
        return self._call(method_name, params)

    def setOffline(self) -> dict:
        """
        Помечает текущего пользователя как offline (только в текущем приложении).



        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'setOffline'
        return self._call(method_name, params)

    def setOnline(self, voip: str = None) -> dict:
        """
        Помечает текущего пользователя как online на 5 минут.

        :param voip: возможны ли видеозвонки для данного устройства

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'setOnline'
        return self._call(method_name, params)

    def setPushSettings(self, device_id: str = None, settings: str = None, key: str = None, value: str = None) -> dict:
        """
        Изменяет настройку Push-уведомлений.

        :param device_id: уникальный идентификатор устройства.
        :param settings: сериализованный JSON-объект, описывающий настройки уведомлений в специальном формате.
        :param key: ключ уведомления.
        :param value: новое значение уведомления в специальном формате.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'setPushSettings'
        return self._call(method_name, params)

    def setSilenceMode(self, device_id: str = None, time: str = None, peer_id: str = None, sound: str = None) -> dict:
        """
        Отключает push-уведомления на заданный промежуток времени.

        :param device_id: уникальный идентификатор устройства.
        :param time: время в секундах на которое требуется отключить уведомления, -1 отключить навсегда
        :param peer_id: идентификатор назначения. Для пользователя:  id пользователя.   Для групповой беседы:
            2000000000 + id беседы.   Для сообщества:  -id сообщества.
        :param sound: 1 — включить звук в этом диалоге, 0 — отключить звук (параметр работает, только если в
            peer_id передан идентификатор групповой беседы или пользователя).

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'setSilenceMode'
        return self._call(method_name, params)

    def unban(self, owner_id: str = None) -> dict:
        """
        Удаляет пользователя или группу из черного списка.

        :param owner_id: идентификатор пользователя или группы, которого нужно удалить из черного списка.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'unban'
        return self._call(method_name, params)

    def unregisterDevice(self, device_id: str = None, sandbox: str = None) -> dict:
        """
        Отписывает устройство от Push уведомлений.

        :param device_id: уникальный идентификатор устройства.
        :param sandbox: флаг предназначен для iOS устройств. Возможные значения:   1 — отписать устройство,
            использующего sandbox сервер для отправки push-уведомлений;  0 — отписать устройство, не использующее
            sandbox сервер.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'unregisterDevice'
        return self._call(method_name, params)

