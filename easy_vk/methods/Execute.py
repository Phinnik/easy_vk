from _ApiMethod import ApiMethod
from typing import List


class Execute(ApiMethod):
    def __init__(self, session, access_token, v, requests_per_s):
        super().__init__(session, access_token, v, requests_per_s)

    def execute(self, code: str = None):
        """
        
        :param code: 
        """
    
        method_name = 'execute'
        return self.call(method_name, locals())

