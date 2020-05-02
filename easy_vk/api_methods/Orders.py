from ApiMethod import ApiMethod


class Orders(ApiMethod):
    def __init__(self, access_token, v, session, calls_per_second):
        super(Orders, self).__init__(access_token, v, session, calls_per_second)
        self._base_method = 'orders.'

    def cancelSubscription(self, user_id: str = None, subscription_id: str = None, pending_cancel: str = None) -> dict:
        """
        Отменяет подписку.

        :param user_id: идентификатор пользователя.
        :param subscription_id: идентификатор подписки.
        :param pending_cancel: 1 — отключить подписку по истечении текущего оплаченного периода;  0 — отключить
            подписку сразу.

        :return: После успешного выполнения возвращает 1. При отмене подписки на адрес обратного вызова будет
            отправлено платёжное уведомление с типом subscription_status_change
        """

        params = locals()
        method_name = self._base_method + 'cancelSubscription'
        return self._call(method_name, params)

    def changeState(self, order_id: str = None, action: str = None, app_order_id: str = None,
                    test_mode: str = None) -> dict:
        """
        Изменяет состояние заказа.

        :param order_id: идентификатор заказа.
        :param action: действие, которое нужно произвести с заказом.  Возможные действия:   cancel — отменить
            неподтверждённый заказ.  charge — подтвердить неподтверждённый заказ. Применяется только если не удалось
            обработать уведомление order_change_state.  refund — отменить подтверждённый заказ.
        :param app_order_id: внутренний идентификатор заказа в приложении.
        :param test_mode: если этот параметр равен 1, изменяется состояние заказа тестового режима. По умолчанию
            0.

        :return: После успешного выполнения возвращает новый статус заказа.   Статусы заказа   chargeable —
            неподтверждённый заказ. В это состояние заказы попадают в случае, если магазин не обрабатывает
            уведомления.  declined — отменённый заказ на этапе получения информации о товаре, например, была получена
            ошибка 20, "Товара не существует". В это состояние заказ может попасть из состояния chargeable.
            cancelled — отменённый заказ. В это состояние заказ может попасть из состояния chargeable.  charged —
            оплаченный заказ. В это состояние заказ может попасть из состояния chargeable, либо сразу после оплаты,
            если приложение обрабатывает уведомления.  refunded — отменённый после оплаты заказ, голоса возвращены
            пользователю
        """

        params = locals()
        method_name = self._base_method + 'changeState'
        return self._call(method_name, params)

    def get(self, offset: str = None, count: str = None, test_mode: str = None) -> dict:
        """
        Возвращает список заказов.

        :param offset: смещение относительно самого нового найденного заказа для выборки определенного
            подмножества. По умолчанию 0.
        :param count: количество возвращаемых заказов.
        :param test_mode: если этот параметр равен 1, возвращается список заказов тестового режима. По умолчанию
            0.

        :return: После успешного выполнения возвращает массив найденных заказов, отсортированный по дате в
            обратном порядке (самый новый в начале).   Статусы заказа   chargeable — неподтверждённый заказ. В это
            состояние заказы попадают в случае, если магазин не обрабатывает уведомления.  declined — отменённый
            заказ на этапе получения информации о товаре, например, была получена ошибка 20, "Товара не существует".
            В это состояние заказ может попасть из состояния chargeable.  cancelled — отменённый заказ. В это
            состояние заказ может попасть из состояния chargeable.  charged — оплаченный заказ. В это состояние заказ
            может попасть из состояния chargeable, либо сразу после оплаты, если приложение обрабатывает уведомления.
            refunded — отменённый после оплаты заказ, голоса возвращены пользователю
        """

        params = locals()
        method_name = self._base_method + 'get'
        return self._call(method_name, params)

    def getAmount(self, user_id: str = None, votes: str = None) -> dict:
        """
        Возвращает стоимость голосов в валюте пользователя.

        :param user_id: идентификатор пользователя
        :param votes: список голосов. Например: 1,7,77

        :return: Возвращает валюту пользователя и массив результатов для каждого значения из votes
        """

        params = locals()
        method_name = self._base_method + 'getAmount'
        return self._call(method_name, params)

    def getById(self, order_id: str = None, order_ids: str = None, test_mode: str = None) -> dict:
        """
        Возвращает информацию об отдельном заказе.

        :param order_id: идентификатор заказа.
        :param order_ids: идентификаторы заказов (при запросе информации о нескольких заказах).
        :param test_mode: если этот параметр равен 1, возвращаются заказы тестового режима. По умолчанию 0.

        :return: Возвращается массив найденных заказов, отсортированный по дате в обратном порядке (самый новый в
            начале).   Статусы заказа   chargeable — неподтверждённый заказ. В это состояние заказы попадают в
            случае, если магазин не обрабатывает уведомления.  declined — отменённый заказ на этапе получения
            информации о товаре, например, была получена ошибка 20, "Товара не существует". В это состояние заказ
            может попасть из состояния chargeable.  cancelled — отменённый заказ. В это состояние заказ может попасть
            из состояния chargeable.  charged — оплаченный заказ. В это состояние заказ может попасть из состояния
            chargeable, либо сразу после оплаты, если приложение обрабатывает уведомления.  refunded — отменённый
            после оплаты заказ, голоса возвращены пользователю
        """

        params = locals()
        method_name = self._base_method + 'getById'
        return self._call(method_name, params)

    def getUserSubscriptionById(self, user_id: str = None, subscription_id: str = None) -> dict:
        """
        Получает информацию о подписке по её идентификатору.

        :param user_id: идентификатор пользователя.
        :param subscription_id: идентификатор подписки.

        :return: Возвращает объект, описывающий подписку. Содержит следующие поля:   id (integer) — идентификатор
            подписки.  item_id (string) — идентификатор товара в приложении.  status (string) — статус подписки.
            Возможные значения:   chargeable — неподтвержденная подписка;  active — подписка активна;  cancelled —
            подписка отменена.   price (integer) — стоимость подписки.  period (integer) — период подписки.
            create_time (integer) — дата создания в Unixtime.  update_time (integer) — дата обновления в Unixtime.
            period_start_time (integer) — дата начала периода в Unixtime.  next_bill_time (integer) — дата следующего
            платежа в Unixtime (если status = active).  trial_expire_time (integer) — дата истечения триал-периода
            (если есть).  pending_cancel (boolean, [true]) — true, если подписка ожидает отмены.  cancel_reason
            (string) — причина отмены (если есть). Возможные значения:   user_decision — по инициативе пользователя;
            app_decision — по инициативе приложения;  payment_fail — из-за проблемы с платежом;  unknown — причина
            неизвестна.   test_mode (boolean, [true]) — true, если используется тестовый режим
        """

        params = locals()
        method_name = self._base_method + 'getUserSubscriptionById'
        return self._call(method_name, params)

    def getUserSubscriptions(self, user_id: str = None) -> dict:
        """
        Получает список активных подписок пользователя.

        :param user_id: идентификатор пользователя, подписки которого необходимо получить.

        :return: После успешного выполнения возвращает объект, содержащий число результатов в поле count и массив
            объектов, описывающих подписку, в поле items. Каждый объект массива items содержит следующие поля:    id
            (integer) — идентификатор подписки.  item_id (string) — идентификатор товара в приложении.  status
            (string) — статус подписки. Возможные значения:   active — подписка активна.   price (integer) —
            стоимость подписки.  period (integer) — период подписки.  create_time (integer) — дата создания в
            Unixtime.  update_time (integer) — дата обновления в Unixtime.  period_start_time (integer) — дата начала
            периода в Unixtime.  next_bill_time (integer) — дата следующего платежа в Unixtime (если status =
            active).  trial_expire_time (integer) — дата истечения триал-периода (если есть).  pending_cancel
            (boolean, [true]) — true, если подписка ожидает отмены.  cancel_reason (string) — причина отмены (если
            есть). Возможные значения:   user_decision — по инициативе пользователя;  app_decision — по инициативе
            приложения;  payment_fail — из-за проблемы с платежом;  unknown — причина неизвестна.   test_mode
            (boolean, [true]) — true, если используется тестовый режим
        """

        params = locals()
        method_name = self._base_method + 'getUserSubscriptions'
        return self._call(method_name, params)

    def updateSubscription(self, user_id: str = None, subscription_id: str = None, price: str = None) -> dict:
        """
        Обновляет цену подписки для пользователя.

        :param user_id: идентификатор пользователя.
        :param subscription_id: идентификатор подписки. Подписка должна быть активна.
        :param price: новая стоимость подписки (должна быть ниже, чем текущая).

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'updateSubscription'
        return self._call(method_name, params)

