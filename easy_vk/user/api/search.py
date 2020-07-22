from typing import List, Union, Optional
from easy_vk.types import objects, responses
from .base import BaseCategory


class Search(BaseCategory):
    def __init__(self, session, access_token: str, v: str, delay: float, auto_retry: bool, max_retries: int, timeout: float):
        super().__init__(session, access_token, v, delay, auto_retry, max_retries, timeout)

    def get_hints(self, q: str = None, offset: int = None, limit: int = None, filters: List[str] = None, fields: List[str] = None, search_global: bool = None) -> responses.SearchGetHints:
        """
        Allows the programmer to do a quick search for any substring.
        
        :param q: Search query string.
        :param offset: Offset for querying specific result subset
        :param limit: Maximum number of results to return.
        :param filters: 
        :param fields: 
        :param search_global: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'search.getHints'
        param_aliases = []
        response_type = responses.SearchGetHints
        return self._call(method_name, method_parameters, param_aliases, response_type)

