# This file was autogenerated from vk-api json schema

from typing import List, Union, Optional, Literal, overload
from easy_vk.types import objects
from easy_vk.types import responses
from easy_vk.api_category import BaseCategory


class Users(BaseCategory):
    def __init__(self, session, access_token: str, v: str, last_call_timer, delay: float, auto_retry: bool, max_retries: int, timeout: float):
        super().__init__(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)

    def get(self, user_ids: Optional[List[str]] = None, fields: Optional[List[Union[objects.UsersFields, str]]] = None, name_case: Optional[str] = None) -> responses.UsersGet:
        """
        Returns detailed information on users.
        
        :param user_ids: User IDs or screen names ('screen_name'). By default, current user ID.
        :param fields: Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'contacts', 'education', 'online', 'counters', 'relation', 'last_seen', 'activity', 'can_write_private_message', 'can_see_all_posts', 'can_post', 'universities', 'can_invite_to_chats'
        :param name_case: Case for declension of user name and surname: 'nom' — nominative (default), 'gen' — genitive , 'dat' — dative, 'acc' — accusative , 'ins' — instrumental , 'abl' — prepositional
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'users.get'
        response_type = responses.UsersGet
        return self._call(method_name, method_parameters, param_aliases, response_type)

    @overload
    def get_followers(self, user_id: Optional[int] = None, offset: Optional[int] = None, count: Optional[int] = None, fields: None = None, name_case: Optional[str] = None) -> responses.UsersGetFollowers: ...
    @overload
    def get_followers(self, fields: List[Union[objects.UsersFields, str]], user_id: Optional[int] = None, offset: Optional[int] = None, count: Optional[int] = None, name_case: Optional[str] = None) -> responses.UsersGetFollowersFields: ...
    def get_followers(self, user_id: Optional[int] = None, offset: Optional[int] = None, count: Optional[int] = None, fields: Optional[List[Union[objects.UsersFields, str]]] = None, name_case: Optional[str] = None):
        """
        Returns a list of IDs of followers of the user in question, sorted by date added, most recent first.
        
        :param user_id: User ID.
        :param offset: Offset needed to return a specific subset of followers.
        :param count: Number of followers to return.
        :param fields: Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'rate', 'contacts', 'education', 'online'.
        :param name_case: Case for declension of user name and surname: 'nom' — nominative (default), 'gen' — genitive , 'dat' — dative, 'acc' — accusative , 'ins' — instrumental , 'abl' — prepositional
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'users.getFollowers'
        if not fields:
            response_type = responses.UsersGetFollowers
        if fields:
            response_type = responses.UsersGetFollowersFields
        return self._call(method_name, method_parameters, param_aliases, response_type)

    @overload
    def get_subscriptions(self, user_id: Optional[int] = None, extended: None = None, offset: Optional[int] = None, count: Optional[int] = None, fields: Optional[List[Union[objects.UsersFields, str]]] = None) -> responses.UsersGetSubscriptions: ...
    @overload
    def get_subscriptions(self, extended: bool, user_id: Optional[int] = None, offset: Optional[int] = None, count: Optional[int] = None, fields: Optional[List[Union[objects.UsersFields, str]]] = None) -> responses.UsersGetSubscriptionsExtended: ...
    def get_subscriptions(self, user_id: Optional[int] = None, extended: Optional[bool] = None, offset: Optional[int] = None, count: Optional[int] = None, fields: Optional[List[Union[objects.UsersFields, str]]] = None):
        """
        Returns a list of IDs of users and communities followed by the user.
        
        :param user_id: User ID.
        :param extended: '1' — to return a combined list of users and communities, '0' — to return separate lists of users and communities (default)
        :param offset: Offset needed to return a specific subset of subscriptions.
        :param count: Number of users and communities to return.
        :param fields:
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'users.getSubscriptions'
        if not extended:
            response_type = responses.UsersGetSubscriptions
        if extended:
            response_type = responses.UsersGetSubscriptionsExtended
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def report(self, user_id: int, type_: str, comment: Optional[str] = None) -> responses.BaseOk:
        """
        Reports (submits a complain about) a user.
        
        :param user_id: ID of the user about whom a complaint is being made.
        :param type_: Type of complaint: 'porn' – pornography, 'spam' – spamming, 'insult' – abusive behavior, 'advertisement' – disruptive advertisements
        :param comment: Comment describing the complaint.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = [('type_', 'type')]
        method_name = 'users.report'
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def search(self, q: Optional[str] = None, sort: Optional[int] = None, offset: Optional[int] = None, count: Optional[int] = None, fields: Optional[List[Union[objects.UsersFields, str]]] = None, city: Optional[int] = None, country: Optional[int] = None, hometown: Optional[str] = None, university_country: Optional[int] = None, university: Optional[int] = None, university_year: Optional[int] = None, university_faculty: Optional[int] = None, university_chair: Optional[int] = None, sex: Optional[int] = None, status: Optional[int] = None, age_from: Optional[int] = None, age_to: Optional[int] = None, birth_day: Optional[int] = None, birth_month: Optional[int] = None, birth_year: Optional[int] = None, online: Optional[bool] = None, has_photo: Optional[bool] = None, school_country: Optional[int] = None, school_city: Optional[int] = None, school_class: Optional[int] = None, school: Optional[int] = None, school_year: Optional[int] = None, religion: Optional[str] = None, company: Optional[str] = None, position: Optional[str] = None, group_id: Optional[int] = None, from_list: Optional[List[str]] = None) -> responses.UsersSearch:
        """
        Returns a list of users matching the search criteria.
        
        :param q: Search query string (e.g., 'Vasya Babich').
        :param sort: Sort order: '1' — by date registered, '0' — by rating
        :param offset: Offset needed to return a specific subset of users.
        :param count: Number of users to return.
        :param fields: Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'rate', 'contacts', 'education', 'online',
        :param city: City ID.
        :param country: Country ID.
        :param hometown: City name in a string.
        :param university_country: ID of the country where the user graduated.
        :param university: ID of the institution of higher education.
        :param university_year: Year of graduation from an institution of higher education.
        :param university_faculty: Faculty ID.
        :param university_chair: Chair ID.
        :param sex: '1' — female, '2' — male, '0' — any (default)
        :param status: Relationship status: '1' — Not married, '2' — In a relationship, '3' — Engaged, '4' — Married, '5' — It's complicated, '6' — Actively searching, '7' — In love
        :param age_from: Minimum age.
        :param age_to: Maximum age.
        :param birth_day: Day of birth.
        :param birth_month: Month of birth.
        :param birth_year: Year of birth.
        :param online: '1' — online only, '0' — all users
        :param has_photo: '1' — with photo only, '0' — all users
        :param school_country: ID of the country where users finished school.
        :param school_city: ID of the city where users finished school.
        :param school_class:
        :param school: ID of the school.
        :param school_year: School graduation year.
        :param religion: Users' religious affiliation.
        :param company: Name of the company where users work.
        :param position: Job position.
        :param group_id: ID of a community to search in communities.
        :param from_list:
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'users.search'
        response_type = responses.UsersSearch
        return self._call(method_name, method_parameters, param_aliases, response_type)
