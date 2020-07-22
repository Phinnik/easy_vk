from typing import List, Union, Optional
from easy_vk.types import objects, responses
from .base import BaseCategory


class Messages(BaseCategory):
    def __init__(self, session, access_token: str, v: str, delay: float, auto_retry: bool, max_retries: int, timeout: float):
        super().__init__(session, access_token, v, delay, auto_retry, max_retries, timeout)

    def add_chat_user(self, chat_id: int = None, user_id: int = None, visible_messages_count: int = None) -> responses.BaseOk:
        """
        Adds a new user to a chat.
        
        :param chat_id: Chat ID.
        :param user_id: ID of the user to be added to the chat.
        :param visible_messages_count: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'messages.addChatUser'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def allow_messages_from_group(self, group_id: int = None, key: str = None) -> responses.BaseOk:
        """
        Allows sending messages from community to the current user.
        
        :param group_id: Group ID.
        :param key: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'messages.allowMessagesFromGroup'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def create_chat(self, user_ids: List[int] = None, title: str = None, group_id: int = None) -> responses.MessagesCreateChat:
        """
        Creates a chat with several participants.
        
        :param user_ids: IDs of the users to be added to the chat.
        :param title: Chat title.
        :param group_id: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'messages.createChat'
        param_aliases = []
        response_type = responses.MessagesCreateChat
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def delete(self, message_ids: List[int] = None, spam: bool = None, group_id: int = None, delete_for_all: bool = None) -> responses.MessagesDelete:
        """
        Deletes one or more messages.
        
        :param message_ids: Message IDs.
        :param spam: '1' — to mark message as spam.
        :param group_id: Group ID (for group messages with user access token)
        :param delete_for_all: '1' — delete message for for all.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'messages.delete'
        param_aliases = []
        response_type = responses.MessagesDelete
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def delete_chat_photo(self, chat_id: int = None, group_id: int = None) -> responses.MessagesDeleteChatPhoto:
        """
        Deletes a chat's cover picture.
        
        :param chat_id: Chat ID.
        :param group_id: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'messages.deleteChatPhoto'
        param_aliases = []
        response_type = responses.MessagesDeleteChatPhoto
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def delete_conversation(self, user_id: int = None, peer_id: int = None, group_id: int = None) -> responses.MessagesDeleteConversation:
        """
        Deletes all private messages in a conversation.
        
        :param user_id: User ID. To clear a chat history use 'chat_id'
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param group_id: Group ID (for group messages with user access token)
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'messages.deleteConversation'
        param_aliases = []
        response_type = responses.MessagesDeleteConversation
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def deny_messages_from_group(self, group_id: int = None) -> responses.BaseOk:
        """
        Denies sending message from community to the current user.
        
        :param group_id: Group ID.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'messages.denyMessagesFromGroup'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def edit(self, peer_id: int = None, message: str = None, lat: float = None, long: float = None, attachment: str = None, keep_forward_messages: bool = None, keep_snippets: bool = None, group_id: int = None, dont_parse_links: bool = None, message_id: int = None, conversation_message_id: int = None, template: str = None, keyboard: str = None) -> responses.MessagesEdit:
        """
        Edits the message.
        
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param message: (Required if 'attachments' is not set.) Text of the message.
        :param lat: Geographical latitude of a check-in, in degrees (from -90 to 90).
        :param long: Geographical longitude of a check-in, in degrees (from -180 to 180).
        :param attachment: (Required if 'message' is not set.) List of objects attached to the message, separated by commas, in the following format: "<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, 'wall' — wall post, '<owner_id>' — ID of the media attachment owner. '<media_id>' — media attachment ID. Example: "photo100172_166443618"
        :param keep_forward_messages: '1' — to keep forwarded, messages.
        :param keep_snippets: '1' — to keep attached snippets.
        :param group_id: Group ID (for group messages with user access token)
        :param dont_parse_links: 
        :param message_id: 
        :param conversation_message_id: 
        :param template: 
        :param keyboard: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'messages.edit'
        param_aliases = []
        response_type = responses.MessagesEdit
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def edit_chat(self, chat_id: int = None, title: str = None) -> responses.BaseOk:
        """
        Edits the title of a chat.
        
        :param chat_id: Chat ID.
        :param title: New title of the chat.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'messages.editChat'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_by_conversation_message_id(self, peer_id: int = None, conversation_message_ids: List[int] = None, extended: bool = None, fields: List[Union[objects.UsersFields, str]] = None, group_id: int = None) -> responses.MessagesGetByConversationMessageId:
        """
        Returns messages by their IDs within the conversation.
        
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param conversation_message_ids: Conversation message IDs.
        :param extended: Information whether the response should be extended
        :param fields: Profile fields to return.
        :param group_id: Group ID (for group messages with group access token)
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'messages.getByConversationMessageId'
        param_aliases = []
        response_type = responses.MessagesGetByConversationMessageId
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_by_id(self, message_ids: List[int] = None, preview_length: int = None, extended: bool = None, fields: List[Union[objects.UsersFields, str]] = None, group_id: int = None) -> Union[responses.MessagesGetById, responses.MessagesGetByIdExtended]:
        """
        Returns messages by their IDs.
        
        :param message_ids: Message IDs.
        :param preview_length: Number of characters after which to truncate a previewed message. To preview the full message, specify '0'. "NOTE: Messages are not truncated by default. Messages are truncated by words."
        :param extended: Information whether the response should be extended
        :param fields: Profile fields to return.
        :param group_id: Group ID (for group messages with group access token)
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'messages.getById'
        param_aliases = []
        if not extended:
            response_type = responses.MessagesGetById
        else:
            response_type = responses.MessagesGetByIdExtended
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_chat_preview(self, peer_id: int = None, link: str = None, fields: List[Union[objects.UsersFields, str]] = None) -> responses.MessagesGetChatPreview:
        """
        :param peer_id: 
        :param link: Invitation link.
        :param fields: Profile fields to return.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'messages.getChatPreview'
        param_aliases = []
        response_type = responses.MessagesGetChatPreview
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_conversation_members(self, peer_id: int = None, fields: List[Union[objects.UsersFields, str]] = None, group_id: int = None) -> responses.MessagesGetConversationMembers:
        """
        Returns a list of IDs of users participating in a chat.
        
        :param peer_id: Peer ID.
        :param fields: Profile fields to return.
        :param group_id: Group ID (for group messages with group access token)
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'messages.getConversationMembers'
        param_aliases = []
        response_type = responses.MessagesGetConversationMembers
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_conversations(self, offset: int = None, count: int = None, filter_: str = None, extended: bool = None, start_message_id: int = None, fields: List[Union[objects.BaseUserGroupFields, str]] = None, group_id: int = None) -> responses.MessagesGetConversations:
        """
        Returns a list of the current user's conversations.
        
        :param offset: Offset needed to return a specific subset of conversations.
        :param count: Number of conversations to return.
        :param filter_: Filter to apply: 'all' — all conversations, 'unread' — conversations with unread messages, 'important' — conversations, marked as important (only for community messages), 'unanswered' — conversations, marked as unanswered (only for community messages)
        :param extended: '1' — return extra information about users and communities
        :param start_message_id: ID of the message from what to return dialogs.
        :param fields: Profile and communities fields to return.
        :param group_id: Group ID (for group messages with group access token)
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'messages.getConversations'
        param_aliases = [('filter_', 'filter')]
        response_type = responses.MessagesGetConversations
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_conversations_by_id(self, peer_ids: List[int] = None, extended: bool = None, fields: List[Union[objects.BaseUserGroupFields, str]] = None, group_id: int = None) -> Union[responses.MessagesGetConversationsById, responses.MessagesGetConversationsByIdExtended]:
        """
        Returns conversations by their IDs
        
        :param peer_ids: Destination IDs. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param extended: Return extended properties
        :param fields: Profile and communities fields to return.
        :param group_id: Group ID (for group messages with group access token)
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'messages.getConversationsById'
        param_aliases = []
        if not extended:
            response_type = responses.MessagesGetConversationsById
        else:
            response_type = responses.MessagesGetConversationsByIdExtended
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_history(self, offset: int = None, count: int = None, user_id: int = None, peer_id: int = None, start_message_id: int = None, rev: int = None, extended: bool = None, fields: List[Union[objects.UsersFields, str]] = None, group_id: int = None) -> responses.MessagesGetHistory:
        """
        Returns message history for the specified user or group chat.
        
        :param offset: Offset needed to return a specific subset of messages.
        :param count: Number of messages to return.
        :param user_id: ID of the user whose message history you want to return.
        :param peer_id: 
        :param start_message_id: Starting message ID from which to return history.
        :param rev: Sort order: '1' — return messages in chronological order. '0' — return messages in reverse chronological order.
        :param extended: Information whether the response should be extended
        :param fields: Profile fields to return.
        :param group_id: Group ID (for group messages with group access token)
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'messages.getHistory'
        param_aliases = []
        response_type = responses.MessagesGetHistory
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_history_attachments(self, peer_id: int = None, media_type: str = None, start_from: str = None, count: int = None, photo_sizes: bool = None, fields: List[Union[objects.UsersFields, str]] = None, group_id: int = None, preserve_order: bool = None, max_forwards_level: int = None) -> responses.MessagesGetHistoryAttachments:
        """
        Returns media files from the dialog or group chat.
        
        :param peer_id: Peer ID. ", For group chat: '2000000000 + chat ID' , , For community: '-community ID'"
        :param media_type: Type of media files to return: *'photo',, *'video',, *'audio',, *'doc',, *'link'.,*'market'.,*'wall'.,*'share'
        :param start_from: Message ID to start return results from.
        :param count: Number of objects to return.
        :param photo_sizes: '1' — to return photo sizes in a
        :param fields: Additional profile [vk.com/dev/fields|fields] to return. 
        :param group_id: Group ID (for group messages with group access token)
        :param preserve_order: 
        :param max_forwards_level: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'messages.getHistoryAttachments'
        param_aliases = []
        response_type = responses.MessagesGetHistoryAttachments
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_invite_link(self, peer_id: int = None, reset: bool = None, group_id: int = None) -> responses.MessagesGetInviteLink:
        """
        :param peer_id: Destination ID.
        :param reset: 1 — to generate new link (revoke previous), 0 — to return previous link.
        :param group_id: Group ID
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'messages.getInviteLink'
        param_aliases = []
        response_type = responses.MessagesGetInviteLink
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_last_activity(self, user_id: int = None) -> responses.MessagesGetLastActivity:
        """
        Returns a user's current status and date of last activity.
        
        :param user_id: User ID.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'messages.getLastActivity'
        param_aliases = []
        response_type = responses.MessagesGetLastActivity
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_long_poll_history(self, ts: int = None, pts: int = None, preview_length: int = None, onlines: bool = None, fields: List[Union[objects.UsersFields, str]] = None, events_limit: int = None, msgs_limit: int = None, max_msg_id: int = None, group_id: int = None, lp_version: int = None, last_n: int = None, credentials: bool = None) -> responses.MessagesGetLongPollHistory:
        """
        Returns updates in user's private messages.
        
        :param ts: Last value of the 'ts' parameter returned from the Long Poll server or by using [vk.com/dev/messages.getLongPollHistory|messages.getLongPollHistory] method.
        :param pts: Lsat value of 'pts' parameter returned from the Long Poll server or by using [vk.com/dev/messages.getLongPollHistory|messages.getLongPollHistory] method.
        :param preview_length: Number of characters after which to truncate a previewed message. To preview the full message, specify '0'. "NOTE: Messages are not truncated by default. Messages are truncated by words."
        :param onlines: '1' — to return history with online users only.
        :param fields: Additional profile [vk.com/dev/fields|fields] to return.
        :param events_limit: Maximum number of events to return.
        :param msgs_limit: Maximum number of messages to return.
        :param max_msg_id: Maximum ID of the message among existing ones in the local copy. Both messages received with API methods (for example, , ), and data received from a Long Poll server (events with code 4) are taken into account.
        :param group_id: Group ID (for group messages with user access token)
        :param lp_version: 
        :param last_n: 
        :param credentials: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'messages.getLongPollHistory'
        param_aliases = []
        response_type = responses.MessagesGetLongPollHistory
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_long_poll_server(self, need_pts: bool = None, group_id: int = None, lp_version: int = None) -> responses.MessagesGetLongPollServer:
        """
        Returns data required for connection to a Long Poll server.
        
        :param need_pts: '1' — to return the 'pts' field, needed for the [vk.com/dev/messages.getLongPollHistory|messages.getLongPollHistory] method.
        :param group_id: Group ID (for group messages with user access token)
        :param lp_version: Long poll version
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'messages.getLongPollServer'
        param_aliases = []
        response_type = responses.MessagesGetLongPollServer
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def is_messages_from_group_allowed(self, group_id: int = None, user_id: int = None) -> responses.MessagesIsMessagesFromGroupAllowed:
        """
        Returns information whether sending messages from the community to current user is allowed.
        
        :param group_id: Group ID.
        :param user_id: User ID.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'messages.isMessagesFromGroupAllowed'
        param_aliases = []
        response_type = responses.MessagesIsMessagesFromGroupAllowed
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def join_chat_by_invite_link(self, link: str = None) -> responses.MessagesJoinChatByInviteLink:
        """
        :param link: Invitation link.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'messages.joinChatByInviteLink'
        param_aliases = []
        response_type = responses.MessagesJoinChatByInviteLink
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def mark_as_answered_conversation(self, peer_id: int = None, answered: bool = None, group_id: int = None) -> responses.BaseOk:
        """
        Marks and unmarks conversations as unanswered.
        
        :param peer_id: ID of conversation to mark as important.
        :param answered: '1' — to mark as answered, '0' — to remove the mark
        :param group_id: Group ID (for group messages with group access token)
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'messages.markAsAnsweredConversation'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def mark_as_important(self, message_ids: List[int] = None, important: int = None) -> responses.MessagesMarkAsImportant:
        """
        Marks and unmarks messages as important (starred).
        
        :param message_ids: IDs of messages to mark as important.
        :param important: '1' — to add a star (mark as important), '0' — to remove the star
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'messages.markAsImportant'
        param_aliases = []
        response_type = responses.MessagesMarkAsImportant
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def mark_as_important_conversation(self, peer_id: int = None, important: bool = None, group_id: int = None) -> responses.BaseOk:
        """
        Marks and unmarks conversations as important.
        
        :param peer_id: ID of conversation to mark as important.
        :param important: '1' — to add a star (mark as important), '0' — to remove the star
        :param group_id: Group ID (for group messages with group access token)
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'messages.markAsImportantConversation'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def mark_as_read(self, message_ids: List[int] = None, peer_id: int = None, start_message_id: int = None, group_id: int = None, mark_conversation_as_read: bool = None) -> responses.BaseOk:
        """
        Marks messages as read.
        
        :param message_ids: IDs of messages to mark as read.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param start_message_id: Message ID to start from.
        :param group_id: Group ID (for group messages with user access token)
        :param mark_conversation_as_read: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'messages.markAsRead'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def pin(self, peer_id: int = None, message_id: int = None) -> responses.MessagesPin:
        """
        Pin a message.
        
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'Chat ID', e.g. '2000000001'. For community: '- Community ID', e.g. '-12345'. "
        :param message_id: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'messages.pin'
        param_aliases = []
        response_type = responses.MessagesPin
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def remove_chat_user(self, chat_id: int = None, user_id: int = None, member_id: int = None) -> responses.BaseOk:
        """
        Allows the current user to leave a chat or, if the current user started the chat, allows the user to remove another user from the chat.
        
        :param chat_id: Chat ID.
        :param user_id: ID of the user to be removed from the chat.
        :param member_id: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'messages.removeChatUser'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def restore(self, message_id: int = None, group_id: int = None) -> responses.BaseOk:
        """
        Restores a deleted message.
        
        :param message_id: ID of a previously-deleted message to restore.
        :param group_id: Group ID (for group messages with user access token)
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'messages.restore'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def search(self, q: str = None, peer_id: int = None, date: int = None, preview_length: int = None, offset: int = None, count: int = None, extended: bool = None, fields: List[str] = None, group_id: int = None) -> responses.MessagesSearch:
        """
        Returns a list of the current user's private messages that match search criteria.
        
        :param q: Search query string.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param date: Date to search message before in Unixtime.
        :param preview_length: Number of characters after which to truncate a previewed message. To preview the full message, specify '0'. "NOTE: Messages are not truncated by default. Messages are truncated by words."
        :param offset: Offset needed to return a specific subset of messages.
        :param count: Number of messages to return.
        :param extended: 
        :param fields: 
        :param group_id: Group ID (for group messages with group access token)
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'messages.search'
        param_aliases = []
        response_type = responses.MessagesSearch
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def search_conversations(self, q: str = None, count: int = None, extended: bool = None, fields: List[Union[objects.UsersFields, str]] = None, group_id: int = None) -> responses.MessagesSearchConversations:
        """
        Returns a list of the current user's conversations that match search criteria.
        
        :param q: Search query string.
        :param count: Maximum number of results.
        :param extended: '1' — return extra information about users and communities
        :param fields: Profile fields to return.
        :param group_id: Group ID (for group messages with user access token)
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'messages.searchConversations'
        param_aliases = []
        response_type = responses.MessagesSearchConversations
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def send(self, user_id: int = None, random_id: int = None, peer_id: int = None, domain: str = None, chat_id: int = None, user_ids: List[int] = None, message: str = None, lat: float = None, long: float = None, attachment: str = None, reply_to: int = None, forward_messages: List[int] = None, sticker_id: int = None, group_id: int = None, keyboard: Union[objects.MessagesKeyboard, dict] = None, payload: str = None, dont_parse_links: bool = None, disable_mentions: bool = None, intent: str = None, subscribe_id: int = None) -> Union[responses.MessagesSend, responses.MessagesSendUserIds]:
        """
        Sends a message.
        
        :param user_id: User ID (by default — current user).
        :param random_id: Unique identifier to avoid resending the message.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param domain: User's short address (for example, 'illarionov').
        :param chat_id: ID of conversation the message will relate to.
        :param user_ids: IDs of message recipients (if new conversation shall be started).
        :param message: (Required if 'attachments' is not set.) Text of the message.
        :param lat: Geographical latitude of a check-in, in degrees (from -90 to 90).
        :param long: Geographical longitude of a check-in, in degrees (from -180 to 180).
        :param attachment: (Required if 'message' is not set.) List of objects attached to the message, separated by commas, in the following format: "<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, 'wall' — wall post, '<owner_id>' — ID of the media attachment owner. '<media_id>' — media attachment ID. Example: "photo100172_166443618"
        :param reply_to: 
        :param forward_messages: ID of forwarded messages, separated with a comma. Listed messages of the sender will be shown in the message body at the recipient's. Example: "123,431,544"
        :param sticker_id: Sticker id.
        :param group_id: Group ID (for group messages with group access token)
        :param keyboard: 
        :param payload: 
        :param dont_parse_links: 
        :param disable_mentions: 
        :param intent: 
        :param subscribe_id: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'messages.send'
        param_aliases = []
        if not user_ids:
            response_type = responses.MessagesSend
        else:
            response_type = responses.MessagesSendUserIds
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def set_activity(self, user_id: int = None, type_: str = None, peer_id: int = None, group_id: int = None) -> responses.BaseOk:
        """
        Changes the status of a user as typing in a conversation.
        
        :param user_id: User ID.
        :param type_: 'typing' — user has started to type.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param group_id: Group ID (for group messages with group access token)
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'messages.setActivity'
        param_aliases = [('type_', 'type')]
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def set_chat_photo(self, file: str = None) -> responses.MessagesSetChatPhoto:
        """
        Sets a previously-uploaded picture as the cover picture of a chat.
        
        :param file: Upload URL from the 'response' field returned by the [vk.com/dev/photos.getChatUploadServer|photos.getChatUploadServer] method upon successfully uploading an image.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'messages.setChatPhoto'
        param_aliases = []
        response_type = responses.MessagesSetChatPhoto
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def unpin(self, peer_id: int = None, group_id: int = None) -> responses.BaseOk:
        """
        :param peer_id: 
        :param group_id: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'messages.unpin'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

