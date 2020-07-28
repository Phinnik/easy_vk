# This file was autogenerated from vk-api json schema

from typing import List, Union, Optional, overload
from easy_vk.types import objects
from easy_vk.types import responses
from easy_vk.api_category import BaseCategory
try:
    from typing import Literal
except Exception:
    from typing_extensions import Literal


class Streaming(BaseCategory):
    def __init__(self, session, access_token: str, v: str, last_call_timer, delay: float, auto_retry: bool, max_retries: int, timeout: float):
        super().__init__(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)

    def get_server_url(self) -> responses.StreamingGetServerUrl:
        """
        Allows to receive data for the connection to Streaming API.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'streaming.getServerUrl'
        response_type = responses.StreamingGetServerUrl
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def set_settings(self, monthly_tier: Optional[str] = None) -> responses.BaseOk:
        """
        :param monthly_tier:
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'streaming.setSettings'
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)
