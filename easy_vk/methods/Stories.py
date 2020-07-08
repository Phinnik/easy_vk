from ._ApiMethod import ApiMethod
from typing import List


class Stories(ApiMethod):
    def __init__(self, session, access_token, v, requests_per_s):
        super().__init__(session, access_token, v, requests_per_s)

    def ban_owner(self, owners_ids: List[int]):
        """
        Allows to hide stories from chosen sources from current user's feed.
        
        :param owners_ids: List of sources IDs
        """
    
        if owners_ids:
            owners_ids = [str(o) for o in owners_ids]
            owners_ids = ','.join(owners_ids)
        
        method_name = 'stories.banOwner'
        return self._call(method_name, locals())

    def delete(self, owner_id: int, story_id: int):
        """
        Allows to delete story.
        
        :param owner_id: Story owner's ID. Current user id is used by default.
        :param story_id: Story ID.
        """
    
        method_name = 'stories.delete'
        return self._call(method_name, locals())

    def get(self, owner_id: int = None, extended: bool = None, fields: List[str] = None):
        """
        Returns stories available for current user.
        
        :param owner_id: Owner ID.
        :param extended: '1' — to return additional fields for users and communities. Default value is 0.
        :param fields: 
        """
    
        if fields:
            fields = ','.join(fields)
        
        method_name = 'stories.get'
        return self._call(method_name, locals())

    def get_banned(self, extended: bool = None, fields: List[str] = None):
        """
        Returns list of sources hidden from current user's feed.
        
        :param extended: '1' — to return additional fields for users and communities. Default value is 0.
        :param fields: Additional fields to return
        """
    
        if fields:
            fields = ','.join(fields)
        
        method_name = 'stories.getBanned'
        return self._call(method_name, locals())

    def get_by_id(self, stories: List[str], extended: bool = None, fields: List[str] = None):
        """
        Returns story by its ID.
        
        :param stories: Stories IDs separated by commas. Use format {owner_id}+'_'+{story_id}, for example, 12345_54331.
        :param extended: '1' — to return additional fields for users and communities. Default value is 0.
        :param fields: Additional fields to return
        """
    
        if stories:
            stories = ','.join(stories)
        if fields:
            fields = ','.join(fields)
        
        method_name = 'stories.getById'
        return self._call(method_name, locals())

    def get_photo_upload_server(self, add_to_news: bool = None, user_ids: List[int] = None, reply_to_story: str = None, link_text: str = None, link_url: str = None, group_id: int = None, clickable_stickers: str = None):
        """
        Returns URL for uploading a story with photo.
        
        :param add_to_news: 1 — to add the story to friend's feed.
        :param user_ids: List of users IDs who can see the story.
        :param reply_to_story: ID of the story to reply with the current.
        :param link_text: Link text (for community's stories only).
        :param link_url: Link URL. Internal links on https://vk.com only.
        :param group_id: ID of the community to upload the story (should be verified or with the "fire" icon).
        :param clickable_stickers: 
        """
    
        if user_ids:
            user_ids = [str(u) for u in user_ids]
            user_ids = ','.join(user_ids)
        
        method_name = 'stories.getPhotoUploadServer'
        return self._call(method_name, locals())

    def get_replies(self, owner_id: int, story_id: int, access_key: str = None, extended: bool = None, fields: List[str] = None):
        """
        Returns replies to the story.
        
        :param owner_id: Story owner ID.
        :param story_id: Story ID.
        :param access_key: Access key for the private object.
        :param extended: '1' — to return additional fields for users and communities. Default value is 0.
        :param fields: Additional fields to return
        """
    
        if fields:
            fields = ','.join(fields)
        
        method_name = 'stories.getReplies'
        return self._call(method_name, locals())

    def get_stats(self, owner_id: int, story_id: int):
        """
        Returns stories available for current user.
        
        :param owner_id: Story owner ID. 
        :param story_id: Story ID.
        """
    
        method_name = 'stories.getStats'
        return self._call(method_name, locals())

    def get_video_upload_server(self, add_to_news: bool = None, user_ids: List[int] = None, reply_to_story: str = None, link_text: str = None, link_url: str = None, group_id: int = None, clickable_stickers: str = None):
        """
        Allows to receive URL for uploading story with video.
        
        :param add_to_news: 1 — to add the story to friend's feed.
        :param user_ids: List of users IDs who can see the story.
        :param reply_to_story: ID of the story to reply with the current.
        :param link_text: Link text (for community's stories only).
        :param link_url: Link URL. Internal links on https://vk.com only.
        :param group_id: ID of the community to upload the story (should be verified or with the "fire" icon).
        :param clickable_stickers: 
        """
    
        if user_ids:
            user_ids = [str(u) for u in user_ids]
            user_ids = ','.join(user_ids)
        
        method_name = 'stories.getVideoUploadServer'
        return self._call(method_name, locals())

    def get_viewers(self, owner_id: int, story_id: int, count: int = None, offset: int = None, extended: bool = None):
        """
        Returns a list of story viewers.
        
        :param owner_id: Story owner ID.
        :param story_id: Story ID.
        :param count: Maximum number of results.
        :param offset: Offset needed to return a specific subset of results.
        :param extended: '1' — to return detailed information about photos
        """
    
        method_name = 'stories.getViewers'
        return self._call(method_name, locals())

    def hide_all_replies(self, owner_id: int, group_id: int = None):
        """
        Hides all replies in the last 24 hours from the user to current user's stories.
        
        :param owner_id: ID of the user whose replies should be hidden.
        :param group_id: 
        """
    
        method_name = 'stories.hideAllReplies'
        return self._call(method_name, locals())

    def hide_reply(self, owner_id: int, story_id: int):
        """
        Hides the reply to the current user's story.
        
        :param owner_id: ID of the user whose replies should be hidden.
        :param story_id: Story ID.
        """
    
        method_name = 'stories.hideReply'
        return self._call(method_name, locals())

    def search(self, q: str = None, place_id: int = None, latitude: float = None, longitude: float = None, radius: int = None, mentioned_id: int = None, count: int = None, extended: bool = None, fields: List[str] = None):
        """
        
        :param q: 
        :param place_id: 
        :param latitude: 
        :param longitude: 
        :param radius: 
        :param mentioned_id: 
        :param count: 
        :param extended: 
        :param fields: 
        """
    
        if fields:
            fields = ','.join(fields)
        
        method_name = 'stories.search'
        return self._call(method_name, locals())

    def unban_owner(self, owners_ids: List[int]):
        """
        Allows to show stories from hidden sources in current user's feed.
        
        :param owners_ids: List of hidden sources to show stories from.
        """
    
        if owners_ids:
            owners_ids = [str(o) for o in owners_ids]
            owners_ids = ','.join(owners_ids)
        
        method_name = 'stories.unbanOwner'
        return self._call(method_name, locals())

