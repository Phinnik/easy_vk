from ApiMethod import ApiMethod


class Database(ApiMethod):
    def __init__(self, access_token, v, session, calls_per_second):
        super(Database, self).__init__(access_token, v, session, calls_per_second)
        self._base_method = 'database.'

    def getChairs(self, faculty_id: str = None, offset: str = None, count: str = None) -> dict:
        """
        Возвращает список кафедр университета по указанному факультету.

        :param faculty_id: идентификатор факультета, кафедры которого необходимо получить.
        :param offset: отступ, необходимый для получения определенного подмножества кафедр.
        :param count: количество кафедр которое необходимо получить.

        :return: После успешного выполнения возвращает объект, содержащий число результатов в поле count и массив
            объектов, описывающих кафедры, в поле items.  Каждый объект содержит следующие поля:   id (integer) —
            идентификатор кафедры;  title (string) — название кафедры
        """

        params = locals()
        method_name = self._base_method + 'getChairs'
        return self._call(method_name, params)

    def getCities(self, country_id: str = None, region_id: str = None, q: str = None, need_all: str = None,
                  offset: str = None, count: str = None) -> dict:
        """
        Возвращает список городов.

        :param country_id: идентификатор страны, полученный database.getCountries.
        :param region_id: идентификатор региона, города которого необходимо получить.
        :param q:  поискового запроса. Например, Санкт.  Максимальная длина строки — 15 символов.
        :param need_all:   1 – возвращать все города.  0 – возвращать только основные города.
        :param offset: отступ, необходимый для получения определенного подмножества городов.
        :param count: количество городов, которые необходимо вернуть.

        :return: После успешного выполнения возвращает объект, содержащий число результатов в поле count и массив
            объектов, описывающих города, в поле items.  Каждый объект содержит следующие поля:   id (integer) —
            идентификатор города;  title (string) — название города.   Объект может содержать дополнительные поля:
            area (string) — область;  region (string) — регион.   Если не задан параметр q, то будет возвращен список
            самых крупных городов в заданной стране. Если задан параметр q, то будет возвращен список городов,
            которые релевантны поисковому запросу. Полем important отмечены ключевые города для текущего
            пользователя
        """

        params = locals()
        method_name = self._base_method + 'getCities'
        return self._call(method_name, params)

    def getCitiesById(self, city_ids: str = None) -> dict:
        """
        Возвращает информацию о городах и регионах по их идентификаторам.

        :param city_ids: идентификаторы городов и регионов.

        :return: Возвращает массив объектов, описывающих города.  Каждый объект содержит следующие поля:   id
            (integer) — идентификатор города или региона;  title (string) — название города или региона
        """

        params = locals()
        method_name = self._base_method + 'getCitiesById'
        return self._call(method_name, params)

    def getCountries(self, need_all: str = None, code: str = None, offset: str = None, count: str = None) -> dict:
        """
        Возвращает список стран.

        :param need_all: 1 — вернуть список всех стран.
        :param code: перечисленные через запятую двухбуквенные коды стран в стандарте ISO 3166-1 alpha-2, для
            которых необходимо выдать информацию. Пример значения code: RU,UA,BY
        :param offset: отступ, необходимый для выбора определенного подмножества стран.
        :param count: количество стран, которое необходимо вернуть.

        :return: После успешного выполнения возвращает объект, содержащий число результатов в поле count и массив
            объектов, описывающих страны, в поле items.  Каждый объект содержит следующие поля:   id (integer) —
            идентификатор страны;  title (string) — название страны.   Если не заданы параметры need_all и code, то
            возвращается краткий список стран, расположенных наиболее близко к стране текущего пользователя. Если
            задан параметр need_all, то будет возвращен список всех стран. Если задан параметр code, то будут
            возвращены только страны с перечисленными ISO 3166-1 alpha-2 кодами
        """

        params = locals()
        method_name = self._base_method + 'getCountries'
        return self._call(method_name, params)

    def getCountriesById(self, country_ids: str = None) -> dict:
        """
        Возвращает информацию о странах по их идентификаторам

        :param country_ids: идентификаторы стран.

        :return: Возвращает массив объектов, описывающих страны.  Каждый объект содержит следующие поля:   id
            (integer) — идентификатор региона;  title (string) — название региона
        """

        params = locals()
        method_name = self._base_method + 'getCountriesById'
        return self._call(method_name, params)

    def getFaculties(self, university_id: str = None, offset: str = None, count: str = None) -> dict:
        """
        Возвращает список факультетов.

        :param university_id: идентификатор университета, факультеты которого необходимо получить.
        :param offset: отступ, необходимый для получения определенного подмножества факультетов.
        :param count: количество факультетов которое необходимо получить.

        :return: После успешного выполнения возвращает объект, содержащий число результатов в поле count и массив
            объектов, описывающих факультеты, в поле items.  Каждый объект содержит следующие поля:   id (integer) —
            идентификатор факультета;  title (string) — название факультета
        """

        params = locals()
        method_name = self._base_method + 'getFaculties'
        return self._call(method_name, params)

    def getMetroStations(self, city_id: str = None, offset: str = None, count: str = None,
                         extended: str = None) -> dict:
        """
        Возвращает список станций метро

        :param city_id: идентификатор города, полученный методом database.getCities.
        :param offset: отступ, необходимый для выбора определенного подмножества станций.
        :param count: количество станций, которое необходимо вернуть.
        :param extended:

        :return: После успешного выполнения возвращает объект, содержащий число результатов в поле count и массив
            объектов, описывающих станции метро, в поле items.  Каждый объект содержит следующие поля:   id (integer)
            — идентификатор;  name (string) — название;  color (string) — цвет линии
        """

        params = locals()
        method_name = self._base_method + 'getMetroStations'
        return self._call(method_name, params)

    def getMetroStationsById(self, station_ids: str = None) -> dict:
        """
        Возвращает информацию об одной или нескольких станциях метро по их идентификаторам.

        :param station_ids: список идентификаторов станций метро

        :return: После успешного выполнения возвращает массив объектов, описывающих станции метро.  Каждый объект
            содержит следующие поля:   id (integer) — идентификатор;  name (string) — название;  color (string) —
            цвет линии
        """

        params = locals()
        method_name = self._base_method + 'getMetroStationsById'
        return self._call(method_name, params)

    def getRegions(self, country_id: str = None, q: str = None, offset: str = None, count: str = None) -> dict:
        """
        Возвращает список регионов.

        :param country_id: идентификатор страны, полученный в методе database.getCountries.
        :param q:  поискового запроса. Например, Лен.
        :param offset: отступ, необходимый для выбора определенного подмножества регионов.
        :param count: количество регионов, которое необходимо вернуть.

        :return: После успешного выполнения возвращает объект, содержащий число результатов в поле count и массив
            объектов, описывающих регионы, в поле items.  Каждый объект содержит следующие поля:   id (integer) —
            идентификатор региона;  title (string) — название региона.   Если не задан параметр q, то будет возвращен
            список всех регионов в заданной стране. Если задан параметр q, то будет возвращен список регионов,
            которые релевантны поисковому запросу
        """

        params = locals()
        method_name = self._base_method + 'getRegions'
        return self._call(method_name, params)

    def getSchoolClasses(self, country_id: str = None) -> dict:
        """
        Возвращает список классов, характерных для школ определенной страны.

        :param country_id: идентификатор страны, доступные классы в которой необходимо вернуть.

        :return: Возвращает массив, каждый элемент которого представляет собой пару: идентификатор и строковое
            обозначение класса
        """

        params = locals()
        method_name = self._base_method + 'getSchoolClasses'
        return self._call(method_name, params)

    def getSchools(self, q: str = None, city_id: str = None, offset: str = None, count: str = None) -> dict:
        """
        Возвращает список школ.

        :param q:  поискового запроса. Например, гимназия.
        :param city_id: идентификатор города, школы которого необходимо вернуть.
        :param offset: отступ, необходимый для получения определенного подмножества школ.
        :param count: количество школ, которое необходимо вернуть.

        :return: После успешного выполнения возвращает объект, содержащий число результатов в поле count и массив
            объектов, описывающих школы, в поле items.  Каждый объект содержит следующие поля:   id (integer) —
            идентификатор школы;  title (string) — название школы
        """

        params = locals()
        method_name = self._base_method + 'getSchools'
        return self._call(method_name, params)

    def getUniversities(self, q: str = None, country_id: str = None, city_id: str = None, offset: str = None,
                        count: str = None) -> dict:
        """
        Возвращает список высших учебных заведений.

        :param q:  поискового запроса. Например, СПБ.
        :param country_id: идентификатор страны, учебные заведения которой необходимо вернуть.
        :param city_id: идентификатор города, учебные заведения которого необходимо вернуть.
        :param offset: отступ, необходимый для получения определенного подмножества учебных заведений.
        :param count: количество учебных заведений, которое необходимо вернуть.

        :return: После успешного выполнения возвращает объект, содержащий число результатов в поле count и массив
            объектов, описывающих университеты, в поле items.  Каждый объект содержит следующие поля:   id (integer)
            — идентификатор университета;  title (string) — название университета
        """

        params = locals()
        method_name = self._base_method + 'getUniversities'
        return self._call(method_name, params)
