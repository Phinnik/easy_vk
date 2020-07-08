from ._ApiMethod import ApiMethod
from typing import List


class Newsfeed(ApiMethod):
    def __init__(self, session, access_token, v, requests_per_s):
        super().__init__(session, access_token, v, requests_per_s)

    def add_ban(self, user_ids: List[int] = None, group_ids: List[int] = None):
        """
        Prevents news from specified users and communities from appearing in the current user's newsfeed.
        
        :param user_ids: 
        :param group_ids: 
        """
    
        if user_ids:
            user_ids = [str(u) for u in user_ids]
            user_ids = ','.join(user_ids)
        if group_ids:
            group_ids = [str(g) for g in group_ids]
            group_ids = ','.join(group_ids)
        
        method_name = 'newsfeed.addBan'
        return self._call(method_name, locals())

    def delete_ban(self, user_ids: List[int] = None, group_ids: List[int] = None):
        """
        Allows news from previously banned users and communities to be shown in the current user's newsfeed.
        
        :param user_ids: 
        :param group_ids: 
        """
    
        if user_ids:
            user_ids = [str(u) for u in user_ids]
            user_ids = ','.join(user_ids)
        if group_ids:
            group_ids = [str(g) for g in group_ids]
            group_ids = ','.join(group_ids)
        
        method_name = 'newsfeed.deleteBan'
        return self._call(method_name, locals())

    def delete_list(self, list_id: int):
        """
        
        :param list_id: 
        """
    
        method_name = 'newsfeed.deleteList'
        return self._call(method_name, locals())

    def get(self, filters: List[str] = None, return_banned: bool = None, start_time: int = None, end_time: int = None, max_photos: int = None, source_ids: str = None, start_from: str = None, count: int = None, fields: List[str] = None, section: str = None):
        """
        Returns data required to show newsfeed for the current user.
        
        :param filters: Filters to apply: 'post' — new wall posts, 'photo' — new photos, 'photo_tag' — new photo tags, 'wall_photo' — new wall photos, 'friend' — new friends, 'note' — new notes
        :param return_banned: '1' — to return news items from banned sources
        :param start_time: Earliest timestamp (in Unix time) of a news item to return. By default, 24 hours ago.
        :param end_time: Latest timestamp (in Unix time) of a news item to return. By default, the current time.
        :param max_photos: Maximum number of photos to return. By default, '5'.
        :param source_ids: Sources to obtain news from, separated by commas. User IDs can be specified in formats '' or 'u' , where '' is the user's friend ID. Community IDs can be specified in formats '-' or 'g' , where '' is the community ID. If the parameter is not set, all of the user's friends and communities are returned, except for banned sources, which can be obtained with the [vk.com/dev/newsfeed.getBanned|newsfeed.getBanned] method.
        :param start_from: identifier required to get the next page of results. Value for this parameter is returned in 'next_from' field in a reply.
        :param count: Number of news items to return (default 50, maximum 100). For auto feed, you can use the 'new_offset' parameter returned by this method.
        :param fields: Additional fields of [vk.com/dev/fields|profiles] and [vk.com/dev/fields_groups|communities] to return.
        :param section: 
        """
    
        if filters:
            filters = ','.join(filters)
        if fields:
            fields = ','.join(fields)
        
        method_name = 'newsfeed.get'
        return self._call(method_name, locals())

    def get_banned(self, extended: bool = None, fields: List[str] = None, name_case: str = None):
        """
        Returns a list of users and communities banned from the current user's newsfeed.
        
        :param extended: '1' — return extra information about users and communities
        :param fields: Profile fields to return.
        :param name_case: Case for declension of user name and surname: 'nom' — nominative (default), 'gen' — genitive , 'dat' — dative, 'acc' — accusative , 'ins' — instrumental , 'abl' — prepositional
        """
    
        if fields:
            fields = ','.join(fields)
        
        method_name = 'newsfeed.getBanned'
        return self._call(method_name, locals())

    def get_comments(self, count: int = None, filters: List[str] = None, reposts: str = None, start_time: int = None, end_time: int = None, last_comments_count: int = None, start_from: str = None, fields: List[str] = None):
        """
        Returns a list of comments in the current user's newsfeed.
        
        :param count: Number of comments to return. For auto feed, you can use the 'new_offset' parameter returned by this method.
        :param filters: Filters to apply: 'post' — new comments on wall posts, 'photo' — new comments on photos, 'video' — new comments on videos, 'topic' — new comments on discussions, 'note' — new comments on notes,
        :param reposts: Object ID, comments on repost of which shall be returned, e.g. 'wall1_45486'. (If the parameter is set, the 'filters' parameter is optional.),
        :param start_time: Earliest timestamp (in Unix time) of a comment to return. By default, 24 hours ago.
        :param end_time: Latest timestamp (in Unix time) of a comment to return. By default, the current time.
        :param last_comments_count: 
        :param start_from: Identificator needed to return the next page with results. Value for this parameter returns in 'next_from' field.
        :param fields: Additional fields of [vk.com/dev/fields|profiles] and [vk.com/dev/fields_groups|communities] to return.
        """
    
        if filters:
            filters = ','.join(filters)
        if fields:
            fields = ','.join(fields)
        
        method_name = 'newsfeed.getComments'
        return self._call(method_name, locals())

    def get_lists(self, list_ids: List[int] = None, extended: bool = None):
        """
        Returns a list of newsfeeds followed by the current user.
        
        :param list_ids: numeric list identifiers.
        :param extended: Return additional list info
        """
    
        if list_ids:
            list_ids = [str(l) for l in list_ids]
            list_ids = ','.join(list_ids)
        
        method_name = 'newsfeed.getLists'
        return self._call(method_name, locals())

    def get_mentions(self, owner_id: int = None, start_time: int = None, end_time: int = None, offset: int = None, count: int = None):
        """
        Returns a list of posts on user walls in which the current user is mentioned.
        
        :param owner_id: Owner ID.
        :param start_time: Earliest timestamp (in Unix time) of a post to return. By default, 24 hours ago.
        :param end_time: Latest timestamp (in Unix time) of a post to return. By default, the current time.
        :param offset: Offset needed to return a specific subset of posts.
        :param count: Number of posts to return.
        """
    
        method_name = 'newsfeed.getMentions'
        return self._call(method_name, locals())

    def get_recommended(self, start_time: int = None, end_time: int = None, max_photos: int = None, start_from: str = None, count: int = None, fields: List[str] = None):
        """
        , Returns a list of newsfeeds recommended to the current user.
        
        :param start_time: Earliest timestamp (in Unix time) of a news item to return. By default, 24 hours ago.
        :param end_time: Latest timestamp (in Unix time) of a news item to return. By default, the current time.
        :param max_photos: Maximum number of photos to return. By default, '5'.
        :param start_from: 'new_from' value obtained in previous call.
        :param count: Number of news items to return.
        :param fields: Additional fields of [vk.com/dev/fields|profiles] and [vk.com/dev/fields_groups|communities] to return.
        """
    
        if fields:
            fields = ','.join(fields)
        
        method_name = 'newsfeed.getRecommended'
        return self._call(method_name, locals())

    def get_suggested_sources(self, offset: int = None, count: int = None, shuffle: bool = None, fields: List[str] = None):
        """
        Returns communities and users that current user is suggested to follow.
        
        :param offset: offset required to choose a particular subset of communities or users.
        :param count: amount of communities or users to return.
        :param shuffle: shuffle the returned list or not.
        :param fields: list of extra fields to be returned. See available fields for [vk.com/dev/fields|users] and [vk.com/dev/fields_groups|communities].
        """
    
        if fields:
            fields = ','.join(fields)
        
        method_name = 'newsfeed.getSuggestedSources'
        return self._call(method_name, locals())

    def ignore_item(self, type_: str, owner_id: int, item_id: int):
        """
        Hides an item from the newsfeed.
        
        :param type_: Item type. Possible values: *'wall' – post on the wall,, *'tag' – tag on a photo,, *'profilephoto' – profile photo,, *'video' – video,, *'audio' – audio.
        :param owner_id: Item owner's identifier (user or community), "Note that community id must be negative. 'owner_id=1' – user , 'owner_id=-1' – community "
        :param item_id: Item identifier
        """
    
        param_alias_dict = {'type_': 'type'}
        method_name = 'newsfeed.ignoreItem'
        return self._call(method_name, locals())

    def save_list(self, title: str, list_id: int = None, source_ids: List[int] = None, no_reposts: bool = None):
        """
        Creates and edits user newsfeed lists
        
        :param title: list name.
        :param list_id: numeric list identifier (if not sent, will be set automatically).
        :param source_ids: users and communities identifiers to be added to the list. Community identifiers must be negative numbers.
        :param no_reposts: reposts display on and off ('1' is for off).
        """
    
        if source_ids:
            source_ids = [str(s) for s in source_ids]
            source_ids = ','.join(source_ids)
        
        method_name = 'newsfeed.saveList'
        return self._call(method_name, locals())

    def search(self, q: str = None, extended: bool = None, count: int = None, latitude: float = None, longitude: float = None, start_time: int = None, end_time: int = None, start_from: str = None, fields: List[str] = None):
        """
        Returns search results by statuses.
        
        :param q: Search query string (e.g., 'New Year').
        :param extended: '1' — to return additional information about the user or community that placed the post.
        :param count: Number of posts to return.
        :param latitude: Geographical latitude point (in degrees, -90 to 90) within which to search.
        :param longitude: Geographical longitude point (in degrees, -180 to 180) within which to search.
        :param start_time: Earliest timestamp (in Unix time) of a news item to return. By default, 24 hours ago.
        :param end_time: Latest timestamp (in Unix time) of a news item to return. By default, the current time.
        :param start_from: 
        :param fields: Additional fields of [vk.com/dev/fields|profiles] and [vk.com/dev/fields_groups|communities] to return.
        """
    
        if fields:
            fields = ','.join(fields)
        
        method_name = 'newsfeed.search'
        return self._call(method_name, locals())

    def unignore_item(self, type_: str, owner_id: int, item_id: int):
        """
        Returns a hidden item to the newsfeed.
        
        :param type_: Item type. Possible values: *'wall' – post on the wall,, *'tag' – tag on a photo,, *'profilephoto' – profile photo,, *'video' – video,, *'audio' – audio.
        :param owner_id: Item owner's identifier (user or community), "Note that community id must be negative. 'owner_id=1' – user , 'owner_id=-1' – community "
        :param item_id: Item identifier
        """
    
        param_alias_dict = {'type_': 'type'}
        method_name = 'newsfeed.unignoreItem'
        return self._call(method_name, locals())

    def unsubscribe(self, type_: str, item_id: int, owner_id: int = None):
        """
        Unsubscribes the current user from specified newsfeeds.
        
        :param type_: Type of object from which to unsubscribe: 'note' — note, 'photo' — photo, 'post' — post on user wall or community wall, 'topic' — topic, 'video' — video
        :param item_id: Object ID.
        :param owner_id: Object owner ID.
        """
    
        param_alias_dict = {'type_': 'type'}
        method_name = 'newsfeed.unsubscribe'
        return self._call(method_name, locals())

