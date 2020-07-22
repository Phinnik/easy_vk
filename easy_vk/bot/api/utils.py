from typing import List, Union, Optional
from easy_vk.types import objects, responses
from .base import BaseCategory


class Utils(BaseCategory):
    def __init__(self, session, access_token: str, v: str, delay: float, auto_retry: bool, max_retries: int, timeout: float):
        super().__init__(session, access_token, v, delay, auto_retry, max_retries, timeout)

    def check_link(self, url: str = None) -> responses.UtilsCheckLink:
        """
        Checks whether a link is blocked in VK.
        
        :param url: Link to check (e.g., 'http://google.com').
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'utils.checkLink'
        param_aliases = []
        response_type = responses.UtilsCheckLink
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_link_stats(self, key: str = None, source: str = None, access_key: str = None, interval: str = None, intervals_count: int = None, extended: bool = None) -> Union[responses.UtilsGetLinkStats, responses.UtilsGetLinkStatsExtended]:
        """
        Returns stats data for shortened link.
        
        :param key: Link key (characters after vk.cc/).
        :param source: Source of scope
        :param access_key: Access key for private link stats.
        :param interval: Interval.
        :param intervals_count: Number of intervals to return.
        :param extended: 1 — to return extended stats data (sex, age, geo). 0 — to return views number only.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'utils.getLinkStats'
        param_aliases = []
        if not extended:
            response_type = responses.UtilsGetLinkStats
        else:
            response_type = responses.UtilsGetLinkStatsExtended
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_server_time(self) -> responses.UtilsGetServerTime:
        """
        Returns the current time of the VK server.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'utils.getServerTime'
        param_aliases = []
        response_type = responses.UtilsGetServerTime
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_short_link(self, url: str = None, private: bool = None) -> responses.UtilsGetShortLink:
        """
        Allows to receive a link shortened via vk.cc.
        
        :param url: URL to be shortened.
        :param private: 1 — private stats, 0 — public stats.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'utils.getShortLink'
        param_aliases = []
        response_type = responses.UtilsGetShortLink
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def resolve_screen_name(self, screen_name: str = None) -> responses.UtilsResolveScreenName:
        """
        Detects a type of object (e.g., user, community, application) and its ID by screen name.
        
        :param screen_name: Screen name of the user, community (e.g., 'apiclub,' 'andrew', or 'rules_of_war'), or application.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'utils.resolveScreenName'
        param_aliases = []
        response_type = responses.UtilsResolveScreenName
        return self._call(method_name, method_parameters, param_aliases, response_type)

