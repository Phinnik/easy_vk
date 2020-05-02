from ApiMethod import ApiMethod


class LeadForms(ApiMethod):
    def __init__(self, access_token, v, session, calls_per_second):
        super(LeadForms, self).__init__(access_token, v, session, calls_per_second)
        self._base_method = 'leadForms.'

    def create(self, group_id: str = None, name: str = None, title: str = None, description: str = None,
               questions: str = None, policy_link_url: str = None, photo: str = None, confirmation: str = None,
               site_link_url: str = None, active: str = None, once_per_user: str = None, pixel_code: str = None,
               notify_admins: str = None, notify_emails: str = None) -> dict:
        """
        Создаёт форму сбора заявок.

        :param group_id: Идентификатор группы, в которой надо создать форму.
        :param name: Название формы (видно только администратору).
        :param title: Заголовок формы (видят пользователи).
        :param description: Описание формы.
        :param questions: Информация о вопросах формы. Массив структур следующего формата:   type — тип вопроса;
            label — заголовок вопроса (только для нестандартных вопросов);  key — уникальный ключ вопроса
            (необязательно; только для нестандартных вопросов);  options — массив возможных ответов на вопрос (только
            для нестандартных вопросов типа radio, select, checkbox);   Типы стандартных вопросов:   first_name —
            имя;  patronymic_name — отчество;  last_name — фамилия;  email — адрес электронной почты;  phone_number —
            номер телефона;  age — возраст;  birthday — день рождения;  location — город и страна.   Типы
            нестандартных вопросов:   input — простое текстовое поле (строка);  textarea — большое текстовое поле
            (абзац);  radio — выбор одного из нескольких вариантов;  checkbox — выбор нескольких вариантов;  select —
            выбор одного варианта из выпадающего списка.   options должен быть массивом структур, описывающих
            варианты ответа:   label — текст ответа;  key — ключ ответа (необязательно).   Пример:[     {
                  "type":"first_name"     },     {        "type":"input",        "label":"Кличка кота"     },     {
                  "type":"select",        "key":"favorite_color",        "label":"Любимый цвет",        "options":[{
                    "key":"red",          "label":"Красный"        },{          "key":"green",
                    "label":"Зелёный"        }]     },     {        "type":"radio",        "label":"Я ношу часы...",
                  "options":[{           "key":"left",           "label":"на левой руке"        },{
                     "key":"right",           "label":"на правой руке"        }]     },     {
                  "type":"checkbox",        "key":"visited_cities",        "label":"Города, в которых я был",
                  "options":[{           "label":"Екатеринбург"        },{           "label":"Волгоград"        },{
                     "label":"Санкт-Петербург"        }]     }  ]
        :param policy_link_url: Ссылка на политику конфиденциальности.
        :param photo: Обложка формы.  Используйте значение, полученное после загрузки фотографии на сервер. См.
            метод leadForms.getUploadURL.  Также можно переиспользовать существующую фотографию из другой формы.
            Используйте значение поля photo, которое возвращает метод leadForms.get или leadForms.list.
        :param confirmation: Текст подтверждения, который увидит пользователь после отправки формы.
        :param site_link_url: Ссылка на сайт или сообщество автора формы.
        :param active: Передайте 1, чтобы активировать форму сразу после создания. Пользователи могут оставлять
            заявки только в активных формах.
        :param once_per_user: Передайте 1, чтобы разрешить каждому пользователю заполнять форму только один раз.
        :param pixel_code: Передайте код пикселя ретаргетинга ВКонтакте в виде VK-RTRG-000000-XXXXX. По этому
            пикселю будет собираться аудитория пользователей, открывших форму. Подробнее о пикселе см. здесь.
        :param notify_admins: Передайте список идентификаторов пользователей, которым будут отправлены оповещения
            о заполнении пользователями формы. Оповещения могут быть отправлены только администраторам сообщества.
        :param notify_emails: Передайте список email-адресов, разделённых запятой, на которые будут отправлены
            оповещения о заполнении пользователями формы. Можно указать до 10 адресов.

        :return: Возвращается структура с информацией о созданной форме:   form_id — идентификатор формы;  url —
            ссылка на форму
        """

        params = locals()
        method_name = self._base_method + 'create'
        return self._call(method_name, params)

    def delete(self, group_id: str = None, form_id: str = None) -> dict:
        """
        Удаляет форму сбора заявок.

        :param group_id: Идентификатор группы, из которой надо удалить форму.
        :param form_id: Идентификатор удаляемой формы.

        :return: Возвращает идентификатор удалённой форм
        """

        params = locals()
        method_name = self._base_method + 'delete'
        return self._call(method_name, params)

    def get(self, group_id: str = None, form_id: str = None) -> dict:
        """
        Возвращает информацию о форме сбора заявок.

        :param group_id: Идентификатор группы, в которой находится форма.
        :param form_id: Идентификатор формы.

        :return: Возвращает структуру с информацией о форме. Значения полей см. в методе leadForms.create.
            Дополнительно возвращает следующие поля:   form_id — идентификатор формы;  leads_count — количество
            заявок;  url — ссылка на форму
        """

        params = locals()
        method_name = self._base_method + 'get'
        return self._call(method_name, params)

    def getLeads(self, group_id: str = None, form_id: str = None, limit: str = None,
                 next_page_token: str = None) -> dict:
        """
        Возвращает заявки формы.

        :param group_id: идентификатор сообщества, в котором находится форма.
        :param form_id: идентификатор формы.
        :param limit: количество возвращаемых заявок за один запрос.
        :param next_page_token: , полученная из предыдущего запроса для получения следующей порции результатов.

        :return: Возвращает массив структур со следующими полями:   lead_id — идентификатор заявки, уникальный в
            рамках сообщества, в котором находится форма;  user_id — идентификатор пользователя, оставившего заявку;
            date — дата и время оставления заявки в формате unix timestamp;  answers — информация об ответах на
            вопросы — массив структур со следующими полями:   key — ключ вопроса. Совпадает с типом стандартного
            вопроса (его полем type), или с ключом нестандартного вопроса (поле key). Для нестандартных вопросов, для
            которых не был задан ключ, будет использовано значение вида custom_0, где «0» — порядковый номер
            нестандартного вопроса, считая с 0.  answer — ответ на вопрос. Структура (для всех вопросов, кроме типа
            checkbox) или массив структур (для типа checkbox) со следующими полями:   key — ключ ответа (в случае,
            если был задан при создании формы);  value — текст ответа;    ad_id — идентификатор рекламного
            объявления, с которого пришла заявка (поле отсутствует в случае, если заявка пришла не из рекламного
            объявления)
        """

        params = locals()
        method_name = self._base_method + 'getLeads'
        return self._call(method_name, params)

    def getUploadURL(self) -> dict:
        """
        Возвращает URL для загрузки обложки для формы.

        :return: Возвращает URL для загрузки обложки для формы
        """

        params = locals()
        method_name = self._base_method + 'getUploadURL'
        return self._call(method_name, params)

    def list(self, group_id: str = None) -> dict:
        """
        Возвращает список форм сообщества.

        :param group_id: Идентификатор сообщества.

        :return: Возвращает массив структур с описанием форм. Подробнее о структуре описания формы см. метод
            leadForms.get
        """

        params = locals()
        method_name = self._base_method + 'list'
        return self._call(method_name, params)

    def update(self, group_id: str = None, form_id: str = None, name: str = None, title: str = None,
               description: str = None, questions: str = None, policy_link_url: str = None, photo: str = None,
               confirmation: str = None, site_link_url: str = None, active: str = None, once_per_user: str = None,
               pixel_code: str = None, notify_admins: str = None, notify_emails: str = None) -> dict:
        """
        Обновляет форму сбора заявок.

        :param group_id: Идентификатор группы, в которой надо обновить форму.
        :param form_id: Идентификатор формы, которую надо обновить.
        :param name: Новое название формы (видно только администратору).
        :param title: Новый заголовок формы (видят пользователи).
        :param description: Новое описание формы.
        :param questions: Новые вопросы формы. Подробнее см. метод leadForms.create.
        :param policy_link_url: Новая ссылка на политику конфиденциальности.
        :param photo: Новая обложка формы.
        :param confirmation: Новый текст подтверждения, который увидит пользователь после отправки формы.
        :param site_link_url: Новая ссылка на сайт или сообщество автора формы.
        :param active: Передайте 1, чтобы активировать форму. Пользователи могут оставлять заявки только в
            активных формах.
        :param once_per_user: Передайте 1, чтобы разрешить каждому пользователю заполнять форму только один раз.
        :param pixel_code: Новый код пикселя ретаргетинга ВКонтакте.
        :param notify_admins: Новый список идентификаторов пользователей, которым будут отправлены оповещения о
            заполнении пользователями формы. Оповещения могут быть отправлены только администраторам сообщества.
        :param notify_emails: Новый список email-адресов, разделённых запятой, на которые будут отправлены
            оповещения о заполнении пользователями формы. Можно указать до 10 адресов.

        :return: Возвращается структура с информацией об обновлённой форме:   form_id — идентификатор формы;  url
            — ссылка на форму
        """

        params = locals()
        method_name = self._base_method + 'update'
        return self._call(method_name, params)
