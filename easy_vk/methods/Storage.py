from _ApiMethod import ApiMethod
from typing import List


class Storage(ApiMethod):
    def __init__(self, session, access_token, v, requests_per_s):
        super().__init__(session, access_token, v, requests_per_s)

    def get(self, key: str = None, keys: List[str] = None, user_id: int = None):
        """
        Returns a value of variable with the name set by key parameter.
        
        :param key: 
        :param keys: 
        :param user_id: 
        """
    
        if keys:
            keys = ','.join(keys)
        
        method_name = 'storage.get'
        return self.call(method_name, locals())

    def get_keys(self, user_id: int = None, offset: int = None, count: int = None):
        """
        Returns the names of all variables.
        
        :param user_id: user id, whose variables names are returned if they were requested with a server method.
        :param offset: 
        :param count: amount of variable names the info needs to be collected from.
        """
    
        method_name = 'storage.getKeys'
        return self.call(method_name, locals())

    def set(self, key: str, value: str = None, user_id: int = None):
        """
        Saves a value of variable with the name set by 'key' parameter.
        
        :param key: 
        :param value: 
        :param user_id: 
        """
    
        method_name = 'storage.set'
        return self.call(method_name, locals())

