from typing import List, Union, Optional
from easy_vk.types import objects, responses
from .base import BaseCategory


class Users(BaseCategory):
    def __init__(self, session, access_token: str, v: str, delay: float, auto_retry: bool, max_retries: int, timeout: float):
        super().__init__(session, access_token, v, delay, auto_retry, max_retries, timeout)

    def get(self, user_ids: List[str] = None, fields: List[Union[objects.UsersFields, str]] = None, name_case: str = None) -> responses.UsersGet:
        """
        Returns detailed information on users.
        
        :param user_ids: User IDs or screen names ('screen_name'). By default, current user ID.
        :param fields: Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'contacts', 'education', 'online', 'counters', 'relation', 'last_seen', 'activity', 'can_write_private_message', 'can_see_all_posts', 'can_post', 'universities', 'can_invite_to_chats'
        :param name_case: Case for declension of user name and surname: 'nom' — nominative (default), 'gen' — genitive , 'dat' — dative, 'acc' — accusative , 'ins' — instrumental , 'abl' — prepositional
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'users.get'
        param_aliases = []
        response_type = responses.UsersGet
        return self._call(method_name, method_parameters, param_aliases, response_type)

