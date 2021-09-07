# This file was autogenerated from vk-api json schema

from typing import List, Union, Optional, overload
from easy_vk.types import objects
from easy_vk.types import responses
from easy_vk.api_category import BaseCategory
try:
    from typing import Literal
except Exception:
    from typing_extensions import Literal


class Groups(BaseCategory):
    def add_address(self, group_id: int, title: str, address: str, country_id: int, city_id: int, latitude: float, longitude: float, additional_address: Optional[str] = None, metro_id: Optional[int] = None, phone: Optional[str] = None, work_info_status: Optional[str] = None, timetable: Optional[str] = None, is_main_address: Optional[bool] = None) -> responses.GroupsAddAddress:
        """
        :param group_id:
        :param title:
        :param address:
        :param country_id:
        :param city_id:
        :param latitude:
        :param longitude:
        :param additional_address:
        :param metro_id:
        :param phone:
        :param work_info_status:
        :param timetable:
        :param is_main_address:
        """

        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'groups.addAddress'
        response_type = responses.GroupsAddAddress
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def add_callback_server(self, group_id: int, url: str, title: str, secret_key: Optional[str] = None) -> responses.GroupsAddCallbackServer:
        """
        :param group_id:
        :param url:
        :param title:
        :param secret_key:
        """

        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'groups.addCallbackServer'
        response_type = responses.GroupsAddCallbackServer
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def delete_callback_server(self, group_id: int, server_id: int) -> responses.BaseOk:
        """
        :param group_id:
        :param server_id:
        """

        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'groups.deleteCallbackServer'
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def disable_online(self, group_id: int) -> responses.BaseOk:
        """
        :param group_id:
        """

        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'groups.disableOnline'
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def edit_address(self, group_id: int, address_id: int, title: Optional[str] = None, address: Optional[str] = None, additional_address: Optional[str] = None, country_id: Optional[int] = None, city_id: Optional[int] = None, metro_id: Optional[int] = None, latitude: Optional[float] = None, longitude: Optional[float] = None, phone: Optional[str] = None, work_info_status: Optional[str] = None, timetable: Optional[str] = None, is_main_address: Optional[bool] = None) -> responses.GroupsEditAddress:
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
        param_aliases = []
        method_name = 'groups.editAddress'
        response_type = responses.GroupsEditAddress
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def edit_callback_server(self, group_id: int, server_id: int, url: str, title: str, secret_key: Optional[str] = None) -> responses.BaseOk:
        """
        :param group_id:
        :param server_id:
        :param url:
        :param title:
        :param secret_key:
        """

        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'groups.editCallbackServer'
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def enable_online(self, group_id: int) -> responses.BaseOk:
        """
        :param group_id:
        """

        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'groups.enableOnline'
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_banned(self, group_id: int, offset: Optional[int] = None, count: Optional[int] = None, fields: Optional[List[Union[objects.BaseUserGroupFields, str]]] = None, owner_id: Optional[int] = None) -> responses.GroupsGetBanned:
        """
        Returns a list of users on a community blacklist.

        :param group_id: Community ID.
        :param offset: Offset needed to return a specific subset of users.
        :param count: Number of users to return.
        :param fields:
        :param owner_id:
        """

        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'groups.getBanned'
        response_type = responses.GroupsGetBanned
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_by_id(self, group_ids: Optional[List[str]] = None, group_id: Optional[str] = None, fields: Optional[List[Union[objects.GroupsFields, str]]] = None) -> responses.GroupsGetById:
        """
        Returns information about communities by their IDs.

        :param group_ids: IDs or screen names of communities.
        :param group_id: ID or screen name of the community.
        :param fields: Group fields to return.
        """

        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'groups.getById'
        response_type = responses.GroupsGetById
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_callback_confirmation_code(self, group_id: int) -> responses.GroupsGetCallbackConfirmationCode:
        """
        Returns Callback API confirmation code for the community.

        :param group_id: Community ID.
        """

        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'groups.getCallbackConfirmationCode'
        response_type = responses.GroupsGetCallbackConfirmationCode
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_callback_servers(self, group_id: int, server_ids: Optional[List[int]] = None) -> responses.GroupsGetCallbackServers:
        """
        :param group_id:
        :param server_ids:
        """

        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'groups.getCallbackServers'
        response_type = responses.GroupsGetCallbackServers
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_callback_settings(self, group_id: int, server_id: Optional[int] = None) -> responses.GroupsGetCallbackSettings:
        """
        Returns [vk.com/dev/callback_api|Callback API] notifications settings.

        :param group_id: Community ID.
        :param server_id: Server ID.
        """

        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'groups.getCallbackSettings'
        response_type = responses.GroupsGetCallbackSettings
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_long_poll_server(self, group_id: int) -> responses.GroupsGetLongPollServer:
        """
        Returns the data needed to query a Long Poll server for events

        :param group_id: Community ID
        """

        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'groups.getLongPollServer'
        response_type = responses.GroupsGetLongPollServer
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_long_poll_settings(self, group_id: int) -> responses.GroupsGetLongPollSettings:
        """
        Returns Long Poll notification settings

        :param group_id: Community ID.
        """

        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'groups.getLongPollSettings'
        response_type = responses.GroupsGetLongPollSettings
        return self._call(method_name, method_parameters, param_aliases, response_type)

    @overload
    def get_members(self, group_id: Optional[str] = None, sort: Optional[str] = None, offset: Optional[int] = None, count: Optional[int] = None, fields: None = None, filter_: None = None) -> responses.GroupsGetMembers: ...
    @overload
    def get_members(self, fields: List[Union[objects.UsersFields, str]], group_id: Optional[str] = None, sort: Optional[str] = None, offset: Optional[int] = None, count: Optional[int] = None, filter_: None = None) -> responses.GroupsGetMembersFields: ...
    @overload
    def get_members(self, filter_: str, group_id: Optional[str] = None, sort: Optional[str] = None, offset: Optional[int] = None, count: Optional[int] = None, fields: None = None) -> responses.GroupsGetMembersFilter: ...
    def get_members(self, group_id: Optional[str] = None, sort: Optional[str] = None, offset: Optional[int] = None, count: Optional[int] = None, fields: Optional[List[Union[objects.UsersFields, str]]] = None, filter_: Optional[str] = None):
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
        param_aliases = [('filter_', 'filter')]
        method_name = 'groups.getMembers'
        if not fields and not filter_:
            response_type = responses.GroupsGetMembers
        if fields and not filter_:
            response_type = responses.GroupsGetMembersFields
        if not fields and filter_:
            response_type = responses.GroupsGetMembersFilter
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_token_permissions(self) -> responses.GroupsGetTokenPermissions:
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'groups.getTokenPermissions'
        response_type = responses.GroupsGetTokenPermissions
        return self._call(method_name, method_parameters, param_aliases, response_type)

    @overload
    def is_member(self, group_id: str, user_id: Optional[int] = None, user_ids: None = None, extended: None = None) -> responses.GroupsIsMember: ...
    @overload
    def is_member(self, group_id: str, user_ids: List[int], user_id: Optional[int] = None, extended: None = None) -> responses.GroupsIsMemberUserIds: ...
    @overload
    def is_member(self, group_id: str, extended: bool, user_id: Optional[int] = None, user_ids: None = None) -> responses.GroupsIsMemberExtended: ...
    @overload
    def is_member(self, group_id: str, user_ids: List[int], extended: bool, user_id: Optional[int] = None) -> responses.GroupsIsMemberUserIdsExtended: ...
    def is_member(self, group_id: str, user_id: Optional[int] = None, user_ids: Optional[List[int]] = None, extended: Optional[bool] = None):
        """
        Returns information specifying whether a user is a member of a community.

        :param group_id: ID or screen name of the community.
        :param user_id: User ID.
        :param user_ids: User IDs.
        :param extended: '1' — to return an extended response with additional fields. By default: '0'.
        """

        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'groups.isMember'
        if not user_ids and not extended:
            response_type = responses.GroupsIsMember
        if user_ids and not extended:
            response_type = responses.GroupsIsMemberUserIds
        if not user_ids and extended:
            response_type = responses.GroupsIsMemberExtended
        if user_ids and extended:
            response_type = responses.GroupsIsMemberUserIdsExtended
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def set_callback_settings(self, group_id: int, server_id: Optional[int] = None, api_version: Optional[str] = None, message_new: Optional[bool] = None, message_reply: Optional[bool] = None, message_allow: Optional[bool] = None, message_edit: Optional[bool] = None, message_deny: Optional[bool] = None, message_typing_state: Optional[bool] = None, photo_new: Optional[bool] = None, audio_new: Optional[bool] = None, video_new: Optional[bool] = None, wall_reply_new: Optional[bool] = None, wall_reply_edit: Optional[bool] = None, wall_reply_delete: Optional[bool] = None, wall_reply_restore: Optional[bool] = None, wall_post_new: Optional[bool] = None, wall_repost: Optional[bool] = None, board_post_new: Optional[bool] = None, board_post_edit: Optional[bool] = None, board_post_restore: Optional[bool] = None, board_post_delete: Optional[bool] = None, photo_comment_new: Optional[bool] = None, photo_comment_edit: Optional[bool] = None, photo_comment_delete: Optional[bool] = None, photo_comment_restore: Optional[bool] = None, video_comment_new: Optional[bool] = None, video_comment_edit: Optional[bool] = None, video_comment_delete: Optional[bool] = None, video_comment_restore: Optional[bool] = None, market_comment_new: Optional[bool] = None, market_comment_edit: Optional[bool] = None, market_comment_delete: Optional[bool] = None, market_comment_restore: Optional[bool] = None, poll_vote_new: Optional[bool] = None, group_join: Optional[bool] = None, group_leave: Optional[bool] = None, group_change_settings: Optional[bool] = None, group_change_photo: Optional[bool] = None, group_officers_edit: Optional[bool] = None, user_block: Optional[bool] = None, user_unblock: Optional[bool] = None, lead_forms_new: Optional[bool] = None, like_add: Optional[bool] = None, like_remove: Optional[bool] = None, message_event: Optional[bool] = None) -> responses.BaseOk:
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
        param_aliases = []
        method_name = 'groups.setCallbackSettings'
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def set_long_poll_settings(self, group_id: int, enabled: Optional[bool] = None, api_version: Optional[str] = None, message_new: Optional[bool] = None, message_reply: Optional[bool] = None, message_allow: Optional[bool] = None, message_deny: Optional[bool] = None, message_edit: Optional[bool] = None, message_typing_state: Optional[bool] = None, photo_new: Optional[bool] = None, audio_new: Optional[bool] = None, video_new: Optional[bool] = None, wall_reply_new: Optional[bool] = None, wall_reply_edit: Optional[bool] = None, wall_reply_delete: Optional[bool] = None, wall_reply_restore: Optional[bool] = None, wall_post_new: Optional[bool] = None, wall_repost: Optional[bool] = None, board_post_new: Optional[bool] = None, board_post_edit: Optional[bool] = None, board_post_restore: Optional[bool] = None, board_post_delete: Optional[bool] = None, photo_comment_new: Optional[bool] = None, photo_comment_edit: Optional[bool] = None, photo_comment_delete: Optional[bool] = None, photo_comment_restore: Optional[bool] = None, video_comment_new: Optional[bool] = None, video_comment_edit: Optional[bool] = None, video_comment_delete: Optional[bool] = None, video_comment_restore: Optional[bool] = None, market_comment_new: Optional[bool] = None, market_comment_edit: Optional[bool] = None, market_comment_delete: Optional[bool] = None, market_comment_restore: Optional[bool] = None, poll_vote_new: Optional[bool] = None, group_join: Optional[bool] = None, group_leave: Optional[bool] = None, group_change_settings: Optional[bool] = None, group_change_photo: Optional[bool] = None, group_officers_edit: Optional[bool] = None, user_block: Optional[bool] = None, user_unblock: Optional[bool] = None, like_add: Optional[bool] = None, like_remove: Optional[bool] = None, message_event: Optional[bool] = None) -> responses.BaseOk:
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
        param_aliases = []
        method_name = 'groups.setLongPollSettings'
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)
