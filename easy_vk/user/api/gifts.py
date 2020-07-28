# This file was autogenerated from vk-api json schema

from typing import List, Union, Optional, overload
from easy_vk.types import objects
from easy_vk.types import responses
from easy_vk.api_category import BaseCategory
try:
    from typing import Literal
except Exception:
    from typing_extensions import Literal


class Gifts(BaseCategory):
    def __init__(self, session, access_token: str, v: str, last_call_timer, delay: float, auto_retry: bool, max_retries: int, timeout: float):
        super().__init__(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)

    def get(self, user_id: Optional[int] = None, count: Optional[int] = None, offset: Optional[int] = None) -> responses.GiftsGet:
        """
        Returns a list of user gifts.
        
        :param user_id: User ID.
        :param count: Number of gifts to return.
        :param offset: Offset needed to return a specific subset of results.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'gifts.get'
        response_type = responses.GiftsGet
        return self._call(method_name, method_parameters, param_aliases, response_type)
