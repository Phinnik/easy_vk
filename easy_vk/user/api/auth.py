# This file was autogenerated from vk-api json schema

from typing import List, Union, Optional, overload
from easy_vk.types import objects
from easy_vk.types import responses
from easy_vk.api_category import BaseCategory
try:
    from typing import Literal
except Exception:
    from typing_extensions import Literal


class Auth(BaseCategory):
    def __init__(self, session, access_token: str, v: str, last_call_timer, delay: float, auto_retry: bool, max_retries: int, timeout: float):
        super().__init__(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)

    def check_phone(self, phone: str, client_id: Optional[int] = None, client_secret: Optional[str] = None, auth_by_phone: Optional[bool] = None) -> responses.BaseOk:
        """
        Checks a user's phone number for correctness.
        
        :param phone: Phone number.
        :param client_id: User ID.
        :param client_secret:
        :param auth_by_phone:
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'auth.checkPhone'
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def restore(self, phone: str, last_name: str) -> responses.AuthRestore:
        """
        Allows to restore account access using a code received via SMS. " This method is only available for apps with [vk.com/dev/auth_direct|Direct authorization] access. "
        
        :param phone: User phone number.
        :param last_name: User last name.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'auth.restore'
        response_type = responses.AuthRestore
        return self._call(method_name, method_parameters, param_aliases, response_type)
