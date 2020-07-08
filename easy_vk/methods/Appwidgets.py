from ._ApiMethod import ApiMethod
from typing import List


class Appwidgets(ApiMethod):
    def __init__(self, session, access_token, v, requests_per_s):
        super().__init__(session, access_token, v, requests_per_s)

    def update(self, code: str, type_: str):
        """
        Allows to update community app widget
        
        :param code: 
        :param type_: 
        """
    
        param_alias_dict = {'type_': 'type'}
        method_name = 'appWidgets.update'
        return self._call(method_name, locals())

