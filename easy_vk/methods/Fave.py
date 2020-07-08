from ._ApiMethod import ApiMethod
from typing import List


class Fave(ApiMethod):
    def __init__(self, session, access_token, v, requests_per_s):
        super().__init__(session, access_token, v, requests_per_s)

    def add_article(self, url: str):
        """
        
        :param url: 
        """
    
        method_name = 'fave.addArticle'
        return self._call(method_name, locals())

    def add_link(self, link: str):
        """
        Adds a link to user faves.
        
        :param link: Link URL.
        """
    
        method_name = 'fave.addLink'
        return self._call(method_name, locals())

    def add_page(self, user_id: int = None, group_id: int = None):
        """
        
        :param user_id: 
        :param group_id: 
        """
    
        method_name = 'fave.addPage'
        return self._call(method_name, locals())

    def add_post(self, owner_id: int, id_: int, access_key: str = None):
        """
        
        :param owner_id: 
        :param id_: 
        :param access_key: 
        """
    
        param_alias_dict = {'id_': 'id'}
        method_name = 'fave.addPost'
        return self._call(method_name, locals())

    def add_product(self, owner_id: int, id_: int, access_key: str = None):
        """
        
        :param owner_id: 
        :param id_: 
        :param access_key: 
        """
    
        param_alias_dict = {'id_': 'id'}
        method_name = 'fave.addProduct'
        return self._call(method_name, locals())

    def add_tag(self, name: str = None, position: str = None):
        """
        
        :param name: 
        :param position: 
        """
    
        method_name = 'fave.addTag'
        return self._call(method_name, locals())

    def add_video(self, owner_id: int, id_: int, access_key: str = None):
        """
        
        :param owner_id: 
        :param id_: 
        :param access_key: 
        """
    
        param_alias_dict = {'id_': 'id'}
        method_name = 'fave.addVideo'
        return self._call(method_name, locals())

    def edit_tag(self, id_: int, name: str):
        """
        
        :param id_: 
        :param name: 
        """
    
        param_alias_dict = {'id_': 'id'}
        method_name = 'fave.editTag'
        return self._call(method_name, locals())

    def get(self, extended: bool = None, item_type: str = None, tag_id: int = None, offset: int = None, count: int = None, fields: str = None, is_from_snackbar: bool = None):
        """
        
        :param extended: '1' — to return additional 'wall', 'profiles', and 'groups' fields. By default: '0'.
        :param item_type: 
        :param tag_id: Tag ID.
        :param offset: Offset needed to return a specific subset of users.
        :param count: Number of users to return.
        :param fields: 
        :param is_from_snackbar: 
        """
    
        method_name = 'fave.get'
        return self._call(method_name, locals())

    def get_pages(self, offset: int = None, count: int = None, type_: str = None, fields: List[str] = None, tag_id: int = None):
        """
        
        :param offset: 
        :param count: 
        :param type_: 
        :param fields: 
        :param tag_id: 
        """
    
        if fields:
            fields = ','.join(fields)
        
        param_alias_dict = {'type_': 'type'}
        method_name = 'fave.getPages'
        return self._call(method_name, locals())

    def get_tags(self):
        """
        
        """
    
        method_name = 'fave.getTags'
        return self._call(method_name, locals())

    def mark_seen(self):
        """
        
        """
    
        method_name = 'fave.markSeen'
        return self._call(method_name, locals())

    def remove_article(self, owner_id: int, article_id: int):
        """
        
        :param owner_id: 
        :param article_id: 
        """
    
        method_name = 'fave.removeArticle'
        return self._call(method_name, locals())

    def remove_link(self, link_id: str = None, link: str = None):
        """
        Removes link from the user's faves.
        
        :param link_id: Link ID (can be obtained by [vk.com/dev/faves.getLinks|faves.getLinks] method).
        :param link: Link URL
        """
    
        method_name = 'fave.removeLink'
        return self._call(method_name, locals())

    def remove_page(self, user_id: int = None, group_id: int = None):
        """
        
        :param user_id: 
        :param group_id: 
        """
    
        method_name = 'fave.removePage'
        return self._call(method_name, locals())

    def remove_post(self, owner_id: int, id_: int):
        """
        
        :param owner_id: 
        :param id_: 
        """
    
        param_alias_dict = {'id_': 'id'}
        method_name = 'fave.removePost'
        return self._call(method_name, locals())

    def remove_product(self, owner_id: int, id_: int):
        """
        
        :param owner_id: 
        :param id_: 
        """
    
        param_alias_dict = {'id_': 'id'}
        method_name = 'fave.removeProduct'
        return self._call(method_name, locals())

    def remove_tag(self, id_: int):
        """
        
        :param id_: 
        """
    
        param_alias_dict = {'id_': 'id'}
        method_name = 'fave.removeTag'
        return self._call(method_name, locals())

    def reorder_tags(self, ids: List[int]):
        """
        
        :param ids: 
        """
    
        if ids:
            ids = [str(i) for i in ids]
            ids = ','.join(ids)
        
        method_name = 'fave.reorderTags'
        return self._call(method_name, locals())

    def set_page_tags(self, user_id: int = None, group_id: int = None, tag_ids: List[int] = None):
        """
        
        :param user_id: 
        :param group_id: 
        :param tag_ids: 
        """
    
        if tag_ids:
            tag_ids = [str(t) for t in tag_ids]
            tag_ids = ','.join(tag_ids)
        
        method_name = 'fave.setPageTags'
        return self._call(method_name, locals())

    def set_tags(self, item_type: str = None, item_owner_id: int = None, item_id: int = None, tag_ids: List[int] = None, link_id: str = None, link_url: str = None):
        """
        
        :param item_type: 
        :param item_owner_id: 
        :param item_id: 
        :param tag_ids: 
        :param link_id: 
        :param link_url: 
        """
    
        if tag_ids:
            tag_ids = [str(t) for t in tag_ids]
            tag_ids = ','.join(tag_ids)
        
        method_name = 'fave.setTags'
        return self._call(method_name, locals())

    def track_page_interaction(self, user_id: int = None, group_id: int = None):
        """
        
        :param user_id: 
        :param group_id: 
        """
    
        method_name = 'fave.trackPageInteraction'
        return self._call(method_name, locals())

