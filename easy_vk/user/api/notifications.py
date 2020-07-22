from typing import List, Union, Optional
from easy_vk.types import objects, responses
from .base import BaseCategory


class Notifications(BaseCategory):
    def __init__(self, session, access_token: str, v: str, delay: float, auto_retry: bool, max_retries: int, timeout: float):
        super().__init__(session, access_token, v, delay, auto_retry, max_retries, timeout)

    def get(self, count: int = None, start_from: str = None, filters: List[str] = None, start_time: int = None, end_time: int = None) -> responses.NotificationsGet:
        """
        Returns a list of notifications about other users' feedback to the current user's wall posts.
        
        :param count: Number of notifications to return.
        :param start_from: 
        :param filters: Type of notifications to return: 'wall' — wall posts, 'mentions' — mentions in wall posts, comments, or topics, 'comments' — comments to wall posts, photos, and videos, 'likes' — likes, 'reposted' — wall posts that are copied from the current user's wall, 'followers' — new followers, 'friends' — accepted friend requests
        :param start_time: Earliest timestamp (in Unix time) of a notification to return. By default, 24 hours ago.
        :param end_time: Latest timestamp (in Unix time) of a notification to return. By default, the current time.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'notifications.get'
        param_aliases = []
        response_type = responses.NotificationsGet
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def mark_as_viewed(self) -> responses.NotificationsMarkAsViewed:
        """
        Resets the counter of new notifications about other users' feedback to the current user's wall posts.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'notifications.markAsViewed'
        param_aliases = []
        response_type = responses.NotificationsMarkAsViewed
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def send_message(self, user_ids: List[int] = None, message: str = None, fragment: str = None, group_id: int = None, random_id: int = None) -> responses.NotificationsSendMessage:
        """
        :param user_ids: 
        :param message: 
        :param fragment: 
        :param group_id: 
        :param random_id: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'notifications.sendMessage'
        param_aliases = []
        response_type = responses.NotificationsSendMessage
        return self._call(method_name, method_parameters, param_aliases, response_type)

