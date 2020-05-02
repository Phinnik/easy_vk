from ApiMethod import ApiMethod


class PrettyCards(ApiMethod):
    def __init__(self, access_token, v, session, calls_per_second):
        super(PrettyCards, self).__init__(access_token, v, session, calls_per_second)
        self._base_method = 'prettyCards.'

    def create(self, owner_id: str = None, photo: str = None, title: str = None, link: str = None, price: str = None,
               price_old: str = None, button: str = None) -> dict:
        """
        Создаёт карточку карусели.

        :param owner_id: Идентификатор владельца карточки. Необходимо указать идентификатор сообщества, взятый со
            знаком минус. Пример: -19542789.
        :param photo: Фотография карточки.  Используйте значение, полученное после загрузки фотографии на сервер.
            См. метод prettyCards.getUploadURL.  Также можно переиспользовать существующую фотографию из другой
            карточки. Используйте значение поля photo, которое возвращает метод prettyCards.get или
            prettyCards.getById.
        :param title: Заголовок
        :param link: Ссылка. Кроме http(s)-ссылок также допускается указание телефонных номеров в виде
            tel:+79111234567
        :param price: Цена. «0» будет отображён как «Бесплатно». Не передавайте этот параметр, чтобы не указывать
            цену.
        :param price_old: Старая цена. Отображается зачёркнутой. «0» будет отображён как «Бесплатно». Не
            передавайте этот параметр, чтобы не указывать старую цену.
        :param button: Кнопка. Не передавайте этот параметр, чтобы не использовать кнопку.  button Текст Действие
            Тип ссылок app_join Запустить Переход по ссылке Приложения и игры app_game_join Играть Переход по ссылке
            Игры open_url Перейти Переход по ссылке Внешние сайты, сообщества, приложения open Открыть Переход по
            ссылке Внешние сайты more Подробнее Переход по ссылке Сообщества call Позвонить Набор номера Телефонные
            номера book Забронировать Набор номера Телефонные номера enroll Записаться Переход по ссылке или набор
            номера Внешние сайты, телефонные номера register Зарегистрироваться Набор номера Телефонные номера buy
            Купить Переход по ссылке Внешние сайты buy_ticket Купить билет Переход по ссылке Внешние сайты to_shop В
            магазин Переход по ссылке Внешние сайты order Заказать Переход по ссылке Внешние сайты create Создать
            Переход по ссылке Внешние сайты install Установить Переход по ссылке Внешние сайты contact Связаться
            Переход по ссылке Внешние сайты fill Заполнить Переход по ссылке Внешние сайты choose Выбрать Переход по
            ссылке Внешние сайты try Попробовать Переход по ссылке Внешние сайты join_public Подписаться Подписка на
            публичную страницу Публичные страницы join_event Я пойду Участие в мероприятии События join_group
            Вступить Вступление в сообщество Сообщества im_group Связаться Переход к диалогу с сообществом
            Сообщества, публичные страницы, события im_group2 Написать Переход к диалогу с сообществом Сообщества,
            публичные страницы, события begin Начать Переход по ссылке Внешние сайты get Получить Переход по ссылке
            Внешние сайты

        :return: Возвращает структуру с информаций о созданной карточке.   owner_id — идентификатор владельца
            карточки  card_id — идентификатор карточк
        """

        params = locals()
        method_name = self._base_method + 'create'
        return self._call(method_name, params)

    def delete(self, owner_id: str = None, card_id: str = None) -> dict:
        """
        Удаляет карточку.

        :param owner_id: Идентификатор владельца карточки.
        :param card_id: Идентификатор карточки.

        :return: Возвращает структуру с информаций об удалённой карточке.   owner_id — идентификатор владельца
            карточки  card_id — идентификатор карточк
        """

        params = locals()
        method_name = self._base_method + 'delete'
        return self._call(method_name, params)

    def edit(self, owner_id: str = None, card_id: str = None, photo: str = None, title: str = None, link: str = None,
             price: str = None, price_old: str = None, button: str = None) -> dict:
        """
        Редактирует карточку карусели.

        :param owner_id: Идентификатор владельца карточки.
        :param card_id: Идентификатор карточки.
        :param photo: Новая фотография. Подробнее см. метод prettyCards.create.
        :param title: Новый заголовок.
        :param link: Новая ссылка. Подробнее см. метод prettyCards.create.
        :param price: Новая цена. Подробнее см. метод prettyCards.create.
        :param price_old: Обновлённая старая цена. Подробнее см. метод prettyCards.create.
        :param button: Новая кнопка. Подробнее см. метод prettyCards.create.

        :return: Возвращает структуру с информаций об обновлённой карточке.   owner_id — идентификатор владельца
            карточки  card_id — идентификатор карточк
        """

        params = locals()
        method_name = self._base_method + 'edit'
        return self._call(method_name, params)

    def get(self, owner_id: str = None, offset: str = None, count: str = None) -> dict:
        """
        Возвращает неиспользованные карточки владельца.

        :param owner_id: Идентификатор владельца.
        :param offset: Смещение относительно начала списка карточек.
        :param count: Количество возвращаемых карточек.

        :return: Возвращает массив структур с описанием карточек (подробнее о структуре ответа см. метод
            prettyCards.getById). Возвращаются только те карточки, которые не были прикреплены к рекламной записи
        """

        params = locals()
        method_name = self._base_method + 'get'
        return self._call(method_name, params)

    def getById(self, owner_id: str = None, card_ids: str = None) -> dict:
        """
        Возвращает информацию о карточке.

        :param owner_id: Идентификатор владельца карточки.
        :param card_ids: Список идентификаторов карточек, которые необходимо вернуть. Строка с числами,
            разделёнными запятой.

        :return: Возвращает массив структур со следующими полями:   card_id — идентификатор карточки,  link_url —
            целевая ссылка,  title — заголовок,  button — идентификатор кнопки (см. метод prettyCards.create),
            button_text — текст кнопки,  photo — идентификатор фотографии,  images — массив структур с разными
            размерами фотографии:   url — url фотографии,  width — ширина фотографии,  height — высота фотографии,
            price — цена,  price_old — старая цена
        """

        params = locals()
        method_name = self._base_method + 'getById'
        return self._call(method_name, params)

    def getUploadURL(self) -> dict:
        """
        Возвращает URL для загрузки фотографии для карточки.

        :return: Возвращает URL для загрузки фотографии для карточки
        """

        params = locals()
        method_name = self._base_method + 'getUploadURL'
        return self._call(method_name, params)
