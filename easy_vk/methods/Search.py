from _ApiMethod import ApiMethod
from typing import List


class Search(ApiMethod):
    def __init__(self, session, access_token, v, requests_per_s):
        super().__init__(session, access_token, v, requests_per_s)

    def get_hints(self, q: str = None, offset: int = None, limit: int = None, filters: List[str] = None, fields: List[str] = None, search_global: bool = None):
        """
        Allows the programmer to do a quick search for any substring.
        
        :param q: Search query string.
        :param offset: Offset for querying specific result subset
        :param limit: Maximum number of results to return.
        :param filters: 
        :param fields: 
        :param search_global: 
        """
    
        if filters:
            filters = ','.join(filters)
        if fields:
            fields = ','.join(fields)
        
        method_name = 'search.getHints'
        return self.call(method_name, locals())

