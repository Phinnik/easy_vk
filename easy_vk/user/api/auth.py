from typing import List, Union, Optional
from easy_vk.types import objects, responses
from .base import BaseCategory


class Auth(BaseCategory):
    def __init__(self, session, access_token: str, v: str, delay: float, auto_retry: bool, max_retries: int, timeout: float):
        super().__init__(session, access_token, v, delay, auto_retry, max_retries, timeout)

    def check_phone(self, phone: str = None, client_id: int = None, client_secret: str = None, auth_by_phone: bool = None) -> responses.BaseOk:
        """
        Checks a user's phone number for correctness.
        
        :param phone: Phone number.
        :param client_id: User ID.
        :param client_secret: 
        :param auth_by_phone: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'auth.checkPhone'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def restore(self, phone: str = None, last_name: str = None) -> responses.AuthRestore:
        """
        Allows to restore account access using a code received via SMS. " This method is only available for apps with [vk.com/dev/auth_direct|Direct authorization] access. "
        
        :param phone: User phone number.
        :param last_name: User last name.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'auth.restore'
        param_aliases = []
        response_type = responses.AuthRestore
        return self._call(method_name, method_parameters, param_aliases, response_type)

