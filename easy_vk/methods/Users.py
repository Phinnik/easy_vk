from _ApiMethod import ApiMethod
from typing import List


class Users(ApiMethod):
    def __init__(self, session, access_token, v, requests_per_s):
        super().__init__(session, access_token, v, requests_per_s)

    def get(self, user_ids: List[str] = None, fields: List[str] = None, name_case: str = None):
        """
        Returns detailed information on users.
        
        :param user_ids: User IDs or screen names ('screen_name'). By default, current user ID.
        :param fields: Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'contacts', 'education', 'online', 'counters', 'relation', 'last_seen', 'activity', 'can_write_private_message', 'can_see_all_posts', 'can_post', 'universities', 'can_invite_to_chats'
        :param name_case: Case for declension of user name and surname: 'nom' — nominative (default), 'gen' — genitive , 'dat' — dative, 'acc' — accusative , 'ins' — instrumental , 'abl' — prepositional
        """
    
        if user_ids:
            user_ids = ','.join(user_ids)
        if fields:
            fields = ','.join(fields)
        
        method_name = 'users.get'
        return self.call(method_name, locals())

    def get_followers(self, user_id: int = None, offset: int = None, count: int = None, fields: List[str] = None, name_case: str = None):
        """
        Returns a list of IDs of followers of the user in question, sorted by date added, most recent first.
        
        :param user_id: User ID.
        :param offset: Offset needed to return a specific subset of followers.
        :param count: Number of followers to return.
        :param fields: Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'rate', 'contacts', 'education', 'online'.
        :param name_case: Case for declension of user name and surname: 'nom' — nominative (default), 'gen' — genitive , 'dat' — dative, 'acc' — accusative , 'ins' — instrumental , 'abl' — prepositional
        """
    
        if fields:
            fields = ','.join(fields)
        
        method_name = 'users.getFollowers'
        return self.call(method_name, locals())

    def get_subscriptions(self, user_id: int = None, extended: bool = None, offset: int = None, count: int = None, fields: List[str] = None):
        """
        Returns a list of IDs of users and communities followed by the user.
        
        :param user_id: User ID.
        :param extended: '1' — to return a combined list of users and communities, '0' — to return separate lists of users and communities (default)
        :param offset: Offset needed to return a specific subset of subscriptions.
        :param count: Number of users and communities to return.
        :param fields: 
        """
    
        if fields:
            fields = ','.join(fields)
        
        method_name = 'users.getSubscriptions'
        return self.call(method_name, locals())

    def report(self, user_id: int, type_: str, comment: str = None):
        """
        Reports (submits a complain about) a user.
        
        :param user_id: ID of the user about whom a complaint is being made.
        :param type_: Type of complaint: 'porn' – pornography, 'spam' – spamming, 'insult' – abusive behavior, 'advertisement' – disruptive advertisements
        :param comment: Comment describing the complaint.
        """
    
        param_alias_dict = {'type_': 'type'}
        method_name = 'users.report'
        return self.call(method_name, locals())

    def search(self, q: str = None, sort: int = None, offset: int = None, count: int = None, fields: List[str] = None, city: int = None, country: int = None, hometown: str = None, university_country: int = None, university: int = None, university_year: int = None, university_faculty: int = None, university_chair: int = None, sex: int = None, status: int = None, age_from: int = None, age_to: int = None, birth_day: int = None, birth_month: int = None, birth_year: int = None, online: bool = None, has_photo: bool = None, school_country: int = None, school_city: int = None, school_class: int = None, school: int = None, school_year: int = None, religion: str = None, company: str = None, position: str = None, group_id: int = None, from_list: List[str] = None):
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
    
        if fields:
            fields = ','.join(fields)
        if from_list:
            from_list = ','.join(from_list)
        
        method_name = 'users.search'
        return self.call(method_name, locals())

