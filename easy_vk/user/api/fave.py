from typing import List, Union, Optional
from easy_vk.types import objects, responses
from .base import BaseCategory


class Fave(BaseCategory):
    def __init__(self, session, access_token: str, v: str, delay: float, auto_retry: bool, max_retries: int, timeout: float):
        super().__init__(session, access_token, v, delay, auto_retry, max_retries, timeout)

    def add_article(self, url: str = None) -> responses.BaseOk:
        """
        :param url: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'fave.addArticle'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def add_link(self, link: str = None) -> responses.BaseOk:
        """
        Adds a link to user faves.
        
        :param link: Link URL.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'fave.addLink'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def add_page(self, user_id: int = None, group_id: int = None) -> responses.BaseOk:
        """
        :param user_id: 
        :param group_id: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'fave.addPage'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def add_post(self, owner_id: int = None, id_: int = None, access_key: str = None) -> responses.BaseOk:
        """
        :param owner_id: 
        :param id_: 
        :param access_key: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'fave.addPost'
        param_aliases = [('id_', 'id')]
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def add_product(self, owner_id: int = None, id_: int = None, access_key: str = None) -> responses.BaseOk:
        """
        :param owner_id: 
        :param id_: 
        :param access_key: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'fave.addProduct'
        param_aliases = [('id_', 'id')]
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def add_tag(self, name: str = None, position: str = None) -> responses.FaveAddTag:
        """
        :param name: 
        :param position: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'fave.addTag'
        param_aliases = []
        response_type = responses.FaveAddTag
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def add_video(self, owner_id: int = None, id_: int = None, access_key: str = None) -> responses.BaseOk:
        """
        :param owner_id: 
        :param id_: 
        :param access_key: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'fave.addVideo'
        param_aliases = [('id_', 'id')]
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def edit_tag(self, id_: int = None, name: str = None) -> responses.BaseOk:
        """
        :param id_: 
        :param name: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'fave.editTag'
        param_aliases = [('id_', 'id')]
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get(self, extended: bool = None, item_type: str = None, tag_id: int = None, offset: int = None, count: int = None, fields: str = None, is_from_snackbar: bool = None) -> Union[responses.FaveGet, responses.FaveGetExtended]:
        """
        :param extended: '1' — to return additional 'wall', 'profiles', and 'groups' fields. By default: '0'.
        :param item_type: 
        :param tag_id: Tag ID.
        :param offset: Offset needed to return a specific subset of users.
        :param count: Number of users to return.
        :param fields: 
        :param is_from_snackbar: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'fave.get'
        param_aliases = []
        if not extended:
            response_type = responses.FaveGet
        else:
            response_type = responses.FaveGetExtended
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_pages(self, offset: int = None, count: int = None, type_: str = None, fields: List[Union[objects.BaseUserGroupFields, str]] = None, tag_id: int = None) -> responses.FaveGetPages:
        """
        :param offset: 
        :param count: 
        :param type_: 
        :param fields: 
        :param tag_id: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'fave.getPages'
        param_aliases = [('type_', 'type')]
        response_type = responses.FaveGetPages
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_tags(self) -> responses.FaveGetTags:
        
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'fave.getTags'
        param_aliases = []
        response_type = responses.FaveGetTags
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def mark_seen(self) -> responses.BaseBool:
        
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'fave.markSeen'
        param_aliases = []
        response_type = responses.BaseBool
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def remove_article(self, owner_id: int = None, article_id: int = None) -> responses.BaseBool:
        """
        :param owner_id: 
        :param article_id: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'fave.removeArticle'
        param_aliases = []
        response_type = responses.BaseBool
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def remove_link(self, link_id: str = None, link: str = None) -> responses.BaseOk:
        """
        Removes link from the user's faves.
        
        :param link_id: Link ID (can be obtained by [vk.com/dev/faves.getLinks|faves.getLinks] method).
        :param link: Link URL
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'fave.removeLink'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def remove_page(self, user_id: int = None, group_id: int = None) -> responses.BaseOk:
        """
        :param user_id: 
        :param group_id: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'fave.removePage'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def remove_post(self, owner_id: int = None, id_: int = None) -> responses.BaseOk:
        """
        :param owner_id: 
        :param id_: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'fave.removePost'
        param_aliases = [('id_', 'id')]
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def remove_product(self, owner_id: int = None, id_: int = None) -> responses.BaseOk:
        """
        :param owner_id: 
        :param id_: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'fave.removeProduct'
        param_aliases = [('id_', 'id')]
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def remove_tag(self, id_: int = None) -> responses.BaseOk:
        """
        :param id_: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'fave.removeTag'
        param_aliases = [('id_', 'id')]
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def reorder_tags(self, ids: List[int] = None) -> responses.BaseOk:
        """
        :param ids: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'fave.reorderTags'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def set_page_tags(self, user_id: int = None, group_id: int = None, tag_ids: List[int] = None) -> responses.BaseOk:
        """
        :param user_id: 
        :param group_id: 
        :param tag_ids: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'fave.setPageTags'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def set_tags(self, item_type: str = None, item_owner_id: int = None, item_id: int = None, tag_ids: List[int] = None, link_id: str = None, link_url: str = None) -> responses.BaseOk:
        """
        :param item_type: 
        :param item_owner_id: 
        :param item_id: 
        :param tag_ids: 
        :param link_id: 
        :param link_url: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'fave.setTags'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def track_page_interaction(self, user_id: int = None, group_id: int = None) -> responses.BaseOk:
        """
        :param user_id: 
        :param group_id: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'fave.trackPageInteraction'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

