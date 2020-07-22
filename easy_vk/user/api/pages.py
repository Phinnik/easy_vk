from typing import List, Union, Optional
from easy_vk.types import objects, responses
from .base import BaseCategory


class Pages(BaseCategory):
    def __init__(self, session, access_token: str, v: str, delay: float, auto_retry: bool, max_retries: int, timeout: float):
        super().__init__(session, access_token, v, delay, auto_retry, max_retries, timeout)

    def clear_cache(self, url: str = None) -> responses.BaseOk:
        """
        Allows to clear the cache of particular 'external' pages which may be attached to VK posts.
        
        :param url: Address of the page where you need to refesh the cached version
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'pages.clearCache'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get(self, owner_id: int = None, page_id: int = None, global_: bool = None, site_preview: bool = None, title: str = None, need_source: bool = None, need_html: bool = None) -> responses.PagesGet:
        """
        Returns information about a wiki page.
        
        :param owner_id: Page owner ID.
        :param page_id: Wiki page ID.
        :param global_: '1' — to return information about a global wiki page
        :param site_preview: '1' — resulting wiki page is a preview for the attached link
        :param title: Wiki page title.
        :param need_source: 
        :param need_html: '1' — to return the page as HTML,
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'pages.get'
        param_aliases = [('global_', 'global')]
        response_type = responses.PagesGet
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_history(self, page_id: int = None, group_id: int = None, user_id: int = None) -> responses.PagesGetHistory:
        """
        Returns a list of all previous versions of a wiki page.
        
        :param page_id: Wiki page ID.
        :param group_id: ID of the community that owns the wiki page.
        :param user_id: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'pages.getHistory'
        param_aliases = []
        response_type = responses.PagesGetHistory
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_titles(self, group_id: int = None) -> responses.PagesGetTitles:
        """
        Returns a list of wiki pages in a group.
        
        :param group_id: ID of the community that owns the wiki page.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'pages.getTitles'
        param_aliases = []
        response_type = responses.PagesGetTitles
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_version(self, version_id: int = None, group_id: int = None, user_id: int = None, need_html: bool = None) -> responses.PagesGetVersion:
        """
        Returns the text of one of the previous versions of a wiki page.
        
        :param version_id: 
        :param group_id: ID of the community that owns the wiki page.
        :param user_id: 
        :param need_html: '1' — to return the page as HTML
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'pages.getVersion'
        param_aliases = []
        response_type = responses.PagesGetVersion
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def parse_wiki(self, text: str = None, group_id: int = None) -> responses.PagesParseWiki:
        """
        Returns HTML representation of the wiki markup.
        
        :param text: Text of the wiki page.
        :param group_id: ID of the group in the context of which this markup is interpreted.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'pages.parseWiki'
        param_aliases = []
        response_type = responses.PagesParseWiki
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def save(self, text: str = None, page_id: int = None, group_id: int = None, user_id: int = None, title: str = None) -> responses.PagesSave:
        """
        Saves the text of a wiki page.
        
        :param text: Text of the wiki page in wiki-format.
        :param page_id: Wiki page ID. The 'title' parameter can be passed instead of 'pid'.
        :param group_id: ID of the community that owns the wiki page.
        :param user_id: User ID
        :param title: Wiki page title.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'pages.save'
        param_aliases = []
        response_type = responses.PagesSave
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def save_access(self, page_id: int = None, group_id: int = None, user_id: int = None, view: int = None, edit: int = None) -> responses.PagesSaveAccess:
        """
        Saves modified read and edit access settings for a wiki page.
        
        :param page_id: Wiki page ID.
        :param group_id: ID of the community that owns the wiki page.
        :param user_id: 
        :param view: Who can view the wiki page: '1' — only community members, '2' — all users can view the page, '0' — only community managers
        :param edit: Who can edit the wiki page: '1' — only community members, '2' — all users can edit the page, '0' — only community managers
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'pages.saveAccess'
        param_aliases = []
        response_type = responses.PagesSaveAccess
        return self._call(method_name, method_parameters, param_aliases, response_type)

