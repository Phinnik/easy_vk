from _ApiMethod import ApiMethod
from typing import List


class Notifications(ApiMethod):
    def __init__(self, session, access_token, v, requests_per_s):
        super().__init__(session, access_token, v, requests_per_s)

    def get(self, count: int = None, start_from: str = None, filters: List[str] = None, start_time: int = None, end_time: int = None):
        """
        Returns a list of notifications about other users' feedback to the current user's wall posts.
        
        :param count: Number of notifications to return.
        :param start_from: 
        :param filters: Type of notifications to return: 'wall' — wall posts, 'mentions' — mentions in wall posts, comments, or topics, 'comments' — comments to wall posts, photos, and videos, 'likes' — likes, 'reposted' — wall posts that are copied from the current user's wall, 'followers' — new followers, 'friends' — accepted friend requests
        :param start_time: Earliest timestamp (in Unix time) of a notification to return. By default, 24 hours ago.
        :param end_time: Latest timestamp (in Unix time) of a notification to return. By default, the current time.
        """
    
        if filters:
            filters = ','.join(filters)
        
        method_name = 'notifications.get'
        return self.call(method_name, locals())

    def mark_as_viewed(self):
        """
        Resets the counter of new notifications about other users' feedback to the current user's wall posts.
        
        """
    
        method_name = 'notifications.markAsViewed'
        return self.call(method_name, locals())

    def send_message(self, user_ids: List[int], message: str, fragment: str = None, group_id: int = None):
        """
        
        :param user_ids: 
        :param message: 
        :param fragment: 
        :param group_id: 
        """
    
        if user_ids:
            user_ids = [str(u) for u in user_ids]
            user_ids = ','.join(user_ids)
        
        method_name = 'notifications.sendMessage'
        return self.call(method_name, locals())

