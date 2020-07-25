# This file was autogenerated from vk-api json schema

from typing import List, Union, Optional, Literal, overload
from easy_vk.types import objects
from easy_vk.types import responses
from easy_vk.api_category import BaseCategory


class Downloadedgames(BaseCategory):
    def __init__(self, session, access_token: str, v: str, delay: float, auto_retry: bool, max_retries: int, timeout: float):
        super().__init__(session, access_token, v, delay, auto_retry, max_retries, timeout)

    def get_paid_status(self, user_id: Optional[int] = None) -> responses.DownloadedGamesPaidStatus:
        """
        :param user_id:
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'downloadedGames.getPaidStatus'
        response_type = responses.DownloadedGamesPaidStatus
        return self._call(method_name, method_parameters, param_aliases, response_type)
