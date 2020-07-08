from ._ApiMethod import ApiMethod
from typing import List


class Streaming(ApiMethod):
    def __init__(self, session, access_token, v, requests_per_s):
        super().__init__(session, access_token, v, requests_per_s)

    def get_server_url(self):
        """
        Allows to receive data for the connection to Streaming API.
        
        """
    
        method_name = 'streaming.getServerUrl'
        return self._call(method_name, locals())

    def set_settings(self, monthly_tier: str = None):
        """
        
        :param monthly_tier: 
        """
    
        method_name = 'streaming.setSettings'
        return self._call(method_name, locals())

