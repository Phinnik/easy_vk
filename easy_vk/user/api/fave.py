# This file was autogenerated from vk-api json schema

from typing import List, Union, Optional, overload
from easy_vk.types import objects
from easy_vk.types import responses
from easy_vk.api_category import BaseCategory
try:
    from typing import Literal
except Exception:
    from typing_extensions import Literal


class Fave(BaseCategory):
    def __init__(self, session, access_token: str, v: str, last_call_timer, delay: float, auto_retry: bool, max_retries: int, timeout: float):
        super().__init__(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)

    def add_article(self, url: str) -> responses.BaseOk:
        """
        :param url:
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'fave.addArticle'
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def add_link(self, link: str) -> responses.BaseOk:
        """
        Adds a link to user faves.
        
        :param link: Link URL.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'fave.addLink'
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def add_page(self, user_id: Optional[int] = None, group_id: Optional[int] = None) -> responses.BaseOk:
        """
        :param user_id:
        :param group_id:
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'fave.addPage'
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def add_post(self, owner_id: int, id_: int, access_key: Optional[str] = None) -> responses.BaseOk:
        """
        :param owner_id:
        :param id_:
        :param access_key:
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = [('id_', 'id')]
        method_name = 'fave.addPost'
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def add_product(self, owner_id: int, id_: int, access_key: Optional[str] = None) -> responses.BaseOk:
        """
        :param owner_id:
        :param id_:
        :param access_key:
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = [('id_', 'id')]
        method_name = 'fave.addProduct'
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def add_tag(self, name: Optional[str] = None, position: Optional[str] = None) -> responses.FaveAddTag:
        """
        :param name:
        :param position:
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'fave.addTag'
        response_type = responses.FaveAddTag
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def add_video(self, owner_id: int, id_: int, access_key: Optional[str] = None) -> responses.BaseOk:
        """
        :param owner_id:
        :param id_:
        :param access_key:
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = [('id_', 'id')]
        method_name = 'fave.addVideo'
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def edit_tag(self, id_: int, name: str) -> responses.BaseOk:
        """
        :param id_:
        :param name:
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = [('id_', 'id')]
        method_name = 'fave.editTag'
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    @overload
    def get(self, extended: None = None, item_type: Optional[str] = None, tag_id: Optional[int] = None, offset: Optional[int] = None, count: Optional[int] = None, fields: Optional[str] = None, is_from_snackbar: Optional[bool] = None) -> responses.FaveGet: ...
    @overload
    def get(self, extended: bool, item_type: Optional[str] = None, tag_id: Optional[int] = None, offset: Optional[int] = None, count: Optional[int] = None, fields: Optional[str] = None, is_from_snackbar: Optional[bool] = None) -> responses.FaveGetExtended: ...
    def get(self, extended: Optional[bool] = None, item_type: Optional[str] = None, tag_id: Optional[int] = None, offset: Optional[int] = None, count: Optional[int] = None, fields: Optional[str] = None, is_from_snackbar: Optional[bool] = None):
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
        param_aliases = []
        method_name = 'fave.get'
        if not extended:
            response_type = responses.FaveGet
        if extended:
            response_type = responses.FaveGetExtended
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_pages(self, offset: Optional[int] = None, count: Optional[int] = None, type_: Optional[str] = None, fields: Optional[List[Union[objects.BaseUserGroupFields, str]]] = None, tag_id: Optional[int] = None) -> responses.FaveGetPages:
        """
        :param offset:
        :param count:
        :param type_:
        :param fields:
        :param tag_id:
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = [('type_', 'type')]
        method_name = 'fave.getPages'
        response_type = responses.FaveGetPages
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_tags(self) -> responses.FaveGetTags:
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'fave.getTags'
        response_type = responses.FaveGetTags
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def mark_seen(self) -> responses.BaseBool:
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'fave.markSeen'
        response_type = responses.BaseBool
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def remove_article(self, owner_id: int, article_id: int) -> responses.BaseBool:
        """
        :param owner_id:
        :param article_id:
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'fave.removeArticle'
        response_type = responses.BaseBool
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def remove_link(self, link_id: Optional[str] = None, link: Optional[str] = None) -> responses.BaseOk:
        """
        Removes link from the user's faves.
        
        :param link_id: Link ID (can be obtained by [vk.com/dev/faves.getLinks|faves.getLinks] method).
        :param link: Link URL
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'fave.removeLink'
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def remove_page(self, user_id: Optional[int] = None, group_id: Optional[int] = None) -> responses.BaseOk:
        """
        :param user_id:
        :param group_id:
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'fave.removePage'
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def remove_post(self, owner_id: int, id_: int) -> responses.BaseOk:
        """
        :param owner_id:
        :param id_:
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = [('id_', 'id')]
        method_name = 'fave.removePost'
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def remove_product(self, owner_id: int, id_: int) -> responses.BaseOk:
        """
        :param owner_id:
        :param id_:
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = [('id_', 'id')]
        method_name = 'fave.removeProduct'
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def remove_tag(self, id_: int) -> responses.BaseOk:
        """
        :param id_:
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = [('id_', 'id')]
        method_name = 'fave.removeTag'
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def reorder_tags(self, ids: List[int]) -> responses.BaseOk:
        """
        :param ids:
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'fave.reorderTags'
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def set_page_tags(self, user_id: Optional[int] = None, group_id: Optional[int] = None, tag_ids: Optional[List[int]] = None) -> responses.BaseOk:
        """
        :param user_id:
        :param group_id:
        :param tag_ids:
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'fave.setPageTags'
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def set_tags(self, item_type: Optional[str] = None, item_owner_id: Optional[int] = None, item_id: Optional[int] = None, tag_ids: Optional[List[int]] = None, link_id: Optional[str] = None, link_url: Optional[str] = None) -> responses.BaseOk:
        """
        :param item_type:
        :param item_owner_id:
        :param item_id:
        :param tag_ids:
        :param link_id:
        :param link_url:
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'fave.setTags'
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def track_page_interaction(self, user_id: Optional[int] = None, group_id: Optional[int] = None) -> responses.BaseOk:
        """
        :param user_id:
        :param group_id:
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'fave.trackPageInteraction'
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)
