# This file was autogenerated from vk-api json schema

from typing import List, Union, Optional, overload
from easy_vk.types import objects
from easy_vk.types import responses
from easy_vk.api_category import BaseCategory
try:
    from typing import Literal
except Exception:
    from typing_extensions import Literal


class Utils(BaseCategory):
    def __init__(self, session, access_token: str, v: str, last_call_timer, delay: float, auto_retry: bool, max_retries: int, timeout: float):
        super().__init__(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)

    def check_link(self, url: str) -> responses.UtilsCheckLink:
        """
        Checks whether a link is blocked in VK.
        
        :param url: Link to check (e.g., 'http://google.com').
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'utils.checkLink'
        response_type = responses.UtilsCheckLink
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def delete_from_last_shortened(self, key: str) -> responses.BaseOk:
        """
        Deletes shortened link from user's list.
        
        :param key: Link key (characters after vk.cc/).
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'utils.deleteFromLastShortened'
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_last_shortened_links(self, count: Optional[int] = None, offset: Optional[int] = None) -> responses.UtilsGetLastShortenedLinks:
        """
        Returns a list of user's shortened links.
        
        :param count: Number of links to return.
        :param offset: Offset needed to return a specific subset of links.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'utils.getLastShortenedLinks'
        response_type = responses.UtilsGetLastShortenedLinks
        return self._call(method_name, method_parameters, param_aliases, response_type)

    @overload
    def get_link_stats(self, key: str, source: Optional[str] = None, access_key: Optional[str] = None, interval: Optional[str] = None, intervals_count: Optional[int] = None, extended: None = None) -> responses.UtilsGetLinkStats: ...
    @overload
    def get_link_stats(self, key: str, extended: bool, source: Optional[str] = None, access_key: Optional[str] = None, interval: Optional[str] = None, intervals_count: Optional[int] = None) -> responses.UtilsGetLinkStatsExtended: ...
    def get_link_stats(self, key: str, source: Optional[str] = None, access_key: Optional[str] = None, interval: Optional[str] = None, intervals_count: Optional[int] = None, extended: Optional[bool] = None):
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
        param_aliases = []
        method_name = 'utils.getLinkStats'
        if not extended:
            response_type = responses.UtilsGetLinkStats
        if extended:
            response_type = responses.UtilsGetLinkStatsExtended
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_server_time(self) -> responses.UtilsGetServerTime:
        """
        Returns the current time of the VK server.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'utils.getServerTime'
        response_type = responses.UtilsGetServerTime
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_short_link(self, url: str, private: Optional[bool] = None) -> responses.UtilsGetShortLink:
        """
        Allows to receive a link shortened via vk.cc.
        
        :param url: URL to be shortened.
        :param private: 1 — private stats, 0 — public stats.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'utils.getShortLink'
        response_type = responses.UtilsGetShortLink
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def resolve_screen_name(self, screen_name: str) -> responses.UtilsResolveScreenName:
        """
        Detects a type of object (e.g., user, community, application) and its ID by screen name.
        
        :param screen_name: Screen name of the user, community (e.g., 'apiclub,' 'andrew', or 'rules_of_war'), or application.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'utils.resolveScreenName'
        response_type = responses.UtilsResolveScreenName
        return self._call(method_name, method_parameters, param_aliases, response_type)
