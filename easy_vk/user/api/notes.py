from typing import List, Union, Optional
from easy_vk.types import objects, responses
from .base import BaseCategory


class Notes(BaseCategory):
    def __init__(self, session, access_token: str, v: str, delay: float, auto_retry: bool, max_retries: int, timeout: float):
        super().__init__(session, access_token, v, delay, auto_retry, max_retries, timeout)

    def add(self, title: str = None, text: str = None, privacy_view: List[str] = None, privacy_comment: List[str] = None) -> responses.NotesAdd:
        """
        Creates a new note for the current user.
        
        :param title: Note title.
        :param text: Note text.
        :param privacy_view: 
        :param privacy_comment: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'notes.add'
        param_aliases = []
        response_type = responses.NotesAdd
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def create_comment(self, note_id: int = None, owner_id: int = None, reply_to: int = None, message: str = None, guid: str = None) -> responses.NotesCreateComment:
        """
        Adds a new comment on a note.
        
        :param note_id: Note ID.
        :param owner_id: Note owner ID.
        :param reply_to: ID of the user to whom the reply is addressed (if the comment is a reply to another comment).
        :param message: Comment text.
        :param guid: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'notes.createComment'
        param_aliases = []
        response_type = responses.NotesCreateComment
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def delete(self, note_id: int = None) -> responses.BaseOk:
        """
        Deletes a note of the current user.
        
        :param note_id: Note ID.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'notes.delete'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def delete_comment(self, comment_id: int = None, owner_id: int = None) -> responses.BaseOk:
        """
        Deletes a comment on a note.
        
        :param comment_id: Comment ID.
        :param owner_id: Note owner ID.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'notes.deleteComment'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def edit(self, note_id: int = None, title: str = None, text: str = None, privacy_view: List[str] = None, privacy_comment: List[str] = None) -> responses.BaseOk:
        """
        Edits a note of the current user.
        
        :param note_id: Note ID.
        :param title: Note title.
        :param text: Note text.
        :param privacy_view: 
        :param privacy_comment: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'notes.edit'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def edit_comment(self, comment_id: int = None, owner_id: int = None, message: str = None) -> responses.BaseOk:
        """
        Edits a comment on a note.
        
        :param comment_id: Comment ID.
        :param owner_id: Note owner ID.
        :param message: New comment text.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'notes.editComment'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get(self, note_ids: List[int] = None, user_id: int = None, offset: int = None, count: int = None, sort: int = None) -> responses.NotesGet:
        """
        Returns a list of notes created by a user.
        
        :param note_ids: Note IDs.
        :param user_id: Note owner ID.
        :param offset: 
        :param count: Number of notes to return.
        :param sort: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'notes.get'
        param_aliases = []
        response_type = responses.NotesGet
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_by_id(self, note_id: int = None, owner_id: int = None, need_wiki: bool = None) -> responses.NotesGetById:
        """
        Returns a note by its ID.
        
        :param note_id: Note ID.
        :param owner_id: Note owner ID.
        :param need_wiki: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'notes.getById'
        param_aliases = []
        response_type = responses.NotesGetById
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_comments(self, note_id: int = None, owner_id: int = None, sort: int = None, offset: int = None, count: int = None) -> responses.NotesGetComments:
        """
        Returns a list of comments on a note.
        
        :param note_id: Note ID.
        :param owner_id: Note owner ID.
        :param sort: 
        :param offset: 
        :param count: Number of comments to return.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'notes.getComments'
        param_aliases = []
        response_type = responses.NotesGetComments
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def restore_comment(self, comment_id: int = None, owner_id: int = None) -> responses.BaseOk:
        """
        Restores a deleted comment on a note.
        
        :param comment_id: Comment ID.
        :param owner_id: Note owner ID.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'notes.restoreComment'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

