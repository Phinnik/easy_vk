from _ApiMethod import ApiMethod
from typing import List


class Gifts(ApiMethod):
    def __init__(self, session, access_token, v, requests_per_s):
        super().__init__(session, access_token, v, requests_per_s)

    def get(self, user_id: int = None, count: int = None, offset: int = None):
        """
        Returns a list of user gifts.
        
        :param user_id: User ID.
        :param count: Number of gifts to return.
        :param offset: Offset needed to return a specific subset of results.
        """
    
        method_name = 'gifts.get'
        return self.call(method_name, locals())

