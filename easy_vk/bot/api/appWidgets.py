from typing import List, Union, Optional
from easy_vk.types import objects, responses
from .base import BaseCategory


class Appwidgets(BaseCategory):
    def __init__(self, session, access_token: str, v: str, delay: float, auto_retry: bool, max_retries: int, timeout: float):
        super().__init__(session, access_token, v, delay, auto_retry, max_retries, timeout)

    def update(self, code: str = None, type_: str = None) -> responses.BaseOk:
        """
        Allows to update community app widget
        
        :param code: 
        :param type_: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'appWidgets.update'
        param_aliases = [('type_', 'type')]
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)
