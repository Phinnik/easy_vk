from ._ApiMethod import ApiMethod
from typing import List


class Pages(ApiMethod):
    def __init__(self, session, access_token, v, requests_per_s):
        super().__init__(session, access_token, v, requests_per_s)

    def clear_cache(self, url: str):
        """
        Allows to clear the cache of particular 'external' pages which may be attached to VK posts.
        
        :param url: Address of the page where you need to refesh the cached version
        """
    
        method_name = 'pages.clearCache'
        return self._call(method_name, locals())

    def get(self, owner_id: int = None, page_id: int = None, global_: bool = None, site_preview: bool = None, title: str = None, need_source: bool = None, need_html: bool = None):
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
    
        param_alias_dict = {'global_': 'global'}
        method_name = 'pages.get'
        return self._call(method_name, locals())

    def get_history(self, page_id: int, group_id: int = None, user_id: int = None):
        """
        Returns a list of all previous versions of a wiki page.
        
        :param page_id: Wiki page ID.
        :param group_id: ID of the community that owns the wiki page.
        :param user_id: 
        """
    
        method_name = 'pages.getHistory'
        return self._call(method_name, locals())

    def get_titles(self, group_id: int = None):
        """
        Returns a list of wiki pages in a group.
        
        :param group_id: ID of the community that owns the wiki page.
        """
    
        method_name = 'pages.getTitles'
        return self._call(method_name, locals())

    def get_version(self, version_id: int, group_id: int = None, user_id: int = None, need_html: bool = None):
        """
        Returns the text of one of the previous versions of a wiki page.
        
        :param version_id: 
        :param group_id: ID of the community that owns the wiki page.
        :param user_id: 
        :param need_html: '1' — to return the page as HTML
        """
    
        method_name = 'pages.getVersion'
        return self._call(method_name, locals())

    def parse_wiki(self, text: str, group_id: int = None):
        """
        Returns HTML representation of the wiki markup.
        
        :param text: Text of the wiki page.
        :param group_id: ID of the group in the context of which this markup is interpreted.
        """
    
        method_name = 'pages.parseWiki'
        return self._call(method_name, locals())

    def save(self, text: str = None, page_id: int = None, group_id: int = None, user_id: int = None, title: str = None):
        """
        Saves the text of a wiki page.
        
        :param text: Text of the wiki page in wiki-format.
        :param page_id: Wiki page ID. The 'title' parameter can be passed instead of 'pid'.
        :param group_id: ID of the community that owns the wiki page.
        :param user_id: User ID
        :param title: Wiki page title.
        """
    
        method_name = 'pages.save'
        return self._call(method_name, locals())

    def save_access(self, page_id: int, group_id: int = None, user_id: int = None, view: int = None, edit: int = None):
        """
        Saves modified read and edit access settings for a wiki page.
        
        :param page_id: Wiki page ID.
        :param group_id: ID of the community that owns the wiki page.
        :param user_id: 
        :param view: Who can view the wiki page: '1' — only community members, '2' — all users can view the page, '0' — only community managers
        :param edit: Who can edit the wiki page: '1' — only community members, '2' — all users can edit the page, '0' — only community managers
        """
    
        method_name = 'pages.saveAccess'
        return self._call(method_name, locals())

