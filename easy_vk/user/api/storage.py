from typing import List, Union, Optional
from easy_vk.types import objects, responses
from .base import BaseCategory


class Storage(BaseCategory):
    def __init__(self, session, access_token: str, v: str, delay: float, auto_retry: bool, max_retries: int, timeout: float):
        super().__init__(session, access_token, v, delay, auto_retry, max_retries, timeout)

    def get(self, key: str = None, keys: List[str] = None, user_id: int = None) -> Union[responses.StorageGetV5110, responses.StorageGetWithKeys]:
        """
        Returns a value of variable with the name set by key parameter.
        
        :param key: 
        :param keys: 
        :param user_id: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'storage.get'
        param_aliases = []
        if not keys:
            response_type = responses.StorageGetV5110
        else:
            response_type = responses.StorageGetWithKeys
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_keys(self, user_id: int = None, offset: int = None, count: int = None) -> responses.StorageGetKeys:
        """
        Returns the names of all variables.
        
        :param user_id: user id, whose variables names are returned if they were requested with a server method.
        :param offset: 
        :param count: amount of variable names the info needs to be collected from.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'storage.getKeys'
        param_aliases = []
        response_type = responses.StorageGetKeys
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def set_(self, key: str = None, value: str = None, user_id: int = None) -> responses.BaseOk:
        """
        Saves a value of variable with the name set by 'key' parameter.
        
        :param key: 
        :param value: 
        :param user_id: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'storage.set'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

