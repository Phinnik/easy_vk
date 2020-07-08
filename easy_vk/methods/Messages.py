from ._ApiMethod import ApiMethod
from typing import List


class Messages(ApiMethod):
    def __init__(self, session, access_token, v, requests_per_s):
        super().__init__(session, access_token, v, requests_per_s)

    def add_chat_user(self, chat_id: int, user_id: int = None, visible_messages_count: int = None):
        """
        Adds a new user to a chat.
        
        :param chat_id: Chat ID.
        :param user_id: ID of the user to be added to the chat.
        :param visible_messages_count: 
        """
    
        method_name = 'messages.addChatUser'
        return self._call(method_name, locals())

    def allow_messages_from_group(self, group_id: int, key: str = None):
        """
        Allows sending messages from community to the current user.
        
        :param group_id: Group ID.
        :param key: 
        """
    
        method_name = 'messages.allowMessagesFromGroup'
        return self._call(method_name, locals())

    def create_chat(self, user_ids: List[int] = None, title: str = None, group_id: int = None):
        """
        Creates a chat with several participants.
        
        :param user_ids: IDs of the users to be added to the chat.
        :param title: Chat title.
        :param group_id: 
        """
    
        if user_ids:
            user_ids = [str(u) for u in user_ids]
            user_ids = ','.join(user_ids)
        
        method_name = 'messages.createChat'
        return self._call(method_name, locals())

    def delete(self, message_ids: List[int] = None, spam: bool = None, group_id: int = None, delete_for_all: bool = None):
        """
        Deletes one or more messages.
        
        :param message_ids: Message IDs.
        :param spam: '1' — to mark message as spam.
        :param group_id: Group ID (for group messages with user access token)
        :param delete_for_all: '1' — delete message for for all.
        """
    
        if message_ids:
            message_ids = [str(m) for m in message_ids]
            message_ids = ','.join(message_ids)
        
        method_name = 'messages.delete'
        return self._call(method_name, locals())

    def delete_chat_photo(self, chat_id: int, group_id: int = None):
        """
        Deletes a chat's cover picture.
        
        :param chat_id: Chat ID.
        :param group_id: 
        """
    
        method_name = 'messages.deleteChatPhoto'
        return self._call(method_name, locals())

    def delete_conversation(self, user_id: int = None, peer_id: int = None, group_id: int = None):
        """
        Deletes all private messages in a conversation.
        
        :param user_id: User ID. To clear a chat history use 'chat_id'
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param group_id: Group ID (for group messages with user access token)
        """
    
        method_name = 'messages.deleteConversation'
        return self._call(method_name, locals())

    def deny_messages_from_group(self, group_id: int):
        """
        Denies sending message from community to the current user.
        
        :param group_id: Group ID.
        """
    
        method_name = 'messages.denyMessagesFromGroup'
        return self._call(method_name, locals())

    def edit(self, peer_id: int, message: str = None, lat: float = None, long: float = None, attachment: str = None, keep_forward_messages: bool = None, keep_snippets: bool = None, group_id: int = None, dont_parse_links: bool = None, message_id: int = None):
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
        """
    
        method_name = 'messages.edit'
        return self._call(method_name, locals())

    def edit_chat(self, chat_id: int, title: str):
        """
        Edits the title of a chat.
        
        :param chat_id: Chat ID.
        :param title: New title of the chat.
        """
    
        method_name = 'messages.editChat'
        return self._call(method_name, locals())

    def get_by_conversation_message_id(self, peer_id: int, conversation_message_ids: List[int], extended: bool = None, fields: List[str] = None, group_id: int = None):
        """
        Returns messages by their IDs within the conversation.
        
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param conversation_message_ids: Conversation message IDs.
        :param extended: Information whether the response should be extended
        :param fields: Profile fields to return.
        :param group_id: Group ID (for group messages with group access token)
        """
    
        if conversation_message_ids:
            conversation_message_ids = [str(c) for c in conversation_message_ids]
            conversation_message_ids = ','.join(conversation_message_ids)
        if fields:
            fields = ','.join(fields)
        
        method_name = 'messages.getByConversationMessageId'
        return self._call(method_name, locals())

    def get_by_id(self, message_ids: List[int], preview_length: int = None, extended: bool = None, fields: List[str] = None, group_id: int = None):
        """
        Returns messages by their IDs.
        
        :param message_ids: Message IDs.
        :param preview_length: Number of characters after which to truncate a previewed message. To preview the full message, specify '0'. "NOTE: Messages are not truncated by default. Messages are truncated by words."
        :param extended: Information whether the response should be extended
        :param fields: Profile fields to return.
        :param group_id: Group ID (for group messages with group access token)
        """
    
        if message_ids:
            message_ids = [str(m) for m in message_ids]
            message_ids = ','.join(message_ids)
        if fields:
            fields = ','.join(fields)
        
        method_name = 'messages.getById'
        return self._call(method_name, locals())

    def get_chat_preview(self, peer_id: int = None, link: str = None, fields: List[str] = None):
        """
        
        :param peer_id: 
        :param link: Invitation link.
        :param fields: Profile fields to return.
        """
    
        if fields:
            fields = ','.join(fields)
        
        method_name = 'messages.getChatPreview'
        return self._call(method_name, locals())

    def get_conversation_members(self, peer_id: int, fields: List[str] = None, group_id: int = None):
        """
        Returns a list of IDs of users participating in a chat.
        
        :param peer_id: Peer ID.
        :param fields: Profile fields to return.
        :param group_id: Group ID (for group messages with group access token)
        """
    
        if fields:
            fields = ','.join(fields)
        
        method_name = 'messages.getConversationMembers'
        return self._call(method_name, locals())

    def get_conversations(self, offset: int = None, count: int = None, filter_: str = None, extended: bool = None, start_message_id: int = None, fields: List[str] = None, group_id: int = None):
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
    
        if fields:
            fields = ','.join(fields)
        
        param_alias_dict = {'filter_': 'filter'}
        method_name = 'messages.getConversations'
        return self._call(method_name, locals())

    def get_conversations_by_id(self, peer_ids: List[int], extended: bool = None, fields: List[str] = None, group_id: int = None):
        """
        Returns conversations by their IDs
        
        :param peer_ids: Destination IDs. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param extended: Return extended properties
        :param fields: Profile and communities fields to return.
        :param group_id: Group ID (for group messages with group access token)
        """
    
        if peer_ids:
            peer_ids = [str(p) for p in peer_ids]
            peer_ids = ','.join(peer_ids)
        if fields:
            fields = ','.join(fields)
        
        method_name = 'messages.getConversationsById'
        return self._call(method_name, locals())

    def get_history(self, offset: int = None, count: int = None, user_id: int = None, peer_id: int = None, start_message_id: int = None, rev: int = None, extended: bool = None, fields: List[str] = None, group_id: int = None):
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
    
        if fields:
            fields = ','.join(fields)
        
        method_name = 'messages.getHistory'
        return self._call(method_name, locals())

    def get_history_attachments(self, peer_id: int, media_type: str = None, start_from: str = None, count: int = None, photo_sizes: bool = None, fields: List[str] = None, group_id: int = None, preserve_order: bool = None, max_forwards_level: int = None):
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
    
        if fields:
            fields = ','.join(fields)
        
        method_name = 'messages.getHistoryAttachments'
        return self._call(method_name, locals())

    def get_invite_link(self, peer_id: int, reset: bool = None, group_id: int = None):
        """
        
        :param peer_id: Destination ID.
        :param reset: 1 — to generate new link (revoke previous), 0 — to return previous link.
        :param group_id: Group ID
        """
    
        method_name = 'messages.getInviteLink'
        return self._call(method_name, locals())

    def get_last_activity(self, user_id: int):
        """
        Returns a user's current status and date of last activity.
        
        :param user_id: User ID.
        """
    
        method_name = 'messages.getLastActivity'
        return self._call(method_name, locals())

    def get_long_poll_history(self, ts: int = None, pts: int = None, preview_length: int = None, onlines: bool = None, fields: List[str] = None, events_limit: int = None, msgs_limit: int = None, max_msg_id: int = None, group_id: int = None, lp_version: int = None, last_n: int = None, credentials: bool = None):
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
    
        if fields:
            fields = ','.join(fields)
        
        method_name = 'messages.getLongPollHistory'
        return self._call(method_name, locals())

    def get_long_poll_server(self, need_pts: bool = None, group_id: int = None, lp_version: int = None):
        """
        Returns data required for connection to a Long Poll server.
        
        :param need_pts: '1' — to return the 'pts' field, needed for the [vk.com/dev/messages.getLongPollHistory|messages.getLongPollHistory] method.
        :param group_id: Group ID (for group messages with user access token)
        :param lp_version: Long poll version
        """
    
        method_name = 'messages.getLongPollServer'
        return self._call(method_name, locals())

    def is_messages_from_group_allowed(self, group_id: int, user_id: int):
        """
        Returns information whether sending messages from the community to current user is allowed.
        
        :param group_id: Group ID.
        :param user_id: User ID.
        """
    
        method_name = 'messages.isMessagesFromGroupAllowed'
        return self._call(method_name, locals())

    def join_chat_by_invite_link(self, link: str):
        """
        
        :param link: Invitation link.
        """
    
        method_name = 'messages.joinChatByInviteLink'
        return self._call(method_name, locals())

    def mark_as_answered_conversation(self, peer_id: int, answered: bool = None, group_id: int = None):
        """
        Marks and unmarks conversations as unanswered.
        
        :param peer_id: ID of conversation to mark as important.
        :param answered: '1' — to mark as answered, '0' — to remove the mark
        :param group_id: Group ID (for group messages with group access token)
        """
    
        method_name = 'messages.markAsAnsweredConversation'
        return self._call(method_name, locals())

    def mark_as_important(self, message_ids: List[int] = None, important: int = None):
        """
        Marks and unmarks messages as important (starred).
        
        :param message_ids: IDs of messages to mark as important.
        :param important: '1' — to add a star (mark as important), '0' — to remove the star
        """
    
        if message_ids:
            message_ids = [str(m) for m in message_ids]
            message_ids = ','.join(message_ids)
        
        method_name = 'messages.markAsImportant'
        return self._call(method_name, locals())

    def mark_as_important_conversation(self, peer_id: int, important: bool = None, group_id: int = None):
        """
        Marks and unmarks conversations as important.
        
        :param peer_id: ID of conversation to mark as important.
        :param important: '1' — to add a star (mark as important), '0' — to remove the star
        :param group_id: Group ID (for group messages with group access token)
        """
    
        method_name = 'messages.markAsImportantConversation'
        return self._call(method_name, locals())

    def mark_as_read(self, message_ids: List[int] = None, peer_id: int = None, start_message_id: int = None, group_id: int = None):
        """
        Marks messages as read.
        
        :param message_ids: IDs of messages to mark as read.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param start_message_id: Message ID to start from.
        :param group_id: Group ID (for group messages with user access token)
        """
    
        if message_ids:
            message_ids = [str(m) for m in message_ids]
            message_ids = ','.join(message_ids)
        
        method_name = 'messages.markAsRead'
        return self._call(method_name, locals())

    def pin(self, peer_id: int, message_id: int = None):
        """
        Pin a message.
        
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'Chat ID', e.g. '2000000001'. For community: '- Community ID', e.g. '-12345'. "
        :param message_id: 
        """
    
        method_name = 'messages.pin'
        return self._call(method_name, locals())

    def remove_chat_user(self, chat_id: int, user_id: int = None, member_id: int = None):
        """
        Allows the current user to leave a chat or, if the current user started the chat, allows the user to remove another user from the chat.
        
        :param chat_id: Chat ID.
        :param user_id: ID of the user to be removed from the chat.
        :param member_id: 
        """
    
        method_name = 'messages.removeChatUser'
        return self._call(method_name, locals())

    def restore(self, message_id: int, group_id: int = None):
        """
        Restores a deleted message.
        
        :param message_id: ID of a previously-deleted message to restore.
        :param group_id: Group ID (for group messages with user access token)
        """
    
        method_name = 'messages.restore'
        return self._call(method_name, locals())

    def search(self, q: str = None, peer_id: int = None, date: int = None, preview_length: int = None, offset: int = None, count: int = None, extended: bool = None, fields: List[str] = None, group_id: int = None):
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
    
        if fields:
            fields = ','.join(fields)
        
        method_name = 'messages.search'
        return self._call(method_name, locals())

    def search_conversations(self, q: str = None, count: int = None, extended: bool = None, fields: List[str] = None, group_id: int = None):
        """
        Returns a list of the current user's conversations that match search criteria.
        
        :param q: Search query string.
        :param count: Maximum number of results.
        :param extended: '1' — return extra information about users and communities
        :param fields: Profile fields to return.
        :param group_id: Group ID (for group messages with user access token)
        """
    
        if fields:
            fields = ','.join(fields)
        
        method_name = 'messages.searchConversations'
        return self._call(method_name, locals())

    def send(self, user_id: int = None, random_id: int = None, peer_id: int = None, domain: str = None, chat_id: int = None, user_ids: List[int] = None, message: str = None, lat: float = None, long: float = None, attachment: str = None, reply_to: int = None, forward_messages: List[int] = None, sticker_id: int = None, group_id: int = None, keyboard: str = None, payload: str = None, dont_parse_links: bool = None, disable_mentions: bool = None, intent: str = None):
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
        """
    
        if user_ids:
            user_ids = [str(u) for u in user_ids]
            user_ids = ','.join(user_ids)
        if forward_messages:
            forward_messages = [str(f) for f in forward_messages]
            forward_messages = ','.join(forward_messages)
        
        method_name = 'messages.send'
        return self._call(method_name, locals())

    def set_activity(self, user_id: int = None, type_: str = None, peer_id: int = None, group_id: int = None):
        """
        Changes the status of a user as typing in a conversation.
        
        :param user_id: User ID.
        :param type_: 'typing' — user has started to type.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param group_id: Group ID (for group messages with group access token)
        """
    
        param_alias_dict = {'type_': 'type'}
        method_name = 'messages.setActivity'
        return self._call(method_name, locals())

    def set_chat_photo(self, file: str):
        """
        Sets a previously-uploaded picture as the cover picture of a chat.
        
        :param file: Upload URL from the 'response' field returned by the [vk.com/dev/photos.getChatUploadServer|photos.getChatUploadServer] method upon successfully uploading an image.
        """
    
        method_name = 'messages.setChatPhoto'
        return self._call(method_name, locals())

    def unpin(self, peer_id: int, group_id: int = None):
        """
        
        :param peer_id: 
        :param group_id: 
        """
    
        method_name = 'messages.unpin'
        return self._call(method_name, locals())

