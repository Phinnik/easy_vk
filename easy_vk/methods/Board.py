from ._ApiMethod import ApiMethod
from typing import List


class Board(ApiMethod):
    def __init__(self, session, access_token, v, requests_per_s):
        super().__init__(session, access_token, v, requests_per_s)

    def add_topic(self, group_id: int, title: str, text: str = None, from_group: bool = None, attachments: List[str] = None):
        """
        Creates a new topic on a community's discussion board.
        
        :param group_id: ID of the community that owns the discussion board.
        :param title: Topic title.
        :param text: Text of the topic.
        :param from_group: For a community: '1' — to post the topic as by the community, '0' — to post the topic as by the user (default)
        :param attachments: List of media objects attached to the topic, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media object: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media owner. '<media_id>' — Media ID. Example: "photo100172_166443618,photo66748_265827614", , "NOTE: If you try to attach more than one reference, an error will be thrown.",
        """
    
        if attachments:
            attachments = ','.join(attachments)
        
        method_name = 'board.addTopic'
        return self._call(method_name, locals())

    def close_topic(self, group_id: int, topic_id: int):
        """
        Closes a topic on a community's discussion board so that comments cannot be posted.
        
        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        """
    
        method_name = 'board.closeTopic'
        return self._call(method_name, locals())

    def create_comment(self, group_id: int, topic_id: int, message: str = None, attachments: List[str] = None, from_group: bool = None, sticker_id: int = None, guid: str = None):
        """
        Adds a comment on a topic on a community's discussion board.
        
        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: ID of the topic to be commented on.
        :param message: (Required if 'attachments' is not set.) Text of the comment.
        :param attachments: (Required if 'text' is not set.) List of media objects attached to the comment, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media object: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media owner. '<media_id>' — Media ID.
        :param from_group: '1' — to post the comment as by the community, '0' — to post the comment as by the user (default)
        :param sticker_id: Sticker ID.
        :param guid: Unique identifier to avoid repeated comments.
        """
    
        if attachments:
            attachments = ','.join(attachments)
        
        method_name = 'board.createComment'
        return self._call(method_name, locals())

    def delete_comment(self, group_id: int, topic_id: int, comment_id: int):
        """
        Deletes a comment on a topic on a community's discussion board.
        
        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        :param comment_id: Comment ID.
        """
    
        method_name = 'board.deleteComment'
        return self._call(method_name, locals())

    def delete_topic(self, group_id: int, topic_id: int):
        """
        Deletes a topic from a community's discussion board.
        
        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        """
    
        method_name = 'board.deleteTopic'
        return self._call(method_name, locals())

    def edit_comment(self, group_id: int, topic_id: int, comment_id: int, message: str = None, attachments: List[str] = None):
        """
        Edits a comment on a topic on a community's discussion board.
        
        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        :param comment_id: ID of the comment on the topic.
        :param message: (Required if 'attachments' is not set). New comment text.
        :param attachments: (Required if 'message' is not set.) List of media objects attached to the comment, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media object: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media owner. '<media_id>' — Media ID. Example: "photo100172_166443618,photo66748_265827614"
        """
    
        if attachments:
            attachments = ','.join(attachments)
        
        method_name = 'board.editComment'
        return self._call(method_name, locals())

    def edit_topic(self, group_id: int, topic_id: int, title: str):
        """
        Edits the title of a topic on a community's discussion board.
        
        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        :param title: New title of the topic.
        """
    
        method_name = 'board.editTopic'
        return self._call(method_name, locals())

    def fix_topic(self, group_id: int, topic_id: int):
        """
        Pins a topic (fixes its place) to the top of a community's discussion board.
        
        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        """
    
        method_name = 'board.fixTopic'
        return self._call(method_name, locals())

    def get_comments(self, group_id: int, topic_id: int, need_likes: bool = None, start_comment_id: int = None, offset: int = None, count: int = None, extended: bool = None, sort: str = None):
        """
        Returns a list of comments on a topic on a community's discussion board.
        
        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        :param need_likes: '1' — to return the 'likes' field, '0' — not to return the 'likes' field (default)
        :param start_comment_id: 
        :param offset: Offset needed to return a specific subset of comments.
        :param count: Number of comments to return.
        :param extended: '1' — to return information about users who posted comments, '0' — to return no additional fields (default)
        :param sort: Sort order: 'asc' — by creation date in chronological order, 'desc' — by creation date in reverse chronological order,
        """
    
        method_name = 'board.getComments'
        return self._call(method_name, locals())

    def get_topics(self, group_id: int, topic_ids: List[int] = None, order: int = None, offset: int = None, count: int = None, extended: bool = None, preview: int = None, preview_length: int = None):
        """
        Returns a list of topics on a community's discussion board.
        
        :param group_id: ID of the community that owns the discussion board.
        :param topic_ids: IDs of topics to be returned (100 maximum). By default, all topics are returned. If this parameter is set, the 'order', 'offset', and 'count' parameters are ignored.
        :param order: Sort order: '1' — by date updated in reverse chronological order. '2' — by date created in reverse chronological order. '-1' — by date updated in chronological order. '-2' — by date created in chronological order. If no sort order is specified, topics are returned in the order specified by the group administrator. Pinned topics are returned first, regardless of the sorting.
        :param offset: Offset needed to return a specific subset of topics.
        :param count: Number of topics to return.
        :param extended: '1' — to return information about users who created topics or who posted there last, '0' — to return no additional fields (default)
        :param preview: '1' — to return the first comment in each topic,, '2' — to return the last comment in each topic,, '0' — to return no comments. By default: '0'.
        :param preview_length: Number of characters after which to truncate the previewed comment. To preview the full comment, specify '0'.
        """
    
        if topic_ids:
            topic_ids = [str(t) for t in topic_ids]
            topic_ids = ','.join(topic_ids)
        
        method_name = 'board.getTopics'
        return self._call(method_name, locals())

    def open_topic(self, group_id: int, topic_id: int):
        """
        Re-opens a previously closed topic on a community's discussion board.
        
        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        """
    
        method_name = 'board.openTopic'
        return self._call(method_name, locals())

    def restore_comment(self, group_id: int, topic_id: int, comment_id: int):
        """
        Restores a comment deleted from a topic on a community's discussion board.
        
        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        :param comment_id: Comment ID.
        """
    
        method_name = 'board.restoreComment'
        return self._call(method_name, locals())

    def unfix_topic(self, group_id: int, topic_id: int):
        """
        Unpins a pinned topic from the top of a community's discussion board.
        
        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        """
    
        method_name = 'board.unfixTopic'
        return self._call(method_name, locals())

