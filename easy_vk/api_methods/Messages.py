from ApiMethod import ApiMethod
from vk_objects import Media
from typing import List, Dict, Union, Optional
import time


class Messages(ApiMethod):
    def __init__(self, access_token, v, session, calls_per_second):
        super(Messages, self).__init__(access_token, v, session, calls_per_second)
        self._base_method = 'messages.'

    def addChatUser(self, chat_id: int, user_id: int, visible_messages_count: int = None) -> int:
        """
        Добавляет в мультидиалог нового пользователя. тобы пользователю вернуться в беседу, которую он сам покинул,
        достаточно отправить сообщение в неё (если есть свободные места), либо вызвать этот метод, передав свой
        идентификатор в параметре user_id.

        :param chat_id: идентификатор беседы.
        :param user_id: идентификатор пользователя, которого необходимо включить в беседу.
        :param visible_messages_count:

        :return: После успешного выполнения возвращает 1.
        """

        params = locals()
        method_name = self._base_method + 'addChatUser'
        return self._call(method_name, params)

    def allowMessagesFromGroup(self, group_id: int, key: str = None) -> int:
        """
        Позволяет разрешить отправку сообщений от сообщества текущему пользователю.

        :param group_id: идентификатор сообщества.
        :param key: произвольная строка. Этот параметр можно использовать для идентификации пользователя.
            Его значение будет возвращено в событии message_allow Callback API.

        :return: После успешного выполнения возвращает 1.
        """

        params = locals()
        method_name = self._base_method + 'allowMessagesFromGroup'
        return self._call(method_name, params)

    def createChat(self, user_ids: List[int], title: str = None, group_id: int = None) -> dict:
        """
        Создаёт беседу с несколькими участниками.

        :param user_ids: идентификаторы пользователей, которых нужно включить в мультидиалог. Должны быть в
            друзьях у текущего пользователя.
        :param title: название беседы.
        :param group_id: идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя).

        :return: После успешного выполнения возвращает идентификатор созданного чата (chat_id).
        """

        params = locals()
        params['user_ids'] = str([user_ids]).strip('[]')
        method_name = self._base_method + 'createChat'
        return self._call(method_name, params)

    def delete(self, message_ids: List[int], spam: bool = None, group_id: int = None,
               delete_for_all: bool = None) -> int:
        """
        Удаляет сообщение.

        :param message_ids: список идентификаторов сообщений, разделённых через запятую.
        :param spam: пометить сообщения как спам.
        :param group_id: идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя).
        :param delete_for_all: 1 — если сообщение нужно удалить для получателей (если с момента отправки
            сообщения прошло не более 24 часов ).

        :return: После успешного выполнения возвращает 1 для каждого удаленного сообщения.
        """

        params = locals()
        params['message_ids'] = str([message_ids]).strip('[]')
        method_name = self._base_method + 'delete'
        return self._call(method_name, params)

    # TODO: объект мультидиалога
    def deleteChatPhoto(self, chat_id: int, group_id: int = None) -> int:
        """
        Позволяет удалить фотографию мультидиалога.

        :param chat_id: идентификатор беседы.
        :param group_id: идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя).

        :return: После успешного выполнения возвращает объект, содержащий следующие поля:
            message_id — идентификатор отправленного системного сообщения;
            chat — объект мультидиалога.
        """

        params = locals()
        method_name = self._base_method + 'deleteChatPhoto'
        return self._call(method_name, params)

    def deleteConversation(self, user_id: int = None, peer_id: int = None, group_id: int = None) -> dict:
        """
        Удаляет беседу.

        :param user_id: идентификатор пользователя. Если требуется очистить историю беседы, используйте
            peer_id.
        :param peer_id: идентификатор назначения. Для групповой беседы: 2000000000 + id беседы.
            Для сообщества: -id сообщества.
        :param group_id: идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя).

        :return: После успешного выполнения возвращает поле last_deleted_id, содержащее идентификатор
            последнего удалённого сообщения в переписке.
        """

        params = locals()
        method_name = self._base_method + 'deleteConversation'
        return self._call(method_name, params)

    def denyMessagesFromGroup(self, group_id: int) -> int:
        """
        Позволяет запретить отправку сообщений от сообщества текущему пользователю.

        :param group_id: идентификатор сообщества.

        :return: После успешного выполнения возвращает 1.
        """

        params = locals()
        method_name = self._base_method + 'denyMessagesFromGroup'
        return self._call(method_name, params)

    # TODO make attachments
    def edit(self, peer_id: int, message: str = None, message_id: int = None, lat: float = None, long: float = None,
             attachment: int = None, keep_forward_messages: bool = None, keep_snippets: bool = None,
             group_id: int = None, dont_parse_links: bool = None) -> int:
        """
        Редактирует сообщение.

        :param peer_id: идентификатор назначения. Для пользователя: id пользователя.
            Для групповой беседы: 2000000000 + id беседы.
            Для сообщества: -id сообщества.
        :param message: текст сообщения. Обязательный параметр, если не задан параметр attachment.
        :param message_id: идентификатор сообщения.
        :param lat: географическая широта (от -90 до 90).
        :param long: географическая долгота (от -180 до 180).
        :param attachment: медиавложения к личному сообщению, перечисленные через запятую.
            Каждое прикрепление представлено в формате: <type><owner_id>_<media_id>
                <type> — тип медиавложения:
                    photo — фотография;
                    video — видеозапись;
                    audio — аудиозапись;
                    doc — документ;
                    wall — запись на стене;
                    market — товар.
                <owner_id> — идентификатор владельца медиавложения (обратите внимание, если объект находится в
                сообществе, этот параметр должен быть отрицательным).
                <media_id> — идентификатор медиавложения.
            Например: photo100172_166443618
            Параметр является обязательным, если не задан параметр message.
            В случае, если прикрепляется объект, принадлежащий другому пользователю следует добавлять к вложению его
            access_key в формате <type><owner_id>_<media_id>_<access_key>,
            Например: video85635407_165186811_69dff3de4372ae9b6e
        :param keep_forward_messages: 1, чтобы сохранить прикреплённые пересланные сообщения.
        :param keep_snippets: 1, чтобы сохранить прикреплённые внешние ссылки (сниппеты).
        :param group_id: идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя).
        :param dont_parse_links: 1 — не создавать сниппет ссылки из сообщения

        :return: После успешного выполнения возвращает 1.
        """

        params = locals()
        method_name = self._base_method + 'edit'
        return self._call(method_name, params)

    def editChat(self, chat_id: int, title: str) -> int:
        """
        Изменяет название беседы.

        :param chat_id: идентификатор беседы.
        :param title: новое название для беседы.

        :return: После успешного выполнения возвращает 1.
        """

        params = locals()
        method_name = self._base_method + 'editChat'
        return self._call(method_name, params)

    # TODO сделать объект сообщения
    def getByConversationMessageId(self, peer_id: int, conversation_message_ids: int, extended: bool = None,
                                   fields: str = None, group_id: int = None) -> dict:
        """
        Возвращает сообщения по их идентификаторам в рамках беседы или диалога.

        :param peer_id: идентификаторы назначений, разделённые запятой. Для пользователя: id пользователя.
            Для групповой беседы: 2000000000 + id беседы (недоступно с ключом сообщества)
            Для сообщества: -id сообщества.
        :param conversation_message_ids: идентификаторы сообщений. Максимум 100 идентификаторов.
        :param extended: 1 — возвращать дополнительные поля.
        :param fields: дополнительные поля пользователей и сообществ, которые необходимо вернуть в ответе.
        :param group_id: идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя).

        :return: После успешного выполнения возвращает объект, содержащий число результатов в поле count и
            массив объектов, описывающих сообщения, в поле items.
        """

        params = locals()
        method_name = self._base_method + 'getByConversationMessageId'
        return self._call(method_name, params)

    # TODO сделать объект сообщения
    def getById(self, message_ids: List[int], preview_length: bool = None, extended: bool = None, fields: str = None,
                group_id: int = None) -> dict:
        """
        Возвращает сообщения по их идентификаторам.

        :param message_ids: идентификаторы сообщений. Максимум 100 идентификаторов.
        :param preview_length: количество символов, по которому нужно обрезать сообщение. Укажите 0, если Вы
            не хотите обрезать сообщение. (по умолчанию сообщения не обрезаются).
        :param extended: 1 — возвращать дополнительные поля.
        :param fields: список дополнительных полей для пользователей и сообществ.
        :param group_id: идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя).

        :return: После успешного выполнения возвращает объект, содержащий число результатов в поле count и
            массив объектов, описывающих сообщения, в поле items.
        """

        params = locals()
        params['message_ids'] = str([message_ids]).strip('[]')
        method_name = self._base_method + 'getById'
        return self._call(method_name, params)

    # TODO: сделать объект мультидиалога
    def getChat(self, chat_id: int = None, chat_ids: List[int] = None, fields: str = None,
                name_case: str = None) -> Union[List[dict], dict]:
        """
        Возвращает информацию о беседе.

        :param chat_id: идентификатор беседы.
        :param chat_ids: список идентификаторов бесед.
        :param fields: список дополнительных полей профилей, которые необходимо вернуть. Доступные
            значения: nickname, screen_name, sex, bdate, city, country, timezone, photo_50, photo_100,
            photo_200_orig, has_mobile, contacts, education, online, counters, relation, last_seen, status,
            can_write_private_message, can_see_all_posts, can_post, universities
        :param name_case: падеж для склонения имени и фамилии пользователя. Возможные значения:
            nom — именительный;
            gen — родительный;
            dat — дательный;
            acc — винительный;
            ins — творительный;
            abl — предложный.
            По умолчанию: nom.

        :return: После успешного выполнения возвращает объект (или список объектов) мультидиалога. Если был
            задан параметр fields, поле users содержит список объектов пользователей с дополнительным полем
            invited_by, содержащим идентификатор пользователя, пригласившего в беседу.
        """

        params = locals()
        if chat_ids:
            params['chat_ids'] = str([chat_ids]).strip('[]')
        method_name = self._base_method + 'getChat'
        return self._call(method_name, params)

    def getChatPreview(self, peer_id: int, link: str = None, fields: str = None) -> dict:
        """
        Получает данные для превью чата с приглашением по ссылке.

        :param peer_id:
        :param link: ссылка-приглашение.
        :param fields: список полей профилей, данные о которых нужно получить. Полный список смотрите на
            этой странице. (https://vk.com/dev/objects/user)

        :return: Возвращает объект, который содержит следующие поля:
            preview - информация о чате. Объект, который содержит поля:
                admin_id (object) — идентификатор создателя чата;
                members (array) — массив идентификаторов участников чата;
                title (string) — название чата;
                photo (object) — обложка чата. Объект, который содержит поля:
                    photo_50 (string) — URL копии фотографии с шириной 50 px;
                    photo_100 (string) — URL копии фотографии с шириной 100 px;
                    photo_200 (string) — URL копии фотографии с шириной 200px.
                local_id (integer) — идентификатор чата для текущего пользователя.
            profiles (array) - массив объектов пользователей;
            groups (array) - массив объектов сообществ;
            emails (array) - массив объектов, описывающих e-mail. Каждый из объектов содержит поля:
                id (integer) — идентификатор e-mail;
                address (string) — адрес e-mail.
        """

        params = locals()
        method_name = self._base_method + 'getChatPreview'
        return self._call(method_name, params)

    def getConversationMembers(self, peer_id: int, fields: str = None, group_id: int = None) -> dict:
        """
        Позволяет получить список участников беседы.

        :param peer_id: идентификатор назначения. Для пользователя: id пользователя.
            Для групповой беседы: 2000000000 + id беседы. Для сообщества: -id сообщества.
        :param fields: дополнительные поля пользователей и сообществ, которые необходимо вернуть в ответе.
        :param group_id: идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя).

        :return: Возвращает объект, который содержит следующие поля:
            count (integer) - число участников беседы.
            items (array) - участники беседы. Массив объектов, каждый из которых содержит поля:
                member_id (integer) — идентификатор участника беседы;
                invited_by (integer) — идентификатор пользователя, который пригласил участника;
                join_date (integer) — дата добавления в беседу;
                is_admin (boolean) — является ли пользователь администратором;
                can_kick (boolean) — может ли текущий пользователь исключить участника.
            profiles (array) - массив объектов пользователей.
            groups (array) - массив объектов сообществ.
        """

        params = locals()
        method_name = self._base_method + 'getConversationMembers'
        return self._call(method_name, params)

    # TODO: сделать объект сообществ
    def getConversations(self, offset, count, filter, extended, start_message_id, fields, group_id) -> dict:
        """
        Возвращает список бесед пользователя.

        :param offset: смещение, необходимое для выборки определенного подмножества результатов.
        :param count: максимальное число результатов, которые нужно получить.
        :param filter: фильтр. Возможные значения:
            all — все беседы;
            unread — беседы с непрочитанными сообщениями;
            important — беседы, помеченные как важные (только для сообщений сообществ);
            unanswered — беседы, помеченные как неотвеченные (только для сообщений сообществ).
            По умолчанию: all.
        :param extended: 1 — возвращать дополнительные поля для пользователей и сообществ.
        :param start_message_id: идентификатор сообщения, начиная с которого нужно возвращать беседы.
        :param fields: список дополнительных полей для пользователей и сообществ.
        :param group_id: идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя).

        :return: Возвращает объект, который содержит следующие поля:
         count (integer) - число результатов.
         items (array) - беседы. Массив объектов, каждый из которых содержит поля:
            conversation (object) — объект беседы.
            last_message (object) — объект, описывающий последнее сообщение в беседе.
        unread_count (integer) - число непрочитанных бесед.
        profiles (array) - массив объектов пользователей.
        groups (array) массив объектов сообществ.
        """

        params = locals()
        method_name = self._base_method + 'getConversations'
        return self._call(method_name, params)

    # TODO: сделать объект бемед
    def getConversationsById(self, peer_ids: Union[List[int], int], extended: bool = None, fields: str = None,
                             group_id: int = None) -> dict:
        """
        Позволяет получить беседу по её идентификатору.

        :param peer_ids: идентификаторы назначений, разделённые запятой. Для пользователя: id
            пользователя. Для групповой беседы: 2000000000 + id беседы. Для сообщества: -id сообщества.
            Максимум – 100 идентификаторов.
        :param extended: 1 — возвращать дополнительные поля.
        :param fields: дополнительные поля пользователей и сообществ, которые необходимо вернуть в ответе.
        :param group_id: идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя).

        :return: Возвращает общее число результатов в поле count (integer) и массив объектов бесед в поле items.
        """

        params = locals()
        params['peer_ids'] = str([peer_ids]).strip('[]')
        method_name = self._base_method + 'getConversationsById'
        return self._call(method_name, params)

    # TODO объект сообщений
    def getHistory(self, offset: int = None, count: int = None, user_id: int = None, peer_id: int = None,
                   start_message_id: int = None, rev: bool = None, extended: bool = None,
                   fields: str = None, group_id: int = None) -> dict:
        """
        Возвращает историю сообщений для указанного диалога.

        :param offset: смещение, необходимое для выборки определенного подмножества сообщений, должен быть >= 0,
        если не передан параметр start_message_id, и должен быть <= 0, если передан.
        :param count: количество сообщений, которое необходимо получить (но не более 200).
        :param user_id: идентификатор пользователя, историю переписки с которым необходимо вернуть.
        :param peer_id: идентификатор назначения. Для пользователя: id пользователя. Для групповой
            беседы: 2000000000 + id беседы. (недоступно для вызовов от имени сообщества) Для сообщества: -id
            сообщества.
        :param start_message_id: если значение > 0, то это идентификатор сообщения, начиная с которого нужно
            вернуть историю переписки, если передано значение 0 то вернутся сообщения с самого начала переписки,
            если же передано значение -1, то к значению параметра offset прибавляется количество входящих
            непрочитанных сообщений в конце диалога (подробности см. ниже)
        :param rev: 1 – возвращать сообщения в хронологическом порядке. 0 – возвращать сообщения в обратном
            хронологическом порядке (по умолчанию).
        :param extended: Если указать в качестве этого параметра 1, то будет возвращена информация о
            пользователях, являющихся авторами сообщений. По умолчанию 0.
        :param fields: список дополнительных полей профилей, которые необходимо вернуть.
            См. https://vk.com/dev/objects/user
        :param group_id: идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя).

        :return: После успешного выполнения возвращает список объектов сообщений. В случае наличия в этом
            диалоге непрочитанных входящих сообщений, дополнительно (после поля count, перед полем items) в
            список будет добавлено поле unread с количеством непрочитанных входящих сообщений. Поля in_read и
            out_read являются идентификаторами прочтения. in_read возвращает идентификатор последнего
            прочитанного сообщения текущим пользователем, а out_read возвращает идентификатор последнего
            прочитанного сообщения собеседником. При переданном start_message_id в случае, если не было
            возвращено последнее сообщение в истории переписки (то есть сколько-то сообщений было пропущено),
            количество пропущенных сообщений (то есть реальное значение offset, которое использовалось для
            получения интервала истории) будет возвращено в поле skipped (вместе с count, items и иногда
            unread).
        """

        params = locals()
        method_name = self._base_method + 'getHistory'
        return self._call(method_name, params)

    def getHistoryAttachments(self, peer_id: str = None, media_type: str = None, start_from: str = None,
                              count: str = None, photo_sizes: str = None, fields: str = None, group_id: str = None,
                              preserve_order: str = None, max_forwards_level: str = None) -> dict:
        """
        Возвращает материалы диалога или беседы.

        :param peer_id: идентификатор назначения. Для групповой беседы:  2000000000 + id беседы.   Для
            пользователя:  id пользователя.   Для сообщества:  -id сообщества.
        :param media_type: тип материалов, который необходимо вернуть.  Доступные значения:   photo — фотографии;
            video — видеозаписи;  audio — аудиозаписи;  doc — документы;  link — ссылки;  market — товары;  wall —
            записи;  share — ссылки, товары и записи.   Обратите внимание — существует ограничение по дате отправки
            вложений. Так, для получения доступны вложения типов photo,video,audio,doc , отправленные не ранее
            25.03.2013, link — не ранее 20.05.13, market,wall — 01.02.2016.
        :param start_from: смещение, необходимое для выборки определенного подмножества объектов.
        :param count: количество объектов, которое необходимо получить (но не более 200).
        :param photo_sizes: параметр, указывающий нужно ли возвращать ли доступные размеры фотографии в
            специальном формате.
        :param fields: дополнительные поля профилей пользователей и сообществ, которые необходимо вернуть в
            ответе.
        :param group_id: идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя).
        :param preserve_order: параметр, указывающий нужно ли возвращать вложения в оригинальном порядке.
        :param max_forwards_level: максимальная глубина вложенности пересланных сообщений.

        :return: После успешного выполнения возвращает массив items, содержащий объекты, которые описывают
            вложения, а также дополнительное поле next_from, содержащее новое значение start_from. Каждый объект из
            массива items содержит следующие поля:  message_id  integerидентификатор сообщения, в котором было
            отправлено вложение. attachment  objectинформация о вложении. Объект, который содержит следующие поля:
            type (string) — тип вложения. Возможные значения:   photo — фотография;  video — видеозапись;  audio —
            аудиозапись;  doc — документ;  link — ссылка;  market — товар;  wall — запись.   photo, video, audio,
            doc, link, market, wall (название поля зависит от значения поля type) — описание вложения. Содержит,
            соответственно, объект, описывающий фотографию, видеозапись, аудиозапись, документ, ссылку, товар или
            запись на стене
        """

        params = locals()
        method_name = self._base_method + 'getHistoryAttachments'
        return self._call(method_name, params)

    def getImportantMessages(self, count: str = None, offset: str = None, start_message_id: str = None,
                             preview_length: str = None, fields: str = None, extended: str = None,
                             group_id: str = None) -> dict:
        """
        Возвращает список важных сообщений пользователя.

        :param count: максимальное число результатов, которые нужно получить.
        :param offset: смещение, необходимое для выборки определенного подмножества результатов.
        :param start_message_id: идентификатор сообщения, начиная с которого нужно возвращать список.
        :param preview_length:
        :param fields: список дополнительных полей для пользователей и сообществ.
        :param extended: 1 — возвращать дополнительные поля для пользователей и сообществ.
        :param group_id: идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя).

        :return
        """

        params = locals()
        method_name = self._base_method + 'getImportantMessages'
        return self._call(method_name, params)

    def getInviteLink(self, peer_id: str = None, reset: str = None, group_id: str = None) -> dict:
        """
        Получает ссылку для приглашения пользователя в беседу.

        :param peer_id: идентификатор назначения.  Для групповой беседы:  2000000000 + id беседы.
        :param reset: 1 — сгенерировать новую ссылку, сбросив предыдущую. 0 — получить предыдущую ссылку.
        :param group_id:

        :return: Возвращает объект с единственным полем link (string), которое содержит ссылку для приглашения в
            беседу
        """

        params = locals()
        method_name = self._base_method + 'getInviteLink'
        return self._call(method_name, params)

    def getLastActivity(self, user_id: str = None) -> dict:
        """
        Возвращает текущий статус и дату последней активности указанного пользователя.

        :param user_id: идентификатор пользователя, информацию о последней активности которого требуется
            получить.

        :return: Возвращает объект, содержащий следующие поля:   online — текущий статус пользователя (1 — в
            сети, 0 — не в сети);  time — дата последней активности пользователя в формате unixtime
        """

        params = locals()
        method_name = self._base_method + 'getLastActivity'
        return self._call(method_name, params)

    def getLongPollHistory(self, ts: str = None, pts: str = None, preview_length: str = None, onlines: str = None,
                           fields: str = None, events_limit: str = None, msgs_limit: str = None, max_msg_id: str = None,
                           group_id: str = None, lp_version: str = None, last_n: str = None,
                           credentials: str = None) -> dict:
        """
        Возвращает обновления в личных сообщениях пользователя.

        :param ts: последнее значение параметра ts, полученное от Long Poll сервера или с помощью метода
            messages.getLongPollServer
        :param pts: последнее значение параметра new_pts, полученное от Long Poll сервера, используется для
            получения действий, которые хранятся всегда.
        :param preview_length: количество символов, по которому нужно обрезать сообщение. Укажите 0, если Вы не
            хотите обрезать сообщение. (по умолчанию сообщения не обрезаются).
        :param onlines: 1 — возвращать в числе прочих события 8 и 9 (пользователь стал онлайн/оффлайн).
            Учитывается только при использовании ts.
        :param fields: список дополнительных полей профилей, которые необходимо вернуть. См. подробное описание.
            Доступные значения: sex, bdate, city, country, photo_50, photo_100, photo_200_orig, photo_200,
            photo_400_orig, photo_max, photo_max_orig, photo_id, online, online_mobile, domain, has_mobile, contacts,
            connections, site, education, universities, schools, can_post, can_see_all_posts, can_see_audio,
            can_write_private_message, status, last_seen, common_count, relation, relatives, counters, screen_name,
            maiden_name, timezone, occupation, activities, interests, music, movies, tv, books, games, about, quotes,
            personal, friend_status, military, career
        :param events_limit: лимит по количеству всех событий в истории. Обратите внимание, параметры
            events_limit и msgs_limit применяются совместно. Число результатов в ответе ограничивается первым
            достигнутым лимитом.
        :param msgs_limit: лимит по количеству событий с сообщениями в истории. Обратите внимание, параметры
            events_limit и msgs_limit применяются совместно. Число результатов в ответе ограничивается первым
            достигнутым лимитом.
        :param max_msg_id: максимальный идентификатор сообщения среди уже имеющихся в локальной копии. Необходимо
            учитывать как сообщения, полученные через методы API (например messages.getDialogs, messages.getHistory),
            так и данные, полученные из Long Poll сервера (события с кодом 4).
        :param group_id: идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя).
        :param lp_version: версия Long Poll.
        :param last_n:
        :param credentials:

        :return: Возвращает объект, который содержит поля history, messages, а также groups — массив объектов
            сообществ и profiles — массив объектов пользователей.  Поле history представляет из себя массив,
            аналогичный полю updates, получаемому от Long Poll сервера, за некоторыми исключениями: для событий с
            кодом 4 (добавление нового сообщения) отсутствуют все поля, кроме первых трёх, а также отсутствуют
            события с кодами 8, 9 (друг появился/пропал из сети) и 61, 62 (набор текста в диалоге/беседе).  Поле
            messages представляет из себя массив личных сообщений – объектов message, которые встречались среди
            событий с кодом 4 (добавление нового сообщения) из поля history. Каждый объект message содержит набор
            полей, описание которых доступно здесь. Первый элемент массива представляет собой общее количество
            сообщений.   Ограничения В случае, если ts слишком старый (больше суток), а max_msg_id не передан, метод
            может вернуть ошибку 10 (Internal server error).  Если количество событий превышает значение events_limit
            или количество событий с сообщениями превышает значение msgs_limit, ответ содержит дополнительное поле
            more со значением 1 — это означает, что нужно запросить оставшиеся данные с помощью запроса с параметром
            max_msg_id. Обратите внимание, что параметры events_limit и msgs_limit применяются совместно — число
            объектов в результате не превышает значения меньшего из этих параметров.  Ошибки с кодами 907 и 908
            означают, что нужно получить новое значение pts (''ts''') и вызвать метод повторно с новыми значениями,
            поскольку данных для переданных значений не существует
        """

        params = locals()
        method_name = self._base_method + 'getLongPollHistory'
        return self._call(method_name, params)

    def getLongPollServer(self, need_pts: str = None, group_id: str = None, lp_version: str = None) -> dict:
        """
        Возвращает данные, необходимые для подключения к Long Poll серверу.

        :param need_pts: 1 — возвращать поле pts, необходимое для работы метода messages.getLongPollHistory
        :param group_id: идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя).
        :param lp_version: версия для подключения к Long Poll. Актуальная версия: 3.  Подробную информацию об
            изменениях в версиях Вы найдёте на этой странице.

        :return: Возвращает объект, который содержит поля key, server, ts.  Используя эти данные, Вы можете
            подключиться к серверу быстрых сообщений для мгновенного получения приходящих сообщений и других событий.
            Формат взаимодействия с LongPoll сервером
        """

        params = locals()
        method_name = self._base_method + 'getLongPollServer'
        return self._call(method_name, params)

    def isMessagesFromGroupAllowed(self, group_id: str = None, user_id: str = None) -> dict:
        """
        Возвращает информацию о том, разрешена ли отправка сообщений от сообщества пользователю.

        :param group_id: идентификатор сообщества.
        :param user_id: идентификатор пользователя.

        :return: Возвращает объект с единственным полем is_allowed (integer, [0,1]). Если отправка сообщений
            разрешена, поле содержит 1, иначе — 0
        """

        params = locals()
        method_name = self._base_method + 'isMessagesFromGroupAllowed'
        return self._call(method_name, params)

    def joinChatByInviteLink(self, link: str = None) -> dict:
        """
        Позволяет присоединиться к чату по ссылке-приглашению.

        :param link: ссылка-приглашение.

        :return: Возвращает идентификатор чата в поле chat_id
        """

        params = locals()
        method_name = self._base_method + 'joinChatByInviteLink'
        return self._call(method_name, params)

    def markAsAnsweredConversation(self, peer_id: str = None, answered: str = None, group_id: str = None) -> dict:
        """
        Помечает беседу как отвеченную либо снимает отметку.

        :param peer_id: идентификатор беседы
        :param answered: 1 - беседа отмечена отвеченной, 0 - неотвеченной
        :param group_id: идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя).

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'markAsAnsweredConversation'
        return self._call(method_name, params)

    def markAsImportant(self, message_ids: str = None, important: str = None) -> dict:
        """
        Помечает сообщения как важные либо снимает отметку.

        :param message_ids: список идентификаторов сообщений, которые необходимо пометить.
        :param important: 1, если сообщения необходимо пометить, как важные;  0, если необходимо снять пометку.

        :return: Возвращает массив идентификаторов успешно помеченных сообщений
        """

        params = locals()
        method_name = self._base_method + 'markAsImportant'
        return self._call(method_name, params)

    def markAsImportantConversation(self, peer_id: str = None, important: str = None, group_id: str = None) -> dict:
        """
        Помечает беседу как важную либо снимает отметку.

        :param peer_id: идентификатор беседы
        :param important: 1, если сообщения необходимо пометить, как важные;  0, если необходимо снять пометку.
        :param group_id: идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя).

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'markAsImportantConversation'
        return self._call(method_name, params)

    def markAsRead(self, message_ids: str = None, peer_id: str = None, start_message_id: str = None,
                   group_id: str = None) -> dict:
        """
        Помечает сообщения как прочитанные.

        :param message_ids: идентификаторы сообщений.
        :param peer_id: идентификатор назначения.  Для пользователя:  id пользователя.   Для групповой беседы:
            2000000000 + id беседы.   Для сообщества:  -id сообщества.
        :param start_message_id: при передаче этого параметра будут помечены как прочитанные все сообщения,
            начиная с данного.
        :param group_id: идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя).

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'markAsRead'
        return self._call(method_name, params)

    def pin(self, peer_id: str = None, message_id: str = None) -> dict:
        """
        Закрепляет сообщение.

        :param peer_id: идентификатор назначения.  Для пользователя:  id пользователя.   Для групповой беседы:
            2000000000 + id беседы.   Для сообщества:  -id сообщества.
        :param message_id: идентификатор сообщения, которое нужно закрепить.

        :return: Возвращает объект закрепленного сообщения
        """

        params = locals()
        method_name = self._base_method + 'pin'
        return self._call(method_name, params)

    def removeChatUser(self, chat_id: str = None, user_id: str = None, member_id: str = None) -> dict:
        """
        Исключает из мультидиалога пользователя, если текущий пользователь или сообщество является администратором
        беседы либо текущий пользователь пригласил исключаемого пользователя.

        :param chat_id: идентификатор беседы.
        :param user_id: идентификатор пользователя, которого необходимо исключить из беседы. Может быть меньше
            нуля в случае, если пользователь приглашён по email.
        :param member_id: идентификатор участника, которого необходимо исключить из беседы. Для сообществ —
            идентификатор сообщества со знаком «минус».

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'removeChatUser'
        return self._call(method_name, params)

    def restore(self, message_id: str = None, group_id: str = None) -> dict:
        """
        Восстанавливает удаленное сообщение.

        :param message_id: идентификатор сообщения, которое нужно восстановить.
        :param group_id: идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя).

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'restore'
        return self._call(method_name, params)

    def search(self, q: str = None, peer_id: str = None, date: str = None, preview_length: str = None,
               offset: str = None, count: str = None, extended: str = None, fields: str = None,
               group_id: str = None) -> dict:
        """
        Возвращает список найденных личных сообщений текущего пользователя по введенной строке поиска.

        :param q: под, по которой будет производиться поиск.
        :param peer_id: фильтр по идентификатору назначения для поиска по отдельному диалогу.  Для пользователя:
            id пользователя.   Для групповой беседы:  2000000000 + id беседы.   Для сообщества:  -id сообщества.
        :param date: дата в формате DDMMYYYY — если параметр задан, в ответе будут только сообщения, отправленные
            до указанной даты.
        :param preview_length: количество символов, по которому нужно обрезать сообщение. Укажите 0, если Вы не
            хотите обрезать сообщение. (по умолчанию сообщения не обрезаются).
        :param offset: смещение, необходимое для выборки определенного подмножества сообщений из списка
            найденных.
        :param count: количество сообщений, которое необходимо получить.
        :param extended: 1 — возвращать дополнительные поля для пользователей и сообществ. В ответе будет
            содержаться массив объектов бесед.
        :param fields: список дополнительных полей для пользователей и сообществ.
        :param group_id: идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя).

        :return: После успешного выполнения возвращает объект, содержащий число результатов в поле count и массив
            объектов, описывающих личные сообщения, в поле items.  Обратите внимание, даже при использовании
            параметра offset максимальное число доступных результатов — 10000.  Если extended = 1, в поле items
            возвращается массив объектов бесед. Дополнительно возвращаются массивы profiles и groups, содержащие
            объекты пользователей и сообществ
        """

        params = locals()
        method_name = self._base_method + 'search'
        return self._call(method_name, params)

    def searchConversations(self, q: str = None, count: str = None, extended: str = None, fields: str = None,
                            group_id: str = None) -> dict:
        """
        Позволяет искать диалоги.

        :param q: поисковой запрос.
        :param count: максимальное число результатов для получения.
        :param extended: 1 — возвращать дополнительные поля.
        :param fields: дополнительные поля пользователей и сообществ, которые необходимо вернуть в ответе.
        :param group_id: идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя).

        :return: Возвращает общее число результатов в поле count (integer) и массив объектов диалогов в поле
            items
        """

        params = locals()
        method_name = self._base_method + 'searchConversations'
        return self._call(method_name, params)

    def send(self, user_id: str = None, random_id: str = None, peer_id: str = None, domain: str = None,
             chat_id: str = None, user_ids: str = None, message: str = None, lat: str = None, long: str = None,
             attachment: str = None, reply_to: str = None, forward_messages: str = None, sticker_id: str = None,
             group_id: str = None, keyboard: str = None, payload: str = None, dont_parse_links: str = None,
             disable_mentions: str = None, intent: str = None) -> dict:
        """
        Отправляет сообщение.

        :param user_id: идентификатор пользователя, которому отправляется сообщение.
        :param random_id: уникальный (в привязке к API_ID и ID отправителя) идентификатор, предназначенный для
            предотвращения повторной отправки одинакового сообщения. Сохраняется вместе с сообщением и доступен в
            истории сообщений.  Заданный random_id используется для проверки уникальности за всю историю сообщений,
            поэтому используйте большой диапазон (до int64).
        :param peer_id: идентификатор назначения.  Для пользователя:  id пользователя.   Для групповой беседы:
            2000000000 + id беседы.   Для сообщества:  -id сообщества.
        :param domain: короткий адрес пользователя (например, illarionov).
        :param chat_id: идентификатор беседы, к которой будет относиться сообщение.
        :param user_ids: идентификаторы получателей сообщения (при необходимости отправить сообщение сразу
            нескольким пользователям). Доступно только для ключа доступа сообщества. Максимальное количество
            идентификаторов: 100.
        :param message: текст личного сообщения. Обязательный параметр, если не задан параметр attachment.
        :param lat: географическая широта (от -90 до 90).
        :param long: географическая долгота (от -180 до 180).
        :param attachment: медиавложения к личному сообщению, перечисленные через запятую. Каждое прикрепление
            представлено в формате: <type><owner_id>_<media_id>  <type> — тип медиавложения:   photo — фотография;
            video — видеозапись;  audio — аудиозапись;  doc — документ;  wall — запись на стене;  market — товар.
            poll — опрос.     <owner_id> — идентификатор владельца медиавложения (обратите внимание, если объект
            находится в сообществе, этот параметр должен быть отрицательным). <media_id> — идентификатор
            медиавложения.  Например: photo100172_166443618  Параметр является обязательным, если не задан параметр
            message.  В случае, если прикрепляется объект, принадлежащий другому пользователю следует добавлять к
            вложению его access_key в формате <type><owner_id>_<media_id>_<access_key>, Например:
            video85635407_165186811_69dff3de4372ae9b6e
        :param reply_to: идентификатор сообщения, на которое требуется ответить.
        :param forward_messages: идентификаторы пересылаемых сообщений, перечисленные через запятую.
            Перечисленные сообщения отправителя будут отображаться в теле письма у получателя. Не более 100 значений
            на верхнем уровне, максимальный уровень вложенности: 45, максимальное количество пересылаемых сообщений
            500  Например: 123,431,544
        :param sticker_id: идентификатор стикера.
        :param group_id: идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя).
        :param keyboard: объект, описывающий клавиатуру бота.
        :param payload: Полезная нагрузка
        :param dont_parse_links: 1 — не создавать сниппет ссылки из сообщения
        :param disable_mentions: 1 - отключить уведомление об упоминании в сообщении
        :param intent: , описывающая интенты

        :return: После успешного выполнения возвращает идентификатор отправленного сообщения.  Если передан
            параметр user_ids, возвращает массив объектов, каждый из которых содержит поля:   peer_id — идентификатор
            назначения;  message_id — идентификатор сообщения;  error — сообщение об ошибке, если сообщение не было
            доставлено получателю
        """

        params = locals()
        method_name = self._base_method + 'send'
        return self._call(method_name, params)

    def setActivity(self, user_id: str = None, type: str = None, peer_id: str = None, group_id: str = None) -> dict:
        """
        Изменяет статус набора текста пользователем в диалоге.

        :param user_id: идентификатор пользователя.
        :param type: typing — пользователь начал набирать текст,  audiomessage — пользователь записывает
            голосовое сообщение
        :param peer_id: идентификатор назначения.  Для групповой беседы:  2000000000 + id беседы.   Для
            сообщества:  -id сообщества.
        :param group_id: идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя).

        :return: После успешного выполнения возвращает 1.  Текст «N набирает сообщение...» отображается в течение
            10 секунд после вызова метода, либо до момента отправки сообщения
        """

        params = locals()
        method_name = self._base_method + 'setActivity'
        return self._call(method_name, params)

    def setChatPhoto(self, file: str = None) -> dict:
        """
        Позволяет установить фотографию мультидиалога, загруженную с помощью метода photos.getChatUploadServer.

        :param file: Содержимое поля response из ответа специального upload сервера, полученного в результате
            загрузки изображения на адрес, полученный методом photos.getChatUploadServer.

        :return: После успешного выполнения возвращает объект, содержащий следующие поля:  message_id
            — идентификатор отправленного системного сообщения;  chat — объект мультидиалога
        """

        params = locals()
        method_name = self._base_method + 'setChatPhoto'
        return self._call(method_name, params)

    def unpin(self, peer_id: str = None, group_id: str = None) -> dict:
        """
        Открепляет сообщение.

        :param peer_id: идентификатор назначения.  Для пользователя:  id пользователя.   Для групповой беседы:
            2000000000 + id беседы.   Для сообщества:  -id сообщества.
        :param group_id: идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя).

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'unpin'
        return self._call(method_name, params)
