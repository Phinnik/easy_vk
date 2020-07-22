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

    def add_link(self, group_id: int = None, link: str = None, text: str = None) -> responses.GroupsAddLink:
        """
        Allows to add a link to the community.
        
        :param group_id: Community ID.
        :param link: Link URL.
        :param text: Description text for the link.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'groups.addLink'
        param_aliases = []
        response_type = responses.GroupsAddLink
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def approve_request(self, group_id: int = None, user_id: int = None) -> responses.BaseOk:
        """
        Allows to approve join request to the community.
        
        :param group_id: Community ID.
        :param user_id: User ID.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'groups.approveRequest'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def ban(self, group_id: int = None, owner_id: int = None, end_date: int = None, reason: int = None, comment: str = None, comment_visible: bool = None) -> responses.BaseOk:
        """
        :param group_id: 
        :param owner_id: 
        :param end_date: 
        :param reason: 
        :param comment: 
        :param comment_visible: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'groups.ban'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def create(self, title: str = None, description: str = None, type_: str = None, public_category: int = None, subtype: int = None) -> responses.GroupsCreate:
        """
        Creates a new community.
        
        :param title: Community title.
        :param description: Community description (ignored for 'type' = 'public').
        :param type_: Community type. Possible values: *'group' – group,, *'event' – event,, *'public' – public page
        :param public_category: Category ID (for 'type' = 'public' only).
        :param subtype: Public page subtype. Possible values: *'1' – place or small business,, *'2' – company, organization or website,, *'3' – famous person or group of people,, *'4' – product or work of art.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'groups.create'
        param_aliases = [('type_', 'type')]
        response_type = responses.GroupsCreate
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

    def delete_link(self, group_id: int = None, link_id: int = None) -> responses.BaseOk:
        """
        Allows to delete a link from the community.
        
        :param group_id: Community ID.
        :param link_id: Link ID.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'groups.deleteLink'
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

    def edit(self, group_id: int = None, title: str = None, description: str = None, screen_name: str = None, access: Union[objects.GroupsGroupAccess, int] = None, website: str = None, subject: Union[objects.GroupsGroupSubject, str] = None, email: str = None, phone: str = None, rss: str = None, event_start_date: int = None, event_finish_date: int = None, event_group_id: int = None, public_category: int = None, public_subcategory: int = None, public_date: str = None, wall: Union[objects.GroupsGroupWall, int] = None, topics: Union[objects.GroupsGroupTopics, int] = None, photos: Union[objects.GroupsGroupPhotos, int] = None, video: Union[objects.GroupsGroupVideo, int] = None, audio: Union[objects.GroupsGroupAudio, int] = None, links: bool = None, events: bool = None, places: bool = None, contacts: bool = None, docs: Union[objects.GroupsGroupDocs, int] = None, wiki: Union[objects.GroupsGroupWiki, int] = None, messages: bool = None, articles: bool = None, addresses: bool = None, age_limits: Union[objects.GroupsGroupAgeLimits, int] = None, market: bool = None, market_comments: bool = None, market_country: List[int] = None, market_city: List[int] = None, market_currency: Union[objects.GroupsGroupMarketCurrency, int] = None, market_contact: int = None, market_wiki: int = None, obscene_filter: bool = None, obscene_stopwords: bool = None, obscene_words: List[str] = None, main_section: int = None, secondary_section: int = None, country: int = None, city: int = None) -> responses.BaseOk:
        """
        Edits a community.
        
        :param group_id: Community ID.
        :param title: Community title.
        :param description: Community description.
        :param screen_name: Community screen name.
        :param access: Community type. Possible values: *'0' – open,, *'1' – closed,, *'2' – private.
        :param website: Website that will be displayed in the community information field.
        :param subject: Community subject. Possible values: , *'1' – auto/moto,, *'2' – activity holidays,, *'3' – business,, *'4' – pets,, *'5' – health,, *'6' – dating and communication, , *'7' – games,, *'8' – IT (computers and software),, *'9' – cinema,, *'10' – beauty and fashion,, *'11' – cooking,, *'12' – art and culture,, *'13' – literature,, *'14' – mobile services and internet,, *'15' – music,, *'16' – science and technology,, *'17' – real estate,, *'18' – news and media,, *'19' – security,, *'20' – education,, *'21' – home and renovations,, *'22' – politics,, *'23' – food,, *'24' – industry,, *'25' – travel,, *'26' – work,, *'27' – entertainment,, *'28' – religion,, *'29' – family,, *'30' – sports,, *'31' – insurance,, *'32' – television,, *'33' – goods and services,, *'34' – hobbies,, *'35' – finance,, *'36' – photo,, *'37' – esoterics,, *'38' – electronics and appliances,, *'39' – erotic,, *'40' – humor,, *'41' – society, humanities,, *'42' – design and graphics.
        :param email: Organizer email (for events).
        :param phone: Organizer phone number (for events).
        :param rss: RSS feed address for import (available only to communities with special permission. Contact vk.com/support to get it.
        :param event_start_date: Event start date in Unixtime format.
        :param event_finish_date: Event finish date in Unixtime format.
        :param event_group_id: Organizer community ID (for events only).
        :param public_category: Public page category ID.
        :param public_subcategory: Public page subcategory ID.
        :param public_date: Founding date of a company or organization owning the community in "dd.mm.YYYY" format.
        :param wall: Wall settings. Possible values: *'0' – disabled,, *'1' – open,, *'2' – limited (groups and events only),, *'3' – closed (groups and events only).
        :param topics: Board topics settings. Possbile values: , *'0' – disabled,, *'1' – open,, *'2' – limited (for groups and events only).
        :param photos: Photos settings. Possible values: *'0' – disabled,, *'1' – open,, *'2' – limited (for groups and events only).
        :param video: Video settings. Possible values: *'0' – disabled,, *'1' – open,, *'2' – limited (for groups and events only).
        :param audio: Audio settings. Possible values: *'0' – disabled,, *'1' – open,, *'2' – limited (for groups and events only).
        :param links: Links settings (for public pages only). Possible values: *'0' – disabled,, *'1' – enabled.
        :param events: Events settings (for public pages only). Possible values: *'0' – disabled,, *'1' – enabled.
        :param places: Places settings (for public pages only). Possible values: *'0' – disabled,, *'1' – enabled.
        :param contacts: Contacts settings (for public pages only). Possible values: *'0' – disabled,, *'1' – enabled.
        :param docs: Documents settings. Possible values: *'0' – disabled,, *'1' – open,, *'2' – limited (for groups and events only).
        :param wiki: Wiki pages settings. Possible values: *'0' – disabled,, *'1' – open,, *'2' – limited (for groups and events only).
        :param messages: Community messages. Possible values: *'0' — disabled,, *'1' — enabled.
        :param articles: 
        :param addresses: 
        :param age_limits: Community age limits. Possible values: *'1' — no limits,, *'2' — 16+,, *'3' — 18+.
        :param market: Market settings. Possible values: *'0' – disabled,, *'1' – enabled.
        :param market_comments: market comments settings. Possible values: *'0' – disabled,, *'1' – enabled.
        :param market_country: Market delivery countries.
        :param market_city: Market delivery cities (if only one country is specified).
        :param market_currency: Market currency settings. Possbile values: , *'643' – Russian rubles,, *'980' – Ukrainian hryvnia,, *'398' – Kazakh tenge,, *'978' – Euro,, *'840' – US dollars
        :param market_contact: Seller contact for market. Set '0' for community messages.
        :param market_wiki: ID of a wiki page with market description.
        :param obscene_filter: Obscene expressions filter in comments. Possible values: , *'0' – disabled,, *'1' – enabled.
        :param obscene_stopwords: Stopwords filter in comments. Possible values: , *'0' – disabled,, *'1' – enabled.
        :param obscene_words: Keywords for stopwords filter.
        :param main_section: 
        :param secondary_section: 
        :param country: Country of the community.
        :param city: City of the community.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'groups.edit'
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

    def edit_link(self, group_id: int = None, link_id: int = None, text: str = None) -> responses.BaseOk:
        """
        Allows to edit a link in the community.
        
        :param group_id: Community ID.
        :param link_id: Link ID.
        :param text: New description text for the link.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'groups.editLink'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def edit_manager(self, group_id: int = None, user_id: int = None, role: Union[objects.GroupsGroupRole, str] = None, is_contact: bool = None, contact_position: str = None, contact_phone: str = None, contact_email: str = None) -> responses.BaseOk:
        """
        Allows to add, remove or edit the community manager.
        
        :param group_id: Community ID.
        :param user_id: User ID.
        :param role: Manager role. Possible values: *'moderator',, *'editor',, *'administrator'.
        :param is_contact: '1' — to show the manager in Contacts block of the community.
        :param contact_position: Position to show in Contacts block.
        :param contact_phone: Contact phone.
        :param contact_email: Contact e-mail.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'groups.editManager'
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

    def get(self, user_id: int = None, extended: bool = None, filter_: List[Union[objects.GroupsFilter, str]] = None, fields: List[Union[objects.GroupsFields, str]] = None, offset: int = None, count: int = None) -> Union[responses.GroupsGet, responses.GroupsGetExtended]:
        """
        Returns a list of the communities to which a user belongs.
        
        :param user_id: User ID.
        :param extended: '1' — to return complete information about a user's communities, '0' — to return a list of community IDs without any additional fields (default),
        :param filter_: Types of communities to return: 'admin' — to return communities administered by the user , 'editor' — to return communities where the user is an administrator or editor, 'moder' — to return communities where the user is an administrator, editor, or moderator, 'groups' — to return only groups, 'publics' — to return only public pages, 'events' — to return only events
        :param fields: Profile fields to return.
        :param offset: Offset needed to return a specific subset of communities.
        :param count: Number of communities to return.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'groups.get'
        param_aliases = [('filter_', 'filter')]
        if not extended:
            response_type = responses.GroupsGet
        else:
            response_type = responses.GroupsGetExtended
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_addresses(self, group_id: int = None, address_ids: List[int] = None, latitude: float = None, longitude: float = None, offset: int = None, count: int = None, fields: List[Union[objects.AddressesFields, str]] = None) -> responses.GroupsGetAddresses:
        """
        Returns a list of community addresses.
        
        :param group_id: ID or screen name of the community.
        :param address_ids: 
        :param latitude: Latitude of  the user geo position.
        :param longitude: Longitude of the user geo position.
        :param offset: Offset needed to return a specific subset of community addresses.
        :param count: Number of community addresses to return.
        :param fields: Address fields
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'groups.getAddresses'
        param_aliases = []
        response_type = responses.GroupsGetAddresses
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

    def get_catalog(self, category_id: int = None, subcategory_id: int = None) -> responses.GroupsGetCatalog:
        """
        Returns communities list for a catalog category.
        
        :param category_id: Category id received from [vk.com/dev/groups.getCatalogInfo|groups.getCatalogInfo].
        :param subcategory_id: Subcategory id received from [vk.com/dev/groups.getCatalogInfo|groups.getCatalogInfo].
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'groups.getCatalog'
        param_aliases = []
        response_type = responses.GroupsGetCatalog
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_catalog_info(self, extended: bool = None, subcategories: bool = None) -> Union[responses.GroupsGetCatalogInfo, responses.GroupsGetCatalogInfoExtended]:
        """
        Returns categories list for communities catalog
        
        :param extended: 1 – to return communities count and three communities for preview. By default: 0.
        :param subcategories: 1 – to return subcategories info. By default: 0.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'groups.getCatalogInfo'
        param_aliases = []
        if not extended:
            response_type = responses.GroupsGetCatalogInfo
        else:
            response_type = responses.GroupsGetCatalogInfoExtended
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_invited_users(self, group_id: int = None, offset: int = None, count: int = None, fields: List[Union[objects.UsersFields, str]] = None, name_case: str = None) -> responses.GroupsGetInvitedUsers:
        """
        Returns invited users list of a community
        
        :param group_id: Group ID to return invited users for.
        :param offset: Offset needed to return a specific subset of results.
        :param count: Number of results to return.
        :param fields: List of additional fields to be returned. Available values: 'sex, bdate, city, country, photo_50, photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig, online, online_mobile, lists, domain, has_mobile, contacts, connections, site, education, universities, schools, can_post, can_see_all_posts, can_see_audio, can_write_private_message, status, last_seen, common_count, relation, relatives, counters'.
        :param name_case: Case for declension of user name and surname. Possible values: *'nom' — nominative (default),, *'gen' — genitive,, *'dat' — dative,, *'acc' — accusative, , *'ins' — instrumental,, *'abl' — prepositional.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'groups.getInvitedUsers'
        param_aliases = []
        response_type = responses.GroupsGetInvitedUsers
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_invites(self, offset: int = None, count: int = None, extended: bool = None) -> Union[responses.GroupsGetInvites, responses.GroupsGetInvitesExtended]:
        """
        Returns a list of invitations to join communities and events.
        
        :param offset: Offset needed to return a specific subset of invitations.
        :param count: Number of invitations to return.
        :param extended: '1' — to return additional [vk.com/dev/fields_groups|fields] for communities..
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'groups.getInvites'
        param_aliases = []
        if not extended:
            response_type = responses.GroupsGetInvites
        else:
            response_type = responses.GroupsGetInvitesExtended
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

    def get_requests(self, group_id: int = None, offset: int = None, count: int = None, fields: List[Union[objects.UsersFields, str]] = None) -> Union[responses.GroupsGetRequests, responses.GroupsGetRequestsFields]:
        """
        Returns a list of requests to the community.
        
        :param group_id: Community ID.
        :param offset: Offset needed to return a specific subset of results.
        :param count: Number of results to return.
        :param fields: Profile fields to return.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'groups.getRequests'
        param_aliases = []
        if not fields:
            response_type = responses.GroupsGetRequests
        else:
            response_type = responses.GroupsGetRequestsFields
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_settings(self, group_id: int = None) -> responses.GroupsGetSettings:
        """
        Returns community settings.
        
        :param group_id: Community ID.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'groups.getSettings'
        param_aliases = []
        response_type = responses.GroupsGetSettings
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def invite(self, group_id: int = None, user_id: int = None) -> responses.BaseOk:
        """
        Allows to invite friends to the community.
        
        :param group_id: Community ID.
        :param user_id: User ID.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'groups.invite'
        param_aliases = []
        response_type = responses.BaseOk
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

    def join(self, group_id: int = None, not_sure: str = None) -> responses.BaseOk:
        """
        With this method you can join the group or public page, and also confirm your participation in an event.
        
        :param group_id: ID or screen name of the community.
        :param not_sure: Optional parameter which is taken into account when 'gid' belongs to the event: '1' — Perhaps I will attend, '0' — I will be there for sure (default), ,
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'groups.join'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def leave(self, group_id: int = None) -> responses.BaseOk:
        """
        With this method you can leave a group, public page, or event.
        
        :param group_id: ID or screen name of the community.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'groups.leave'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def remove_user(self, group_id: int = None, user_id: int = None) -> responses.BaseOk:
        """
        Removes a user from the community.
        
        :param group_id: Community ID.
        :param user_id: User ID.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'groups.removeUser'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def reorder_link(self, group_id: int = None, link_id: int = None, after: int = None) -> responses.BaseOk:
        """
        Allows to reorder links in the community.
        
        :param group_id: Community ID.
        :param link_id: Link ID.
        :param after: ID of the link after which to place the link with 'link_id'.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'groups.reorderLink'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def search(self, q: str = None, type_: str = None, country_id: int = None, city_id: int = None, future: bool = None, market: bool = None, sort: int = None, offset: int = None, count: int = None) -> responses.GroupsSearch:
        """
        Returns a list of communities matching the search criteria.
        
        :param q: Search query string.
        :param type_: Community type. Possible values: 'group, page, event.'
        :param country_id: Country ID.
        :param city_id: City ID. If this parameter is transmitted, country_id is ignored.
        :param future: '1' — to return only upcoming events. Works with the 'type' = 'event' only.
        :param market: '1' — to return communities with enabled market only.
        :param sort: Sort order. Possible values: *'0' — default sorting (similar the full version of the site),, *'1' — by growth speed,, *'2'— by the "day attendance/members number" ratio,, *'3' — by the "Likes number/members number" ratio,, *'4' — by the "comments number/members number" ratio,, *'5' — by the "boards entries number/members number" ratio.
        :param offset: Offset needed to return a specific subset of results.
        :param count: Number of communities to return. "Note that you can not receive more than first thousand of results, regardless of 'count' and 'offset' values."
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'groups.search'
        param_aliases = [('type_', 'type')]
        response_type = responses.GroupsSearch
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

    def unban(self, group_id: int = None, owner_id: int = None) -> responses.BaseOk:
        """
        :param group_id: 
        :param owner_id: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'groups.unban'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)
