from typing import List, Union, Optional
from easy_vk.types import objects, responses
from .base import BaseCategory


class Wall(BaseCategory):
    def __init__(self, session, access_token: str, v: str, delay: float, auto_retry: bool, max_retries: int, timeout: float):
        super().__init__(session, access_token, v, delay, auto_retry, max_retries, timeout)

    def close_comments(self, owner_id: int = None, post_id: int = None) -> responses.BaseBool:
        """
        :param owner_id: 
        :param post_id: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'wall.closeComments'
        param_aliases = []
        response_type = responses.BaseBool
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def create_comment(self, owner_id: int = None, post_id: int = None, from_group: int = None, message: str = None, reply_to_comment: int = None, attachments: List[str] = None, sticker_id: int = None, guid: str = None) -> responses.WallCreateComment:
        """
        Adds a comment to a post on a user wall or community wall.
        
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param post_id: Post ID.
        :param from_group: Group ID.
        :param message: (Required if 'attachments' is not set.) Text of the comment.
        :param reply_to_comment: ID of comment to reply.
        :param attachments: (Required if 'message' is not set.) List of media objects attached to the comment, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media ojbect: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media owner. '<media_id>' — Media ID. For example: "photo100172_166443618,photo66748_265827614"
        :param sticker_id: Sticker ID.
        :param guid: Unique identifier to avoid repeated comments.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'wall.createComment'
        param_aliases = []
        response_type = responses.WallCreateComment
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def open_comments(self, owner_id: int = None, post_id: int = None) -> responses.BaseBool:
        """
        :param owner_id: 
        :param post_id: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'wall.openComments'
        param_aliases = []
        response_type = responses.BaseBool
        return self._call(method_name, method_parameters, param_aliases, response_type)
