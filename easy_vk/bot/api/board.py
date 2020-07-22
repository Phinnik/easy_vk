from typing import List, Union, Optional
from easy_vk.types import objects, responses
from .base import BaseCategory


class Board(BaseCategory):
    def __init__(self, session, access_token: str, v: str, delay: float, auto_retry: bool, max_retries: int, timeout: float):
        super().__init__(session, access_token, v, delay, auto_retry, max_retries, timeout)

    def delete_comment(self, group_id: int = None, topic_id: int = None, comment_id: int = None) -> responses.BaseOk:
        """
        Deletes a comment on a topic on a community's discussion board.
        
        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        :param comment_id: Comment ID.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'board.deleteComment'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def restore_comment(self, group_id: int = None, topic_id: int = None, comment_id: int = None) -> responses.BaseOk:
        """
        Restores a comment deleted from a topic on a community's discussion board.
        
        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        :param comment_id: Comment ID.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'board.restoreComment'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

