from ._ApiMethod import ApiMethod
from typing import List


class Likes(ApiMethod):
    def __init__(self, session, access_token, v, requests_per_s):
        super().__init__(session, access_token, v, requests_per_s)

    def add(self, type_: str, item_id: int, owner_id: int = None, access_key: str = None):
        """
        Adds the specified object to the 'Likes' list of the current user.
        
        :param type_: Object type: 'post' — post on user or community wall, 'comment' — comment on a wall post, 'photo' — photo, 'audio' — audio, 'video' — video, 'note' — note, 'photo_comment' — comment on the photo, 'video_comment' — comment on the video, 'topic_comment' — comment in the discussion, 'sitepage' — page of the site where the [vk.com/dev/Like|Like widget] is installed
        :param item_id: Object ID.
        :param owner_id: ID of the user or community that owns the object.
        :param access_key: Access key required for an object owned by a private entity.
        """
    
        param_alias_dict = {'type_': 'type'}
        method_name = 'likes.add'
        return self._call(method_name, locals())

    def delete(self, type_: str, item_id: int, owner_id: int = None, access_key: str = None):
        """
        Deletes the specified object from the 'Likes' list of the current user.
        
        :param type_: Object type: 'post' — post on user or community wall, 'comment' — comment on a wall post, 'photo' — photo, 'audio' — audio, 'video' — video, 'note' — note, 'photo_comment' — comment on the photo, 'video_comment' — comment on the video, 'topic_comment' — comment in the discussion, 'sitepage' — page of the site where the [vk.com/dev/Like|Like widget] is installed
        :param item_id: Object ID.
        :param owner_id: ID of the user or community that owns the object.
        :param access_key: Access key required for an object owned by a private entity.
        """
    
        param_alias_dict = {'type_': 'type'}
        method_name = 'likes.delete'
        return self._call(method_name, locals())

    def get_list(self, type_: str, owner_id: int = None, item_id: int = None, page_url: str = None, filter_: str = None, friends_only: int = None, extended: bool = None, offset: int = None, count: int = None, skip_own: bool = None):
        """
        Returns a list of IDs of users who added the specified object to their 'Likes' list.
        
        :param type_: , Object type: 'post' — post on user or community wall, 'comment' — comment on a wall post, 'photo' — photo, 'audio' — audio, 'video' — video, 'note' — note, 'photo_comment' — comment on the photo, 'video_comment' — comment on the video, 'topic_comment' — comment in the discussion, 'sitepage' — page of the site where the [vk.com/dev/Like|Like widget] is installed
        :param owner_id: ID of the user, community, or application that owns the object. If the 'type' parameter is set as 'sitepage', the application ID is passed as 'owner_id'. Use negative value for a community id. If the 'type' parameter is not set, the 'owner_id' is assumed to be either the current user or the same application ID as if the 'type' parameter was set to 'sitepage'.
        :param item_id: Object ID. If 'type' is set as 'sitepage', 'item_id' can include the 'page_id' parameter value used during initialization of the [vk.com/dev/Like|Like widget].
        :param page_url: URL of the page where the [vk.com/dev/Like|Like widget] is installed. Used instead of the 'item_id' parameter.
        :param filter_: Filters to apply: 'likes' — returns information about all users who liked the object (default), 'copies' — returns information only about users who told their friends about the object
        :param friends_only: Specifies which users are returned: '1' — to return only the current user's friends, '0' — to return all users (default)
        :param extended: Specifies whether extended information will be returned. '1' — to return extended information about users and communities from the 'Likes' list, '0' — to return no additional information (default)
        :param offset: Offset needed to select a specific subset of users.
        :param count: Number of user IDs to return (maximum '1000'). Default is '100' if 'friends_only' is set to '0', otherwise, the default is '10' if 'friends_only' is set to '1'.
        :param skip_own: 
        """
    
        param_alias_dict = {'type_': 'type', 'filter_': 'filter'}
        method_name = 'likes.getList'
        return self._call(method_name, locals())

    def is_liked(self, type_: str, item_id: int, user_id: int = None, owner_id: int = None):
        """
        Checks for the object in the 'Likes' list of the specified user.
        
        :param type_: Object type: 'post' — post on user or community wall, 'comment' — comment on a wall post, 'photo' — photo, 'audio' — audio, 'video' — video, 'note' — note, 'photo_comment' — comment on the photo, 'video_comment' — comment on the video, 'topic_comment' — comment in the discussion
        :param item_id: Object ID.
        :param user_id: User ID.
        :param owner_id: ID of the user or community that owns the object.
        """
    
        param_alias_dict = {'type_': 'type'}
        method_name = 'likes.isLiked'
        return self._call(method_name, locals())

