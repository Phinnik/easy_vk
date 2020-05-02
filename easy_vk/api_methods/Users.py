from .ApiMethod import ApiMethod


class Users(ApiMethod):
    def __init__(self, access_token, v, session, calls_per_second):
        super(Users, self).__init__(access_token, v, session, calls_per_second)
        self._base_method = 'users.'

    def get(self, user_ids: str = None, fields: str = None, name_case: str = None) -> dict:
        """
        Возвращает расширенную информацию о пользователях.

        :param user_ids: перечисленные через запятую идентификаторы пользователей или их короткие имена
            (screen_name). По умолчанию — идентификатор текущего пользователя.
        :param fields: список дополнительных полей профилей, которые необходимо вернуть. См. подробное описание.
            Доступные значения: photo_id, verified, sex, bdate, city, country, home_town, has_photo, photo_50,
            photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig, online, domain,
            has_mobile, contacts, site, education, universities, schools, status, last_seen, followers_count,
            common_count, occupation, nickname, relatives, relation, personal, connections, exports, activities,
            interests, music, movies, tv, books, games, about, quotes, can_post, can_see_all_posts, can_see_audio,
            can_write_private_message, can_send_friend_request, is_favorite, is_hidden_from_feed, timezone,
            screen_name, maiden_name, crop_photo, is_friend, friend_status, career, military, blacklisted,
            blacklisted_by_me, can_be_invited_group.
        :param name_case: падеж для склонения имени и фамилии пользователя. Возможные значения: именительный –
            nom, родительный – gen, дательный – dat, винительный – acc, творительный – ins, предложный – abl. По
            умолчанию nom.

        :return: После успешного выполнения возвращает массив объектов пользователей
        """

        params = locals()
        method_name = self._base_method + 'get'
        return self._call(method_name, params)

    def getFollowers(self, user_id: str = None, offset: str = None, count: str = None, fields: str = None,
                     name_case: str = None) -> dict:
        """
        Возвращает список идентификаторов пользователей, которые являются подписчиками пользователя.

        :param user_id: идентификатор пользователя.
        :param offset: смещение, необходимое для выборки определенного подмножества подписчиков.
        :param count: количество подписчиков, информацию о которых нужно получить.
        :param fields: список дополнительных полей профилей, которые необходимо вернуть. См. подробное описание.
            Доступные значения: photo_id, verified, sex, bdate, city, country, home_town, has_photo, photo_50,
            photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig, online, lists, domain,
            has_mobile, contacts, site, education, universities, schools, status, last_seen, followers_count,
            common_count, occupation, nickname, relatives, relation, personal, connections, exports, wall_comments,
            activities, interests, music, movies, tv, books, games, about, quotes, can_post, can_see_all_posts,
            can_see_audio, can_write_private_message, can_send_friend_request, is_favorite, is_hidden_from_feed,
            timezone, screen_name, maiden_name, crop_photo, is_friend, friend_status, career, military, blacklisted,
            blacklisted_by_me.
        :param name_case: падеж для склонения имени и фамилии пользователя. Возможные значения: именительный –
            nom, родительный – gen, дательный – dat, винительный – acc, творительный – ins, предложный – abl. По
            умолчанию nom.

        :return: После успешного выполнения возвращает объект, содержащий число результатов в поле count и массив
            объектов user в поле items.  Идентификаторы пользователей в списке отсортированы в порядке убывания
            времени их добавления
        """

        params = locals()
        method_name = self._base_method + 'getFollowers'
        return self._call(method_name, params)

    def getSubscriptions(self, user_id: str = None, extended: str = None, offset: str = None, count: str = None,
                         fields: str = None) -> dict:
        """
        Возвращает список идентификаторов пользователей и публичных страниц, которые входят в список подписок
        пользователя.

        :param user_id: идентификатор пользователя, подписки которого необходимо получить.
        :param extended: 1 – возвращает объединенный список, содержащий объекты group и user вместе. 0 –
            возвращает список идентификаторов групп и пользователей отдельно. (по умолчанию)
        :param offset: смещение необходимое для выборки определенного подмножества подписок. Этот параметр
            используется только если передан extended=1.
        :param count: количество подписок, которые необходимо вернуть. Этот параметр используется только если
            передан extended=1.
        :param fields: список дополнительных полей для объектов user и group, которые необходимо вернуть.

        :return: После успешного выполнения возвращает объекты users и groups, каждый из которых содержит поле
            count — количество результатов и items — список идентификаторов пользователей или публичных страниц, на
            которые подписан текущий пользователь (из раздела «Интересные страницы»).  Если был задан параметр
            extended=1, возвращает объединенный массив объектов group и user в поле items, а также общее число
            результатов в поле count
        """

        params = locals()
        method_name = self._base_method + 'getSubscriptions'
        return self._call(method_name, params)

    def report(self, user_id: str = None, type: str = None, comment: str = None) -> dict:
        """
        Позволяет пожаловаться на пользователя.

        :param user_id: идентификатор пользователя, на которого нужно подать жалобу.
        :param type: тип жалобы, может принимать следующие значения:   porn — порнография;  spam — рассылка
            спама;  insult — оскорбительное поведение;  advertisеment — рекламная страница, засоряющая поиск.
        :param comment: комментарий к жалобе на пользователя.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'report'
        return self._call(method_name, params)

    def search(self, q: str = None, sort: str = None, offset: str = None, count: str = None, fields: str = None,
               city: str = None, country: str = None, hometown: str = None, university_country: str = None,
               university: str = None, university_year: str = None, university_faculty: str = None,
               university_chair: str = None, sex: str = None, status: str = None, age_from: str = None,
               age_to: str = None, birth_day: str = None, birth_month: str = None, birth_year: str = None,
               online: str = None, has_photo: str = None, school_country: str = None, school_city: str = None,
               school_class: str = None, school: str = None, school_year: str = None, religion: str = None,
               company: str = None, position: str = None, group_id: str = None, from_list: str = None) -> dict:
        """
        Возвращает список пользователей в соответствии с заданным критерием поиска.

        :param q:  поискового запроса. Например, Вася Бабич.
        :param sort: сортировка результатов. Возможные значения:   1 — по дате регистрации;  0 — по популярности.
        :param offset: смещение относительно первого найденного пользователя для выборки определенного
            подмножества.
        :param count: количество возвращаемых пользователей. Обратите внимание — даже при использовании параметра
            offset для получения информации доступны только первые 1000 результатов.
        :param fields: список дополнительных полей профилей, которые необходимо вернуть. См. подробное описание.
            Доступные значения: photo_id, verified, sex, bdate, city, country, home_town, has_photo, photo_50,
            photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig, online, lists, domain,
            has_mobile, contacts, site, education, universities, schools, status, last_seen, followers_count,
            common_count, occupation, nickname, relatives, relation, personal, connections, exports, wall_comments,
            activities, interests, music, movies, tv, books, games, about, quotes, can_post, can_see_all_posts,
            can_see_audio, can_write_private_message, can_send_friend_request, is_favorite, is_hidden_from_feed,
            timezone, screen_name, maiden_name, crop_photo, is_friend, friend_status, career, military, blacklisted,
            blacklisted_by_me
        :param city: идентификатор города.
        :param country: идентификатор страны.
        :param hometown: название города строкой.
        :param university_country: идентификатор страны, в которой пользователи закончили ВУЗ.
        :param university: идентификатор ВУЗа.
        :param university_year: год окончания ВУЗа.
        :param university_faculty: идентификатор факультета.
        :param university_chair: идентификатор кафедры.
        :param sex: пол. Возможные значения:   1 — женщина;  2 — мужчина;  0 — любой (по умолчанию).
        :param status: семейное положение. Возможные значения:   1 — не женат (не замужем);  2 — встречается;  3
            — помолвлен(-а);  4 — женат (замужем);  5 — всё сложно;  6 — в активном поиске;  7 — влюблен(-а);  8 — в
            гражданском браке.
        :param age_from: возраст, от.
        :param age_to: возраст, до.
        :param birth_day: день рождения.
        :param birth_month: месяц рождения.
        :param birth_year: год рождения.
        :param online: учитывать ли статус «онлайн». Возможные значения:   1 — искать только пользователей
            онлайн;  0 — искать по всем пользователям.
        :param has_photo: учитывать ли наличие фото. Возможные значения:   1 — искать только пользователей с
            фотографией;  0 — искать по всем пользователям.
        :param school_country: идентификатор страны, в которой пользователи закончили школу.
        :param school_city: идентификатор города, в котором пользователи закончили школу.
        :param school_class: буква класса.
        :param school: идентификатор школы, которую закончили пользователи.
        :param school_year: год окончания школы.
        :param religion: религиозные взгляды.
        :param company: название компании, в которой работают пользователи.
        :param position: название должности.
        :param group_id: идентификатор группы, среди пользователей которой необходимо проводить поиск.
        :param from_list: Разделы среди которых нужно осуществить поиск, перечисленные через запятую. Возможные
            значения:   friends — искать среди друзей;  subscriptions — искать среди друзей и подписок пользователя.

        :return: После успешного выполнения возвращает объект, содержащий число результатов в поле count и массив
            объектов, описывающих пользователей в поле items
        """

        params = locals()
        method_name = self._base_method + 'search'
        return self._call(method_name, params)
