from typing import List, Union, Optional
from easy_vk.types import objects, responses
from .base import BaseCategory


class Friends(BaseCategory):
    def __init__(self, session, access_token: str, v: str, delay: float, auto_retry: bool, max_retries: int, timeout: float):
        super().__init__(session, access_token, v, delay, auto_retry, max_retries, timeout)

    def add(self, user_id: int = None, text: str = None, follow: bool = None) -> responses.FriendsAdd:
        """
        Approves or creates a friend request.
        
        :param user_id: ID of the user whose friend request will be approved or to whom a friend request will be sent.
        :param text: Text of the message (up to 500 characters) for the friend request, if any.
        :param follow: '1' to pass an incoming request to followers list.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'friends.add'
        param_aliases = []
        response_type = responses.FriendsAdd
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def add_list(self, name: str = None, user_ids: List[int] = None) -> responses.FriendsAddList:
        """
        Creates a new friend list for the current user.
        
        :param name: Name of the friend list.
        :param user_ids: IDs of users to be added to the friend list.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'friends.addList'
        param_aliases = []
        response_type = responses.FriendsAddList
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def are_friends(self, user_ids: List[int] = None, need_sign: bool = None, extended: bool = None) -> Union[responses.FriendsAreFriends, responses.FriendsAreFriendsExtended]:
        """
        Checks the current user's friendship status with other specified users.
        
        :param user_ids: IDs of the users whose friendship status to check.
        :param need_sign: '1' — to return 'sign' field. 'sign' is md5("{id}_{user_id}_{friends_status}_{application_secret}"), where id is current user ID. This field allows to check that data has not been modified by the client. By default: '0'.
        :param extended: Return friend request read_state field
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'friends.areFriends'
        param_aliases = []
        if not extended:
            response_type = responses.FriendsAreFriends
        else:
            response_type = responses.FriendsAreFriendsExtended
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def delete(self, user_id: int = None) -> responses.FriendsDelete:
        """
        Declines a friend request or deletes a user from the current user's friend list.
        
        :param user_id: ID of the user whose friend request is to be declined or who is to be deleted from the current user's friend list.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'friends.delete'
        param_aliases = []
        response_type = responses.FriendsDelete
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def delete_all_requests(self) -> responses.BaseOk:
        """
        Marks all incoming friend requests as viewed.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'friends.deleteAllRequests'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def delete_list(self, list_id: int = None) -> responses.BaseOk:
        """
        Deletes a friend list of the current user.
        
        :param list_id: ID of the friend list to delete.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'friends.deleteList'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def edit(self, user_id: int = None, list_ids: List[int] = None) -> responses.BaseOk:
        """
        Edits the friend lists of the selected user.
        
        :param user_id: ID of the user whose friend list is to be edited.
        :param list_ids: IDs of the friend lists to which to add the user.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'friends.edit'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def edit_list(self, name: str = None, list_id: int = None, user_ids: List[int] = None, add_user_ids: List[int] = None, delete_user_ids: List[int] = None) -> responses.BaseOk:
        """
        Edits a friend list of the current user.
        
        :param name: Name of the friend list.
        :param list_id: Friend list ID.
        :param user_ids: IDs of users in the friend list.
        :param add_user_ids: (Applies if 'user_ids' parameter is not set.), User IDs to add to the friend list.
        :param delete_user_ids: (Applies if 'user_ids' parameter is not set.), User IDs to delete from the friend list.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'friends.editList'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get(self, user_id: int = None, order: str = None, list_id: int = None, count: int = None, offset: int = None, fields: List[Union[objects.UsersFields, str]] = None, name_case: str = None, ref: str = None) -> Union[responses.FriendsGet, responses.FriendsGetFields]:
        """
        Returns a list of user IDs or detailed information about a user's friends.
        
        :param user_id: User ID. By default, the current user ID.
        :param order: Sort order: , 'name' — by name (enabled only if the 'fields' parameter is used), 'hints' — by rating, similar to how friends are sorted in My friends section, , This parameter is available only for [vk.com/dev/standalone|desktop applications].
        :param list_id: ID of the friend list returned by the [vk.com/dev/friends.getLists|friends.getLists] method to be used as the source. This parameter is taken into account only when the uid parameter is set to the current user ID. This parameter is available only for [vk.com/dev/standalone|desktop applications].
        :param count: Number of friends to return.
        :param offset: Offset needed to return a specific subset of friends.
        :param fields: Profile fields to return. Sample values: 'uid', 'first_name', 'last_name', 'nickname', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'domain', 'has_mobile', 'rate', 'contacts', 'education'.
        :param name_case: Case for declension of user name and surname: , 'nom' — nominative (default) , 'gen' — genitive , 'dat' — dative , 'acc' — accusative , 'ins' — instrumental , 'abl' — prepositional
        :param ref: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'friends.get'
        param_aliases = []
        if not fields:
            response_type = responses.FriendsGet
        else:
            response_type = responses.FriendsGetFields
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_app_users(self) -> responses.FriendsGetAppUsers:
        """
        Returns a list of IDs of the current user's friends who installed the application.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'friends.getAppUsers'
        param_aliases = []
        response_type = responses.FriendsGetAppUsers
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_by_phones(self, phones: List[str] = None, fields: List[Union[objects.UsersFields, str]] = None) -> responses.FriendsGetByPhones:
        """
        Returns a list of the current user's friends whose phone numbers, validated or specified in a profile, are in a given list.
        
        :param phones: List of phone numbers in MSISDN format (maximum 1000). Example: "+79219876543,+79111234567"
        :param fields: Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'rate', 'contacts', 'education', 'online, counters'.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'friends.getByPhones'
        param_aliases = []
        response_type = responses.FriendsGetByPhones
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_lists(self, user_id: int = None, return_system: bool = None) -> responses.FriendsGetLists:
        """
        Returns a list of the user's friend lists.
        
        :param user_id: User ID.
        :param return_system: '1' — to return system friend lists. By default: '0'.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'friends.getLists'
        param_aliases = []
        response_type = responses.FriendsGetLists
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_mutual(self, source_uid: int = None, target_uid: int = None, target_uids: List[int] = None, order: str = None, count: int = None, offset: int = None) -> Union[responses.FriendsGetMutual, responses.FriendsGetMutualTargetUids]:
        """
        Returns a list of user IDs of the mutual friends of two users.
        
        :param source_uid: ID of the user whose friends will be checked against the friends of the user specified in 'target_uid'.
        :param target_uid: ID of the user whose friends will be checked against the friends of the user specified in 'source_uid'.
        :param target_uids: IDs of the users whose friends will be checked against the friends of the user specified in 'source_uid'.
        :param order: Sort order: 'random' — random order
        :param count: Number of mutual friends to return.
        :param offset: Offset needed to return a specific subset of mutual friends.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'friends.getMutual'
        param_aliases = []
        if not target_uids:
            response_type = responses.FriendsGetMutual
        else:
            response_type = responses.FriendsGetMutualTargetUids
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_online(self, user_id: int = None, list_id: int = None, online_mobile: bool = None, order: str = None, count: int = None, offset: int = None) -> Union[responses.FriendsGetOnline, responses.FriendsGetOnlineOnlineMobile]:
        """
        Returns a list of user IDs of a user's friends who are online.
        
        :param user_id: User ID.
        :param list_id: Friend list ID. If this parameter is not set, information about all online friends is returned.
        :param online_mobile: '1' — to return an additional 'online_mobile' field, '0' — (default),
        :param order: Sort order: 'random' — random order
        :param count: Number of friends to return.
        :param offset: Offset needed to return a specific subset of friends.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'friends.getOnline'
        param_aliases = []
        if not online_mobile:
            response_type = responses.FriendsGetOnline
        else:
            response_type = responses.FriendsGetOnlineOnlineMobile
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_recent(self, count: int = None) -> responses.FriendsGetRecent:
        """
        Returns a list of user IDs of the current user's recently added friends.
        
        :param count: Number of recently added friends to return.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'friends.getRecent'
        param_aliases = []
        response_type = responses.FriendsGetRecent
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_requests(self, offset: int = None, count: int = None, extended: bool = None, need_mutual: bool = None, out: bool = None, sort: int = None, need_viewed: bool = None, suggested: bool = None, ref: str = None, fields: List[Union[objects.UsersFields, str]] = None) -> Union[responses.FriendsGetRequests, responses.FriendsGetRequestsNeedMutual, responses.FriendsGetRequestsExtended]:
        """
        Returns information about the current user's incoming and outgoing friend requests.
        
        :param offset: Offset needed to return a specific subset of friend requests.
        :param count: Number of friend requests to return (default 100, maximum 1000).
        :param extended: '1' — to return response messages from users who have sent a friend request or, if 'suggested' is set to '1', to return a list of suggested friends
        :param need_mutual: '1' — to return a list of mutual friends (up to 20), if any
        :param out: '1' — to return outgoing requests, '0' — to return incoming requests (default)
        :param sort: Sort order: '1' — by number of mutual friends, '0' — by date
        :param need_viewed: 
        :param suggested: '1' — to return a list of suggested friends, '0' — to return friend requests (default)
        :param ref: 
        :param fields: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'friends.getRequests'
        param_aliases = []
        if not extended and not need_mutual:
            response_type = responses.FriendsGetRequests
        elif need_mutual and not extended:
            response_type = responses.FriendsGetRequestsNeedMutual
        else:
            response_type = responses.FriendsGetRequestsExtended
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_suggestions(self, filter_: List[str] = None, count: int = None, offset: int = None, fields: List[Union[objects.UsersFields, str]] = None, name_case: str = None) -> responses.FriendsGetSuggestions:
        """
        Returns a list of profiles of users whom the current user may know.
        
        :param filter_: Types of potential friends to return: 'mutual' — users with many mutual friends , 'contacts' — users found with the [vk.com/dev/account.importContacts|account.importContacts] method , 'mutual_contacts' — users who imported the same contacts as the current user with the [vk.com/dev/account.importContacts|account.importContacts] method
        :param count: Number of suggestions to return.
        :param offset: Offset needed to return a specific subset of suggestions.
        :param fields: Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'rate', 'contacts', 'education', 'online', 'counters'.
        :param name_case: Case for declension of user name and surname: , 'nom' — nominative (default) , 'gen' — genitive , 'dat' — dative , 'acc' — accusative , 'ins' — instrumental , 'abl' — prepositional
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'friends.getSuggestions'
        param_aliases = [('filter_', 'filter')]
        response_type = responses.FriendsGetSuggestions
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def search(self, user_id: int = None, q: str = None, fields: List[Union[objects.UsersFields, str]] = None, name_case: str = None, offset: int = None, count: int = None) -> responses.FriendsSearch:
        """
        Returns a list of friends matching the search criteria.
        
        :param user_id: User ID.
        :param q: Search query string (e.g., 'Vasya Babich').
        :param fields: Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'rate', 'contacts', 'education', 'online',
        :param name_case: Case for declension of user name and surname: 'nom' — nominative (default), 'gen' — genitive , 'dat' — dative, 'acc' — accusative , 'ins' — instrumental , 'abl' — prepositional
        :param offset: Offset needed to return a specific subset of friends.
        :param count: Number of friends to return.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'friends.search'
        param_aliases = []
        response_type = responses.FriendsSearch
        return self._call(method_name, method_parameters, param_aliases, response_type)

