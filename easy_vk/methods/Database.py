from _ApiMethod import ApiMethod
from typing import List


class Database(ApiMethod):
    def __init__(self, session, access_token, v, requests_per_s):
        super().__init__(session, access_token, v, requests_per_s)

    def get_chairs(self, faculty_id: int, offset: int = None, count: int = None):
        """
        Returns list of chairs on a specified faculty.
        
        :param faculty_id: id of the faculty to get chairs from
        :param offset: offset required to get a certain subset of chairs
        :param count: amount of chairs to get
        """
    
        method_name = 'database.getChairs'
        return self.call(method_name, locals())

    def get_cities(self, country_id: int, region_id: int = None, q: str = None, need_all: bool = None, offset: int = None, count: int = None):
        """
        Returns a list of cities.
        
        :param country_id: Country ID.
        :param region_id: Region ID.
        :param q: Search query.
        :param need_all: '1' — to return all cities in the country, '0' — to return major cities in the country (default),
        :param offset: Offset needed to return a specific subset of cities.
        :param count: Number of cities to return.
        """
    
        method_name = 'database.getCities'
        return self.call(method_name, locals())

    def get_cities_by_id(self, city_ids: List[int] = None):
        """
        Returns information about cities by their IDs.
        
        :param city_ids: City IDs.
        """
    
        if city_ids:
            city_ids = [str(c) for c in city_ids]
            city_ids = ','.join(city_ids)
        
        method_name = 'database.getCitiesById'
        return self.call(method_name, locals())

    def get_countries(self, need_all: bool = None, code: str = None, offset: int = None, count: int = None):
        """
        Returns a list of countries.
        
        :param need_all: '1' — to return a full list of all countries, '0' — to return a list of countries near the current user's country (default).
        :param code: Country codes in [vk.com/dev/country_codes|ISO 3166-1 alpha-2] standard.
        :param offset: Offset needed to return a specific subset of countries.
        :param count: Number of countries to return.
        """
    
        method_name = 'database.getCountries'
        return self.call(method_name, locals())

    def get_countries_by_id(self, country_ids: List[int] = None):
        """
        Returns information about countries by their IDs.
        
        :param country_ids: Country IDs.
        """
    
        if country_ids:
            country_ids = [str(c) for c in country_ids]
            country_ids = ','.join(country_ids)
        
        method_name = 'database.getCountriesById'
        return self.call(method_name, locals())

    def get_faculties(self, university_id: int, offset: int = None, count: int = None):
        """
        Returns a list of faculties (i.e., university departments).
        
        :param university_id: University ID.
        :param offset: Offset needed to return a specific subset of faculties.
        :param count: Number of faculties to return.
        """
    
        method_name = 'database.getFaculties'
        return self.call(method_name, locals())

    def get_metro_stations(self, city_id: int, offset: int = None, count: int = None, extended: bool = None):
        """
        Get metro stations by city
        
        :param city_id: 
        :param offset: 
        :param count: 
        :param extended: 
        """
    
        method_name = 'database.getMetroStations'
        return self.call(method_name, locals())

    def get_metro_stations_by_id(self, station_ids: List[int] = None):
        """
        Get metro station by his id
        
        :param station_ids: 
        """
    
        if station_ids:
            station_ids = [str(s) for s in station_ids]
            station_ids = ','.join(station_ids)
        
        method_name = 'database.getMetroStationsById'
        return self.call(method_name, locals())

    def get_regions(self, country_id: int, q: str = None, offset: int = None, count: int = None):
        """
        Returns a list of regions.
        
        :param country_id: Country ID, received in [vk.com/dev/database.getCountries|database.getCountries] method.
        :param q: Search query.
        :param offset: Offset needed to return specific subset of regions.
        :param count: Number of regions to return.
        """
    
        method_name = 'database.getRegions'
        return self.call(method_name, locals())

    def get_school_classes(self, country_id: int = None):
        """
        Returns a list of school classes specified for the country.
        
        :param country_id: Country ID.
        """
    
        method_name = 'database.getSchoolClasses'
        return self.call(method_name, locals())

    def get_schools(self, city_id: int, q: str = None, offset: int = None, count: int = None):
        """
        Returns a list of schools.
        
        :param city_id: City ID.
        :param q: Search query.
        :param offset: Offset needed to return a specific subset of schools.
        :param count: Number of schools to return.
        """
    
        method_name = 'database.getSchools'
        return self.call(method_name, locals())

    def get_universities(self, q: str = None, country_id: int = None, city_id: int = None, offset: int = None, count: int = None):
        """
        Returns a list of higher education institutions.
        
        :param q: Search query.
        :param country_id: Country ID.
        :param city_id: City ID.
        :param offset: Offset needed to return a specific subset of universities.
        :param count: Number of universities to return.
        """
    
        method_name = 'database.getUniversities'
        return self.call(method_name, locals())

