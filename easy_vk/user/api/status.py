# This file was autogenerated from vk-api json schema

from typing import List, Union, Optional, overload
from easy_vk.types import objects
from easy_vk.types import responses
from easy_vk.api_category import BaseCategory
try:
    from typing import Literal
except Exception:
    from typing_extensions import Literal


class Status(BaseCategory):
    def __init__(self, session, access_token: str, v: str, last_call_timer, delay: float, auto_retry: bool, max_retries: int, timeout: float):
        super().__init__(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)

    def get(self, user_id: Optional[int] = None, group_id: Optional[int] = None) -> responses.StatusGet:
        """
        Returns data required to show the status of a user or community.
        
        :param user_id: User ID or community ID. Use a negative value to designate a community ID.
        :param group_id:
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'status.get'
        response_type = responses.StatusGet
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def set_(self, text: Optional[str] = None, group_id: Optional[int] = None) -> responses.BaseOk:
        """
        Sets a new status for the current user.
        
        :param text: Text of the new status.
        :param group_id: Identifier of a community to set a status in. If left blank the status is set to current user.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'status.set'
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)
