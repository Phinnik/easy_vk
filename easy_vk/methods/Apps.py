from ._ApiMethod import ApiMethod
from typing import List


class Apps(ApiMethod):
    def __init__(self, session, access_token, v, requests_per_s):
        super().__init__(session, access_token, v, requests_per_s)

    def delete_app_requests(self):
        """
        Deletes all request notifications from the current app.
        
        """
    
        method_name = 'apps.deleteAppRequests'
        return self._call(method_name, locals())

    def get(self, app_id: int = None, app_ids: List[str] = None, platform: str = None, extended: bool = None, return_friends: bool = None, fields: List[str] = None, name_case: str = None):
        """
        Returns applications data.
        
        :param app_id: Application ID
        :param app_ids: List of application ID
        :param platform: platform. Possible values: *'ios' — iOS,, *'android' — Android,, *'winphone' — Windows Phone,, *'web' — приложения на vk.com. By default: 'web'.
        :param extended: 
        :param return_friends: 
        :param fields: Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'contacts', 'education', 'online', 'counters', 'relation', 'last_seen', 'activity', 'can_write_private_message', 'can_see_all_posts', 'can_post', 'universities', (only if return_friends - 1)
        :param name_case: Case for declension of user name and surname: 'nom' — nominative (default),, 'gen' — genitive,, 'dat' — dative,, 'acc' — accusative,, 'ins' — instrumental,, 'abl' — prepositional. (only if 'return_friends' = '1')
        """
    
        if app_ids:
            app_ids = ','.join(app_ids)
        if fields:
            fields = ','.join(fields)
        
        method_name = 'apps.get'
        return self._call(method_name, locals())

    def get_catalog(self, count: int, sort: str = None, offset: int = None, platform: str = None, extended: bool = None, return_friends: bool = None, fields: List[str] = None, name_case: str = None, q: str = None, genre_id: int = None, filter_: str = None):
        """
        Returns a list of applications (apps) available to users in the App Catalog.
        
        :param count: Number of apps to return.
        :param sort: Sort order: 'popular_today' — popular for one day (default), 'visitors' — by visitors number , 'create_date' — by creation date, 'growth_rate' — by growth rate, 'popular_week' — popular for one week
        :param offset: Offset required to return a specific subset of apps.
        :param platform: 
        :param extended: '1' — to return additional fields 'screenshots', 'MAU', 'catalog_position', and 'international'. If set, 'count' must be less than or equal to '100'. '0' — not to return additional fields (default).
        :param return_friends: 
        :param fields: 
        :param name_case: 
        :param q: Search query string.
        :param genre_id: 
        :param filter_: 'installed' — to return list of installed apps (only for mobile platform).
        """
    
        if fields:
            fields = ','.join(fields)
        
        param_alias_dict = {'filter_': 'filter'}
        method_name = 'apps.getCatalog'
        return self._call(method_name, locals())

    def get_friends_list(self, extended: bool = None, count: int = None, offset: int = None, type_: str = None, fields: List[str] = None):
        """
        Creates friends list for requests and invites in current app.
        
        :param extended: 
        :param count: List size.
        :param offset: 
        :param type_: List type. Possible values: * 'invite' — available for invites (don't play the game),, * 'request' — available for request (play the game). By default: 'invite'.
        :param fields: Additional profile fields, see [vk.com/dev/fields|description].
        """
    
        if fields:
            fields = ','.join(fields)
        
        param_alias_dict = {'type_': 'type'}
        method_name = 'apps.getFriendsList'
        return self._call(method_name, locals())

    def get_leaderboard(self, type_: str, global_: bool = None, extended: bool = None):
        """
        Returns players rating in the game.
        
        :param type_: Leaderboard type. Possible values: *'level' — by level,, *'points' — by mission points,, *'score' — by score ().
        :param global_: Rating type. Possible values: *'1' — global rating among all players,, *'0' — rating among user friends.
        :param extended: 1 — to return additional info about users
        """
    
        param_alias_dict = {'type_': 'type', 'global_': 'global'}
        method_name = 'apps.getLeaderboard'
        return self._call(method_name, locals())

    def get_scopes(self, type_: str = None):
        """
        Returns scopes for auth
        
        :param type_: 
        """
    
        param_alias_dict = {'type_': 'type'}
        method_name = 'apps.getScopes'
        return self._call(method_name, locals())

    def get_score(self, user_id: int):
        """
        Returns user score in app
        
        :param user_id: 
        """
    
        method_name = 'apps.getScore'
        return self._call(method_name, locals())

    def promo_has_active_gift(self, promo_id: int, user_id: int = None):
        """
        
        :param promo_id: Id of game promo action
        :param user_id: 
        """
    
        method_name = 'apps.promoHasActiveGift'
        return self._call(method_name, locals())

    def promo_use_gift(self, promo_id: int, user_id: int = None):
        """
        
        :param promo_id: Id of game promo action
        :param user_id: 
        """
    
        method_name = 'apps.promoUseGift'
        return self._call(method_name, locals())

    def send_request(self, user_id: int, text: str = None, type_: str = None, name: str = None, key: str = None, separate: bool = None):
        """
        Sends a request to another user in an app that uses VK authorization.
        
        :param user_id: id of the user to send a request
        :param text: request text
        :param type_: request type. Values: 'invite' – if the request is sent to a user who does not have the app installed,, 'request' – if a user has already installed the app
        :param name: 
        :param key: special string key to be sent with the request
        :param separate: 
        """
    
        param_alias_dict = {'type_': 'type'}
        method_name = 'apps.sendRequest'
        return self._call(method_name, locals())

