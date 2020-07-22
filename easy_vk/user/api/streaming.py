from typing import List, Union, Optional
from easy_vk.types import objects, responses
from .base import BaseCategory


class Streaming(BaseCategory):
    def __init__(self, session, access_token: str, v: str, delay: float, auto_retry: bool, max_retries: int, timeout: float):
        super().__init__(session, access_token, v, delay, auto_retry, max_retries, timeout)

    def get_server_url(self) -> responses.StreamingGetServerUrl:
        """
        Allows to receive data for the connection to Streaming API.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'streaming.getServerUrl'
        param_aliases = []
        response_type = responses.StreamingGetServerUrl
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def set_settings(self, monthly_tier: str = None) -> responses.BaseOk:
        """
        :param monthly_tier: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'streaming.setSettings'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

