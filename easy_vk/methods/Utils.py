from _ApiMethod import ApiMethod
from typing import List


class Utils(ApiMethod):
    def __init__(self, session, access_token, v, requests_per_s):
        super().__init__(session, access_token, v, requests_per_s)

    def check_link(self, url: str):
        """
        Checks whether a link is blocked in VK.
        
        :param url: Link to check (e.g., 'http://google.com').
        """
    
        method_name = 'utils.checkLink'
        return self.call(method_name, locals())

    def delete_from_last_shortened(self, key: str):
        """
        Deletes shortened link from user's list.
        
        :param key: Link key (characters after vk.cc/).
        """
    
        method_name = 'utils.deleteFromLastShortened'
        return self.call(method_name, locals())

    def get_last_shortened_links(self, count: int = None, offset: int = None):
        """
        Returns a list of user's shortened links.
        
        :param count: Number of links to return.
        :param offset: Offset needed to return a specific subset of links.
        """
    
        method_name = 'utils.getLastShortenedLinks'
        return self.call(method_name, locals())

    def get_link_stats(self, key: str, source: str = None, access_key: str = None, interval: str = None, intervals_count: int = None, extended: bool = None):
        """
        Returns stats data for shortened link.
        
        :param key: Link key (characters after vk.cc/).
        :param source: Source of scope
        :param access_key: Access key for private link stats.
        :param interval: Interval.
        :param intervals_count: Number of intervals to return.
        :param extended: 1 — to return extended stats data (sex, age, geo). 0 — to return views number only.
        """
    
        method_name = 'utils.getLinkStats'
        return self.call(method_name, locals())

    def get_server_time(self):
        """
        Returns the current time of the VK server.
        
        """
    
        method_name = 'utils.getServerTime'
        return self.call(method_name, locals())

    def get_short_link(self, url: str, private: bool = None):
        """
        Allows to receive a link shortened via vk.cc.
        
        :param url: URL to be shortened.
        :param private: 1 — private stats, 0 — public stats.
        """
    
        method_name = 'utils.getShortLink'
        return self.call(method_name, locals())

    def resolve_screen_name(self, screen_name: str):
        """
        Detects a type of object (e.g., user, community, application) and its ID by screen name.
        
        :param screen_name: Screen name of the user, community (e.g., 'apiclub,' 'andrew', or 'rules_of_war'), or application.
        """
    
        method_name = 'utils.resolveScreenName'
        return self.call(method_name, locals())

