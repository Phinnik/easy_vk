from .ApiMethod import ApiMethod


class Gifts(ApiMethod):
    def __init__(self, access_token, v, session, calls_per_second):
        super(Gifts, self).__init__(access_token, v, session, calls_per_second)
        self._base_method = 'gifts.'

    def get(self, user_id: str = None, count: str = None, offset: str = None) -> dict:
        """
        Возвращает список полученных подарков пользователя.

        :param user_id: идентификатор пользователя, для которого необходимо получить список подарков.
        :param count: количество подарков, которое нужно вернуть.
        :param offset: смещение, необходимое для выборки определенного подмножества подарков.

        :return: Возвращает список объектов gift_item, каждый из которых содержит следующие поля:   id —
            идентификатор полученного подарка;  from_id — идентификатор пользователя, который отправил подарок, или
            0, если отправитель скрыт;  message — текст сообщения, приложенного к подарку;  date — время отправки
            подарка в формате unixtime;  gift — объект подарка в следующем формате:   id — номер подарка;  thumb_256
            — url изображения подарка размером 256x256px;  thumb_96 — url изображения подарка размером 96x96px;
            thumb_48 — url изображения подарка размером 48x48px;   privacy — значение приватности подарка (только для
            текущего пользователя). Возможные значения:   0 — имя отправителя и сообщение видно всем;  1 — имя
            отправителя видно всем, сообщение видно только получателю;  2 — имя отправителя скрыто, сообщение видно
            только получателю
        """

        params = locals()
        method_name = self._base_method + 'get'
        return self._call(method_name, params)
