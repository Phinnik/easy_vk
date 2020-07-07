from _ApiMethod import ApiMethod
from typing import List


class Market(ApiMethod):
    def __init__(self, session, access_token, v, requests_per_s):
        super().__init__(session, access_token, v, requests_per_s)

    def add(self, owner_id: int, name: str, description: str, category_id: int, main_photo_id: int, price: float = None, old_price: float = None, deleted: bool = None, photo_ids: List[int] = None, url: str = None):
        """
        Ads a new item to the market.
        
        :param owner_id: ID of an item owner community.
        :param name: Item name.
        :param description: Item description.
        :param category_id: Item category ID.
        :param main_photo_id: Cover photo ID.
        :param price: Item price.
        :param old_price: 
        :param deleted: Item status ('1' — deleted, '0' — not deleted).
        :param photo_ids: IDs of additional photos.
        :param url: Url for button in market item.
        """
    
        if photo_ids:
            photo_ids = [str(p) for p in photo_ids]
            photo_ids = ','.join(photo_ids)
        
        method_name = 'market.add'
        return self.call(method_name, locals())

    def add_album(self, owner_id: int, title: str, photo_id: int = None, main_album: bool = None):
        """
        Creates new collection of items
        
        :param owner_id: ID of an item owner community.
        :param title: Collection title.
        :param photo_id: Cover photo ID.
        :param main_album: Set as main ('1' – set, '0' – no).
        """
    
        method_name = 'market.addAlbum'
        return self.call(method_name, locals())

    def add_to_album(self, owner_id: int, item_id: int, album_ids: List[int]):
        """
        Adds an item to one or multiple collections.
        
        :param owner_id: ID of an item owner community.
        :param item_id: Item ID.
        :param album_ids: Collections IDs to add item to.
        """
    
        if album_ids:
            album_ids = [str(a) for a in album_ids]
            album_ids = ','.join(album_ids)
        
        method_name = 'market.addToAlbum'
        return self.call(method_name, locals())

    def create_comment(self, owner_id: int, item_id: int, message: str = None, attachments: List[str] = None, from_group: bool = None, reply_to_comment: int = None, sticker_id: int = None, guid: str = None):
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
    
        if attachments:
            attachments = ','.join(attachments)
        
        method_name = 'market.createComment'
        return self.call(method_name, locals())

    def delete(self, owner_id: int, item_id: int):
        """
        Deletes an item.
        
        :param owner_id: ID of an item owner community.
        :param item_id: Item ID.
        """
    
        method_name = 'market.delete'
        return self.call(method_name, locals())

    def delete_album(self, owner_id: int, album_id: int):
        """
        Deletes a collection of items.
        
        :param owner_id: ID of an collection owner community.
        :param album_id: Collection ID.
        """
    
        method_name = 'market.deleteAlbum'
        return self.call(method_name, locals())

    def delete_comment(self, owner_id: int, comment_id: int):
        """
        Deletes an item's comment
        
        :param owner_id: identifier of an item owner community, "Note that community id in the 'owner_id' parameter should be negative number. For example 'owner_id'=-1 matches the [vk.com/apiclub|VK API] community "
        :param comment_id: comment id
        """
    
        method_name = 'market.deleteComment'
        return self.call(method_name, locals())

    def edit(self, owner_id: int, item_id: int, name: str, description: str, category_id: int, price: float, main_photo_id: int, deleted: bool = None, photo_ids: List[int] = None, url: str = None):
        """
        Edits an item.
        
        :param owner_id: ID of an item owner community.
        :param item_id: Item ID.
        :param name: Item name.
        :param description: Item description.
        :param category_id: Item category ID.
        :param price: Item price.
        :param main_photo_id: Cover photo ID.
        :param deleted: Item status ('1' — deleted, '0' — not deleted).
        :param photo_ids: IDs of additional photos.
        :param url: Url for button in market item.
        """
    
        if photo_ids:
            photo_ids = [str(p) for p in photo_ids]
            photo_ids = ','.join(photo_ids)
        
        method_name = 'market.edit'
        return self.call(method_name, locals())

    def edit_album(self, owner_id: int, album_id: int, title: str, photo_id: int = None, main_album: bool = None):
        """
        Edits a collection of items
        
        :param owner_id: ID of an collection owner community.
        :param album_id: Collection ID.
        :param title: Collection title.
        :param photo_id: Cover photo id
        :param main_album: Set as main ('1' – set, '0' – no).
        """
    
        method_name = 'market.editAlbum'
        return self.call(method_name, locals())

    def edit_comment(self, owner_id: int, comment_id: int, message: str = None, attachments: List[str] = None):
        """
        Chages item comment's text
        
        :param owner_id: ID of an item owner community.
        :param comment_id: Comment ID.
        :param message: New comment text (required if 'attachments' are not specified), , 2048 symbols maximum.
        :param attachments: Comma-separated list of objects attached to a comment. The field is submitted the following way: , "'<owner_id>_<media_id>,<owner_id>_<media_id>'", , '' - media attachment type: "'photo' - photo, 'video' - video, 'audio' - audio, 'doc' - document", , '<owner_id>' - media owner id, '<media_id>' - media attachment id, , For example: "photo100172_166443618,photo66748_265827614",
        """
    
        if attachments:
            attachments = ','.join(attachments)
        
        method_name = 'market.editComment'
        return self.call(method_name, locals())

    def get(self, owner_id: int, album_id: int = None, count: int = None, offset: int = None, extended: bool = None):
        """
        Returns items list for a community.
        
        :param owner_id: ID of an item owner community, "Note that community id in the 'owner_id' parameter should be negative number. For example 'owner_id'=-1 matches the [vk.com/apiclub|VK API] community "
        :param album_id: 
        :param count: Number of items to return.
        :param offset: Offset needed to return a specific subset of results.
        :param extended: '1' – method will return additional fields: 'likes, can_comment, car_repost, photos'. These parameters are not returned by default.
        """
    
        method_name = 'market.get'
        return self.call(method_name, locals())

    def get_album_by_id(self, owner_id: int, album_ids: List[int]):
        """
        Returns items album's data
        
        :param owner_id: identifier of an album owner community, "Note that community id in the 'owner_id' parameter should be negative number. For example 'owner_id'=-1 matches the [vk.com/apiclub|VK API] community "
        :param album_ids: collections identifiers to obtain data from
        """
    
        if album_ids:
            album_ids = [str(a) for a in album_ids]
            album_ids = ','.join(album_ids)
        
        method_name = 'market.getAlbumById'
        return self.call(method_name, locals())

    def get_albums(self, owner_id: int, offset: int = None, count: int = None):
        """
        Returns community's collections list.
        
        :param owner_id: ID of an items owner community.
        :param offset: Offset needed to return a specific subset of results.
        :param count: Number of items to return.
        """
    
        method_name = 'market.getAlbums'
        return self.call(method_name, locals())

    def get_by_id(self, item_ids: List[str], extended: bool = None):
        """
        Returns information about market items by their ids.
        
        :param item_ids: Comma-separated ids list: {user id}_{item id}. If an item belongs to a community -{community id} is used. " 'Videos' value example: , '-4363_136089719,13245770_137352259'"
        :param extended: '1' – to return additional fields: 'likes, can_comment, car_repost, photos'. By default: '0'.
        """
    
        if item_ids:
            item_ids = ','.join(item_ids)
        
        method_name = 'market.getById'
        return self.call(method_name, locals())

    def get_categories(self, count: int = None, offset: int = None):
        """
        Returns a list of market categories.
        
        :param count: Number of results to return.
        :param offset: Offset needed to return a specific subset of results.
        """
    
        method_name = 'market.getCategories'
        return self.call(method_name, locals())

    def get_comments(self, owner_id: int, item_id: int, need_likes: bool = None, start_comment_id: int = None, offset: int = None, count: int = None, sort: str = None, extended: bool = None, fields: List[str] = None):
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
    
        if fields:
            fields = ','.join(fields)
        
        method_name = 'market.getComments'
        return self.call(method_name, locals())

    def remove_from_album(self, owner_id: int, item_id: int, album_ids: List[int]):
        """
        Removes an item from one or multiple collections.
        
        :param owner_id: ID of an item owner community.
        :param item_id: Item ID.
        :param album_ids: Collections IDs to remove item from.
        """
    
        if album_ids:
            album_ids = [str(a) for a in album_ids]
            album_ids = ','.join(album_ids)
        
        method_name = 'market.removeFromAlbum'
        return self.call(method_name, locals())

    def reorder_albums(self, owner_id: int, album_id: int, before: int = None, after: int = None):
        """
        Reorders the collections list.
        
        :param owner_id: ID of an item owner community.
        :param album_id: Collection ID.
        :param before: ID of a collection to place current collection before it.
        :param after: ID of a collection to place current collection after it.
        """
    
        method_name = 'market.reorderAlbums'
        return self.call(method_name, locals())

    def reorder_items(self, owner_id: int, item_id: int, album_id: int = None, before: int = None, after: int = None):
        """
        Changes item place in a collection.
        
        :param owner_id: ID of an item owner community.
        :param item_id: Item ID.
        :param album_id: ID of a collection to reorder items in. Set 0 to reorder full items list.
        :param before: ID of an item to place current item before it.
        :param after: ID of an item to place current item after it.
        """
    
        method_name = 'market.reorderItems'
        return self.call(method_name, locals())

    def report(self, owner_id: int, item_id: int, reason: int = None):
        """
        Sends a complaint to the item.
        
        :param owner_id: ID of an item owner community.
        :param item_id: Item ID.
        :param reason: Complaint reason. Possible values: *'0' — spam,, *'1' — child porn,, *'2' — extremism,, *'3' — violence,, *'4' — drugs propaganda,, *'5' — adult materials,, *'6' — insult.
        """
    
        method_name = 'market.report'
        return self.call(method_name, locals())

    def report_comment(self, owner_id: int, comment_id: int, reason: int):
        """
        Sends a complaint to the item's comment.
        
        :param owner_id: ID of an item owner community.
        :param comment_id: Comment ID.
        :param reason: Complaint reason. Possible values: *'0' — spam,, *'1' — child porn,, *'2' — extremism,, *'3' — violence,, *'4' — drugs propaganda,, *'5' — adult materials,, *'6' — insult.
        """
    
        method_name = 'market.reportComment'
        return self.call(method_name, locals())

    def restore(self, owner_id: int, item_id: int):
        """
        Restores recently deleted item
        
        :param owner_id: ID of an item owner community.
        :param item_id: Deleted item ID.
        """
    
        method_name = 'market.restore'
        return self.call(method_name, locals())

    def restore_comment(self, owner_id: int, comment_id: int):
        """
        Restores a recently deleted comment
        
        :param owner_id: identifier of an item owner community, "Note that community id in the 'owner_id' parameter should be negative number. For example 'owner_id'=-1 matches the [vk.com/apiclub|VK API] community "
        :param comment_id: deleted comment id
        """
    
        method_name = 'market.restoreComment'
        return self.call(method_name, locals())

    def search(self, owner_id: int, album_id: int = None, q: str = None, price_from: int = None, price_to: int = None, tags: List[int] = None, sort: int = None, rev: int = None, offset: int = None, count: int = None, extended: bool = None, status: int = None):
        """
        Searches market items in a community's catalog
        
        :param owner_id: ID of an items owner community.
        :param album_id: 
        :param q: Search query, for example "pink slippers".
        :param price_from: Minimum item price value.
        :param price_to: Maximum item price value.
        :param tags: Comma-separated tag IDs list.
        :param sort: 
        :param rev: '0' — do not use reverse order, '1' — use reverse order
        :param offset: Offset needed to return a specific subset of results.
        :param count: Number of items to return.
        :param extended: '1' – to return additional fields: 'likes, can_comment, car_repost, photos'. By default: '0'.
        :param status: 
        """
    
        if tags:
            tags = [str(t) for t in tags]
            tags = ','.join(tags)
        
        method_name = 'market.search'
        return self.call(method_name, locals())

