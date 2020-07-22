from typing import List, Union, Optional
from easy_vk.types import objects, responses
from .base import BaseCategory


class Market(BaseCategory):
    def __init__(self, session, access_token: str, v: str, delay: float, auto_retry: bool, max_retries: int, timeout: float):
        super().__init__(session, access_token, v, delay, auto_retry, max_retries, timeout)

    def add(self, owner_id: int = None, name: str = None, description: str = None, category_id: int = None, price: float = None, old_price: float = None, deleted: bool = None, main_photo_id: int = None, photo_ids: List[int] = None, url: str = None, dimension_width: int = None, dimension_height: int = None, dimension_length: int = None, weight: int = None) -> responses.MarketAdd:
        """
        Ads a new item to the market.
        
        :param owner_id: ID of an item owner community.
        :param name: Item name.
        :param description: Item description.
        :param category_id: Item category ID.
        :param price: Item price.
        :param old_price: 
        :param deleted: Item status ('1' — deleted, '0' — not deleted).
        :param main_photo_id: Cover photo ID.
        :param photo_ids: IDs of additional photos.
        :param url: Url for button in market item.
        :param dimension_width: 
        :param dimension_height: 
        :param dimension_length: 
        :param weight: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'market.add'
        param_aliases = []
        response_type = responses.MarketAdd
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def add_album(self, owner_id: int = None, title: str = None, photo_id: int = None, main_album: bool = None) -> responses.MarketAddAlbum:
        """
        Creates new collection of items
        
        :param owner_id: ID of an item owner community.
        :param title: Collection title.
        :param photo_id: Cover photo ID.
        :param main_album: Set as main ('1' – set, '0' – no).
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'market.addAlbum'
        param_aliases = []
        response_type = responses.MarketAddAlbum
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def add_to_album(self, owner_id: int = None, item_id: int = None, album_ids: List[int] = None) -> responses.BaseOk:
        """
        Adds an item to one or multiple collections.
        
        :param owner_id: ID of an item owner community.
        :param item_id: Item ID.
        :param album_ids: Collections IDs to add item to.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'market.addToAlbum'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def create_comment(self, owner_id: int = None, item_id: int = None, message: str = None, attachments: List[str] = None, from_group: bool = None, reply_to_comment: int = None, sticker_id: int = None, guid: str = None) -> responses.MarketCreateComment:
        """
        Creates a new comment for an item.
        
        :param owner_id: ID of an item owner community.
        :param item_id: Item ID.
        :param message: Comment text (required if 'attachments' parameter is not specified)
        :param attachments: Comma-separated list of objects attached to a comment. The field is submitted the following way: , "'<owner_id>_<media_id>,<owner_id>_<media_id>'", , '' - media attachment type: "'photo' - photo, 'video' - video, 'audio' - audio, 'doc' - document", , '<owner_id>' - media owner id, '<media_id>' - media attachment id, , For example: "photo100172_166443618,photo66748_265827614",
        :param from_group: '1' - comment will be published on behalf of a community, '0' - on behalf of a user (by default).
        :param reply_to_comment: ID of a comment to reply with current comment to.
        :param sticker_id: Sticker ID.
        :param guid: Random value to avoid resending one comment.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'market.createComment'
        param_aliases = []
        response_type = responses.MarketCreateComment
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def delete(self, owner_id: int = None, item_id: int = None) -> responses.BaseOk:
        """
        Deletes an item.
        
        :param owner_id: ID of an item owner community.
        :param item_id: Item ID.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'market.delete'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def delete_album(self, owner_id: int = None, album_id: int = None) -> responses.BaseOk:
        """
        Deletes a collection of items.
        
        :param owner_id: ID of an collection owner community.
        :param album_id: Collection ID.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'market.deleteAlbum'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def delete_comment(self, owner_id: int = None, comment_id: int = None) -> responses.MarketDeleteComment:
        """
        Deletes an item's comment
        
        :param owner_id: identifier of an item owner community, "Note that community id in the 'owner_id' parameter should be negative number. For example 'owner_id'=-1 matches the [vk.com/apiclub|VK API] community "
        :param comment_id: comment id
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'market.deleteComment'
        param_aliases = []
        response_type = responses.MarketDeleteComment
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def edit(self, owner_id: int = None, item_id: int = None, name: str = None, description: str = None, category_id: int = None, price: float = None, deleted: bool = None, main_photo_id: int = None, photo_ids: List[int] = None, url: str = None) -> responses.BaseOk:
        """
        Edits an item.
        
        :param owner_id: ID of an item owner community.
        :param item_id: Item ID.
        :param name: Item name.
        :param description: Item description.
        :param category_id: Item category ID.
        :param price: Item price.
        :param deleted: Item status ('1' — deleted, '0' — not deleted).
        :param main_photo_id: Cover photo ID.
        :param photo_ids: IDs of additional photos.
        :param url: Url for button in market item.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'market.edit'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def edit_album(self, owner_id: int = None, album_id: int = None, title: str = None, photo_id: int = None, main_album: bool = None) -> responses.BaseOk:
        """
        Edits a collection of items
        
        :param owner_id: ID of an collection owner community.
        :param album_id: Collection ID.
        :param title: Collection title.
        :param photo_id: Cover photo id
        :param main_album: Set as main ('1' – set, '0' – no).
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'market.editAlbum'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def edit_comment(self, owner_id: int = None, comment_id: int = None, message: str = None, attachments: List[str] = None) -> responses.BaseOk:
        """
        Chages item comment's text
        
        :param owner_id: ID of an item owner community.
        :param comment_id: Comment ID.
        :param message: New comment text (required if 'attachments' are not specified), , 2048 symbols maximum.
        :param attachments: Comma-separated list of objects attached to a comment. The field is submitted the following way: , "'<owner_id>_<media_id>,<owner_id>_<media_id>'", , '' - media attachment type: "'photo' - photo, 'video' - video, 'audio' - audio, 'doc' - document", , '<owner_id>' - media owner id, '<media_id>' - media attachment id, , For example: "photo100172_166443618,photo66748_265827614",
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'market.editComment'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get(self, owner_id: int = None, album_id: int = None, count: int = None, offset: int = None, extended: bool = None) -> Union[responses.MarketGet, responses.MarketGetExtended]:
        """
        Returns items list for a community.
        
        :param owner_id: ID of an item owner community, "Note that community id in the 'owner_id' parameter should be negative number. For example 'owner_id'=-1 matches the [vk.com/apiclub|VK API] community "
        :param album_id: 
        :param count: Number of items to return.
        :param offset: Offset needed to return a specific subset of results.
        :param extended: '1' – method will return additional fields: 'likes, can_comment, car_repost, photos'. These parameters are not returned by default.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'market.get'
        param_aliases = []
        if not extended:
            response_type = responses.MarketGet
        else:
            response_type = responses.MarketGetExtended
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_album_by_id(self, owner_id: int = None, album_ids: List[int] = None) -> responses.MarketGetAlbumById:
        """
        Returns items album's data
        
        :param owner_id: identifier of an album owner community, "Note that community id in the 'owner_id' parameter should be negative number. For example 'owner_id'=-1 matches the [vk.com/apiclub|VK API] community "
        :param album_ids: collections identifiers to obtain data from
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'market.getAlbumById'
        param_aliases = []
        response_type = responses.MarketGetAlbumById
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_albums(self, owner_id: int = None, offset: int = None, count: int = None) -> responses.MarketGetAlbums:
        """
        Returns community's collections list.
        
        :param owner_id: ID of an items owner community.
        :param offset: Offset needed to return a specific subset of results.
        :param count: Number of items to return.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'market.getAlbums'
        param_aliases = []
        response_type = responses.MarketGetAlbums
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_by_id(self, item_ids: List[str] = None, extended: bool = None) -> Union[responses.MarketGetById, responses.MarketGetByIdExtended]:
        """
        Returns information about market items by their ids.
        
        :param item_ids: Comma-separated ids list: {user id}_{item id}. If an item belongs to a community -{community id} is used. " 'Videos' value example: , '-4363_136089719,13245770_137352259'"
        :param extended: '1' – to return additional fields: 'likes, can_comment, car_repost, photos'. By default: '0'.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'market.getById'
        param_aliases = []
        if not extended:
            response_type = responses.MarketGetById
        else:
            response_type = responses.MarketGetByIdExtended
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_categories(self, count: int = None, offset: int = None) -> responses.MarketGetCategories:
        """
        Returns a list of market categories.
        
        :param count: Number of results to return.
        :param offset: Offset needed to return a specific subset of results.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'market.getCategories'
        param_aliases = []
        response_type = responses.MarketGetCategories
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_comments(self, owner_id: int = None, item_id: int = None, need_likes: bool = None, start_comment_id: int = None, offset: int = None, count: int = None, sort: str = None, extended: bool = None, fields: List[Union[objects.UsersFields, str]] = None) -> responses.MarketGetComments:
        """
        Returns comments list for an item.
        
        :param owner_id: ID of an item owner community
        :param item_id: Item ID.
        :param need_likes: '1' — to return likes info.
        :param start_comment_id: ID of a comment to start a list from (details below).
        :param offset: 
        :param count: Number of results to return.
        :param sort: Sort order ('asc' — from old to new, 'desc' — from new to old)
        :param extended: '1' — comments will be returned as numbered objects, in addition lists of 'profiles' and 'groups' objects will be returned.
        :param fields: List of additional profile fields to return. See the [vk.com/dev/fields|details]
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'market.getComments'
        param_aliases = []
        response_type = responses.MarketGetComments
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def remove_from_album(self, owner_id: int = None, item_id: int = None, album_ids: List[int] = None) -> responses.BaseOk:
        """
        Removes an item from one or multiple collections.
        
        :param owner_id: ID of an item owner community.
        :param item_id: Item ID.
        :param album_ids: Collections IDs to remove item from.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'market.removeFromAlbum'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def reorder_albums(self, owner_id: int = None, album_id: int = None, before: int = None, after: int = None) -> responses.BaseOk:
        """
        Reorders the collections list.
        
        :param owner_id: ID of an item owner community.
        :param album_id: Collection ID.
        :param before: ID of a collection to place current collection before it.
        :param after: ID of a collection to place current collection after it.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'market.reorderAlbums'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def reorder_items(self, owner_id: int = None, album_id: int = None, item_id: int = None, before: int = None, after: int = None) -> responses.BaseOk:
        """
        Changes item place in a collection.
        
        :param owner_id: ID of an item owner community.
        :param album_id: ID of a collection to reorder items in. Set 0 to reorder full items list.
        :param item_id: Item ID.
        :param before: ID of an item to place current item before it.
        :param after: ID of an item to place current item after it.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'market.reorderItems'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def report(self, owner_id: int = None, item_id: int = None, reason: int = None) -> responses.BaseOk:
        """
        Sends a complaint to the item.
        
        :param owner_id: ID of an item owner community.
        :param item_id: Item ID.
        :param reason: Complaint reason. Possible values: *'0' — spam,, *'1' — child porn,, *'2' — extremism,, *'3' — violence,, *'4' — drugs propaganda,, *'5' — adult materials,, *'6' — insult.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'market.report'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def report_comment(self, owner_id: int = None, comment_id: int = None, reason: int = None) -> responses.BaseOk:
        """
        Sends a complaint to the item's comment.
        
        :param owner_id: ID of an item owner community.
        :param comment_id: Comment ID.
        :param reason: Complaint reason. Possible values: *'0' — spam,, *'1' — child porn,, *'2' — extremism,, *'3' — violence,, *'4' — drugs propaganda,, *'5' — adult materials,, *'6' — insult.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'market.reportComment'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def restore(self, owner_id: int = None, item_id: int = None) -> responses.BaseOk:
        """
        Restores recently deleted item
        
        :param owner_id: ID of an item owner community.
        :param item_id: Deleted item ID.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'market.restore'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def restore_comment(self, owner_id: int = None, comment_id: int = None) -> responses.MarketRestoreComment:
        """
        Restores a recently deleted comment
        
        :param owner_id: identifier of an item owner community, "Note that community id in the 'owner_id' parameter should be negative number. For example 'owner_id'=-1 matches the [vk.com/apiclub|VK API] community "
        :param comment_id: deleted comment id
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'market.restoreComment'
        param_aliases = []
        response_type = responses.MarketRestoreComment
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def search(self, owner_id: int = None, album_id: int = None, q: str = None, price_from: int = None, price_to: int = None, sort: int = None, rev: int = None, offset: int = None, count: int = None, extended: bool = None, status: int = None) -> Union[responses.MarketSearch, responses.MarketSearchExtended]:
        """
        Searches market items in a community's catalog
        
        :param owner_id: ID of an items owner community.
        :param album_id: 
        :param q: Search query, for example "pink slippers".
        :param price_from: Minimum item price value.
        :param price_to: Maximum item price value.
        :param sort: 
        :param rev: '0' — do not use reverse order, '1' — use reverse order
        :param offset: Offset needed to return a specific subset of results.
        :param count: Number of items to return.
        :param extended: '1' – to return additional fields: 'likes, can_comment, car_repost, photos'. By default: '0'.
        :param status: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'market.search'
        param_aliases = []
        if not extended:
            response_type = responses.MarketSearch
        else:
            response_type = responses.MarketSearchExtended
        return self._call(method_name, method_parameters, param_aliases, response_type)

