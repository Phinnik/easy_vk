from typing import List, Union, Optional
from easy_vk.types import objects, responses
from .base import BaseCategory


class Downloadedgames(BaseCategory):
    def __init__(self, session, access_token: str, v: str, delay: float, auto_retry: bool, max_retries: int, timeout: float):
        super().__init__(session, access_token, v, delay, auto_retry, max_retries, timeout)

    def get_paid_status(self, user_id: int = None) -> responses.DownloadedGamesPaidStatus:
        """
        :param user_id: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'downloadedGames.getPaidStatus'
        param_aliases = []
        response_type = responses.DownloadedGamesPaidStatus
        return self._call(method_name, method_parameters, param_aliases, response_type)

