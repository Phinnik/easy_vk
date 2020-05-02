from .ApiMethod import ApiMethod


class Groups(ApiMethod):
    def __init__(self, access_token, v, session, calls_per_second):
        super(Groups, self).__init__(access_token, v, session, calls_per_second)
        self._base_method = 'groups.'

    def addAddress(self, group_id: str = None, title: str = None, address: str = None, additional_address: str = None,
                   country_id: str = None, city_id: str = None, metro_id: str = None, latitude: str = None,
                   longitude: str = None, phone: str = None, work_info_status: str = None, timetable: str = None,
                   is_main_address: str = None) -> dict:
        """
        Позволяет добавить адрес в сообщество.  Список адресов может быть получен методом groups.getAddresses.  Для
        того, чтобы воспользоваться этим методом, Вы должны быть администратором сообщества

        :param group_id: идентификатор сообщества, в которое добавляется адрес.
        :param title: заголовок адреса
        :param address: строка адреса Невский проспект, дом 28
        :param additional_address: дополнительное описание адреса. Второй этаж, налево
        :param country_id: идентификатор страны. Для получения можно использовать database.getCountries
        :param city_id: идентификатор города. Для получения можно использовать database.getCities
        :param metro_id: идентификатор станции метро. Для получения можно использовать database.getMetroStations
        :param latitude: географическая широта отметки, заданная в градусах (от -90 до 90).
        :param longitude: географическая долгота отметки, заданная в градусах (от -180 до 180).
        :param phone: номер телефона
        :param work_info_status: тип расписания. Возможные значения:   no_information — нет информации о
            расписании;  temporarily_closed — временно закрыто;  always_opened — открыто круглосуточно;
            forever_closed — закрыто навсегда;  timetable — открыто в указанные часы работы. Для этого типа
            расписания необходимо передать параметр timetable;
        :param timetable: для типа timetable можно передать расписание в формате json. Время передается в минутах
            от 0 часов. Ключ по дню означает, что день рабочий. open_time, close_time - начало и конец рабочего дня.
            break_open_time, break_close_time — время перерыва. {    "mon": {      "open_time": 1080,
                "close_time": 1380    },    "tue": {      "open_time": 1080,      "close_time": 1380    },    "wed":
            {      "open_time": 1080,      "close_time": 1320    },    "thu": {      "open_time": 1080,
                "close_time": 1320    },    "fri": {      "open_time": 1080,      "close_time": 1320    },    "sat":
            {      "open_time": 1080,      "close_time": 1320,      "break_open_time": 1200,      "break_close_time":
            1230    }  }
        :param is_main_address: установить адрес основным. Информация об основном адресе сразу показывается в
            сообществе. Для получения информации об остальных адресах нужно перейти к списку адресов.

        :return
        """

        params = locals()
        method_name = self._base_method + 'addAddress'
        return self._call(method_name, params)

    def addCallbackServer(self, group_id: str = None, url: str = None, title: str = None,
                          secret_key: str = None) -> dict:
        """
        Добавляет сервер для Callback API в сообщество.

        :param group_id: идентификатор сообщества.
        :param url: URL сервера.
        :param title: название сервера.
        :param secret_key: секретный ключ.

        :return: После успешного выполнения возвращает идентификатор добавленного сервера в поле server_id
            (integer)
        """

        params = locals()
        method_name = self._base_method + 'addCallbackServer'
        return self._call(method_name, params)

    def addLink(self, group_id: str = None, link: str = None, text: str = None) -> dict:
        """
        Позволяет добавлять ссылки в сообщество.

        :param group_id: идентификатор сообщества, в которое добавляется ссылка.
        :param link: адрес ссылки.
        :param text: текст ссылки.

        :return: В случае успешного выполнения возвращает объект со следующими полями:   id (integer) —
            идентификатор ссылки;  url (string) — URL ссылки;  name (string) — название ссылки в блоке сообщества;
            edit_title (integer, [0,1]) — возвращается 1, если можно редактировать название ссылки (для внешних
            ссылок);  desc (string) — описание ссылки;  image_processing (integer, [1]) — возвращается 1, если превью
            находится в процессе обработки
        """

        params = locals()
        method_name = self._base_method + 'addLink'
        return self._call(method_name, params)

    def approveRequest(self, group_id: str = None, user_id: str = None) -> dict:
        """
        Позволяет одобрить заявку в группу от пользователя.

        :param group_id: идентификатор группы, заявку в которую необходимо одобрить.
        :param user_id: идентификатор пользователя, заявку которого необходимо одобрить.

        :return: В случае успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'approveRequest'
        return self._call(method_name, params)

    def ban(self, group_id: str = None, owner_id: str = None, end_date: str = None, reason: str = None,
            comment: str = None, comment_visible: str = None) -> dict:
        """
        Добавляет пользователя или группу в черный список сообщества.

        :param group_id: идентификатор сообщества.
        :param owner_id: идентификатор пользователя или сообщества, которое будет добавлено в черный список.
            Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком "-" —
            например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)
        :param end_date: дата завершения срока действия бана в формате unixtime. Максимальный возможный срок
            окончания бана, который можно указать, — один год с его начала. Если параметр не указан, пользователь
            будет заблокирован навсегда.
        :param reason: причина бана:   0 — другое (по умолчанию);  1 — спам;  2 — оскорбление участников;  3
            — нецензурные выражения;  4 — сообщения не по теме.
        :param comment: текст комментария к бану.
        :param comment_visible: 1 – текст комментария будет отображаться пользователю.  0 – текст комментария не
            доступен пользователю. (по умолчанию)

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'ban'
        return self._call(method_name, params)

    def create(self, title: str = None, description: str = None, type: str = None, public_category: str = None,
               subtype: str = None) -> dict:
        """
        Создает новое сообщество.

        :param title: название сообщества.
        :param description: описание сообщества, (не учитывается при type=public).
        :param type: тип создаваемого сообщества:   group — группа;  event — мероприятие;  public — публичная
            страница.
        :param public_category: категория публичной страницы (только для type = public).
        :param subtype: вид публичной страницы (только при type=public):   1 — место или небольшая компания;  2 —
            компания, организация или веб-сайт;  3 — известная личность или коллектив;  4 — произведение или
            продукция.

        :return: После успешного выполнения возвращает объект, описывающий созданное сообщество
        """

        params = locals()
        method_name = self._base_method + 'create'
        return self._call(method_name, params)

    def deleteAddress(self, group_id: str = None, address_id: str = None) -> dict:
        """
        Удаляет адрес сообщества.

        :param group_id: Id группы
        :param address_id: Id адреса

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'deleteAddress'
        return self._call(method_name, params)

    def deleteCallbackServer(self, group_id: str = None, server_id: str = None) -> dict:
        """
        Удаляет сервер для Callback API из сообщества.

        :param group_id: идентификатор сообщества.
        :param server_id: идентификатор сервера, который нужно удалить.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'deleteCallbackServer'
        return self._call(method_name, params)

    def deleteLink(self, group_id: str = None, link_id: str = None) -> dict:
        """
        Позволяет удалить ссылки из сообщества.

        :param group_id: идентификатор сообщества, ссылки которого нужно удалить
        :param link_id: идентификатор ссылки, которую необходимо удалить

        :return: В случае успешного выполнения метод возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'deleteLink'
        return self._call(method_name, params)

    def disableOnline(self, group_id: str = None) -> dict:
        """
        Выключает статус «онлайн» в сообществе.

        :param group_id: идентификатор сообщества.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'disableOnline'
        return self._call(method_name, params)

    def edit(self, group_id: str = None, title: str = None, description: str = None, screen_name: str = None,
             access: str = None, website: str = None, subject: str = None, email: str = None, phone: str = None,
             rss: str = None, event_start_date: str = None, event_finish_date: str = None, event_group_id: str = None,
             public_category: str = None, public_subcategory: str = None, public_date: str = None, wall: str = None,
             topics: str = None, photos: str = None, video: str = None, audio: str = None, links: str = None,
             events: str = None, places: str = None, contacts: str = None, docs: str = None, wiki: str = None,
             messages: str = None, articles: str = None, addresses: str = None, age_limits: str = None,
             market: str = None, market_comments: str = None, market_country: str = None, market_city: str = None,
             market_currency: str = None, market_contact: str = None, market_wiki: str = None,
             obscene_filter: str = None, obscene_stopwords: str = None, obscene_words: str = None,
             main_section: str = None, secondary_section: str = None, country: str = None, city: str = None,
             ads_easy_promote_disable_main_screen_button: str = None,
             ads_easy_promote_disable_promote_post_button: str = None) -> dict:
        """
        Редактирует сообщество.

        :param group_id: идентификатор сообщества.
        :param title: название сообщества.
        :param description: описание сообщества.
        :param screen_name: короткое имя сообщества.
        :param access: тип группы. Возможные значения:   0 — открытая;  1 — закрытая;  2 — частная.
        :param website: адрес сайта, который будет указан в информации о группе.
        :param subject: тематика сообщества. Возможные значения:   1 — авто/мото;  2 — активный отдых;  3 —
            бизнес;  4 — домашние животные;  5 — здоровье;  6 — знакомство и общение;  7 — игры;  8 — ИТ (компьютеры
            и софт);  9 — кино;  10 — красота и мода;  11 — кулинария;  12 — культура и искусство;  13 — литература;
            14 — мобильная связь и интернет;  15 — музыка;  16 — наука и техника;  17 — недвижимость;  18 — новости и
            СМИ;  19 — безопасность;  20 — образование;  21 — обустройство и ремонт;  22 — политика;  23 — продукты
            питания;  24 — промышленность;  25 — путешествия;  26 — работа;  27 — развлечения;  28 — религия;  29 —
            дом и семья;  30 — спорт;  31 — страхование;  32 — телевидение;  33 — товары и услуги;  34 — увлечения и
            хобби;  35 — финансы;  36 — фото;  37 — эзотерика;  38 — электроника и бытовая техника;  39 — эротика;
            40 — юмор;  41 — общество, гуманитарные науки;  42 — дизайн и графика.
        :param email: электронный адрес организатора (для мероприятий).
        :param phone: номер телефона организатора (для мероприятий).
        :param rss: адрес rss для импорта новостей (доступен только группам, получившим соответствующее
            разрешение, обратитесь в http://vk.com/support для получения разрешения).
        :param event_start_date: дата начала события.
        :param event_finish_date: дата окончания события.
        :param event_group_id: идентификатор группы, которая является организатором события (только для событий).
        :param public_category: категория публичной страницы.
        :param public_subcategory: подкатегория публичной станицы. Список подкатегорий можно получить методом
            groups.getSettings.
        :param public_date: дата основания компании, организации, которой посвящена публичная страница в виде
            строки формата "dd.mm.YYYY".
        :param wall: стена. Возможные значения:   0 — выключена;  1 — открытая;  2 — ограниченная (доступно
            только для групп и событий);  3 — закрытая (доступно только для групп и событий).
        :param topics: обсуждения. Возможные значения:   0 — выключены;  1 — открытые;  2 — ограниченные
            (доступно только для групп и событий).
        :param photos: фотографии. Возможные значения:   0 — выключены;  1 — открытые;  2 — ограниченные
            (доступно только для групп и событий).
        :param video: видеозаписи. Возможные значения:   0 — выключены;  1 — открытые;  2 — ограниченные
            (доступно только для групп и событий).
        :param audio: аудиозаписи. Возможные значения:   0 — выключены;  1 — открытые;  2 — ограниченные
            (доступно только для групп и событий).
        :param links: ссылки (доступно только для публичных страниц).  Возможные значения:   0 — выключены;  1 —
            включены.
        :param events: события (доступно только для публичных страниц).  Возможные значения:   0 — выключены;  1
            — включены.
        :param places: места (доступно только для публичных страниц). Возможные значения:   0 — выключены;  1 —
            включены.
        :param contacts: контакты (доступно только для публичных страниц). Возможные значения:   0 — выключены;
            1 — включены.
        :param docs: документы сообщества. Возможные значения:   0 — выключены;  1 — открытые;  2 — ограниченные
            (доступно только для групп и событий).
        :param wiki: wiki-материалы сообщества. Возможные значения:   0 — выключены;  1 — открытые;  2 —
            ограниченные (доступно только для групп и событий).
        :param messages: сообщения сообщества. Возможные значения:   0 — выключены;  1 — включены.
        :param articles:
        :param addresses:
        :param age_limits: возрастное ограничение для сообщества. Возможные значения:   1 — нет ограничений;  2 —
            16+;  3 — 18+.
        :param market: товары. Возможные значения:   0 — выключены;  1 — включены.
        :param market_comments: комментарии к товарам. Возможные значения:   0 — выключены;  1 — включены.
        :param market_country: регионы доставки товаров.
        :param market_city: города доставки товаров (в случае если указана одна страна).
        :param market_currency: идентификатор валюты магазина. Возможные значения:   643 — российский рубль;  980
            — украинская гривна;  398 — казахстанский тенге;  978 — евро;  840 — доллар США.
        :param market_contact: контакт для связи для продавцом.  Для использования сообщений сообщества следует
            включить их и передать значение 0.
        :param market_wiki: идентификатор wiki-страницы с описанием магазина.
        :param obscene_filter: фильтр нецензурных выражений в комментариях. Возможные значения:   0 — выключен;
            1 — включен.
        :param obscene_stopwords: фильтр по ключевым словам в комментариях. Возможные значения:   0 — выключен;
            1 — включен.
        :param obscene_words: ключевые слова для фильтра комментариев.
        :param main_section:
        :param secondary_section:
        :param country:
        :param city:
        :param ads_easy_promote_disable_main_screen_button:
        :param ads_easy_promote_disable_promote_post_button:

        :return: В случае успеха возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'edit'
        return self._call(method_name, params)

    def editAddress(self, group_id: str = None, address_id: str = None, title: str = None, address: str = None,
                    additional_address: str = None, country_id: str = None, city_id: str = None, metro_id: str = None,
                    latitude: str = None, longitude: str = None, phone: str = None, work_info_status: str = None,
                    timetable: str = None, is_main_address: str = None) -> dict:
        """
        Позволяет отредактировать адрес в сообществе.  Список адресов может быть получен методом groups.getAddresses.
        Для того, чтобы воспользоваться этим методом, Вы должны быть администратором сообщества

        :param group_id: идентификатор сообщества, в которое добавляется адрес.
        :param address_id: идентификатор адреса
        :param title: заголовок адреса
        :param address: строка адреса Невский проспект, дом 28
        :param additional_address: дополнительное описание адреса. Второй этаж, налево
        :param country_id: идентификатор страны. Для получения можно использовать database.getCountries
        :param city_id: идентификатор города. Для получения можно использовать database.getCities
        :param metro_id: идентификатор станции метро. Для получения можно использовать database.getMetroStations
        :param latitude: географическая широта отметки, заданная в градусах (от -90 до 90).
        :param longitude: географическая долгота отметки, заданная в градусах (от -180 до 180).
        :param phone: номер телефона
        :param work_info_status: тип расписания. Возможные значения:   no_information — нет информации о
            расписании;  temporarily_closed — временно закрыто;  always_opened — открыто круглосуточно;
            forever_closed — закрыто навсегда;  timetable — открыто в указанные часы работы. Для этого типа
            расписания необходимо передать параметр timetable;
        :param timetable: для типа timetable можно передать расписание в формате json. Время передается в минутах
            от 0 часов. Ключ по дню означает, что день рабочий. open_time, close_time — начало и конец рабочего дня.
            break_open_time, break_close_time - время перерыва {    "mon": {      "open_time": 1080,
                "close_time": 1380    },    "tue": {      "open_time": 1080,      "close_time": 1380    },    "wed":
            {      "open_time": 1080,      "close_time": 1320    },    "thu": {      "open_time": 1080,
                "close_time": 1320    },    "fri": {      "open_time": 1080,      "close_time": 1320    },    "sat":
            {      "open_time": 1080,      "close_time": 1320,      "break_open_time": 1200,      "break_close_time":
            1230    }  }
        :param is_main_address: установить адрес основным. Информация об основном адресе сразу показывается в
            сообществе. Для получения информации об остальных адресах нужно перейти к списку адресов.

        :return
        """

        params = locals()
        method_name = self._base_method + 'editAddress'
        return self._call(method_name, params)

    def editCallbackServer(self, group_id: str = None, server_id: str = None, url: str = None, title: str = None,
                           secret_key: str = None) -> dict:
        """
        Редактирует данные сервера для Callback API в сообществе.

        :param group_id: идентификатор сообщества.
        :param server_id: идентификатор сервера, данные которого нужно отредактировать.
        :param url: новый URL сервера.
        :param title: новое название сервера.
        :param secret_key: новый секретный ключ сервера.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'editCallbackServer'
        return self._call(method_name, params)

    def editLink(self, group_id: str = None, link_id: str = None, text: str = None) -> dict:
        """
        Позволяет редактировать ссылки в сообществе.

        :param group_id: идентификатор сообщества, в которое добавляется ссылка.
        :param link_id: идентификатор ссылки.
        :param text: новый текст описания для ссылки.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'editLink'
        return self._call(method_name, params)

    def editManager(self, group_id: str = None, user_id: str = None, role: str = None, is_contact: str = None,
                    contact_position: str = None, contact_phone: str = None, contact_email: str = None) -> dict:
        """
        Позволяет назначить/разжаловать руководителя в сообществе или изменить уровень его полномочий.

        :param group_id: идентификатор сообщества (указывается без знака «минус»).
        :param user_id: идентификатор пользователя, чьи полномочия в сообществе нужно изменить.
        :param role: уровень полномочий:   moderator — модератор;  editor — редактор;  administrator —
            администратор.   Если параметр не задан, с пользователя user_id снимаются полномочия руководителя.
        :param is_contact: отображать ли пользователя в блоке контактов сообщества.
        :param contact_position: должность пользователя, отображаемая в блоке контактов.
        :param contact_phone: телефон пользователя, отображаемый в блоке контактов.
        :param contact_email: email пользователя, отображаемый в блоке контактов.

        :return: В случае успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'editManager'
        return self._call(method_name, params)

    def enableOnline(self, group_id: str = None) -> dict:
        """
        Включает статус «онлайн» в сообществе.

        :param group_id: идентификатор сообщества.

        :return: После успешного выполнения возращает 1
        """

        params = locals()
        method_name = self._base_method + 'enableOnline'
        return self._call(method_name, params)

    def get(self, user_id: str = None, extended: str = None, filter: str = None, fields: str = None, offset: str = None,
            count: str = None) -> dict:
        """
        Возвращает список сообществ указанного пользователя.

        :param user_id: идентификатор пользователя, информацию о сообществах которого требуется получить.
        :param extended: если указать в качестве этого параметра 1, то будет возвращена полная информация о
            группах пользователя. По умолчанию 0.
        :param filter: список фильтров сообществ, которые необходимо вернуть, перечисленные через запятую.
            Доступны значения admin, editor, moder, advertiser, groups, publics, events, hasAddress. По умолчанию
            возвращаются все сообщества пользователя.  При указании фильтра hasAddress вернутся сообщества, в которых
            указаны адреса в соответствующем блоке, admin будут возвращены сообщества, в которых пользователь
            является администратором, editor — администратором или редактором, moder — администратором, редактором
            или модератором, advertiser — рекламодателем. Если передано несколько фильтров, то их результат
            объединяется.
        :param fields: список дополнительных полей, которые необходимо вернуть. Возможные значения: city,
            country, place, description, wiki_page, members_count, counters, start_date, finish_date, can_post,
            can_see_all_posts, activity, status, contacts, links, fixed_post, verified, site, can_create_topic.
            Подробнее см. описание полей объекта group.  Обратите внимание, этот параметр учитывается только при
            extended=1.
        :param offset: смещение, необходимое для выборки определённого подмножества сообществ.
        :param count: количество сообществ, информацию о которых нужно вернуть.

        :return: После успешного выполнения возвращает объект, содержащий число результатов в поле count
            (integer) и массив идентификаторов сообщества в поле items ([integer]).  Если был задан параметр
            extended=1, возвращает объект, содержащий число результатов в поле count (integer) и массив объектов,
            описывающих сообщества, в поле items
        """

        params = locals()
        method_name = self._base_method + 'get'
        return self._call(method_name, params)

    def getAddresses(self, group_id: str = None, address_ids: str = None, latitude: str = None, longitude: str = None,
                     offset: str = None, count: str = None, fields: str = None) -> dict:
        """
        Возвращает адрес указанного сообщества.

        :param group_id: идентификатор сообщества.
        :param address_ids: перечисленные через запятую идентификаторы адресов, информацию о которых необходимо
            вернуть.
        :param latitude: географическая широта отметки, заданная в градусах (от -90 до 90).
        :param longitude: географическая долгота отметки, заданная в градусах (от -180 до 180).
        :param offset: смещение, необходимое для выборки определенного подмножества черного списка.
        :param count: количество адресов, которое необходимо вернуть.
        :param fields: список дополнительных полей сообществ, которые необходимо вернуть.

        :return: После успешного выполнения возвращает объект, содержащий число результатов в поле count и массив
            объектов адресов в поле items
        """

        params = locals()
        method_name = self._base_method + 'getAddresses'
        return self._call(method_name, params)

    def getBanned(self, group_id: str = None, offset: str = None, count: str = None, fields: str = None,
                  owner_id: str = None) -> dict:
        """
        Возвращает список забаненных пользователей и сообществ в сообществе.

        :param group_id: идентификатор сообщества.
        :param offset: смещение, необходимое для выборки определенного подмножества черного списка.
        :param count: количество пользователей, которое необходимо вернуть.
        :param fields: список дополнительных полей профилей и сообществ, которые необходимо вернуть.
        :param owner_id: идентификатор пользователя или сообщества из чёрного списка, информацию о котором нужно
            получить.

        :return: После успешного выполнения возвращает общее число результатов в поле count (integer) и
            информацию о пользователях и сообществах из чёрного списка в поле items (array). Каждый объект в массиве
            items содержит поля:   type (string) — тип. Возможные значения:   group — сообщество;  profile —
            пользователь.   group (object) — информация о сообществе (для type = group). Объект сообщества.  profile
            (object) — информация о пользователе (для type = profile). Объект пользователя.  ban_info (object) —
            информация о блокировке в сообществе. Объект, который содержит поля:   Объект ban_info — информация о
            внесении в черный список сообщества.  admin_id идентификатор администратора, который добавил пользователя
            или сообщество в черный список.   integer date дата добавления в черный список в формате Unixtime.
            integer reason причина добавления в черный список. Возможные значения:   0 — другое (по умолчанию);  1 —
            спам;  2 — оскорбление участников;  3 — нецензурные выражения;  4 — сообщения не по теме.    integer
            comment текст комментария.   string end_date дата окончания блокировки (0 — блокировка вечная).   intege
        """

        params = locals()
        method_name = self._base_method + 'getBanned'
        return self._call(method_name, params)

    def getById(self, group_ids: str = None, group_id: str = None, fields: str = None) -> dict:
        """
        Возвращает информацию о заданном сообществе или о нескольких сообществах.

        :param group_ids: идентификаторы или короткие имена сообществ. Максимальное число идентификаторов — 500.
        :param group_id: идентификатор или короткое имя сообщества.
        :param fields: список дополнительных полей, которые необходимо вернуть. Например: city, country, place,
            description, wiki_page, market, members_count, counters, start_date, finish_date, can_post,
            can_see_all_posts, activity, status, contacts, links, fixed_post, verified, site, ban_info, cover. Полный
            список полей доступен на этой странице.  Обратите внимание, для получения некоторых полей требуется право
            доступа groups. Подробнее см. описание полей объекта group

        :return: После успешного выполнения возвращает массив объектов, описывающих сообщества
        """

        params = locals()
        method_name = self._base_method + 'getById'
        return self._call(method_name, params)

    def getCallbackConfirmationCode(self, group_id: str = None) -> dict:
        """
        Позволяет получить строку, необходимую для подтверждения адреса сервера в Callback API.

        :param group_id: идентификатор сообщества.

        :return: Возвращает строку, которую необходимо использовать в качестве ответа на уведомление с типом
            "confirmation" для подтверждения адреса сервера в Callback API.  Обратите внимание, что код, возвращаемый
            методом, можно использовать только для настройки сервера средствами API. В настройках Вашего сообщества
            на сайте ВКонтакте код будет отличаться
        """

        params = locals()
        method_name = self._base_method + 'getCallbackConfirmationCode'
        return self._call(method_name, params)

    def getCallbackServers(self, group_id: str = None, server_ids: str = None) -> dict:
        """
        Получает информацию о серверах для Callback API в сообществе.

        :param group_id: идентификатор сообщества.
        :param server_ids: идентификаторы серверов, данные о которых нужно получить. По умолчанию возвращаются
            все серверы.

        :return: Возвращает число серверов в поле count (integer) и массив объектов items с данными о серверах.
            Каждый объект массива items содержит поля:   id (integer) — идентификатор сервера;  title (string) —
            название сервера;  creator_id (integer) — идентификатор пользователя, который добавил сервер (может
            содержать 0);  url (string) — URL сервера;  secret_key (string) — секретный ключ;  status (string) —
            статус сервера. Возможные значения:   unconfigured — адрес не задан;  failed — подтвердить адрес не
            удалось;  wait — адрес ожидает подтверждения;  ok — сервер подключен
        """

        params = locals()
        method_name = self._base_method + 'getCallbackServers'
        return self._call(method_name, params)

    def getCallbackSettings(self, group_id: str = None, server_id: str = None) -> dict:
        """
        Позволяет получить настройки уведомлений Callback API для сообщества.

        :param group_id: идентификатор сообщества.
        :param server_id: идентификатор сервера.

        :return: После успешного выполнения возвращает объект, содержащий настройки уведомлений в формате
            «название события» : «статус» (0 — уведомления о событии выключены, 1 — уведомления о событии включены).
            Объект содержит следующие поля:  message_new новое сообщение  integer, [0,1] message_reply новое
            исходящее сообщение   integer, [0,1] message_edit редактирование сообщения   integer, [0,1] message_allow
            новая подписка на сообщения   integer, [0,1] message_deny новый запрет сообщений   integer, [0,1]
            photo_new добавление новой фотографии   integer, [0,1] audio_new добавление новой аудиозаписи   integer,
            [0,1] video_new добавление новой видеозаписи   integer, [0,1] wall_reply_new добавление нового
            комментария на стене   integer, [0,1] wall_reply_edit редактирование комментария на стене   integer,
            [0,1] wall_reply_delete удаление комментария на стене   integer, [0,1] wall_post_new добавление новой
            записи на стене   integer, [0,1] wall_repost новый репост записи на стене   integer, [0,1] board_post_new
            добавление нового комментария в обсуждении   integer, [0,1] board_post_edit редактирование комментария в
            обсуждении   integer, [0,1] board_post_delete удаление комментария в обсуждении   integer, [0,1]
            board_post_restore восстановление комментария в обсуждении   integer, [0,1] photo_comment_new добавление
            нового комментария к фото  integer, [0,1] photo_comment_edit редактирование комментария к фото  integer,
            [0,1] photo_comment_delete удаление комментария к фото  integer, [0,1] photo_comment_restore
            восстановление комментария к фото  integer, [0,1] video_comment_new добавление нового комментария к видео
            integer, [0,1] video_comment_edit редактирование комментария к видео  integer, [0,1] video_comment_delete
            удаление комментария к видео  integer, [0,1] video_comment_restore восстановление комментария к видео
            integer, [0,1] market_comment_new добавление нового комментария к товару  integer, [0,1]
            market_comment_edit редактирование комментария к товару  integer, [0,1] market_comment_delete удаление
            комментария к товару  integer, [0,1] market_comment_restore восстановление удалённого комментария к
            товару  integer, [0,1] poll_vote_new новый голос в публичном опросе  integer, [0,1] group_join вступление
            в сообщество   integer, [0,1] group_leave выход участника из сообщества   integer, [0,1] user_block
            занесение пользователя в черный список   integer, [0,1] user_unblock удаление пользователя из черного
            списка   integer, [0,1] group_change_settings изменение настроек сообщества   integer, [0,1]
            group_change_photo изменение главной фотографии   integer, [0,1] group_officers_edit изменение
            руководства сообщества   integer, [0,1
        """

        params = locals()
        method_name = self._base_method + 'getCallbackSettings'
        return self._call(method_name, params)

    def getCatalog(self, category_id: str = None, subcategory_id: str = None) -> dict:
        """
        Возвращает список сообществ выбранной категории каталога.

        :param category_id: идентификатор категории, полученный в методе groups.getCatalogInfo.
        :param subcategory_id: идентификатор подкатегории, полученный в методе groups.getCatalogInfo.

        :return: После успешного выполнения возвращает объект, содержащий число результатов в поле count
            (integer) и массив объектов, описывающих сообщества, в поле items
        """

        params = locals()
        method_name = self._base_method + 'getCatalog'
        return self._call(method_name, params)

    def getCatalogInfo(self, extended: str = None, subcategories: str = None) -> dict:
        """
        Возвращает список категорий для каталога сообществ.

        :param extended: 1 — вернуть информацию о количестве сообществ в категории и три сообщества для
            предпросмотра.  По умолчанию 0.
        :param subcategories: 1 — вернуть информацию об подкатегориях.  По умолчанию 0.

        :return: После успешного выполнения возвращает поле enabled (0 — каталог недоступен для пользователя, 1 —
            каталог доступен), и, если enabled=1, массив categories объектов — категорий товаров.  Объект массива
            categories — категория каталога товаров.  id идентификатор категории.   положительное число name название
            категории.   строка subcategories поле возвращается при использовании subcategories=1. Массив объектов-
            подкатегорий. Каждый из объектов содержит поля id и name, содержащие идентификатор и название
            подкатегории.  Дополнительные поля (extended=1)  page_count количество сообществ в категории.
            положительное число page_previews массив объектов сообществ для предпросмотра
        """

        params = locals()
        method_name = self._base_method + 'getCatalogInfo'
        return self._call(method_name, params)

    def getInvitedUsers(self, group_id: str = None, offset: str = None, count: str = None, fields: str = None,
                        name_case: str = None) -> dict:
        """
        Возвращает список пользователей, которые были приглашены в группу.

        :param group_id: идентификатор группы, список приглашенных в которую пользователей нужно вернуть.
        :param offset: смещение, необходимое для выборки определённого подмножества пользователей.
        :param count: количество пользователей, информацию о которых нужно вернуть.
        :param fields: список дополнительных полей, которые необходимо вернуть.  Доступные значения: nickname,
            domain, sex, bdate, city, country, timezone, photo_50, photo_100, photo_200_orig, has_mobile, contacts,
            education, online, relation, last_seen, status, can_write_private_message, can_see_all_posts, can_post,
            universities
        :param name_case: падеж для склонения имени и фамилии пользователя. Возможные значения: именительный –
            nom, родительный – gen, дательный – dat, винительный – acc, творительный – ins, предложный – abl. По
            умолчанию nom.

        :return: Возвращает список объектов пользователей
        """

        params = locals()
        method_name = self._base_method + 'getInvitedUsers'
        return self._call(method_name, params)

    def getInvites(self, offset: str = None, count: str = None, extended: str = None) -> dict:
        """
        Данный метод возвращает список приглашений в сообщества и встречи текущего пользователя.

        :param offset: смещение, необходимое для выборки определённого подмножества приглашений.
        :param count: количество приглашений, которое необходимо вернуть.
        :param extended: 1 — вернуть дополнительную информацию о пользователях, отправлявших приглашения. По
            умолчанию — 0.

        :return: После успешного выполнения возвращает количество результатов в поле count и массив объектов,
            описывающих сообщества, с дополнительным полем invited_by, содержащим идентификатор пользователя, который
            отправил приглашение, в поле items.  Если был передан параметр extended=1, дополнительно будет возвращен
            список profiles пользователей, отправивших приглашения. Каждый объект в списке содержит поля id,
            first_name, last_name
        """

        params = locals()
        method_name = self._base_method + 'getInvites'
        return self._call(method_name, params)

    def getLongPollServer(self, group_id: str = None) -> dict:
        """
        Возвращает данные для подключения к Bots Longpoll API.

        :param group_id: идентификатор сообщества.

        :return: Возвращает объект, который содержит следующие поля:   key (string) — ключ;  server (string) —
            url сервера;  ts (string) — timestamp
        """

        params = locals()
        method_name = self._base_method + 'getLongPollServer'
        return self._call(method_name, params)

    def getLongPollSettings(self, group_id: str = None) -> dict:
        """
        Получает настройки Bots Longpoll API для сообщества.

        :param group_id: идентификатор сообщества.

        :return: Возвращает объект, который содержит следующие поля:   is_enabled (boolean) — true, если Bots
            Longpoll включен в сообществе.  events (object) — настройки Bots Longpoll. объект, содержащий настройки
            уведомлений в формате «название события» : «статус» (0 — уведомления о событии выключены, 1 — уведомления
            о событии включены). Объект содержит следующие поля:   message_new новое сообщение  integer, [0,1]
            message_reply новое исходящее сообщение   integer, [0,1] message_allow новая подписка на сообщения
            integer, [0,1] message_deny новый запрет сообщений   integer, [0,1] photo_new добавление новой фотографии
            integer, [0,1] audio_new добавление новой аудиозаписи   integer, [0,1] video_new добавление новой
            видеозаписи   integer, [0,1] wall_reply_new добавление нового комментария на стене   integer, [0,1]
            wall_reply_edit редактирование комментария на стене   integer, [0,1] wall_reply_delete удаление
            комментария на стене   integer, [0,1] wall_post_new добавление новой записи на стене   integer, [0,1]
            wall_repost новый репост записи на стене   integer, [0,1] board_post_new добавление нового комментария в
            обсуждении   integer, [0,1] board_post_edit редактирование комментария в обсуждении   integer, [0,1]
            board_post_delete удаление комментария в обсуждении   integer, [0,1] board_post_restore восстановление
            комментария в обсуждении   integer, [0,1] photo_comment_new добавление нового комментария к фото
            integer, [0,1] photo_comment_edit редактирование комментария к фото  integer, [0,1] photo_comment_delete
            удаление комментария к фото  integer, [0,1] photo_comment_restore восстановление комментария к фото
            integer, [0,1] video_comment_new добавление нового комментария к видео  integer, [0,1] video_comment_edit
            редактирование комментария к видео  integer, [0,1] video_comment_delete удаление комментария к видео
            integer, [0,1] video_comment_restore восстановление комментария к видео  integer, [0,1]
            market_comment_new добавление нового комментария к товару  integer, [0,1] market_comment_edit
            редактирование комментария к товару  integer, [0,1] market_comment_delete удаление комментария к товару
            integer, [0,1] market_comment_restore восстановление удалённого комментария к товару  integer, [0,1]
            poll_vote_new новый голос в публичном опросе  integer, [0,1] group_join вступление в сообщество
            integer, [0,1] group_leave выход участника из сообщества   integer, [0,1] user_block занесение
            пользователя в черный список   integer, [0,1] user_unblock удаление пользователя из черного списка
            integer, [0,1] group_change_settings изменение настроек сообщества   integer, [0,1] group_change_photo
            изменение главной фотографии   integer, [0,1] group_officers_edit изменение руководства сообщества
            integer, [0,1
        """

        params = locals()
        method_name = self._base_method + 'getLongPollSettings'
        return self._call(method_name, params)

    def getMembers(self, group_id: str = None, sort: str = None, offset: str = None, count: str = None,
                   fields: str = None, filter: str = None) -> dict:
        """
        Возвращает список участников сообщества.

        :param group_id: идентификатор или короткое имя сообщества.
        :param sort: сортировка, с которой необходимо вернуть список участников. Может принимать значения:
            id_asc — в порядке возрастания id;  id_desc — в порядке убывания id;  time_asc — в хронологическом
            порядке по вступлению в сообщество;  time_desc — в антихронологическом порядке по вступлению в
            сообщество.  Сортировка по time_asc и time_desc возможна только при вызове от модератора сообщества.
        :param offset: смещение, необходимое для выборки определенного подмножества участников. По умолчанию 0.
        :param count: количество участников сообщества, информацию о которых необходимо получить.
        :param fields: список дополнительных полей, которые необходимо вернуть.  Доступные значения: sex, bdate,
            city, country, photo_50, photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig,
            online, online_mobile, lists, domain, has_mobile, contacts, connections, site, education, universities,
            schools, can_post, can_see_all_posts, can_see_audio, can_write_private_message, status, last_seen,
            common_count, relation, relatives
        :param filter:   friends — будут возвращены только друзья в этом сообществе.  unsure — будут возвращены
            пользователи, которые выбрали «Возможно пойду» (если сообщество относится к мероприятиям).  managers —
            будут возвращены только руководители сообщества (доступно при запросе с передачей access_token от имени
            администратора сообщества).

        :return: После успешного выполнения возвращает объект, содержащий число результатов в поле count
            (integer) и массив идентификаторов пользователей в поле items ([integer]).  Если был передан параметр
            filter=managers, возвращается дополнительное поле role (string), которое содержит уровень полномочий
            руководителя:   moderator — модератор;  editor — редактор;  administrator — администратор;  creator —
            создатель сообщества
        """

        params = locals()
        method_name = self._base_method + 'getMembers'
        return self._call(method_name, params)

    def getOnlineStatus(self, group_id: str = None) -> dict:
        """
        Получает информацию о статусе «онлайн» в сообществе.

        :param group_id: идентификатор сообщества.

        :return: Возвращает объект, который содержит поля:   status — статус сообщества. Возможные значения:
            none — сообщество не онлайн;  online — сообщество онлайн (отвечает мгновенно);  answer_mark — сообщество
            отвечает быстро.   minutes — оценка времени ответа в минутах (для status = answer_mark)
        """

        params = locals()
        method_name = self._base_method + 'getOnlineStatus'
        return self._call(method_name, params)

    def getRequests(self, group_id: str = None, offset: str = None, count: str = None, fields: str = None) -> dict:
        """
        Возвращает список заявок на вступление в сообщество.

        :param group_id: идентификатор сообщества (указывается без знака «минус»).
        :param offset: смещение, необходимое для выборки определенного подмножества результатов. По умолчанию —
            0.
        :param count: число результатов, которые необходимо вернуть.
        :param fields: список дополнительных полей профилей, которые необходимо вернуть. См. подробное описание.
            Доступные значения: sex, bdate, city, country, photo_50, photo_100, photo_200_orig, photo_200,
            photo_400_orig, photo_max, photo_max_orig, online, online_mobile, domain, has_mobile, contacts,
            connections, site, education, universities, schools, can_post, can_see_all_posts, can_see_audio,
            can_write_private_message, status, last_seen, common_count, relation, relatives, counters, screen_name,
            maiden_name, timezone, occupation,activities, interests, music, movies, tv, books, games, about, quotes

        :return: Возвращает список идентификаторов пользователей, отправивших заявки на вступление в сообщество.
            Если было передано значение в параметре fields, возвращается список объектов пользователей
        """

        params = locals()
        method_name = self._base_method + 'getRequests'
        return self._call(method_name, params)

    def getSettings(self, group_id: str = None) -> dict:
        """
        Позволяет получать данные, необходимые для отображения страницы редактирования данных сообщества.

        :param group_id: идентификатор сообщества, данные которого необходимо получить.

        :return: В случае успешного выполнения метод вернет объект, содержащий данные сообщества, которые
            позволят отобразить форму редактирования для метода groups.edit.  В ответе содержится объект с полями:
            title  stringназвание сообщества. description  stringописание сообщества. address  stringкороткий адрес.
            wall  integerнастройки стены. photos  integerнастройки фотографий. video  integerнастройки видеозаписей.
            audio  integerнастройки аудиозаписей. docs  integerнастройки документов. topics  integerнастройки
            обсуждений. wiki  integerнастройки вики-страниц. messages  integerсообщения сообщества. Возможные
            значения:   1 — включены;  0 — выключены. obscene_filter integerнастройки фильтра нецензурных слов.
            obscene_stopwords integerнастройки фильтра комментариев по ключевым словам. obscene_words stringсписок
            стоп-слов. public_category  integerкатегория публичной страницы. public_subcategory  integerподкатегория
            публичной страницы. public_category_list  arrayсписок возможных категорий для публичных страниц. access
            integerтип сообщества. subject  integerидентификатор тематики. subject_list  arrayсписок возможных
            тематик. Массив объектов, каждый из которых содержит поля:   id (integer) — идентификатор тематики;  name
            (string) — название тематики. rss  stringадрес RSS-ленты. website  stringадрес веб-сайта. age_limits
            integerвозрастные ограничения market  objectнастройки блока товаров. Объект, содержащий поля:   enabled
            (integer) — включен ли блок товаров (1 или 0);  comments_enabled (integer) — включены ли комментарии к
            товарам (1 или 0);  country_ids (array) — идентификаторы стран;  city_ids (array) — идентификаторы
            городов;  contact_id (integer) — идентификатор контактного лица;  currency (object) — объект, описывающий
            валюту
        """

        params = locals()
        method_name = self._base_method + 'getSettings'
        return self._call(method_name, params)

    def getTagList(self, group_id: str = None) -> dict:
        """
        Возвращает список тегов сообщества

        :param group_id: Идентификатор сообщества

        :return
        """

        params = locals()
        method_name = self._base_method + 'getTagList'
        return self._call(method_name, params)

    def getTokenPermissions(self) -> dict:
        """
        Возвращает настройки прав для ключа доступа сообщества.

        :return: Возвращает объект, который содержит поля:   mask (integer) — битовая маска ключа доступа;
            settings (array) — массив объектов, описывающих права доступа. Каждый объект в массиве содержит поля:
            setting (integer) — битовая маска права доступа;  name (string) — название права доступа
        """

        params = locals()
        method_name = self._base_method + 'getTokenPermissions'
        return self._call(method_name, params)

    def invite(self, group_id: str = None, user_id: str = None) -> dict:
        """
        Позволяет приглашать друзей в группу.

        :param group_id: идентификатор группы, в которую необходимо выслать приглашение
        :param user_id: идентификатор пользователя, которому необходимо выслать приглашение

        :return: В случае успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'invite'
        return self._call(method_name, params)

    def isMember(self, group_id: str = None, user_id: str = None, user_ids: str = None, extended: str = None) -> dict:
        """
        Возвращает информацию о том, является ли пользователь участником сообщества.

        :param group_id: идентификатор или короткое имя сообщества.
        :param user_id: идентификатор пользователя.
        :param user_ids: идентификаторы пользователей, не более 500.
        :param extended: 1 — вернуть ответ в расширенной форме. По умолчанию — 0.

        :return: Возвращает 1 в случае, если пользователь с идентификатором user_id является участником
            сообщества с идентификатором group_id, иначе 0.   При использовании параметра extended Возвращает объект,
            который содержит поля:   member (integer, [0,1]) — является ли пользователь участником сообщества;  и
            может содержать поля:   request (integer, [0,1]) — есть ли непринятая заявка от пользователя на
            вступление в группу (такую заявку можно отозвать методом groups.leave);  invitation (integer, [0,1]) —
            приглашён ли пользователь в группу или встречу;  can_invite (integer, [0,1]) — может ли автор запроса
            приглашать пользователя в группу;  can_recall (integer, [0,1]) — может ли автор отменить приглашение.
            Появляется, если invitation: 1.    При передаче нескольких идентификаторов Возвращает результат в виде
            массива объектов, в которых есть поля user_id (integer) и member (integer, [0,1])
        """

        params = locals()
        method_name = self._base_method + 'isMember'
        return self._call(method_name, params)

    def join(self, group_id: str = None, not_sure: str = None) -> dict:
        """
        Данный метод позволяет вступить в группу, публичную страницу, а также подтвердить участие во встрече.

        :param group_id: идентификатор сообщества.
        :param not_sure: опциональный параметр, учитываемый, если group_id принадлежит встрече. 1 — Возможно
            пойду. 0 — Точно пойду. По умолчанию 0.

        :return: В случае успешного вступления метод вернёт 1
        """

        params = locals()
        method_name = self._base_method + 'join'
        return self._call(method_name, params)

    def leave(self, group_id: str = None) -> dict:
        """
        Позволяет покинуть сообщество или отклонить приглашение в сообщество.

        :param group_id: идентификатор сообщества.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'leave'
        return self._call(method_name, params)

    def removeUser(self, group_id: str = None, user_id: str = None) -> dict:
        """
        Позволяет исключить пользователя из группы или отклонить заявку на вступление.

        :param group_id: идентификатор группы, из которой необходимо исключить пользователя.
        :param user_id: идентификатор пользователя, которого нужно исключить.

        :return: В случае успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'removeUser'
        return self._call(method_name, params)

    def reorderLink(self, group_id: str = None, link_id: str = None, after: str = None) -> dict:
        """
        Позволяет менять местоположение ссылки в списке.

        :param group_id: идентификатор группы, внутри которой перемещается ссылка
        :param link_id: идентификатор ссылки, которую необходимо переместить
        :param after: идентификатор ссылки после которой необходимо разместить перемещаемую ссылку. 0 – если
            ссылку нужно разместить в начале списка.

        :return: В случае успешного выполнение метод возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'reorderLink'
        return self._call(method_name, params)

    def search(self, q: str = None, type: str = None, country_id: str = None, city_id: str = None, future: str = None,
               market: str = None, sort: str = None, offset: str = None, count: str = None) -> dict:
        """
        Осуществляет поиск сообществ по заданной подстроке.

        :param q: текст поискового запроса.
        :param type: тип сообщества. Возможные значения: group, page, event.
        :param country_id: идентификатор страны.
        :param city_id: идентификатор города. При передаче этого параметра поле country_id игнорируется.
        :param future: при передаче значения 1 будут выведены предстоящие события. Учитывается только при
            передаче в качестве type значения event.
        :param market: при передаче значения 1 будут выведены сообщества с включенными товарами.
        :param sort:   0 — сортировать по умолчанию (аналогично результатам поиска в полной версии сайта);  1 —
            сортировать по скорости роста;  2 — сортировать по отношению дневной посещаемости к количеству
            пользователей;  3 — сортировать по отношению количества лайков к количеству пользователей;  4 —
            сортировать по отношению количества комментариев к количеству пользователей;  5 — сортировать по
            отношению количества записей в обсуждениях к количеству пользователей.
        :param offset: смещение, необходимое для выборки определённого подмножества результатов поиска. По
            умолчанию — 0.
        :param count: количество результатов поиска, которое необходимо вернуть. Обратите внимание — даже при
            использовании параметра offset для получения информации доступны только первые 1000 результатов.

        :return: После успешного выполнения возвращает объект, содержащий число результатов в поле count
            (integer) и массив объектов group в поле items
        """

        params = locals()
        method_name = self._base_method + 'search'
        return self._call(method_name, params)

    def setCallbackSettings(self, group_id: str = None, server_id: str = None, api_version: str = None,
                            message_new: str = None, message_reply: str = None, message_allow: str = None,
                            message_edit: str = None, message_deny: str = None, message_typing_state: str = None,
                            photo_new: str = None, audio_new: str = None, video_new: str = None,
                            wall_reply_new: str = None, wall_reply_edit: str = None, wall_reply_delete: str = None,
                            wall_reply_restore: str = None, wall_post_new: str = None, wall_repost: str = None,
                            board_post_new: str = None, board_post_edit: str = None, board_post_restore: str = None,
                            board_post_delete: str = None, photo_comment_new: str = None,
                            photo_comment_edit: str = None, photo_comment_delete: str = None,
                            photo_comment_restore: str = None, video_comment_new: str = None,
                            video_comment_edit: str = None, video_comment_delete: str = None,
                            video_comment_restore: str = None, market_comment_new: str = None,
                            market_comment_edit: str = None, market_comment_delete: str = None,
                            market_comment_restore: str = None, poll_vote_new: str = None, group_join: str = None,
                            group_leave: str = None, group_change_settings: str = None, group_change_photo: str = None,
                            group_officers_edit: str = None, user_block: str = None, user_unblock: str = None,
                            lead_forms_new: str = None) -> dict:
        """
        Позволяет задать настройки уведомлений о событиях в Callback API.

        :param group_id: идентификатор сообщества.
        :param server_id: идентификатор сервера.
        :param api_version: версия Callback API
        :param message_new: уведомления о новых сообщениях (0 — выключить, 1 — включить).
        :param message_reply: уведомления об исходящем сообщении (0 — выключить, 1 — включить).
        :param message_allow: уведомления о подписке на сообщения (0 — выключить, 1 — включить).
        :param message_edit: уведомления о редактировании сообщения (0 — выключить, 1 — включить).
        :param message_deny: уведомления о запрете на сообщения (0 — выключить, 1 — включить).
        :param message_typing_state: уведомления о наборе текста сообщения ('0 — выключить, 1'' — включить).
        :param photo_new: уведомления о добавлении новой фотографии (0 — выключить, 1 — включить).
        :param audio_new: уведомления о добавлении новой аудиозаписи (0 — выключить, 1 — включить).
        :param video_new: уведомления о добавлении новой видеозаписи (0 — выключить, 1 — включить).
        :param wall_reply_new: уведомления о добавлении нового комментария на стене (0 — выключить, 1 —
            включить).
        :param wall_reply_edit: уведомления о редактировании комментария на стене (0 — выключить, 1 — включить).
        :param wall_reply_delete: уведомления об удалении комментария на стене (0 — выключить, 1 — включить).
        :param wall_reply_restore: уведомления о восстановлении комментария на стене (0 — выключить, 1 —
            включить).
        :param wall_post_new: уведомления о новой записи на стене (0 — выключить, 1 — включить).
        :param wall_repost: уведомления о репосте записи (0 — выключить, 1 — включить).
        :param board_post_new: уведомления о создании комментария в обсуждении (0 — выключить, 1 — включить).
        :param board_post_edit: уведомления о редактировании комментария в обсуждении (0 — выключить, 1 —
            включить).
        :param board_post_restore: уведомление о восстановлении комментария в обсуждении (0 — выключить, 1 —
            включить).
        :param board_post_delete: уведомления об удалении комментария в обсуждении (0 — выключить, 1 — включить).
        :param photo_comment_new: уведомления о добавлении нового комментария к фото (0 — выключить, 1 —
            включить).
        :param photo_comment_edit: уведомления о редактировании комментария к фото (0 — выключить, 1 — включить).
        :param photo_comment_delete: уведомления об удалении комментария к фото (0 — выключить, 1 — включить).
        :param photo_comment_restore: уведомления о восстановлении комментария к фото (0 — выключить, 1 —
            включить).
        :param video_comment_new: уведомления о добавлении нового комментария к видео (0 — выключить, 1 —
            включить).
        :param video_comment_edit: уведомления о редактировании комментария к видео (0 — выключить, 1 —
            включить).
        :param video_comment_delete: уведомления об удалении комментария к видео (0 — выключить, 1 — включить).
        :param video_comment_restore: уведомления о восстановлении комментария к видео (0 — выключить, 1 —
            включить).
        :param market_comment_new: уведомления о добавлении нового комментария к товару (0 — выключить, 1 —
            включить).
        :param market_comment_edit: уведомления о редактировании комментария к товару (0 — выключить, 1 —
            включить).
        :param market_comment_delete: уведомления об удалении комментария к товару (0 — выключить, 1 — включить).
        :param market_comment_restore: уведомления о восстановлении комментария к товару (0 — выключить, 1 —
            включить).
        :param poll_vote_new: уведомления о новом голосе в публичных опросах (0 — выключить, 1 — включить).
        :param group_join: уведомления о вступлении в сообщество (0 — выключить, 1 — включить).
        :param group_leave: уведомления о выходе из сообщества (0 — выключить, 1 — включить).
        :param group_change_settings: уведомления об изменении настроек (0 — выключить, 1 — включить).
        :param group_change_photo: уведомления об изменении главной фотографии (0 — выключить, 1 — включить).
        :param group_officers_edit: уведомления об изменении руководства (0 — выключить, 1 — включить).
        :param user_block: уведомления об внесении пользователя в чёрный список (0 — выключить, 1 — включить).
        :param user_unblock: уведомления об исключении пользователя из чёрного списка (0 — выключить, 1 —
            включить).
        :param lead_forms_new: уведомления о заполнении формы

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'setCallbackSettings'
        return self._call(method_name, params)

    def setLongPollSettings(self, group_id: str = None, enabled: str = None, api_version: str = None,
                            message_new: str = None, message_reply: str = None, message_allow: str = None,
                            message_deny: str = None, message_edit: str = None, message_typing_state: str = None,
                            photo_new: str = None, audio_new: str = None, video_new: str = None,
                            wall_reply_new: str = None, wall_reply_edit: str = None, wall_reply_delete: str = None,
                            wall_reply_restore: str = None, wall_post_new: str = None, wall_repost: str = None,
                            board_post_new: str = None, board_post_edit: str = None, board_post_restore: str = None,
                            board_post_delete: str = None, photo_comment_new: str = None,
                            photo_comment_edit: str = None, photo_comment_delete: str = None,
                            photo_comment_restore: str = None, video_comment_new: str = None,
                            video_comment_edit: str = None, video_comment_delete: str = None,
                            video_comment_restore: str = None, market_comment_new: str = None,
                            market_comment_edit: str = None, market_comment_delete: str = None,
                            market_comment_restore: str = None, poll_vote_new: str = None, group_join: str = None,
                            group_leave: str = None, group_change_settings: str = None, group_change_photo: str = None,
                            group_officers_edit: str = None, user_block: str = None, user_unblock: str = None) -> dict:
        """
        Задаёт настройки для Bots Long Poll API в сообществе.

        :param group_id: идентификатор сообщества.
        :param enabled: 1 — включить Bots Long Poll, 0 — отключить.
        :param api_version: версия API
        :param message_new: уведомления о новых сообщениях (0 — выключить, 1 — включить).
        :param message_reply: уведомления об исходящем сообщении (0 — выключить, 1 — включить).
        :param message_allow: уведомления о подписке на сообщения (0 — выключить, 1 — включить).
        :param message_deny: уведомления о запрете на сообщения (0 — выключить, 1 — включить).
        :param message_edit: уведомления о редактировании сообщения (0 — выключить, 1 — включить).
        :param message_typing_state:
        :param photo_new: уведомления о добавлении новой фотографии (0 — выключить, 1 — включить).
        :param audio_new: уведомления о добавлении новой аудиозаписи (0 — выключить, 1 — включить).
        :param video_new: уведомления о добавлении новой видеозаписи (0 — выключить, 1 — включить).
        :param wall_reply_new: уведомления о добавлении нового комментария на стене (0 — выключить, 1 —
            включить).
        :param wall_reply_edit: уведомления о редактировании комментария на стене (0 — выключить, 1 — включить).
        :param wall_reply_delete: уведомления об удалении комментария на стене (0 — выключить, 1 — включить).
        :param wall_reply_restore: уведомления о восстановлении комментария на стене (0 — выключить, 1 —
            включить).
        :param wall_post_new: уведомления о новой записи на стене (0 — выключить, 1 — включить).
        :param wall_repost: уведомления о репосте записи (0 — выключить, 1 — включить).
        :param board_post_new: уведомления о создании комментария в обсуждении (0 — выключить, 1 — включить).
        :param board_post_edit: уведомления о редактировании комментария в обсуждении (0 — выключить, 1 —
            включить).
        :param board_post_restore: уведомление о восстановлении комментария в обсуждении (0 — выключить, 1 —
            включить).
        :param board_post_delete: уведомления об удалении комментария в обсуждении (0 — выключить, 1 — включить).
        :param photo_comment_new: уведомления о добавлении нового комментария к фото (0 — выключить, 1 —
            включить).
        :param photo_comment_edit: уведомления о редактировании комментария к фото (0 — выключить, 1 — включить).
        :param photo_comment_delete: уведомления об удалении комментария к фото (0 — выключить, 1 — включить).
        :param photo_comment_restore: уведомления о восстановлении комментария к фото (0 — выключить, 1 —
            включить).
        :param video_comment_new: уведомления о добавлении нового комментария к видео (0 — выключить, 1 —
            включить).
        :param video_comment_edit: уведомления о редактировании комментария к видео (0 — выключить, 1 —
            включить).
        :param video_comment_delete: уведомления об удалении комментария к видео (0 — выключить, 1 — включить).
        :param video_comment_restore: уведомления о восстановлении комментария к видео (0 — выключить, 1 —
            включить).
        :param market_comment_new: уведомления о добавлении нового комментария к товару (0 — выключить, 1 —
            включить).
        :param market_comment_edit: уведомления о редактировании комментария к товару (0 — выключить, 1 —
            включить).
        :param market_comment_delete: уведомления об удалении комментария к товару (0 — выключить, 1 — включить).
        :param market_comment_restore: уведомления о восстановлении комментария к товару (0 — выключить, 1 —
            включить).
        :param poll_vote_new: уведомления о новом голосе в публичных опросах (0 — выключить, 1 — включить).
        :param group_join: уведомления о вступлении в сообщество (0 — выключить, 1 — включить).
        :param group_leave: уведомления о выходе из сообщества (0 — выключить, 1 — включить).
        :param group_change_settings: уведомления об изменении настроек (0 — выключить, 1 — включить).
        :param group_change_photo: уведомления об изменении главной фотографии (0 — выключить, 1 — включить).
        :param group_officers_edit: уведомления об изменении руководства (0 — выключить, 1 — включить).
        :param user_block: уведомления об внесении пользователя в чёрный список (0 — выключить, 1 — включить).
        :param user_unblock: уведомления об исключении пользователя из чёрного списка (0 — выключить, 1 —
            включить).

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'setLongPollSettings'
        return self._call(method_name, params)

    def setSettings(self, group_id: str = None, messages: str = None, bots_capabilities: str = None,
                    bots_start_button: str = None, bots_add_to_chat: str = None) -> dict:
        """
        Устанавливает настройки сообщества

        :param group_id: идентификатор сообщества.
        :param messages: сообщения сообщества. Возможные значения:   0 — выключены;  1 — включены.
        :param bots_capabilities: возможности ботов (использование клавиатуры, добавление в беседу). Возможные
            значения:   0 — выключены;  1 — включены.
        :param bots_start_button: кнопка «Начать» в диалоге с сообществом.  Работает, в случае если
            bots_capabilities=1.  Если эта настройка включена, то при заходе в беседу с Вашим сообществом в первый
            раз пользователь увидит кнопку с командой «Начать», которая отправляет команду start. Payload этого
            сообщения будет выглядеть так: {"command":"start"}    Возможные значения:   0 — выключена;  1 — включена.
        :param bots_add_to_chat: добавление бота в беседы.  Работает, в случае если bots_capabilities=1.
            Возможные значения:   0 — запрещено;  1 — разрешено.

        :return: В случае успеха возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'setSettings'
        return self._call(method_name, params)

    def tagAdd(self, group_id: str = None, tag_name: str = None, tag_color: str = None) -> dict:
        """
        Позволяет добавить новый тег в сообщество

        :param group_id: Идентификатор сообщества
        :param tag_name: Имя тега
        :param tag_color: Цвет тега. Разрешается использовать следующие цвета: 4bb34b, 5c9ce6, e64646, 792ec0,
            63b9ba, ffa000, ffc107, 76787a, 9e8d6b, 45678f, 539b9c, 454647, 7a6c4f, 6bc76b, 5181b8, ff5c5c, a162de,
            7ececf, aaaeb3, bbaa84

        :return
        """

        params = locals()
        method_name = self._base_method + 'tagAdd'
        return self._call(method_name, params)

    def tagBind(self, group_id: str = None, tag_id: str = None, user_id: str = None, act: str = None) -> dict:
        """
        Позволяет "привязывать" и "отвязывать" теги сообщества к беседам.

        :param group_id: Идентификатор группы
        :param tag_id: Идентификатор тега
        :param user_id:
        :param act: Действие с тегом   "bind" -  привязать  "unbind" - отвязать

        :return
        """

        params = locals()
        method_name = self._base_method + 'tagBind'
        return self._call(method_name, params)

    def tagDelete(self, group_id: str = None, tag_id: str = None) -> dict:
        """
        Позволяет удалить тег сообщества

        :param group_id: Идентификатор группы
        :param tag_id: Идентификатор удаляемого тега

        :return
        """

        params = locals()
        method_name = self._base_method + 'tagDelete'
        return self._call(method_name, params)

    def tagUpdate(self, group_id: str = None, tag_id: str = None, tag_name: str = None, tag_color: str = None) -> dict:
        """
        Позволяет изменить существующий тег

        :param group_id: Идентификатор сообщества
        :param tag_id: Идентификатор тега
        :param tag_name: Имя тега
        :param tag_color: Цвет тега. Разрешается использовать следующие цвета: 4bb34b, 5c9ce6, e64646, 792ec0,
            63b9ba, ffa000, ffc107, 76787a, 9e8d6b, 45678f, 539b9c, 454647, 7a6c4f, 6bc76b, 5181b8, ff5c5c, a162de,
            7ececf, aaaeb3, bbaa84

        :return
        """

        params = locals()
        method_name = self._base_method + 'tagUpdate'
        return self._call(method_name, params)

    def unban(self, group_id: str = None, owner_id: str = None) -> dict:
        """
        Убирает пользователя или группу из черного списка сообщества.

        :param group_id: идентификатор сообщества.
        :param owner_id: идентификатор пользователя или группы, которого нужно убрать из черного списка.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'unban'
        return self._call(method_name, params)
