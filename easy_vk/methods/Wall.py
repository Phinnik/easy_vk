from _ApiMethod import ApiMethod
from typing import List


class Wall(ApiMethod):
    def __init__(self, session, access_token, v, requests_per_s):
        super().__init__(session, access_token, v, requests_per_s)

    def close_comments(self, owner_id: int, post_id: int):
        """
        
        :param owner_id: 
        :param post_id: 
        """
    
        method_name = 'wall.closeComments'
        return self.call(method_name, locals())

    def create_comment(self, post_id: int, owner_id: int = None, from_group: int = None, message: str = None, reply_to_comment: int = None, attachments: List[str] = None, sticker_id: int = None, guid: str = None):
        """
        Adds a comment to a post on a user wall or community wall.
        
        :param post_id: Post ID.
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param from_group: Group ID.
        :param message: (Required if 'attachments' is not set.) Text of the comment.
        :param reply_to_comment: ID of comment to reply.
        :param attachments: (Required if 'message' is not set.) List of media objects attached to the comment, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media ojbect: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media owner. '<media_id>' — Media ID. For example: "photo100172_166443618,photo66748_265827614"
        :param sticker_id: Sticker ID.
        :param guid: Unique identifier to avoid repeated comments.
        """
    
        if attachments:
            attachments = ','.join(attachments)
        
        method_name = 'wall.createComment'
        return self.call(method_name, locals())

    def delete(self, owner_id: int = None, post_id: int = None):
        """
        Deletes a post from a user wall or community wall.
        
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param post_id: ID of the post to be deleted.
        """
    
        method_name = 'wall.delete'
        return self.call(method_name, locals())

    def delete_comment(self, comment_id: int, owner_id: int = None):
        """
        Deletes a comment on a post on a user wall or community wall.
        
        :param comment_id: Comment ID.
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        """
    
        method_name = 'wall.deleteComment'
        return self.call(method_name, locals())

    def edit(self, post_id: int, owner_id: int = None, friends_only: bool = None, message: str = None, attachments: List[str] = None, services: str = None, signed: bool = None, publish_date: int = None, lat: float = None, long: float = None, place_id: int = None, mark_as_ads: bool = None, close_comments: bool = None, poster_bkg_id: int = None, poster_bkg_owner_id: int = None, poster_bkg_access_hash: str = None, copyright_: str = None):
        """
        Edits a post on a user wall or community wall.
        
        :param post_id: 
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param friends_only: 
        :param message: (Required if 'attachments' is not set.) Text of the post.
        :param attachments: (Required if 'message' is not set.) List of objects attached to the post, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media application owner. '<media_id>' — Media application ID. Example: "photo100172_166443618,photo66748_265827614", May contain a link to an external page to include in the post. Example: "photo66748_265827614,http://habrahabr.ru", "NOTE: If more than one link is being attached, an error is thrown."
        :param services: 
        :param signed: 
        :param publish_date: 
        :param lat: 
        :param long: 
        :param place_id: 
        :param mark_as_ads: 
        :param close_comments: 
        :param poster_bkg_id: 
        :param poster_bkg_owner_id: 
        :param poster_bkg_access_hash: 
        :param copyright_: 
        """
    
        if attachments:
            attachments = ','.join(attachments)
        
        param_alias_dict = {'copyright_': 'copyright'}
        method_name = 'wall.edit'
        return self.call(method_name, locals())

    def edit_ads_stealth(self, post_id: int, owner_id: int = None, message: str = None, attachments: List[str] = None, signed: bool = None, lat: float = None, long: float = None, place_id: int = None, link_button: str = None, link_title: str = None, link_image: str = None, link_video: str = None):
        """
        Allows to edit hidden post.
        
        :param post_id: Post ID. Used for publishing of scheduled and suggested posts.
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param message: (Required if 'attachments' is not set.) Text of the post.
        :param attachments: (Required if 'message' is not set.) List of objects attached to the post, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, 'page' — wiki-page, 'note' — note, 'poll' — poll, 'album' — photo album, '<owner_id>' — ID of the media application owner. '<media_id>' — Media application ID. Example: "photo100172_166443618,photo66748_265827614", May contain a link to an external page to include in the post. Example: "photo66748_265827614,http://habrahabr.ru", "NOTE: If more than one link is being attached, an error will be thrown."
        :param signed: Only for posts in communities with 'from_group' set to '1': '1' — post will be signed with the name of the posting user, '0' — post will not be signed (default)
        :param lat: Geographical latitude of a check-in, in degrees (from -90 to 90).
        :param long: Geographical longitude of a check-in, in degrees (from -180 to 180).
        :param place_id: ID of the location where the user was tagged.
        :param link_button: Link button ID
        :param link_title: Link title
        :param link_image: Link image url
        :param link_video: Link video ID in format "<owner_id>_<media_id>"
        """
    
        if attachments:
            attachments = ','.join(attachments)
        
        method_name = 'wall.editAdsStealth'
        return self.call(method_name, locals())

    def edit_comment(self, comment_id: int, owner_id: int = None, message: str = None, attachments: List[str] = None):
        """
        Edits a comment on a user wall or community wall.
        
        :param comment_id: Comment ID.
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param message: New comment text.
        :param attachments: List of objects attached to the comment, in the following format: , "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media attachment owner. '<media_id>' — Media attachment ID. For example: "photo100172_166443618,photo66748_265827614"
        """
    
        if attachments:
            attachments = ','.join(attachments)
        
        method_name = 'wall.editComment'
        return self.call(method_name, locals())

    def get(self, owner_id: int = None, domain: str = None, offset: int = None, count: int = None, filter_: str = None, extended: bool = None, fields: List[str] = None):
        """
        Returns a list of posts on a user wall or community wall.
        
        :param owner_id: ID of the user or community that owns the wall. By default, current user ID. Use a negative value to designate a community ID.
        :param domain: User or community short address.
        :param offset: Offset needed to return a specific subset of posts.
        :param count: Number of posts to return (maximum 100).
        :param filter_: Filter to apply: 'owner' — posts by the wall owner, 'others' — posts by someone else, 'all' — posts by the wall owner and others (default), 'postponed' — timed posts (only available for calls with an 'access_token'), 'suggests' — suggested posts on a community wall
        :param extended: '1' — to return 'wall', 'profiles', and 'groups' fields, '0' — to return no additional fields (default)
        :param fields: 
        """
    
        if fields:
            fields = ','.join(fields)
        
        param_alias_dict = {'filter_': 'filter'}
        method_name = 'wall.get'
        return self.call(method_name, locals())

    def get_by_id(self, posts: List[str], extended: bool = None, copy_history_depth: int = None, fields: List[str] = None):
        """
        Returns a list of posts from user or community walls by their IDs.
        
        :param posts: User or community IDs and post IDs, separated by underscores. Use a negative value to designate a community ID. Example: "93388_21539,93388_20904,2943_4276,-1_1"
        :param extended: '1' — to return user and community objects needed to display posts, '0' — no additional fields are returned (default)
        :param copy_history_depth: Sets the number of parent elements to include in the array 'copy_history' that is returned if the post is a repost from another wall.
        :param fields: 
        """
    
        if posts:
            posts = ','.join(posts)
        if fields:
            fields = ','.join(fields)
        
        method_name = 'wall.getById'
        return self.call(method_name, locals())

    def get_comment(self, comment_id: int, owner_id: int = None, extended: bool = None, fields: List[str] = None):
        """
        Returns a comment on a post on a user wall or community wall.
        
        :param comment_id: Comment ID.
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param extended: 
        :param fields: 
        """
    
        if fields:
            fields = ','.join(fields)
        
        method_name = 'wall.getComment'
        return self.call(method_name, locals())

    def get_comments(self, owner_id: int = None, post_id: int = None, need_likes: bool = None, start_comment_id: int = None, offset: int = None, count: int = None, sort: str = None, preview_length: int = None, extended: bool = None, fields: List[str] = None, comment_id: int = None, thread_items_count: int = None):
        """
        Returns a list of comments on a post on a user wall or community wall.
        
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param post_id: Post ID.
        :param need_likes: '1' — to return the 'likes' field, '0' — not to return the 'likes' field (default)
        :param start_comment_id: 
        :param offset: Offset needed to return a specific subset of comments.
        :param count: Number of comments to return (maximum 100).
        :param sort: Sort order: 'asc' — chronological, 'desc' — reverse chronological
        :param preview_length: Number of characters at which to truncate comments when previewed. By default, '90'. Specify '0' if you do not want to truncate comments.
        :param extended: 
        :param fields: 
        :param comment_id: Comment ID.
        :param thread_items_count: Count items in threads.
        """
    
        if fields:
            fields = ','.join(fields)
        
        method_name = 'wall.getComments'
        return self.call(method_name, locals())

    def get_reposts(self, owner_id: int = None, post_id: int = None, offset: int = None, count: int = None):
        """
        Returns information about reposts of a post on user wall or community wall.
        
        :param owner_id: User ID or community ID. By default, current user ID. Use a negative value to designate a community ID.
        :param post_id: Post ID.
        :param offset: Offset needed to return a specific subset of reposts.
        :param count: Number of reposts to return.
        """
    
        method_name = 'wall.getReposts'
        return self.call(method_name, locals())

    def open_comments(self, owner_id: int, post_id: int):
        """
        
        :param owner_id: 
        :param post_id: 
        """
    
        method_name = 'wall.openComments'
        return self.call(method_name, locals())

    def pin(self, post_id: int, owner_id: int = None):
        """
        Pins the post on wall.
        
        :param post_id: Post ID.
        :param owner_id: ID of the user or community that owns the wall. By default, current user ID. Use a negative value to designate a community ID.
        """
    
        method_name = 'wall.pin'
        return self.call(method_name, locals())

    def post(self, owner_id: int = None, friends_only: bool = None, from_group: bool = None, message: str = None, attachments: List[str] = None, services: str = None, signed: bool = None, publish_date: int = None, lat: float = None, long: float = None, place_id: int = None, post_id: int = None, guid: str = None, mark_as_ads: bool = None, close_comments: bool = None, mute_notifications: bool = None, copyright_: str = None):
        """
        Adds a new post on a user wall or community wall. Can also be used to publish suggested or scheduled posts.
        
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param friends_only: '1' — post will be available to friends only, '0' — post will be available to all users (default)
        :param from_group: For a community: '1' — post will be published by the community, '0' — post will be published by the user (default)
        :param message: (Required if 'attachments' is not set.) Text of the post.
        :param attachments: (Required if 'message' is not set.) List of objects attached to the post, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, 'page' — wiki-page, 'note' — note, 'poll' — poll, 'album' — photo album, '<owner_id>' — ID of the media application owner. '<media_id>' — Media application ID. Example: "photo100172_166443618,photo66748_265827614", May contain a link to an external page to include in the post. Example: "photo66748_265827614,http://habrahabr.ru", "NOTE: If more than one link is being attached, an error will be thrown."
        :param services: List of services or websites the update will be exported to, if the user has so requested. Sample values: 'twitter', 'facebook'.
        :param signed: Only for posts in communities with 'from_group' set to '1': '1' — post will be signed with the name of the posting user, '0' — post will not be signed (default)
        :param publish_date: Publication date (in Unix time). If used, posting will be delayed until the set time.
        :param lat: Geographical latitude of a check-in, in degrees (from -90 to 90).
        :param long: Geographical longitude of a check-in, in degrees (from -180 to 180).
        :param place_id: ID of the location where the user was tagged.
        :param post_id: Post ID. Used for publishing of scheduled and suggested posts.
        :param guid: 
        :param mark_as_ads: 
        :param close_comments: 
        :param mute_notifications: 
        :param copyright_: 
        """
    
        if attachments:
            attachments = ','.join(attachments)
        
        param_alias_dict = {'copyright_': 'copyright'}
        method_name = 'wall.post'
        return self.call(method_name, locals())

    def post_ads_stealth(self, owner_id: int, message: str = None, attachments: List[str] = None, signed: bool = None, lat: float = None, long: float = None, place_id: int = None, guid: str = None, link_button: str = None, link_title: str = None, link_image: str = None, link_video: str = None):
        """
        Allows to create hidden post which will not be shown on the community's wall and can be used for creating an ad with type "Community post".
        
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param message: (Required if 'attachments' is not set.) Text of the post.
        :param attachments: (Required if 'message' is not set.) List of objects attached to the post, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, 'page' — wiki-page, 'note' — note, 'poll' — poll, 'album' — photo album, '<owner_id>' — ID of the media application owner. '<media_id>' — Media application ID. Example: "photo100172_166443618,photo66748_265827614", May contain a link to an external page to include in the post. Example: "photo66748_265827614,http://habrahabr.ru", "NOTE: If more than one link is being attached, an error will be thrown."
        :param signed: Only for posts in communities with 'from_group' set to '1': '1' — post will be signed with the name of the posting user, '0' — post will not be signed (default)
        :param lat: Geographical latitude of a check-in, in degrees (from -90 to 90).
        :param long: Geographical longitude of a check-in, in degrees (from -180 to 180).
        :param place_id: ID of the location where the user was tagged.
        :param guid: Unique identifier to avoid duplication the same post.
        :param link_button: Link button ID
        :param link_title: Link title
        :param link_image: Link image url
        :param link_video: Link video ID in format "<owner_id>_<media_id>"
        """
    
        if attachments:
            attachments = ','.join(attachments)
        
        method_name = 'wall.postAdsStealth'
        return self.call(method_name, locals())

    def report_comment(self, owner_id: int, comment_id: int, reason: int = None):
        """
        Reports (submits a complaint about) a comment on a post on a user wall or community wall.
        
        :param owner_id: ID of the user or community that owns the wall.
        :param comment_id: Comment ID.
        :param reason: Reason for the complaint: '0' – spam, '1' – child pornography, '2' – extremism, '3' – violence, '4' – drug propaganda, '5' – adult material, '6' – insult, abuse
        """
    
        method_name = 'wall.reportComment'
        return self.call(method_name, locals())

    def report_post(self, owner_id: int, post_id: int, reason: int = None):
        """
        Reports (submits a complaint about) a post on a user wall or community wall.
        
        :param owner_id: ID of the user or community that owns the wall.
        :param post_id: Post ID.
        :param reason: Reason for the complaint: '0' – spam, '1' – child pornography, '2' – extremism, '3' – violence, '4' – drug propaganda, '5' – adult material, '6' – insult, abuse
        """
    
        method_name = 'wall.reportPost'
        return self.call(method_name, locals())

    def repost(self, object_: str, message: str = None, group_id: int = None, mark_as_ads: bool = None, mute_notifications: bool = None):
        """
        Reposts (copies) an object to a user wall or community wall.
        
        :param object_: ID of the object to be reposted on the wall. Example: "wall66748_3675"
        :param message: Comment to be added along with the reposted object.
        :param group_id: Target community ID when reposting to a community.
        :param mark_as_ads: 
        :param mute_notifications: 
        """
    
        param_alias_dict = {'object_': 'object'}
        method_name = 'wall.repost'
        return self.call(method_name, locals())

    def restore(self, owner_id: int = None, post_id: int = None):
        """
        Restores a post deleted from a user wall or community wall.
        
        :param owner_id: User ID or community ID from whose wall the post was deleted. Use a negative value to designate a community ID.
        :param post_id: ID of the post to be restored.
        """
    
        method_name = 'wall.restore'
        return self.call(method_name, locals())

    def restore_comment(self, comment_id: int, owner_id: int = None):
        """
        Restores a comment deleted from a user wall or community wall.
        
        :param comment_id: Comment ID.
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        """
    
        method_name = 'wall.restoreComment'
        return self.call(method_name, locals())

    def search(self, owner_id: int = None, domain: str = None, query: str = None, owners_only: bool = None, count: int = None, offset: int = None, extended: bool = None, fields: List[str] = None):
        """
        Allows to search posts on user or community walls.
        
        :param owner_id: user or community id. "Remember that for a community 'owner_id' must be negative."
        :param domain: user or community screen name.
        :param query: search query string.
        :param owners_only: '1' – returns only page owner's posts.
        :param count: count of posts to return.
        :param offset: Offset needed to return a specific subset of posts.
        :param extended: show extended post info.
        :param fields: 
        """
    
        if fields:
            fields = ','.join(fields)
        
        method_name = 'wall.search'
        return self.call(method_name, locals())

    def unpin(self, post_id: int, owner_id: int = None):
        """
        Unpins the post on wall.
        
        :param post_id: Post ID.
        :param owner_id: ID of the user or community that owns the wall. By default, current user ID. Use a negative value to designate a community ID.
        """
    
        method_name = 'wall.unpin'
        return self.call(method_name, locals())

