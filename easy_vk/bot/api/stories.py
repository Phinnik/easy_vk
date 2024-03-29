# This file was autogenerated from vk-api json schema

from typing import List, Union, Optional, overload
from easy_vk.types import objects
from easy_vk.types import responses
from easy_vk.api_category import BaseCategory
try:
    from typing import Literal
except Exception:
    from typing_extensions import Literal


class Stories(BaseCategory):
    def delete(self, owner_id: int, story_id: int) -> responses.BaseOk:
        """
        Allows to delete story.

        :param owner_id: Story owner's ID. Current user id is used by default.
        :param story_id: Story ID.
        """

        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'stories.delete'
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get(self, owner_id: Optional[int] = None, extended: Optional[bool] = None, fields: Optional[List[Union[objects.BaseUserGroupFields, str]]] = None) -> responses.StoriesGetV5113:
        """
        Returns stories available for current user.

        :param owner_id: Owner ID.
        :param extended: '1' — to return additional fields for users and communities. Default value is 0.
        :param fields:
        """

        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'stories.get'
        response_type = responses.StoriesGetV5113
        return self._call(method_name, method_parameters, param_aliases, response_type)

    @overload
    def get_by_id(self, stories: List[str], extended: None = None, fields: Optional[List[Union[objects.BaseUserGroupFields, str]]] = None) -> responses.StoriesGetById: ...
    @overload
    def get_by_id(self, stories: List[str], extended: bool, fields: Optional[List[Union[objects.BaseUserGroupFields, str]]] = None) -> responses.StoriesGetByIdExtended: ...
    def get_by_id(self, stories: List[str], extended: Optional[bool] = None, fields: Optional[List[Union[objects.BaseUserGroupFields, str]]] = None):
        """
        Returns story by its ID.

        :param stories: Stories IDs separated by commas. Use format {owner_id}+'_'+{story_id}, for example, 12345_54331.
        :param extended: '1' — to return additional fields for users and communities. Default value is 0.
        :param fields: Additional fields to return
        """

        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'stories.getById'
        if not extended:
            response_type = responses.StoriesGetById
        if extended:
            response_type = responses.StoriesGetByIdExtended
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_photo_upload_server(self, add_to_news: Optional[bool] = None, user_ids: Optional[List[int]] = None, reply_to_story: Optional[str] = None, link_text: Optional[str] = None, link_url: Optional[str] = None, group_id: Optional[int] = None, clickable_stickers: Optional[str] = None) -> responses.StoriesGetPhotoUploadServer:
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
        param_aliases = []
        method_name = 'stories.getPhotoUploadServer'
        response_type = responses.StoriesGetPhotoUploadServer
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_replies(self, owner_id: int, story_id: int, access_key: Optional[str] = None, extended: Optional[bool] = None, fields: Optional[List[Union[objects.BaseUserGroupFields, str]]] = None) -> responses.StoriesGetV5113:
        """
        Returns replies to the story.

        :param owner_id: Story owner ID.
        :param story_id: Story ID.
        :param access_key: Access key for the private object.
        :param extended: '1' — to return additional fields for users and communities. Default value is 0.
        :param fields: Additional fields to return
        """

        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'stories.getReplies'
        response_type = responses.StoriesGetV5113
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_stats(self, owner_id: int, story_id: int) -> responses.StoriesGetStats:
        """
        Returns stories available for current user.

        :param owner_id: Story owner ID.
        :param story_id: Story ID.
        """

        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'stories.getStats'
        response_type = responses.StoriesGetStats
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_video_upload_server(self, add_to_news: Optional[bool] = None, user_ids: Optional[List[int]] = None, reply_to_story: Optional[str] = None, link_text: Optional[str] = None, link_url: Optional[str] = None, group_id: Optional[int] = None, clickable_stickers: Optional[str] = None) -> responses.StoriesGetVideoUploadServer:
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
        param_aliases = []
        method_name = 'stories.getVideoUploadServer'
        response_type = responses.StoriesGetVideoUploadServer
        return self._call(method_name, method_parameters, param_aliases, response_type)

    @overload
    def get_viewers(self, owner_id: int, story_id: int, count: Optional[int] = None, offset: Optional[int] = None, extended: None = None) -> responses.StoriesGetViewersExtendedV5115: ...
    @overload
    def get_viewers(self, owner_id: int, story_id: int, extended: bool, count: Optional[int] = None, offset: Optional[int] = None) -> responses.StoriesGetViewersExtendedV5115: ...
    def get_viewers(self, owner_id: int, story_id: int, count: Optional[int] = None, offset: Optional[int] = None, extended: Optional[bool] = None):
        """
        Returns a list of story viewers.

        :param owner_id: Story owner ID.
        :param story_id: Story ID.
        :param count: Maximum number of results.
        :param offset: Offset needed to return a specific subset of results.
        :param extended: '1' — to return detailed information about photos
        """

        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'stories.getViewers'
        if not extended:
            response_type = responses.StoriesGetViewersExtendedV5115
        if extended:
            response_type = responses.StoriesGetViewersExtendedV5115
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def hide_all_replies(self, owner_id: int, group_id: Optional[int] = None) -> responses.BaseOk:
        """
        Hides all replies in the last 24 hours from the user to current user's stories.

        :param owner_id: ID of the user whose replies should be hidden.
        :param group_id:
        """

        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'stories.hideAllReplies'
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def hide_reply(self, owner_id: int, story_id: int) -> responses.BaseOk:
        """
        Hides the reply to the current user's story.

        :param owner_id: ID of the user whose replies should be hidden.
        :param story_id: Story ID.
        """

        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'stories.hideReply'
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)
