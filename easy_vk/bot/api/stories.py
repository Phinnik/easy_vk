from typing import List, Union, Optional
from easy_vk.types import objects, responses
from .base import BaseCategory


class Stories(BaseCategory):
    def __init__(self, session, access_token: str, v: str, delay: float, auto_retry: bool, max_retries: int, timeout: float):
        super().__init__(session, access_token, v, delay, auto_retry, max_retries, timeout)

    def delete(self, owner_id: int = None, story_id: int = None) -> responses.BaseOk:
        """
        Allows to delete story.
        
        :param owner_id: Story owner's ID. Current user id is used by default.
        :param story_id: Story ID.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'stories.delete'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get(self, owner_id: int = None, extended: bool = None, fields: List[Union[objects.BaseUserGroupFields, str]] = None) -> responses.StoriesGetV5113:
        """
        Returns stories available for current user.
        
        :param owner_id: Owner ID.
        :param extended: '1' — to return additional fields for users and communities. Default value is 0.
        :param fields: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'stories.get'
        param_aliases = []
        response_type = responses.StoriesGetV5113
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_by_id(self, stories: List[str] = None, extended: bool = None, fields: List[Union[objects.BaseUserGroupFields, str]] = None) -> Union[responses.StoriesGetById, responses.StoriesGetByIdExtended]:
        """
        Returns story by its ID.
        
        :param stories: Stories IDs separated by commas. Use format {owner_id}+'_'+{story_id}, for example, 12345_54331.
        :param extended: '1' — to return additional fields for users and communities. Default value is 0.
        :param fields: Additional fields to return
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'stories.getById'
        param_aliases = []
        if not extended:
            response_type = responses.StoriesGetById
        else:
            response_type = responses.StoriesGetByIdExtended
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_photo_upload_server(self, add_to_news: bool = None, user_ids: List[int] = None, reply_to_story: str = None, link_text: Union[objects.StoriesUploadLinkText, str] = None, link_url: str = None, group_id: int = None, clickable_stickers: str = None) -> responses.StoriesGetPhotoUploadServer:
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
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'stories.getPhotoUploadServer'
        param_aliases = []
        response_type = responses.StoriesGetPhotoUploadServer
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_replies(self, owner_id: int = None, story_id: int = None, access_key: str = None, extended: bool = None, fields: List[Union[objects.BaseUserGroupFields, str]] = None) -> responses.StoriesGetV5113:
        """
        Returns replies to the story.
        
        :param owner_id: Story owner ID.
        :param story_id: Story ID.
        :param access_key: Access key for the private object.
        :param extended: '1' — to return additional fields for users and communities. Default value is 0.
        :param fields: Additional fields to return
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'stories.getReplies'
        param_aliases = []
        response_type = responses.StoriesGetV5113
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_stats(self, owner_id: int = None, story_id: int = None) -> responses.StoriesGetStats:
        """
        Returns stories available for current user.
        
        :param owner_id: Story owner ID. 
        :param story_id: Story ID.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'stories.getStats'
        param_aliases = []
        response_type = responses.StoriesGetStats
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_video_upload_server(self, add_to_news: bool = None, user_ids: List[int] = None, reply_to_story: str = None, link_text: Union[objects.StoriesUploadLinkText, str] = None, link_url: str = None, group_id: int = None, clickable_stickers: str = None) -> responses.StoriesGetVideoUploadServer:
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
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'stories.getVideoUploadServer'
        param_aliases = []
        response_type = responses.StoriesGetVideoUploadServer
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_viewers(self, owner_id: int = None, story_id: int = None, count: int = None, offset: int = None, extended: bool = None) -> Union[responses.StoriesGetViewersExtendedV5115, responses.StoriesGetViewersExtendedV5115]:
        """
        Returns a list of story viewers.
        
        :param owner_id: Story owner ID.
        :param story_id: Story ID.
        :param count: Maximum number of results.
        :param offset: Offset needed to return a specific subset of results.
        :param extended: '1' — to return detailed information about photos
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'stories.getViewers'
        param_aliases = []
        if extended:
            response_type = responses.StoriesGetViewersExtendedV5115
        else:
            response_type = responses.StoriesGetViewersExtendedV5115
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def hide_all_replies(self, owner_id: int = None, group_id: int = None) -> responses.BaseOk:
        """
        Hides all replies in the last 24 hours from the user to current user's stories.
        
        :param owner_id: ID of the user whose replies should be hidden.
        :param group_id: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'stories.hideAllReplies'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def hide_reply(self, owner_id: int = None, story_id: int = None) -> responses.BaseOk:
        """
        Hides the reply to the current user's story.
        
        :param owner_id: ID of the user whose replies should be hidden.
        :param story_id: Story ID.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'stories.hideReply'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

