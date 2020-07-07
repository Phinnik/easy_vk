from _ApiMethod import ApiMethod
from typing import List


class Status(ApiMethod):
    def __init__(self, session, access_token, v, requests_per_s):
        super().__init__(session, access_token, v, requests_per_s)

    def get(self, user_id: int = None, group_id: int = None):
        """
        Returns data required to show the status of a user or community.
        
        :param user_id: User ID or community ID. Use a negative value to designate a community ID.
        :param group_id: 
        """
    
        method_name = 'status.get'
        return self.call(method_name, locals())

    def set(self, text: str = None, group_id: int = None):
        """
        Sets a new status for the current user.
        
        :param text: Text of the new status.
        :param group_id: Identifier of a community to set a status in. If left blank the status is set to current user.
        """
    
        method_name = 'status.set'
        return self.call(method_name, locals())

