from .ApiMethod import ApiMethod


class AppWidgets(ApiMethod):
    def __init__(self, access_token, v, session, calls_per_second):
        super(AppWidgets, self).__init__(access_token, v, session, calls_per_second)
        self._base_method = 'appWidgets.'

    def getAppImageUploadServer(self, image_type: str = None) -> dict:
        """
        Позволяет получить адрес для загрузки фотографии в коллекцию приложения для виджетов приложений сообществ.

        :param image_type: тип изображения. Возможные значения:   24x24;  50x50;  160x160;  160x240;  510x128.

        :return: Возвращает объект с единственным полем upload_url, содержащим URL для загрузки изображения.  Для
            загрузки изображения сгенерируйте POST-запрос с файлом в поле image на полученный адрес, а затем вызовите
            метод appWidgets.saveAppImage
        """

        params = locals()
        method_name = self._base_method + 'getAppImageUploadServer'
        return self._call(method_name, params)

    def getAppImages(self) -> dict:
        """
        Позволяет получить коллекцию изображений, загруженных для приложения, в виджетах приложений сообществ.

        :return: Возвращает общее число результатов в поле count (integer) и массив объектов, описывающих
            изображения, в поле items (array).  Каждый объект массива items содержит следующие поля:   id (string) —
            идентификатор изображения. Обратите внимание, идентификаторы изображений для виджетов отличаются от
            обычных фотографий, и НЕ представляют собой сочетание owner_id+"_"+photo_id. Полученный идентификатор
            нужно использовать в коде виджета «как есть».  type (string) — тип изображения. Возможные значения:
            160x160,  160x240,  24x24,  510x128,  50x50.   images (array) — массив копий изображения. Каждый объект в
            массиве содержит следующие поля:   url (string) — URL копии;  width (integer) — ширина в px;  height
            (integer) — высота в px
        """

        params = locals()
        method_name = self._base_method + 'getAppImages'
        return self._call(method_name, params)

    def getGroupImageUploadServer(self) -> dict:
        """
        Позволяет получить адрес для загрузки фотографии в коллекцию сообщества для виджетов приложений сообществ.

        :return: Возвращает объект с единственным полем upload_url, содержащим URL для загрузки изображения.  Для
            загрузки изображения сгенерируйте POST-запрос с файлом в поле image на полученный адрес, а затем вызовите
            метод appWidgets.saveGroupImage
        """

        params = locals()
        method_name = self._base_method + 'getGroupImageUploadServer'
        return self._call(method_name, params)

    def getGroupImages(self) -> dict:
        """
        Позволяет получить коллекцию изображений, загруженных для приложения, в виджетах приложений сообществ.

        :return: Возвращает общее число результатов в поле count (integer) и массив объектов, описывающих
            изображения, в поле items (array).  Каждый объект массива items содержит следующие поля:   id (string) —
            идентификатор изображения. Обратите внимание, идентификаторы изображений для виджетов отличаются от
            обычных фотографий, и НЕ представляют собой сочетание owner_id+"_"+photo_id. Полученный идентификатор
            нужно использовать в коде виджета «как есть».  type (string) — тип изображения. Возможные значения:
            160x160,  160x240,  24x24,  510x128,  50x50.   images (array) — массив копий изображения. Каждый объект в
            массиве содержит следующие поля:   url (string) — URL копии;  width (integer) — ширина в px;  height
            (integer) — высота в px
        """

        params = locals()
        method_name = self._base_method + 'getGroupImages'
        return self._call(method_name, params)

    def getImagesById(self) -> dict:
        """
        Позволяет получить изображение для виджетов приложений сообществ по его идентификатору.

        :return: Возвращает объект, который содержит следующие поля:   id (string) — идентификатор изображения.
            Обратите внимание, идентификаторы изображений для виджетов отличаются от обычных фотографий, и НЕ
            представляют собой сочетание owner_id+"_"+photo_id. Полученный идентификатор нужно использовать в коде
            виджета «как есть».  type (string) — тип изображения. Возможные значения:   160x160,  160x240,  24x24,
            510x128,  50x50.   images (array) — массив копий изображения. Каждый объект в массиве содержит следующие
            поля:   url (string) — URL копии;  width (integer) — ширина в px;  height (integer) — высота в px
        """

        params = locals()
        method_name = self._base_method + 'getImagesById'
        return self._call(method_name, params)

    def saveAppImage(self, hash: str = None, image: str = None) -> dict:
        """
        Позволяет сохранить изображение в коллекцию приложения для виджетов приложений сообществ после загрузки на
        сервер.

        :param hash: параметр hash, полученный после загрузки на сервер.
        :param image: параметр image, полученный после загрузки на сервер.

        :return: Возвращает объект, который содержит следующие поля:   id (string) — идентификатор изображения.
            type (string) — тип изображения. Возможные значения:   160x160,  160x240,  24x24,  510x128,  50x50.
            images (array) — массив копий изображения. Каждый объект в массиве содержит следующие поля:   url
            (string) — URL копии;  width (integer) — ширина в px;  height (integer) — высота в px
        """

        params = locals()
        method_name = self._base_method + 'saveAppImage'
        return self._call(method_name, params)

    def saveGroupImage(self) -> dict:
        """
        Позволяет сохранить изображение в коллекцию сообщества для виджетов приложений сообществ. после загрузки на
        сервер.

        :return: Возвращает объект, который содержит следующие поля:   id (string) — идентификатор изображения.
            type (string) — тип изображения. Возможные значения:   160x160,  160x240,  24x24,  510x128,  50x50.
            images (array) — массив копий изображения. Каждый объект в массиве содержит следующие поля:   url
            (string) — URL копии;  width (integer) — ширина в px;  height (integer) — высота в px
        """

        params = locals()
        method_name = self._base_method + 'saveGroupImage'
        return self._call(method_name, params)

    def update(self) -> dict:
        """
        Позволяет обновить виджет приложения сообщества.

        :return: После успешного выполнения возвращает 1
        """

        params = locals()
        method_name = self._base_method + 'update'
        return self._call(method_name, params)
