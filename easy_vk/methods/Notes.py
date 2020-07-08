from ._ApiMethod import ApiMethod
from typing import List


class Notes(ApiMethod):
    def __init__(self, session, access_token, v, requests_per_s):
        super().__init__(session, access_token, v, requests_per_s)

    def add(self, title: str, text: str, privacy_view: List[str] = None, privacy_comment: List[str] = None):
        """
        Creates a new note for the current user.
        
        :param title: Note title.
        :param text: Note text.
        :param privacy_view: 
        :param privacy_comment: 
        """
    
        if privacy_view:
            privacy_view = ','.join(privacy_view)
        if privacy_comment:
            privacy_comment = ','.join(privacy_comment)
        
        method_name = 'notes.add'
        return self._call(method_name, locals())

    def create_comment(self, note_id: int, message: str, owner_id: int = None, reply_to: int = None, guid: str = None):
        """
        Adds a new comment on a note.
        
        :param note_id: Note ID.
        :param message: Comment text.
        :param owner_id: Note owner ID.
        :param reply_to: ID of the user to whom the reply is addressed (if the comment is a reply to another comment).
        :param guid: 
        """
    
        method_name = 'notes.createComment'
        return self._call(method_name, locals())

    def delete(self, note_id: int):
        """
        Deletes a note of the current user.
        
        :param note_id: Note ID.
        """
    
        method_name = 'notes.delete'
        return self._call(method_name, locals())

    def delete_comment(self, comment_id: int, owner_id: int = None):
        """
        Deletes a comment on a note.
        
        :param comment_id: Comment ID.
        :param owner_id: Note owner ID.
        """
    
        method_name = 'notes.deleteComment'
        return self._call(method_name, locals())

    def edit(self, note_id: int, title: str, text: str, privacy_view: List[str] = None, privacy_comment: List[str] = None):
        """
        Edits a note of the current user.
        
        :param note_id: Note ID.
        :param title: Note title.
        :param text: Note text.
        :param privacy_view: 
        :param privacy_comment: 
        """
    
        if privacy_view:
            privacy_view = ','.join(privacy_view)
        if privacy_comment:
            privacy_comment = ','.join(privacy_comment)
        
        method_name = 'notes.edit'
        return self._call(method_name, locals())

    def edit_comment(self, comment_id: int, message: str, owner_id: int = None):
        """
        Edits a comment on a note.
        
        :param comment_id: Comment ID.
        :param message: New comment text.
        :param owner_id: Note owner ID.
        """
    
        method_name = 'notes.editComment'
        return self._call(method_name, locals())

    def get(self, note_ids: List[int] = None, user_id: int = None, offset: int = None, count: int = None, sort: int = None):
        """
        Returns a list of notes created by a user.
        
        :param note_ids: Note IDs.
        :param user_id: Note owner ID.
        :param offset: 
        :param count: Number of notes to return.
        :param sort: 
        """
    
        if note_ids:
            note_ids = [str(n) for n in note_ids]
            note_ids = ','.join(note_ids)
        
        method_name = 'notes.get'
        return self._call(method_name, locals())

    def get_by_id(self, note_id: int, owner_id: int = None, need_wiki: bool = None):
        """
        Returns a note by its ID.
        
        :param note_id: Note ID.
        :param owner_id: Note owner ID.
        :param need_wiki: 
        """
    
        method_name = 'notes.getById'
        return self._call(method_name, locals())

    def get_comments(self, note_id: int, owner_id: int = None, sort: int = None, offset: int = None, count: int = None):
        """
        Returns a list of comments on a note.
        
        :param note_id: Note ID.
        :param owner_id: Note owner ID.
        :param sort: 
        :param offset: 
        :param count: Number of comments to return.
        """
    
        method_name = 'notes.getComments'
        return self._call(method_name, locals())

    def restore_comment(self, comment_id: int, owner_id: int = None):
        """
        Restores a deleted comment on a note.
        
        :param comment_id: Comment ID.
        :param owner_id: Note owner ID.
        """
    
        method_name = 'notes.restoreComment'
        return self._call(method_name, locals())

