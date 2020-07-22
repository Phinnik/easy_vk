from typing import List, Union, Optional
from easy_vk.types import objects, responses
from .base import BaseCategory


class Database(BaseCategory):
    def __init__(self, session, access_token: str, v: str, delay: float, auto_retry: bool, max_retries: int, timeout: float):
        super().__init__(session, access_token, v, delay, auto_retry, max_retries, timeout)

    def get_chairs(self, faculty_id: int = None, offset: int = None, count: int = None) -> responses.DatabaseGetChairs:
        """
        Returns list of chairs on a specified faculty.
        
        :param faculty_id: id of the faculty to get chairs from
        :param offset: offset required to get a certain subset of chairs
        :param count: amount of chairs to get
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'database.getChairs'
        param_aliases = []
        response_type = responses.DatabaseGetChairs
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_cities(self, country_id: int = None, region_id: int = None, q: str = None, need_all: bool = None, offset: int = None, count: int = None) -> responses.DatabaseGetCities:
        """
        Returns a list of cities.
        
        :param country_id: Country ID.
        :param region_id: Region ID.
        :param q: Search query.
        :param need_all: '1' — to return all cities in the country, '0' — to return major cities in the country (default),
        :param offset: Offset needed to return a specific subset of cities.
        :param count: Number of cities to return.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'database.getCities'
        param_aliases = []
        response_type = responses.DatabaseGetCities
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_cities_by_id(self, city_ids: List[int] = None) -> responses.DatabaseGetCitiesById:
        """
        Returns information about cities by their IDs.
        
        :param city_ids: City IDs.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'database.getCitiesById'
        param_aliases = []
        response_type = responses.DatabaseGetCitiesById
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_countries(self, need_all: bool = None, code: str = None, offset: int = None, count: int = None) -> responses.DatabaseGetCountries:
        """
        Returns a list of countries.
        
        :param need_all: '1' — to return a full list of all countries, '0' — to return a list of countries near the current user's country (default).
        :param code: Country codes in [vk.com/dev/country_codes|ISO 3166-1 alpha-2] standard.
        :param offset: Offset needed to return a specific subset of countries.
        :param count: Number of countries to return.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'database.getCountries'
        param_aliases = []
        response_type = responses.DatabaseGetCountries
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_countries_by_id(self, country_ids: List[int] = None) -> responses.DatabaseGetCountriesById:
        """
        Returns information about countries by their IDs.
        
        :param country_ids: Country IDs.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'database.getCountriesById'
        param_aliases = []
        response_type = responses.DatabaseGetCountriesById
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_faculties(self, university_id: int = None, offset: int = None, count: int = None) -> responses.DatabaseGetFaculties:
        """
        Returns a list of faculties (i.e., university departments).
        
        :param university_id: University ID.
        :param offset: Offset needed to return a specific subset of faculties.
        :param count: Number of faculties to return.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'database.getFaculties'
        param_aliases = []
        response_type = responses.DatabaseGetFaculties
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_metro_stations(self, city_id: int = None, offset: int = None, count: int = None, extended: bool = None) -> responses.DatabaseGetMetroStations:
        """
        Get metro stations by city
        
        :param city_id: 
        :param offset: 
        :param count: 
        :param extended: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'database.getMetroStations'
        param_aliases = []
        response_type = responses.DatabaseGetMetroStations
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_metro_stations_by_id(self, station_ids: List[int] = None) -> responses.DatabaseGetMetroStationsById:
        """
        Get metro station by his id
        
        :param station_ids: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'database.getMetroStationsById'
        param_aliases = []
        response_type = responses.DatabaseGetMetroStationsById
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_regions(self, country_id: int = None, q: str = None, offset: int = None, count: int = None) -> responses.DatabaseGetRegions:
        """
        Returns a list of regions.
        
        :param country_id: Country ID, received in [vk.com/dev/database.getCountries|database.getCountries] method.
        :param q: Search query.
        :param offset: Offset needed to return specific subset of regions.
        :param count: Number of regions to return.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'database.getRegions'
        param_aliases = []
        response_type = responses.DatabaseGetRegions
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_school_classes(self, country_id: int = None) -> responses.DatabaseGetSchoolClasses:
        """
        Returns a list of school classes specified for the country.
        
        :param country_id: Country ID.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'database.getSchoolClasses'
        param_aliases = []
        response_type = responses.DatabaseGetSchoolClasses
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_schools(self, q: str = None, city_id: int = None, offset: int = None, count: int = None) -> responses.DatabaseGetSchools:
        """
        Returns a list of schools.
        
        :param q: Search query.
        :param city_id: City ID.
        :param offset: Offset needed to return a specific subset of schools.
        :param count: Number of schools to return.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'database.getSchools'
        param_aliases = []
        response_type = responses.DatabaseGetSchools
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_universities(self, q: str = None, country_id: int = None, city_id: int = None, offset: int = None, count: int = None) -> responses.DatabaseGetUniversities:
        """
        Returns a list of higher education institutions.
        
        :param q: Search query.
        :param country_id: Country ID.
        :param city_id: City ID.
        :param offset: Offset needed to return a specific subset of universities.
        :param count: Number of universities to return.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'database.getUniversities'
        param_aliases = []
        response_type = responses.DatabaseGetUniversities
        return self._call(method_name, method_parameters, param_aliases, response_type)

