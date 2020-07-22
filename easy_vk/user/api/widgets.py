from typing import List, Union, Optional
from easy_vk.types import objects, responses
from .base import BaseCategory


class Widgets(BaseCategory):
    def __init__(self, session, access_token: str, v: str, delay: float, auto_retry: bool, max_retries: int, timeout: float):
        super().__init__(session, access_token, v, delay, auto_retry, max_retries, timeout)

    def get_comments(self, widget_api_id: int = None, url: str = None, page_id: str = None, order: str = None, fields: List[Union[objects.UsersFields, str]] = None, offset: int = None, count: int = None) -> responses.WidgetsGetComments:
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
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'widgets.getComments'
        param_aliases = []
        response_type = responses.WidgetsGetComments
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_pages(self, widget_api_id: int = None, order: str = None, period: str = None, offset: int = None, count: int = None) -> responses.WidgetsGetPages:
        """
        Gets a list of application/site pages where the [vk.com/dev/Comments|Comments widget] or [vk.com/dev/Like|Like widget] is installed.
        
        :param widget_api_id: 
        :param order: 
        :param period: 
        :param offset: 
        :param count: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'widgets.getPages'
        param_aliases = []
        response_type = responses.WidgetsGetPages
        return self._call(method_name, method_parameters, param_aliases, response_type)

