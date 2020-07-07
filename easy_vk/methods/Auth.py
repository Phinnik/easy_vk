from _ApiMethod import ApiMethod
from typing import List


class Auth(ApiMethod):
    def __init__(self, session, access_token, v, requests_per_s):
        super().__init__(session, access_token, v, requests_per_s)

    def check_phone(self, phone: str, client_id: int = None, client_secret: str = None, auth_by_phone: bool = None):
        """
        Checks a user's phone number for correctness.
        
        :param phone: Phone number.
        :param client_id: User ID.
        :param client_secret: 
        :param auth_by_phone: 
        """
    
        method_name = 'auth.checkPhone'
        return self.call(method_name, locals())

    def restore(self, phone: str, last_name: str):
        """
        Allows to restore account access using a code received via SMS. " This method is only available for apps with [vk.com/dev/auth_direct|Direct authorization] access. "
        
        :param phone: User phone number.
        :param last_name: User last name.
        """
    
        method_name = 'auth.restore'
        return self.call(method_name, locals())

