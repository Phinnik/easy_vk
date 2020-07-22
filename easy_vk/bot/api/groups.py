from typing import List, Union, Optional
from easy_vk.types import objects, responses
from .base import BaseCategory


class Groups(BaseCategory):
    def __init__(self, session, access_token: str, v: str, delay: float, auto_retry: bool, max_retries: int, timeout: float):
        super().__init__(session, access_token, v, delay, auto_retry, max_retries, timeout)

    def add_address(self, group_id: int = None, title: str = None, address: str = None, additional_address: str = None, country_id: int = None, city_id: int = None, metro_id: int = None, latitude: float = None, longitude: float = None, phone: str = None, work_info_status: Union[objects.GroupsAddressWorkInfoStatus, str] = None, timetable: str = None, is_main_address: bool = None) -> responses.GroupsAddAddress:
        """
        :param group_id: 
        :param title: 
        :param address: 
        :param additional_address: 
        :param country_id: 
        :param city_id: 
        :param metro_id: 
        :param latitude: 
        :param longitude: 
        :param phone: 
        :param work_info_status: 
        :param timetable: 
        :param is_main_address: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'groups.addAddress'
        param_aliases = []
        response_type = responses.GroupsAddAddress
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def add_callback_server(self, group_id: int = None, url: str = None, title: str = None, secret_key: str = None) -> responses.GroupsAddCallbackServer:
        """
        :param group_id: 
        :param url: 
        :param title: 
        :param secret_key: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'groups.addCallbackServer'
        param_aliases = []
        response_type = responses.GroupsAddCallbackServer
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def delete_callback_server(self, group_id: int = None, server_id: int = None) -> responses.BaseOk:
        """
        :param group_id: 
        :param server_id: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'groups.deleteCallbackServer'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def disable_online(self, group_id: int = None) -> responses.BaseOk:
        """
        :param group_id: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'groups.disableOnline'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def edit_address(self, group_id: int = None, address_id: int = None, title: str = None, address: str = None, additional_address: str = None, country_id: int = None, city_id: int = None, metro_id: int = None, latitude: float = None, longitude: float = None, phone: str = None, work_info_status: Union[objects.GroupsAddressWorkInfoStatus, str] = None, timetable: str = None, is_main_address: bool = None) -> responses.GroupsEditAddress:
        """
        :param group_id: 
        :param address_id: 
        :param title: 
        :param address: 
        :param additional_address: 
        :param country_id: 
        :param city_id: 
        :param metro_id: 
        :param latitude: 
        :param longitude: 
        :param phone: 
        :param work_info_status: 
        :param timetable: 
        :param is_main_address: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'groups.editAddress'
        param_aliases = []
        response_type = responses.GroupsEditAddress
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def edit_callback_server(self, group_id: int = None, server_id: int = None, url: str = None, title: str = None, secret_key: str = None) -> responses.BaseOk:
        """
        :param group_id: 
        :param server_id: 
        :param url: 
        :param title: 
        :param secret_key: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'groups.editCallbackServer'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def enable_online(self, group_id: int = None) -> responses.BaseOk:
        """
        :param group_id: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'groups.enableOnline'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_banned(self, group_id: int = None, offset: int = None, count: int = None, fields: List[Union[objects.BaseUserGroupFields, str]] = None, owner_id: int = None) -> responses.GroupsGetBanned:
        """
        Returns a list of users on a community blacklist.
        
        :param group_id: Community ID.
        :param offset: Offset needed to return a specific subset of users.
        :param count: Number of users to return.
        :param fields: 
        :param owner_id: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'groups.getBanned'
        param_aliases = []
        response_type = responses.GroupsGetBanned
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_by_id(self, group_ids: List[str] = None, group_id: str = None, fields: List[Union[objects.GroupsFields, str]] = None) -> responses.GroupsGetById:
        """
        Returns information about communities by their IDs.
        
        :param group_ids: IDs or screen names of communities.
        :param group_id: ID or screen name of the community.
        :param fields: Group fields to return.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'groups.getById'
        param_aliases = []
        response_type = responses.GroupsGetById
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_callback_confirmation_code(self, group_id: int = None) -> responses.GroupsGetCallbackConfirmationCode:
        """
        Returns Callback API confirmation code for the community.
        
        :param group_id: Community ID.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'groups.getCallbackConfirmationCode'
        param_aliases = []
        response_type = responses.GroupsGetCallbackConfirmationCode
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_callback_servers(self, group_id: int = None, server_ids: List[int] = None) -> responses.GroupsGetCallbackServers:
        """
        :param group_id: 
        :param server_ids: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'groups.getCallbackServers'
        param_aliases = []
        response_type = responses.GroupsGetCallbackServers
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_callback_settings(self, group_id: int = None, server_id: int = None) -> responses.GroupsGetCallbackSettings:
        """
        Returns [vk.com/dev/callback_api|Callback API] notifications settings.
        
        :param group_id: Community ID.
        :param server_id: Server ID.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'groups.getCallbackSettings'
        param_aliases = []
        response_type = responses.GroupsGetCallbackSettings
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_long_poll_server(self, group_id: int = None) -> responses.GroupsGetLongPollServer:
        """
        Returns the data needed to query a Long Poll server for events
        
        :param group_id: Community ID
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'groups.getLongPollServer'
        param_aliases = []
        response_type = responses.GroupsGetLongPollServer
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_long_poll_settings(self, group_id: int = None) -> responses.GroupsGetLongPollSettings:
        """
        Returns Long Poll notification settings
        
        :param group_id: Community ID.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'groups.getLongPollSettings'
        param_aliases = []
        response_type = responses.GroupsGetLongPollSettings
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_members(self, group_id: str = None, sort: str = None, offset: int = None, count: int = None, fields: List[Union[objects.UsersFields, str]] = None, filter_: str = None) -> Union[responses.GroupsGetMembers, responses.GroupsGetMembersFields, responses.GroupsGetMembersFilter]:
        """
        Returns a list of community members.
        
        :param group_id: ID or screen name of the community.
        :param sort: Sort order. Available values: 'id_asc', 'id_desc', 'time_asc', 'time_desc'. 'time_asc' and 'time_desc' are availavle only if the method is called by the group's 'moderator'.
        :param offset: Offset needed to return a specific subset of community members.
        :param count: Number of community members to return.
        :param fields: List of additional fields to be returned. Available values: 'sex, bdate, city, country, photo_50, photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig, online, online_mobile, lists, domain, has_mobile, contacts, connections, site, education, universities, schools, can_post, can_see_all_posts, can_see_audio, can_write_private_message, status, last_seen, common_count, relation, relatives, counters'.
        :param filter_: *'friends' – only friends in this community will be returned,, *'unsure' – only those who pressed 'I may attend' will be returned (if it's an event).
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'groups.getMembers'
        param_aliases = [('filter_', 'filter')]
        if not filter_ and not fields:
            response_type = responses.GroupsGetMembers
        elif fields and not filter_:
            response_type = responses.GroupsGetMembersFields
        else:
            response_type = responses.GroupsGetMembersFilter
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_token_permissions(self) -> responses.GroupsGetTokenPermissions:
        
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'groups.getTokenPermissions'
        param_aliases = []
        response_type = responses.GroupsGetTokenPermissions
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def is_member(self, group_id: str = None, user_id: int = None, user_ids: List[int] = None, extended: bool = None) -> Union[responses.GroupsIsMember, responses.GroupsIsMemberUserIds, responses.GroupsIsMemberExtended, responses.GroupsIsMemberUserIdsExtended]:
        """
        Returns information specifying whether a user is a member of a community.
        
        :param group_id: ID or screen name of the community.
        :param user_id: User ID.
        :param user_ids: User IDs.
        :param extended: '1' — to return an extended response with additional fields. By default: '0'.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'groups.isMember'
        param_aliases = []
        if not extended and not user_ids:
            response_type = responses.GroupsIsMember
        elif user_ids and not extended:
            response_type = responses.GroupsIsMemberUserIds
        elif extended and not user_ids:
            response_type = responses.GroupsIsMemberExtended
        else:
            response_type = responses.GroupsIsMemberUserIdsExtended
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def set_callback_settings(self, group_id: int = None, server_id: int = None, api_version: str = None, message_new: bool = None, message_reply: bool = None, message_allow: bool = None, message_edit: bool = None, message_deny: bool = None, message_typing_state: bool = None, photo_new: bool = None, audio_new: bool = None, video_new: bool = None, wall_reply_new: bool = None, wall_reply_edit: bool = None, wall_reply_delete: bool = None, wall_reply_restore: bool = None, wall_post_new: bool = None, wall_repost: bool = None, board_post_new: bool = None, board_post_edit: bool = None, board_post_restore: bool = None, board_post_delete: bool = None, photo_comment_new: bool = None, photo_comment_edit: bool = None, photo_comment_delete: bool = None, photo_comment_restore: bool = None, video_comment_new: bool = None, video_comment_edit: bool = None, video_comment_delete: bool = None, video_comment_restore: bool = None, market_comment_new: bool = None, market_comment_edit: bool = None, market_comment_delete: bool = None, market_comment_restore: bool = None, poll_vote_new: bool = None, group_join: bool = None, group_leave: bool = None, group_change_settings: bool = None, group_change_photo: bool = None, group_officers_edit: bool = None, user_block: bool = None, user_unblock: bool = None, lead_forms_new: bool = None, like_add: bool = None, like_remove: bool = None, message_event: bool = None) -> responses.BaseOk:
        """
        Allow to set notifications settings for group.
        
        :param group_id: Community ID.
        :param server_id: Server ID.
        :param api_version: 
        :param message_new: A new incoming message has been received ('0' — disabled, '1' — enabled).
        :param message_reply: A new outcoming message has been received ('0' — disabled, '1' — enabled).
        :param message_allow: Allowed messages notifications ('0' — disabled, '1' — enabled).
        :param message_edit: 
        :param message_deny: Denied messages notifications ('0' — disabled, '1' — enabled).
        :param message_typing_state: 
        :param photo_new: New photos notifications ('0' — disabled, '1' — enabled).
        :param audio_new: New audios notifications ('0' — disabled, '1' — enabled).
        :param video_new: New videos notifications ('0' — disabled, '1' — enabled).
        :param wall_reply_new: New wall replies notifications ('0' — disabled, '1' — enabled).
        :param wall_reply_edit: Wall replies edited notifications ('0' — disabled, '1' — enabled).
        :param wall_reply_delete: A wall comment has been deleted ('0' — disabled, '1' — enabled).
        :param wall_reply_restore: A wall comment has been restored ('0' — disabled, '1' — enabled).
        :param wall_post_new: New wall posts notifications ('0' — disabled, '1' — enabled).
        :param wall_repost: New wall posts notifications ('0' — disabled, '1' — enabled).
        :param board_post_new: New board posts notifications ('0' — disabled, '1' — enabled).
        :param board_post_edit: Board posts edited notifications ('0' — disabled, '1' — enabled).
        :param board_post_restore: Board posts restored notifications ('0' — disabled, '1' — enabled).
        :param board_post_delete: Board posts deleted notifications ('0' — disabled, '1' — enabled).
        :param photo_comment_new: New comment to photo notifications ('0' — disabled, '1' — enabled).
        :param photo_comment_edit: A photo comment has been edited ('0' — disabled, '1' — enabled).
        :param photo_comment_delete: A photo comment has been deleted ('0' — disabled, '1' — enabled).
        :param photo_comment_restore: A photo comment has been restored ('0' — disabled, '1' — enabled).
        :param video_comment_new: New comment to video notifications ('0' — disabled, '1' — enabled).
        :param video_comment_edit: A video comment has been edited ('0' — disabled, '1' — enabled).
        :param video_comment_delete: A video comment has been deleted ('0' — disabled, '1' — enabled).
        :param video_comment_restore: A video comment has been restored ('0' — disabled, '1' — enabled).
        :param market_comment_new: New comment to market item notifications ('0' — disabled, '1' — enabled).
        :param market_comment_edit: A market comment has been edited ('0' — disabled, '1' — enabled).
        :param market_comment_delete: A market comment has been deleted ('0' — disabled, '1' — enabled).
        :param market_comment_restore: A market comment has been restored ('0' — disabled, '1' — enabled).
        :param poll_vote_new: A vote in a public poll has been added ('0' — disabled, '1' — enabled).
        :param group_join: Joined community notifications ('0' — disabled, '1' — enabled).
        :param group_leave: Left community notifications ('0' — disabled, '1' — enabled).
        :param group_change_settings: 
        :param group_change_photo: 
        :param group_officers_edit: 
        :param user_block: User added to community blacklist
        :param user_unblock: User removed from community blacklist
        :param lead_forms_new: New form in lead forms
        :param like_add: 
        :param like_remove: 
        :param message_event: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'groups.setCallbackSettings'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def set_long_poll_settings(self, group_id: int = None, enabled: bool = None, api_version: str = None, message_new: bool = None, message_reply: bool = None, message_allow: bool = None, message_deny: bool = None, message_edit: bool = None, message_typing_state: bool = None, photo_new: bool = None, audio_new: bool = None, video_new: bool = None, wall_reply_new: bool = None, wall_reply_edit: bool = None, wall_reply_delete: bool = None, wall_reply_restore: bool = None, wall_post_new: bool = None, wall_repost: bool = None, board_post_new: bool = None, board_post_edit: bool = None, board_post_restore: bool = None, board_post_delete: bool = None, photo_comment_new: bool = None, photo_comment_edit: bool = None, photo_comment_delete: bool = None, photo_comment_restore: bool = None, video_comment_new: bool = None, video_comment_edit: bool = None, video_comment_delete: bool = None, video_comment_restore: bool = None, market_comment_new: bool = None, market_comment_edit: bool = None, market_comment_delete: bool = None, market_comment_restore: bool = None, poll_vote_new: bool = None, group_join: bool = None, group_leave: bool = None, group_change_settings: bool = None, group_change_photo: bool = None, group_officers_edit: bool = None, user_block: bool = None, user_unblock: bool = None, like_add: bool = None, like_remove: bool = None, message_event: bool = None) -> responses.BaseOk:
        """
        Sets Long Poll notification settings
        
        :param group_id: Community ID.
        :param enabled: Sets whether Long Poll is enabled ('0' — disabled, '1' — enabled).
        :param api_version: 
        :param message_new: A new incoming message has been received ('0' — disabled, '1' — enabled).
        :param message_reply: A new outcoming message has been received ('0' — disabled, '1' — enabled).
        :param message_allow: Allowed messages notifications ('0' — disabled, '1' — enabled).
        :param message_deny: Denied messages notifications ('0' — disabled, '1' — enabled).
        :param message_edit: A message has been edited ('0' — disabled, '1' — enabled).
        :param message_typing_state: 
        :param photo_new: New photos notifications ('0' — disabled, '1' — enabled).
        :param audio_new: New audios notifications ('0' — disabled, '1' — enabled).
        :param video_new: New videos notifications ('0' — disabled, '1' — enabled).
        :param wall_reply_new: New wall replies notifications ('0' — disabled, '1' — enabled).
        :param wall_reply_edit: Wall replies edited notifications ('0' — disabled, '1' — enabled).
        :param wall_reply_delete: A wall comment has been deleted ('0' — disabled, '1' — enabled).
        :param wall_reply_restore: A wall comment has been restored ('0' — disabled, '1' — enabled).
        :param wall_post_new: New wall posts notifications ('0' — disabled, '1' — enabled).
        :param wall_repost: New wall posts notifications ('0' — disabled, '1' — enabled).
        :param board_post_new: New board posts notifications ('0' — disabled, '1' — enabled).
        :param board_post_edit: Board posts edited notifications ('0' — disabled, '1' — enabled).
        :param board_post_restore: Board posts restored notifications ('0' — disabled, '1' — enabled).
        :param board_post_delete: Board posts deleted notifications ('0' — disabled, '1' — enabled).
        :param photo_comment_new: New comment to photo notifications ('0' — disabled, '1' — enabled).
        :param photo_comment_edit: A photo comment has been edited ('0' — disabled, '1' — enabled).
        :param photo_comment_delete: A photo comment has been deleted ('0' — disabled, '1' — enabled).
        :param photo_comment_restore: A photo comment has been restored ('0' — disabled, '1' — enabled).
        :param video_comment_new: New comment to video notifications ('0' — disabled, '1' — enabled).
        :param video_comment_edit: A video comment has been edited ('0' — disabled, '1' — enabled).
        :param video_comment_delete: A video comment has been deleted ('0' — disabled, '1' — enabled).
        :param video_comment_restore: A video comment has been restored ('0' — disabled, '1' — enabled).
        :param market_comment_new: New comment to market item notifications ('0' — disabled, '1' — enabled).
        :param market_comment_edit: A market comment has been edited ('0' — disabled, '1' — enabled).
        :param market_comment_delete: A market comment has been deleted ('0' — disabled, '1' — enabled).
        :param market_comment_restore: A market comment has been restored ('0' — disabled, '1' — enabled).
        :param poll_vote_new: A vote in a public poll has been added ('0' — disabled, '1' — enabled).
        :param group_join: Joined community notifications ('0' — disabled, '1' — enabled).
        :param group_leave: Left community notifications ('0' — disabled, '1' — enabled).
        :param group_change_settings: 
        :param group_change_photo: 
        :param group_officers_edit: 
        :param user_block: User added to community blacklist
        :param user_unblock: User removed from community blacklist
        :param like_add: 
        :param like_remove: 
        :param message_event: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'groups.setLongPollSettings'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)
