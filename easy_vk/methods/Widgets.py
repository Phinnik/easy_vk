from _ApiMethod import ApiMethod
from typing import List


class Widgets(ApiMethod):
    def __init__(self, session, access_token, v, requests_per_s):
        super().__init__(session, access_token, v, requests_per_s)

    def get_comments(self, widget_api_id: int = None, url: str = None, page_id: str = None, order: str = None, fields: List[str] = None, offset: int = None, count: int = None):
        """
        Gets a list of comments for the page added through the [vk.com/dev/Comments|Comments widget].
        
        :param widget_api_id: 
        :param url: 
        :param page_id: 
        :param order: 
        :param fields: 
        :param offset: 
        :param count: 
        """
    
        if fields:
            fields = ','.join(fields)
        
        method_name = 'widgets.getComments'
        return self.call(method_name, locals())

    def get_pages(self, widget_api_id: int = None, order: str = None, period: str = None, offset: int = None, count: int = None):
        """
        Gets a list of application/site pages where the [vk.com/dev/Comments|Comments widget] or [vk.com/dev/Like|Like widget] is installed.
        
        :param widget_api_id: 
        :param order: 
        :param period: 
        :param offset: 
        :param count: 
        """
    
        method_name = 'widgets.getPages'
        return self.call(method_name, locals())

