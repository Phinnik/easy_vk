from pydantic import BaseModel, Field
from typing import List, Union, Optional, NewType
from enum import Enum
from . import objects


class AccountChangePassword(BaseModel):
    token: str = Field(..., description="New token")
    secret: Optional[str] = Field(None, description="New secret")


class AccountGetActiveOffers(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[objects.AccountOffer] = Field(...)


AccountGetAppPermissions = NewType('AccountGetAppPermissions', int)


class AccountGetBanned(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[int] = Field(...)
    profiles: Optional[List[objects.UsersUserMin]] = Field(None)
    groups: Optional[List[objects.GroupsGroup]] = Field(None)


AccountGetCounters = NewType('AccountGetCounters', objects.AccountAccountCounters)

AccountGetInfo = NewType('AccountGetInfo', objects.AccountInfo)

AccountGetProfileInfo = NewType('AccountGetProfileInfo', objects.AccountUserSettings)

AccountGetPushSettings = NewType('AccountGetPushSettings', objects.AccountPushSettings)


class AccountSaveProfileInfo(BaseModel):
    changed: Optional[objects.BaseBoolInt] = Field(None, description="1 if changes has been processed")
    name_request: Optional[objects.AccountNameRequest] = Field(None)


AdsAddOfficeUsers = NewType('AdsAddOfficeUsers', bool)

AdsCheckLink = NewType('AdsCheckLink', objects.AdsLinkStatus)

AdsCreateAds = NewType('AdsCreateAds', List[int])

AdsCreateCampaigns = NewType('AdsCreateCampaigns', List[int])

AdsCreateClients = NewType('AdsCreateClients', List[int])


class AdsCreateTargetGroup(BaseModel):
    id_: Optional[int] = Field(None, alias='id', description="Group ID")
    pixel: Optional[str] = Field(None, description="Pixel code")


AdsDeleteAds = NewType('AdsDeleteAds', List[int])

AdsDeleteCampaigns = NewType('AdsDeleteCampaigns', int)

AdsDeleteClients = NewType('AdsDeleteClients', int)

AdsGetAccounts = NewType('AdsGetAccounts', List[objects.AdsAccount])

AdsGetAdsLayout = NewType('AdsGetAdsLayout', List[objects.AdsAdLayout])

AdsGetAdsTargeting = NewType('AdsGetAdsTargeting', List[objects.AdsTargSettings])

AdsGetAds = NewType('AdsGetAds', List[objects.AdsAd])

AdsGetBudget = NewType('AdsGetBudget', int)

AdsGetCampaigns = NewType('AdsGetCampaigns', List[objects.AdsCampaign])


class AdsGetCategories(BaseModel):
    v1: Optional[List[objects.AdsCategory]] = Field(None, description="Old categories")
    v2: Optional[List[objects.AdsCategory]] = Field(None, description="Actual categories")


AdsGetClients = NewType('AdsGetClients', List[objects.AdsClient])

AdsGetDemographics = NewType('AdsGetDemographics', List[objects.AdsDemoStats])

AdsGetFloodStats = NewType('AdsGetFloodStats', objects.AdsFloodStats)


class AdsGetLookalikeRequests(BaseModel):
    count: int = Field(..., description="Total count of found lookalike requests")
    items: List[objects.AdsLookalikeRequest] = Field(..., description="found lookalike requests")


class AdsGetMusicians(BaseModel):
    items: List[objects.AdsMusician] = Field(..., description="Musicians")


AdsGetOfficeUsers = NewType('AdsGetOfficeUsers', List[objects.AdsUsers])

AdsGetPostsReach = NewType('AdsGetPostsReach', List[objects.AdsPromotedPostReach])

AdsGetRejectionReason = NewType('AdsGetRejectionReason', objects.AdsRejectReason)

AdsGetStatistics = NewType('AdsGetStatistics', List[objects.AdsStats])

AdsGetSuggestionsCities = NewType('AdsGetSuggestionsCities', List[objects.AdsTargSuggestionsCities])

AdsGetSuggestionsRegions = NewType('AdsGetSuggestionsRegions', List[objects.AdsTargSuggestionsRegions])

AdsGetSuggestions = NewType('AdsGetSuggestions', List[objects.AdsTargSuggestions])

AdsGetSuggestionsSchools = NewType('AdsGetSuggestionsSchools', List[objects.AdsTargSuggestionsSchools])

AdsGetTargetGroups = NewType('AdsGetTargetGroups', List[objects.AdsTargetGroup])

AdsGetTargetingStats = NewType('AdsGetTargetingStats', objects.AdsTargStats)

AdsGetUploadUrl = NewType('AdsGetUploadUrl', str)

AdsGetVideoUploadUrl = NewType('AdsGetVideoUploadUrl', str)

AdsImportTargetContacts = NewType('AdsImportTargetContacts', int)

AdsRemoveOfficeUsers = NewType('AdsRemoveOfficeUsers', bool)

AdsUpdateAds = NewType('AdsUpdateAds', List[int])

AdsUpdateCampaigns = NewType('AdsUpdateCampaigns', int)

AdsUpdateClients = NewType('AdsUpdateClients', int)


class AppsGetCatalog(BaseModel):
    count: Optional[int] = Field(None, description="Total number")
    items: Optional[List[objects.AppsApp]] = Field(None)


class AppsGetFriendsList(BaseModel):
    count: Optional[int] = Field(None, description="Total number")
    items: Optional[List[objects.UsersUserFull]] = Field(None)


class AppsGetLeaderboardExtended(BaseModel):
    count: Optional[int] = Field(None, description="Total number")
    items: Optional[List[objects.AppsLeaderboard]] = Field(None)
    profiles: Optional[List[objects.UsersUserMin]] = Field(None)


class AppsGetLeaderboard(BaseModel):
    count: Optional[int] = Field(None, description="Total number")
    items: Optional[List[objects.AppsLeaderboard]] = Field(None)


class AppsGetScopes(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[objects.AppsScope] = Field(...)


AppsGetScore = NewType('AppsGetScore', int)


class AppsGet(BaseModel):
    count: Optional[int] = Field(None, description="Total number of applications")
    items: Optional[List[objects.AppsApp]] = Field(None, description="List of applications")


AppsSendRequest = NewType('AppsSendRequest', int)


class AuthRestore(BaseModel):
    success: Optional[int] = Field(None, description="1 if success")
    sid: Optional[str] = Field(None, description="Parameter needed to grant access by code")


BaseBool = NewType('BaseBool', objects.BaseBoolInt)

BaseGetUploadServer = NewType('BaseGetUploadServer', objects.BaseUploadServer)

BaseOk = NewType('BaseOk', int)

BoardAddTopic = NewType('BoardAddTopic', int)

BoardCreateComment = NewType('BoardCreateComment', int)


class BoardGetCommentsExtended(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[objects.BoardTopicComment] = Field(...)
    poll: Optional[objects.BoardTopicPoll] = Field(None)
    profiles: List[objects.UsersUser] = Field(...)
    groups: List[objects.GroupsGroup] = Field(...)


class BoardGetComments(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[objects.BoardTopicComment] = Field(...)
    poll: Optional[objects.BoardTopicPoll] = Field(None)


class BoardGetTopicsExtended(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[objects.BoardTopic] = Field(...)
    default_order: objects.BoardDefaultOrder = Field(...)
    can_add_topics: objects.BaseBoolInt = Field(..., description="Information whether current user can add topic")
    profiles: List[objects.UsersUserMin] = Field(...)


class BoardGetTopics(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[objects.BoardTopic] = Field(...)
    default_order: objects.BoardDefaultOrder = Field(...)
    can_add_topics: objects.BaseBoolInt = Field(..., description="Information whether current user can add topic")


class DatabaseGetChairs(BaseModel):
    count: Optional[int] = Field(None, description="Total number")
    items: Optional[List[objects.BaseObject]] = Field(None)


DatabaseGetCitiesById = NewType('DatabaseGetCitiesById', List[objects.BaseObject])


class DatabaseGetCities(BaseModel):
    count: Optional[int] = Field(None, description="Total number")
    items: Optional[List[objects.DatabaseCity]] = Field(None)


DatabaseGetCountriesById = NewType('DatabaseGetCountriesById', List[objects.BaseCountry])


class DatabaseGetCountries(BaseModel):
    count: Optional[int] = Field(None, description="Total number")
    items: Optional[List[objects.BaseCountry]] = Field(None)


class DatabaseGetFaculties(BaseModel):
    count: Optional[int] = Field(None, description="Total number")
    items: Optional[List[objects.DatabaseFaculty]] = Field(None)


DatabaseGetMetroStationsById = NewType('DatabaseGetMetroStationsById', List[objects.DatabaseStation])


class DatabaseGetMetroStations(BaseModel):
    count: Optional[int] = Field(None, description="Total number")
    items: Optional[List[objects.DatabaseStation]] = Field(None)


class DatabaseGetRegions(BaseModel):
    count: Optional[int] = Field(None, description="Total number")
    items: Optional[List[objects.DatabaseRegion]] = Field(None)


DatabaseGetSchoolClasses = NewType('DatabaseGetSchoolClasses', List[List[Union[str, int]]])


class DatabaseGetSchools(BaseModel):
    count: Optional[int] = Field(None, description="Total number")
    items: Optional[List[objects.DatabaseSchool]] = Field(None)


class DatabaseGetUniversities(BaseModel):
    count: Optional[int] = Field(None, description="Total number")
    items: Optional[List[objects.DatabaseUniversity]] = Field(None)


class DocsAdd(BaseModel):
    id_: Optional[int] = Field(None, alias='id', description="Doc ID")


DocsGetById = NewType('DocsGetById', List[objects.DocsDoc])


class DocsGetTypes(BaseModel):
    count: Optional[int] = Field(None, description="Total number")
    items: Optional[List[objects.DocsDocTypes]] = Field(None)


DocsGetUploadServer = NewType('DocsGetUploadServer', objects.BaseUploadServer)


class DocsGet(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[objects.DocsDoc] = Field(...)


class DocsSave(BaseModel):
    type_: Optional[objects.DocsDocAttachmentType] = Field(None, alias='type')
    audio_message: Optional[objects.MessagesAudioMessage] = Field(None)
    doc: Optional[objects.DocsDoc] = Field(None)
    graffiti: Optional[objects.MessagesGraffiti] = Field(None)


class DocsSearch(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[objects.DocsDoc] = Field(...)


class DownloadedGamesPaidStatus(BaseModel):
    is_paid: bool = Field(..., description="Game has been paid")


FaveAddTag = NewType('FaveAddTag', objects.FaveTag)


class FaveGetPages(BaseModel):
    count: Optional[int] = Field(None)
    items: Optional[List[objects.FavePage]] = Field(None)


class FaveGetTags(BaseModel):
    count: Optional[int] = Field(None)
    items: Optional[List[objects.FaveTag]] = Field(None)


class FaveGetExtended(BaseModel):
    count: Optional[int] = Field(None, description="Total number")
    items: Optional[List[objects.FaveBookmark]] = Field(None)
    profiles: Optional[List[objects.UsersUserFull]] = Field(None)
    groups: Optional[List[objects.GroupsGroup]] = Field(None)


class FaveGet(BaseModel):
    count: Optional[int] = Field(None, description="Total number")
    items: Optional[List[objects.FaveBookmark]] = Field(None)


class FriendsAddList(BaseModel):
    list_id: int = Field(..., description="List ID")


FriendsAdd = NewType('FriendsAdd', int)

FriendsAreFriendsExtended = NewType('FriendsAreFriendsExtended', List[objects.FriendsFriendExtendedStatus])

FriendsAreFriends = NewType('FriendsAreFriends', List[objects.FriendsFriendStatus])


class FriendsDelete(BaseModel):
    success: int = Field(...)
    friend_deleted: Optional[int] = Field(None, description="Returns 1 if friend has been deleted")
    out_request_deleted: Optional[int] = Field(None, description="Returns 1 if out request has been canceled")
    in_request_deleted: Optional[int] = Field(None, description="Returns 1 if incoming request has been declined")
    suggestion_deleted: Optional[int] = Field(None, description="Returns 1 if suggestion has been declined")


FriendsGetAppUsers = NewType('FriendsGetAppUsers', List[int])

FriendsGetByPhones = NewType('FriendsGetByPhones', List[objects.FriendsUserXtrPhone])


class FriendsGetLists(BaseModel):
    count: int = Field(..., description="Total number of friends lists")
    items: List[objects.FriendsFriendsList] = Field(...)


FriendsGetMutual = NewType('FriendsGetMutual', List[int])

FriendsGetMutualTargetUids = NewType('FriendsGetMutualTargetUids', List[objects.FriendsMutualFriend])


class FriendsGetOnlineOnlineMobile(BaseModel):
    online: Optional[List[int]] = Field(None)
    online_mobile: Optional[List[int]] = Field(None)


FriendsGetOnline = NewType('FriendsGetOnline', List[int])

FriendsGetRecent = NewType('FriendsGetRecent', List[int])


class FriendsGetRequestsExtended(BaseModel):
    count: Optional[int] = Field(None, description="Total requests number")
    items: Optional[List[objects.FriendsRequestsXtrMessage]] = Field(None)


class FriendsGetRequestsNeedMutual(BaseModel):
    count: Optional[int] = Field(None, description="Total requests number")
    items: Optional[List[objects.FriendsRequests]] = Field(None)


class FriendsGetRequests(BaseModel):
    count: Optional[int] = Field(None, description="Total requests number")
    items: Optional[List[int]] = Field(None)
    count_unread: Optional[int] = Field(None, description="Total unread requests number")


class FriendsGetSuggestions(BaseModel):
    count: int = Field(..., description="Total results number")
    items: List[objects.UsersUserFull] = Field(...)


class FriendsGetFields(BaseModel):
    count: int = Field(..., description="Total friends number")
    items: List[objects.FriendsUserXtrLists] = Field(...)


class FriendsGet(BaseModel):
    count: int = Field(..., description="Total friends number")
    items: List[int] = Field(...)


class FriendsSearch(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[objects.UsersUserFull] = Field(...)


class GiftsGet(BaseModel):
    count: Optional[int] = Field(None, description="Total number")
    items: Optional[List[objects.GiftsGift]] = Field(None)


GroupsAddAddress = NewType('GroupsAddAddress', objects.GroupsAddress)


class GroupsAddCallbackServer(BaseModel):
    server_id: Optional[int] = Field(None)


GroupsAddLink = NewType('GroupsAddLink', objects.GroupsGroupLink)

GroupsCreate = NewType('GroupsCreate', objects.GroupsGroup)

GroupsEditAddress = NewType('GroupsEditAddress', objects.GroupsAddress)


class GroupsGetAddresses(BaseModel):
    count: int = Field(..., description="Total count of addresses")
    items: List[objects.GroupsAddress] = Field(...)


class GroupsGetBanned(BaseModel):
    count: int = Field(..., description="Total users number")
    # items: List[objects.GroupsBannedItem] = Field(...)   object GroupsBannedItem has error in json-schema


GroupsGetById = NewType('GroupsGetById', List[objects.GroupsGroupFull])


class GroupsGetCallbackConfirmationCode(BaseModel):
    code: Optional[str] = Field(None, description="Confirmation code")


class GroupsGetCallbackServers(BaseModel):
    count: int = Field(...)
    items: List[objects.GroupsCallbackServer] = Field(...)


GroupsGetCallbackSettings = NewType('GroupsGetCallbackSettings', objects.GroupsCallbackSettings)


class GroupsGetCatalogInfoExtended(BaseModel):
    enabled: int = Field(..., description="Information whether catalog is enabled for current user")
    categories: Optional[List[objects.GroupsGroupCategoryFull]] = Field(None)


class GroupsGetCatalogInfo(BaseModel):
    enabled: int = Field(..., description="Information whether catalog is enabled for current user")
    categories: Optional[List[objects.GroupsGroupCategory]] = Field(None)


class GroupsGetCatalog(BaseModel):
    count: int = Field(..., description="Total communities number")
    items: List[objects.GroupsGroup] = Field(...)


class GroupsGetInvitedUsers(BaseModel):
    count: int = Field(..., description="Total communities number")
    items: List[objects.UsersUserFull] = Field(...)


class GroupsGetInvitesExtended(BaseModel):
    count: int = Field(..., description="Total communities number")
    items: List[objects.GroupsGroupXtrInvitedBy] = Field(...)
    profiles: List[objects.UsersUserMin] = Field(...)
    groups: List[objects.GroupsGroupFull] = Field(...)


class GroupsGetInvites(BaseModel):
    count: int = Field(..., description="Total communities number")
    items: List[objects.GroupsGroupXtrInvitedBy] = Field(...)


GroupsGetLongPollServer = NewType('GroupsGetLongPollServer', objects.GroupsLongPollServer)

GroupsGetLongPollSettings = NewType('GroupsGetLongPollSettings', objects.GroupsLongPollSettings)


class GroupsGetMembersFields(BaseModel):
    count: int = Field(..., description="Total members number")
    items: List[objects.GroupsUserXtrRole] = Field(...)


class GroupsGetMembersFilter(BaseModel):
    count: int = Field(..., description="Total members number")
    items: List[objects.GroupsMemberRole] = Field(...)


class GroupsGetMembers(BaseModel):
    count: int = Field(..., description="Total members number")
    items: List[int] = Field(...)


class GroupsGetRequestsFields(BaseModel):
    count: int = Field(..., description="Total communities number")
    items: List[objects.UsersUserFull] = Field(...)


class GroupsGetRequests(BaseModel):
    count: int = Field(..., description="Total communities number")
    items: List[int] = Field(...)


class GroupsGetSettings(BaseModel):
    access: Optional[int] = Field(None, description="Community access settings")
    address: Optional[str] = Field(None, description="Community's page domain")
    audio: int = Field(..., description="Audio settings")
    articles: int = Field(..., description="Articles settings")
    city_id: int = Field(..., description="City id of group")
    contacts: Optional[objects.BaseBoolInt] = Field(None)
    links: Optional[objects.BaseBoolInt] = Field(None)
    sections_list: Optional[str] = Field(None)
    main_section: Optional[objects.GroupsGroupFullMainSection] = Field(None)
    secondary_section: Optional[int] = Field(None)
    age_limits: Optional[int] = Field(None)
    country_id: int = Field(..., description="Country id of group")
    description: str = Field(..., description="Community description")
    docs: int = Field(..., description="Docs settings")
    events: Optional[objects.BaseBoolInt] = Field(None)
    obscene_filter: objects.BaseBoolInt = Field(..., description="Information whether the obscene filter is enabled")
    obscene_stopwords: objects.BaseBoolInt = Field(...,
                                                   description="Information whether the stopwords filter is enabled")
    obscene_words: List[str] = Field(..., description="The list of stop words")
    event_group_id: Optional[int] = Field(None)
    photos: int = Field(..., description="Photos settings")
    public_category: Optional[int] = Field(None, description="Information about the group category")
    public_category_list: Optional[List[objects.GroupsGroupPublicCategoryList]] = Field(None)
    public_date: Optional[str] = Field(None)
    public_date_label: Optional[str] = Field(None)
    public_subcategory: Optional[int] = Field(None, description="Information about the group subcategory")
    rss: Optional[str] = Field(None, description="URL of the RSS feed")
    start_date: Optional[int] = Field(None, description="Start date")
    finish_date: Optional[int] = Field(None, description="Finish date in Unixtime format")
    subject: Optional[int] = Field(None, description="Community subject ID")
    subject_list: Optional[List[objects.GroupsSubjectItem]] = Field(None)
    suggested_privacy: Optional[int] = Field(None)
    title: str = Field(..., description="Community title")
    topics: int = Field(..., description="Topics settings")
    twitter: Optional[objects.GroupsSettingsTwitter] = Field(None)
    video: int = Field(..., description="Video settings")
    wall: int = Field(..., description="Wall settings")
    website: Optional[str] = Field(None, description="Community website")
    phone: Optional[str] = Field(None, description="Community phone")
    email: Optional[str] = Field(None, description="Community email")
    wiki: int = Field(..., description="Wiki settings")


class GroupsGetTokenPermissions(BaseModel):
    mask: int = Field(...)
    permissions: List[objects.GroupsTokenPermissionSetting] = Field(...)


class GroupsGetExtended(BaseModel):
    count: int = Field(..., description="Total communities number")
    items: List[objects.GroupsGroupFull] = Field(...)


class GroupsGet(BaseModel):
    count: int = Field(..., description="Total communities number")
    items: List[int] = Field(...)


class GroupsIsMemberExtended(BaseModel):
    member: objects.BaseBoolInt = Field(..., description="Information whether user is a member of the group")
    invitation: Optional[objects.BaseBoolInt] = Field(None,
                                                      description="Information whether user has been invited to the "
                                                                  "group")
    can_invite: Optional[objects.BaseBoolInt] = Field(None, description="Information whether user can be invited")
    can_recall: Optional[objects.BaseBoolInt] = Field(None,
                                                      description="Information whether user's invite to the group can "
                                                                  "be recalled")
    request: Optional[objects.BaseBoolInt] = Field(None,
                                                   description="Information whether user has sent request to the group")


GroupsIsMember = NewType('GroupsIsMember', objects.BaseBoolInt)

GroupsIsMemberUserIdsExtended = NewType('GroupsIsMemberUserIdsExtended', List[objects.GroupsMemberStatusFull])

GroupsIsMemberUserIds = NewType('GroupsIsMemberUserIds', List[objects.GroupsMemberStatus])


class GroupsSearch(BaseModel):
    count: int = Field(..., description="Total communities number")
    items: List[objects.GroupsGroup] = Field(...)


LeadsCheckUser = NewType('LeadsCheckUser', objects.LeadsChecked)

LeadsComplete = NewType('LeadsComplete', objects.LeadsComplete)

LeadsGetStats = NewType('LeadsGetStats', objects.LeadsLead)

LeadsGetUsers = NewType('LeadsGetUsers', List[objects.LeadsEntry])


class LeadsMetricHit(BaseModel):
    result: Optional[bool] = Field(None, description="Information whether request has been processed successfully")
    redirect_link: Optional[str] = Field(None, description="Redirect link")


LeadsStart = NewType('LeadsStart', objects.LeadsStart)


class LikesAdd(BaseModel):
    likes: int = Field(..., description="Total likes number")


class LikesDelete(BaseModel):
    likes: int = Field(..., description="Total likes number")


class LikesGetListExtended(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[objects.UsersUserMin] = Field(...)


class LikesGetList(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[int] = Field(...)


class LikesIsLiked(BaseModel):
    liked: objects.BaseBoolInt = Field(..., description="Information whether user liked the object")
    copied: objects.BaseBoolInt = Field(..., description="Information whether user reposted the object")


class MarketAddAlbum(BaseModel):
    market_album_id: Optional[int] = Field(None, description="Album ID")


class MarketAdd(BaseModel):
    market_item_id: Optional[int] = Field(None, description="Item ID")


MarketCreateComment = NewType('MarketCreateComment', int)

MarketDeleteComment = NewType('MarketDeleteComment', objects.BaseBoolInt)


class MarketGetAlbumById(BaseModel):
    count: Optional[int] = Field(None, description="Total number")
    items: Optional[List[objects.MarketMarketAlbum]] = Field(None)


class MarketGetAlbums(BaseModel):
    count: Optional[int] = Field(None, description="Total number")
    items: Optional[List[objects.MarketMarketAlbum]] = Field(None)


class MarketGetByIdExtended(BaseModel):
    count: Optional[int] = Field(None, description="Total number")
    items: Optional[List[objects.MarketMarketItemFull]] = Field(None)


class MarketGetById(BaseModel):
    count: Optional[int] = Field(None, description="Total number")
    items: Optional[List[objects.MarketMarketItem]] = Field(None)


class MarketGetCategories(BaseModel):
    count: Optional[int] = Field(None, description="Total number")
    items: Optional[List[objects.MarketMarketCategory]] = Field(None)


class MarketGetComments(BaseModel):
    count: Optional[int] = Field(None, description="Total number")
    items: Optional[List[objects.WallWallComment]] = Field(None)


class MarketGetExtended(BaseModel):
    count: Optional[int] = Field(None, description="Total number")
    items: Optional[List[objects.MarketMarketItemFull]] = Field(None)


class MarketGet(BaseModel):
    count: Optional[int] = Field(None, description="Total number")
    items: Optional[List[objects.MarketMarketItem]] = Field(None)


MarketRestoreComment = NewType('MarketRestoreComment', objects.BaseBoolInt)


class MarketSearchExtended(BaseModel):
    count: Optional[int] = Field(None, description="Total number")
    items: Optional[List[objects.MarketMarketItemFull]] = Field(None)


class MarketSearch(BaseModel):
    count: Optional[int] = Field(None, description="Total number")
    items: Optional[List[objects.MarketMarketItem]] = Field(None)


MessagesCreateChat = NewType('MessagesCreateChat', int)


class MessagesDeleteChatPhoto(BaseModel):
    message_id: Optional[int] = Field(None, description="Service message ID")
    chat: Optional[objects.MessagesChat] = Field(None)


class MessagesDeleteConversation(BaseModel):
    last_deleted_id: int = Field(..., description="Id of the last message, that was deleted")


MessagesDelete = NewType('MessagesDelete', int)


MessagesEdit = NewType('MessagesEdit', objects.BaseBoolInt)


class MessagesGetByConversationMessageId(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[objects.MessagesMessage] = Field(...)


class MessagesGetByIdExtended(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[objects.MessagesMessage] = Field(...)
    profiles: List[objects.UsersUserFull] = Field(...)
    groups: Optional[List[objects.GroupsGroupFull]] = Field(None)


class MessagesGetById(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[objects.MessagesMessage] = Field(...)


class MessagesGetChatPreview(BaseModel):
    preview: Optional[objects.MessageChatPreview] = Field(None)
    profiles: Optional[List[objects.UsersUserFull]] = Field(None)


MessagesGetChatChatIdsFields = NewType('MessagesGetChatChatIdsFields', List[objects.MessagesChatFull])

MessagesGetChatChatIds = NewType('MessagesGetChatChatIds', List[objects.MessagesChat])

MessagesGetChatFields = NewType('MessagesGetChatFields', objects.MessagesChatFull)

MessagesGetChat = NewType('MessagesGetChat', objects.MessagesChat)


class MessagesGetConversationMembers(BaseModel):
    count: int = Field(..., description="Chat members count")
    items: List[objects.MessagesConversationMember] = Field(...)
    chat_restrictions: Optional[objects.MessagesChatRestrictions] = Field(None)
    profiles: Optional[List[objects.UsersUserFull]] = Field(None)
    groups: Optional[List[objects.GroupsGroupFull]] = Field(None)


class MessagesGetConversationsByIdExtended(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[objects.MessagesConversation] = Field(...)
    profiles: Optional[List[objects.UsersUser]] = Field(None)


class MessagesGetConversationsById(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[objects.MessagesConversation] = Field(...)


class MessagesGetConversations(BaseModel):
    count: int = Field(..., description="Total number")
    unread_count: Optional[int] = Field(None, description="Unread dialogs number")
    items: List[objects.MessagesConversationWithMessage] = Field(...)
    profiles: Optional[List[objects.UsersUserFull]] = Field(None)
    groups: Optional[List[objects.GroupsGroupFull]] = Field(None)


class MessagesGetHistoryAttachments(BaseModel):
    items: Optional[List[objects.MessagesHistoryAttachment]] = Field(None)
    next_from: Optional[str] = Field(None, description="Value for pagination")


class MessagesGetHistory(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[objects.MessagesMessage] = Field(...)
    profiles: Optional[List[objects.UsersUserFull]] = Field(None)
    groups: Optional[List[objects.GroupsGroupFull]] = Field(None)


class MessagesGetInviteLink(BaseModel):
    link: Optional[str] = Field(None)


MessagesGetLastActivity = NewType('MessagesGetLastActivity', objects.MessagesLastActivity)


class MessagesGetLongPollHistory(BaseModel):
    history: Optional[List[List[int]]] = Field(None)
    groups: Optional[List[objects.GroupsGroup]] = Field(None)
    messages: Optional[objects.MessagesLongpollMessages] = Field(None)
    profiles: Optional[List[objects.UsersUserFull]] = Field(None)
    chats: Optional[List[objects.MessagesChat]] = Field(None)
    new_pts: Optional[int] = Field(None, description="Persistence timestamp")
    more: Optional[bool] = Field(None, description="Has more")
    conversations: Optional[List[objects.MessagesConversation]] = Field(None)


MessagesGetLongPollServer = NewType('MessagesGetLongPollServer', objects.MessagesLongpollParams)


class MessagesIsMessagesFromGroupAllowed(BaseModel):
    is_allowed: Optional[objects.BaseBoolInt] = Field(None)


class MessagesJoinChatByInviteLink(BaseModel):
    chat_id: Optional[int] = Field(None)


MessagesMarkAsImportant = NewType('MessagesMarkAsImportant', List[int])

MessagesPin = NewType('MessagesPin', objects.MessagesPinnedMessage)


class MessagesSearchConversations(BaseModel):
    count: Optional[int] = Field(None, description="Total results number")
    items: Optional[List[objects.MessagesConversation]] = Field(None)
    profiles: Optional[List[objects.UsersUserFull]] = Field(None)
    groups: Optional[List[objects.GroupsGroupFull]] = Field(None)


class MessagesSearch(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[objects.MessagesMessage] = Field(...)


MessagesSend = NewType('MessagesSend', int)

MessagesSendUserIds = NewType('MessagesSendUserIds', List[object])


class MessagesSetChatPhoto(BaseModel):
    message_id: Optional[int] = Field(None, description="Service message ID")
    chat: Optional[objects.MessagesChat] = Field(None)


class NewsfeedGetBannedExtended(BaseModel):
    groups: Optional[List[objects.UsersUserFull]] = Field(None)
    profiles: Optional[List[objects.GroupsGroupFull]] = Field(None)


class NewsfeedGetBanned(BaseModel):
    groups: Optional[List[int]] = Field(None)
    members: Optional[List[int]] = Field(None)


class NewsfeedGetComments(BaseModel):
    items: List[objects.NewsfeedNewsfeedItem] = Field(...)
    profiles: List[objects.UsersUserFull] = Field(...)
    groups: List[objects.GroupsGroupFull] = Field(...)
    next_from: Optional[str] = Field(None, description="New from value")


class NewsfeedGetListsExtended(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[objects.NewsfeedListFull] = Field(...)


class NewsfeedGetLists(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[objects.NewsfeedList] = Field(...)


class NewsfeedGetMentions(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[objects.WallWallpostToId] = Field(...)


class NewsfeedGetRecommended(BaseModel):
    items: Optional[List[objects.NewsfeedNewsfeedItem]] = Field(None)
    profiles: Optional[List[objects.UsersUserFull]] = Field(None)
    groups: Optional[List[objects.GroupsGroupFull]] = Field(None)
    new_offset: Optional[str] = Field(None, description="New offset value")
    next_from: Optional[str] = Field(None, description="Next from value")


class NewsfeedGetSuggestedSources(BaseModel):
    count: Optional[int] = Field(None, description="Total number")
    items: Optional[List[Union[objects.GroupsGroupFull, objects.UsersUserXtrType]]] = Field(None)


class NewsfeedGet(BaseModel):
    items: Optional[List[objects.NewsfeedNewsfeedItem]] = Field(None)
    profiles: Optional[List[objects.UsersUserFull]] = Field(None)
    groups: Optional[List[objects.GroupsGroupFull]] = Field(None)
    next_from: Optional[str] = Field(None, description="New from value")


NewsfeedSaveList = NewType('NewsfeedSaveList', int)


class NewsfeedSearchExtended(BaseModel):
    items: Optional[List[objects.WallWallpostFull]] = Field(None)
    profiles: Optional[List[objects.UsersUserFull]] = Field(None)
    groups: Optional[List[objects.GroupsGroupFull]] = Field(None)
    suggested_queries: Optional[List[str]] = Field(None)
    next_from: Optional[str] = Field(None)
    count: Optional[int] = Field(None, description="Filtered number")
    total_count: Optional[int] = Field(None, description="Total number")


class NewsfeedSearch(BaseModel):
    items: Optional[List[objects.WallWallpostFull]] = Field(None)
    suggested_queries: Optional[List[str]] = Field(None)
    next_from: Optional[str] = Field(None)
    count: Optional[int] = Field(None, description="Filtered number")
    total_count: Optional[int] = Field(None, description="Total number")


NotesAdd = NewType('NotesAdd', int)

NotesCreateComment = NewType('NotesCreateComment', int)

NotesGetById = NewType('NotesGetById', objects.NotesNote)


class NotesGetComments(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[objects.NotesNoteComment] = Field(...)


class NotesGet(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[objects.NotesNote] = Field(...)


class NotificationsGet(BaseModel):
    count: Optional[int] = Field(None, description="Total number")
    # items: Optional[List[objects.NotificationsNotificationItem]] = Field(None)  object
    #                NotificationsNotificationItem has error in json-schema
    profiles: Optional[List[objects.UsersUser]] = Field(None)
    groups: Optional[List[objects.GroupsGroup]] = Field(None)
    last_viewed: Optional[int] = Field(None, description="Time when user has been checked notifications last time")
    photos: Optional[List[objects.PhotosPhoto]] = Field(None)
    videos: Optional[List[objects.VideoVideo]] = Field(None)
    apps: Optional[List[objects.AppsApp]] = Field(None)
    next_from: Optional[str] = Field(None)
    ttl: Optional[int] = Field(None)


NotificationsMarkAsViewed = NewType('NotificationsMarkAsViewed', objects.BaseBoolInt)

NotificationsSendMessage = NewType('NotificationsSendMessage', List[objects.NotificationsSendMessageItem])

OrdersCancelSubscription = NewType('OrdersCancelSubscription', objects.BaseBoolInt)

OrdersChangeState = NewType('OrdersChangeState', str)

OrdersGetAmount = NewType('OrdersGetAmount', objects.OrdersAmount)

OrdersGetById = NewType('OrdersGetById', List[objects.OrdersOrder])

OrdersGetUserSubscriptionById = NewType('OrdersGetUserSubscriptionById', objects.OrdersSubscription)


class OrdersGetUserSubscriptions(BaseModel):
    count: Optional[int] = Field(None, description="Total number")
    items: Optional[List[objects.OrdersSubscription]] = Field(None)


OrdersGet = NewType('OrdersGet', List[objects.OrdersOrder])

OrdersUpdateSubscription = NewType('OrdersUpdateSubscription', objects.BaseBoolInt)

PagesGetHistory = NewType('PagesGetHistory', List[objects.PagesWikipageHistory])

PagesGetTitles = NewType('PagesGetTitles', List[objects.PagesWikipage])

PagesGetVersion = NewType('PagesGetVersion', objects.PagesWikipageFull)

PagesGet = NewType('PagesGet', objects.PagesWikipageFull)

PagesParseWiki = NewType('PagesParseWiki', str)

PagesSaveAccess = NewType('PagesSaveAccess', int)

PagesSave = NewType('PagesSave', int)

PhotosCopy = NewType('PhotosCopy', int)

PhotosCreateAlbum = NewType('PhotosCreateAlbum', objects.PhotosPhotoAlbumFull)

PhotosCreateComment = NewType('PhotosCreateComment', int)

PhotosDeleteComment = NewType('PhotosDeleteComment', objects.BaseBoolInt)

PhotosGetAlbumsCount = NewType('PhotosGetAlbumsCount', int)


class PhotosGetAlbums(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[objects.PhotosPhotoAlbumFull] = Field(...)


class PhotosGetAllComments(BaseModel):
    count: Optional[int] = Field(None, description="Total number")
    items: Optional[List[objects.PhotosCommentXtrPid]] = Field(None)


class PhotosGetAllExtended(BaseModel):
    count: Optional[int] = Field(None, description="Total number")
    items: Optional[List[objects.PhotosPhotoFullXtrRealOffset]] = Field(None)
    more: Optional[objects.BaseBoolInt] = Field(None, description="Information whether next page is presented")


class PhotosGetAll(BaseModel):
    count: Optional[int] = Field(None, description="Total number")
    items: Optional[List[objects.PhotosPhotoXtrRealOffset]] = Field(None)
    more: Optional[objects.BaseBoolInt] = Field(None, description="Information whether next page is presented")


PhotosGetByIdExtended = NewType('PhotosGetByIdExtended', List[objects.PhotosPhotoFull])

PhotosGetById = NewType('PhotosGetById', List[objects.PhotosPhoto])


class PhotosGetCommentsExtended(BaseModel):
    count: int = Field(..., description="Total number")
    real_offset: Optional[int] = Field(None, description="Real offset of the comments")
    items: List[objects.WallWallComment] = Field(...)
    profiles: List[objects.UsersUserFull] = Field(...)
    groups: List[objects.GroupsGroupFull] = Field(...)


class PhotosGetComments(BaseModel):
    count: Optional[int] = Field(None, description="Total number")
    real_offset: Optional[int] = Field(None, description="Real offset of the comments")
    items: Optional[List[objects.WallWallComment]] = Field(None)


PhotosGetMarketUploadServer = NewType('PhotosGetMarketUploadServer', objects.BaseUploadServer)

PhotosGetMessagesUploadServer = NewType('PhotosGetMessagesUploadServer', objects.PhotosPhotoUpload)


class PhotosGetNewTags(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[objects.PhotosPhotoXtrTagInfo] = Field(...)


PhotosGetTags = NewType('PhotosGetTags', List[objects.PhotosPhotoTag])

PhotosGetUploadServer = NewType('PhotosGetUploadServer', objects.PhotosPhotoUpload)


class PhotosGetUserPhotosExtended(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[objects.PhotosPhotoFull] = Field(...)


class PhotosGetUserPhotos(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[objects.PhotosPhoto] = Field(...)


PhotosGetWallUploadServer = NewType('PhotosGetWallUploadServer', objects.PhotosPhotoUpload)


class PhotosGetExtended(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[objects.PhotosPhotoFull] = Field(...)


class PhotosGet(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[objects.PhotosPhoto] = Field(...)


PhotosPutTag = NewType('PhotosPutTag', int)

PhotosRestoreComment = NewType('PhotosRestoreComment', objects.BaseBoolInt)

PhotosSaveMarketAlbumPhoto = NewType('PhotosSaveMarketAlbumPhoto', List[objects.PhotosPhoto])

PhotosSaveMarketPhoto = NewType('PhotosSaveMarketPhoto', List[objects.PhotosPhoto])

PhotosSaveMessagesPhoto = NewType('PhotosSaveMessagesPhoto', List[objects.PhotosPhoto])

PhotosSaveOwnerCoverPhoto = NewType('PhotosSaveOwnerCoverPhoto', List[objects.BaseImage])


class PhotosSaveOwnerPhoto(BaseModel):
    photo_hash: str = Field(..., description="Photo hash")
    photo_src: str = Field(..., description="Uploaded image url")
    photo_src_big: Optional[str] = Field(None, description="Uploaded image url")
    photo_src_small: Optional[str] = Field(None, description="Uploaded image url")
    saved: Optional[int] = Field(None, description="Returns 1 if profile photo is saved")
    post_id: Optional[int] = Field(None, description="Created post ID")


PhotosSaveWallPhoto = NewType('PhotosSaveWallPhoto', List[objects.PhotosPhoto])

PhotosSave = NewType('PhotosSave', List[objects.PhotosPhoto])


class PhotosSearch(BaseModel):
    count: Optional[int] = Field(None, description="Total number")
    items: Optional[List[objects.PhotosPhoto]] = Field(None)


PollsAddVote = NewType('PollsAddVote', objects.BaseBoolInt)

PollsCreate = NewType('PollsCreate', objects.PollsPoll)

PollsDeleteVote = NewType('PollsDeleteVote', objects.BaseBoolInt)

PollsGetById = NewType('PollsGetById', objects.PollsPoll)

PollsGetVoters = NewType('PollsGetVoters', List[objects.PollsVoters])


class PrettyCardsCreate(BaseModel):
    owner_id: int = Field(..., description="Owner ID of created pretty card")
    card_id: str = Field(..., description="Card ID of created pretty card")


class PrettyCardsDelete(BaseModel):
    owner_id: int = Field(..., description="Owner ID of deleted pretty card")
    card_id: str = Field(..., description="Card ID of deleted pretty card")
    error: Optional[str] = Field(None, description="Error reason if error happened")


class PrettyCardsEdit(BaseModel):
    owner_id: int = Field(..., description="Owner ID of edited pretty card")
    card_id: str = Field(..., description="Card ID of edited pretty card")


PrettyCardsGetById = NewType('PrettyCardsGetById', List[objects.PrettycardsPrettycard])

PrettyCardsGetUploadUrl = NewType('PrettyCardsGetUploadUrl', str)


class PrettyCardsGet(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[objects.PrettycardsPrettycard] = Field(...)


class SearchGetHints(BaseModel):
    count: int = Field(...)
    items: List[objects.SearchHint] = Field(...)
    suggested_queries: Optional[List[str]] = Field(None)


SecureCheckToken = NewType('SecureCheckToken', objects.SecureTokenChecked)

SecureGetAppBalance = NewType('SecureGetAppBalance', int)

SecureGetSmshistory = NewType('SecureGetSmshistory', List[objects.SecureSmsNotification])

SecureGetTransactionsHistory = NewType('SecureGetTransactionsHistory', List[objects.SecureTransaction])

SecureGetUserLevel = NewType('SecureGetUserLevel', List[objects.SecureLevel])

SecureGiveEventSticker = NewType('SecureGiveEventSticker', List[object])

SecureSendNotification = NewType('SecureSendNotification', List[int])

StatsGetPostReach = NewType('StatsGetPostReach', List[objects.StatsWallpostStat])

StatsGet = NewType('StatsGet', List[objects.StatsPeriod])

StatusGet = NewType('StatusGet', objects.StatusStatus)

StorageGetKeys = NewType('StorageGetKeys', List[str])

StorageGet = NewType('StorageGet', str)

StorageGetV5110 = NewType('StorageGetV5110', List[objects.StorageValue])

StorageGetWithKeys = NewType('StorageGetWithKeys', List[objects.StorageValue])


class StoriesGetBannedExtended(BaseModel):
    count: int = Field(..., description="Stories count")
    items: List[int] = Field(...)
    profiles: List[objects.UsersUserFull] = Field(...)
    groups: List[objects.GroupsGroupFull] = Field(...)


class StoriesGetBanned(BaseModel):
    count: int = Field(..., description="Stories count")
    items: List[int] = Field(...)


class StoriesGetByIdExtended(BaseModel):
    count: int = Field(..., description="Stories count")
    items: List[objects.StoriesStory] = Field(...)
    profiles: List[objects.UsersUserFull] = Field(...)
    groups: List[objects.GroupsGroupFull] = Field(...)


class StoriesGetById(BaseModel):
    count: int = Field(..., description="Stories count")
    items: List[objects.StoriesStory] = Field(...)


class StoriesGetPhotoUploadServer(BaseModel):
    upload_url: str = Field(..., description="Upload URL")
    user_ids: List[int] = Field(..., description="Users ID who can to see story.")


StoriesGetStats = NewType('StoriesGetStats', objects.StoriesStoryStats)


class StoriesGetVideoUploadServer(BaseModel):
    upload_url: str = Field(..., description="Upload URL")
    user_ids: List[int] = Field(..., description="Users ID who can to see story.")


class StoriesGetViewersExtendedV5115(BaseModel):
    count: int = Field(..., description="Viewers count")
    items: List[objects.StoriesViewersItem] = Field(...)
    hidden_reason: Optional[str] = Field(None)


class StoriesGetViewersExtended(BaseModel):
    count: int = Field(..., description="Viewers count")
    items: List[objects.UsersUserFull] = Field(...)


class StoriesGetV5113(BaseModel):
    count: int = Field(...)
    items: List[objects.StoriesFeedItem] = Field(...)
    profiles: Optional[List[objects.UsersUser]] = Field(None)
    groups: Optional[List[objects.GroupsGroup]] = Field(None)
    need_upload_screen: Optional[bool] = Field(None)


class StoriesGet(BaseModel):
    count: int = Field(..., description="Stories count")
    items: List[List[objects.StoriesStory]] = Field(...)
    promo_data: Optional[objects.StoriesPromoBlock] = Field(None)
    profiles: Optional[List[objects.UsersUser]] = Field(None)
    groups: Optional[List[objects.GroupsGroup]] = Field(None)
    need_upload_screen: Optional[bool] = Field(None)


class StoriesUpload(BaseModel):
    upload_result: Optional[str] = Field(None, description="A string hash that is used in the stories.save method")


class StreamingGetServerUrl(BaseModel):
    endpoint: Optional[str] = Field(None, description="Server host")
    key: Optional[str] = Field(None, description="Access key")


class UsersGetFollowersFields(BaseModel):
    count: int = Field(..., description="Total number of available results")
    items: List[objects.UsersUserFull] = Field(...)


class UsersGetFollowers(BaseModel):
    count: int = Field(..., description="Total friends number")
    items: List[int] = Field(...)


class UsersGetSubscriptionsExtended(BaseModel):
    count: int = Field(..., description="Total number of available results")
    items: List[objects.UsersSubscriptionsItem] = Field(...)


class UsersGetSubscriptions(BaseModel):
    users: objects.UsersUsersArray = Field(...)
    groups: objects.GroupsGroupsArray = Field(...)


UsersGet = NewType('UsersGet', List[objects.UsersUserXtrCounters])


class UsersSearch(BaseModel):
    count: Optional[int] = Field(None, description="Total number of available results")
    items: Optional[List[objects.UsersUserFull]] = Field(None)


UtilsCheckLink = NewType('UtilsCheckLink', objects.UtilsLinkChecked)


class UtilsGetLastShortenedLinks(BaseModel):
    count: Optional[int] = Field(None, description="Total number of available results")
    items: Optional[List[objects.UtilsLastShortenedLink]] = Field(None)


UtilsGetLinkStatsExtended = NewType('UtilsGetLinkStatsExtended', objects.UtilsLinkStatsExtended)

UtilsGetLinkStats = NewType('UtilsGetLinkStats', objects.UtilsLinkStats)

UtilsGetServerTime = NewType('UtilsGetServerTime', int)

UtilsGetShortLink = NewType('UtilsGetShortLink', objects.UtilsShortLink)

UtilsResolveScreenName = NewType('UtilsResolveScreenName', objects.UtilsDomainResolved)


class VideoAddAlbum(BaseModel):
    album_id: int = Field(..., description="Created album ID")


VideoCreateComment = NewType('VideoCreateComment', int)

VideoGetAlbumById = NewType('VideoGetAlbumById', objects.VideoVideoAlbumFull)


class VideoGetAlbumsByVideoExtended(BaseModel):
    count: Optional[int] = Field(None, description="Total number")
    items: Optional[List[objects.VideoVideoAlbumFull]] = Field(None)


VideoGetAlbumsByVideo = NewType('VideoGetAlbumsByVideo', List[int])


class VideoGetAlbumsExtended(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[objects.VideoVideoAlbumFull] = Field(...)


class VideoGetAlbums(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[objects.VideoVideoAlbumFull] = Field(...)


class VideoGetCommentsExtended(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[objects.WallWallComment] = Field(...)
    profiles: List[objects.UsersUserMin] = Field(...)
    groups: List[objects.GroupsGroupFull] = Field(...)


class VideoGetComments(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[objects.WallWallComment] = Field(...)


class VideoGetExtended(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[objects.VideoVideoFull] = Field(...)
    profiles: List[objects.UsersUserMin] = Field(...)
    groups: List[objects.GroupsGroupFull] = Field(...)


class VideoGet(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[objects.VideoVideo] = Field(...)


VideoRestoreComment = NewType('VideoRestoreComment', objects.BaseBoolInt)

VideoSave = NewType('VideoSave', objects.VideoSaveResult)


class VideoSearchExtended(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[objects.VideoVideo] = Field(...)
    profiles: List[objects.UsersUserMin] = Field(...)
    groups: List[objects.GroupsGroupFull] = Field(...)


class VideoSearch(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[objects.VideoVideo] = Field(...)


class WallCreateComment(BaseModel):
    comment_id: int = Field(..., description="Created comment ID")


class WallEdit(BaseModel):
    post_id: int = Field(..., description="Edited post ID")


class WallGetByIdExtended(BaseModel):
    items: List[objects.WallWallpostFull] = Field(...)
    profiles: List[objects.UsersUserFull] = Field(...)
    groups: List[objects.GroupsGroupFull] = Field(...)


WallGetById = NewType('WallGetById', List[objects.WallWallpostFull])


class WallGetCommentExtended(BaseModel):
    items: List[objects.WallWallComment] = Field(...)
    profiles: List[objects.UsersUser] = Field(...)
    groups: List[objects.GroupsGroup] = Field(...)


class WallGetComment(BaseModel):
    items: List[objects.WallWallComment] = Field(...)


class WallGetCommentsExtended(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[objects.WallWallComment] = Field(...)
    show_reply_button: Optional[bool] = Field(None)
    can_post: Optional[bool] = Field(None, description="Information whether current user can comment the post")
    groups_can_post: Optional[bool] = Field(None, description="Information whether groups can comment the post")
    current_level_count: Optional[int] = Field(None, description="Count of replies of current level")
    profiles: List[objects.UsersUser] = Field(...)
    groups: List[objects.GroupsGroup] = Field(...)


class WallGetComments(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[objects.WallWallComment] = Field(...)
    can_post: Optional[bool] = Field(None, description="Information whether current user can comment the post")
    groups_can_post: Optional[bool] = Field(None, description="Information whether groups can comment the post")
    current_level_count: Optional[int] = Field(None, description="Count of replies of current level")


class WallGetReposts(BaseModel):
    items: List[objects.WallWallpostFull] = Field(...)
    profiles: List[objects.UsersUser] = Field(...)
    groups: List[objects.GroupsGroup] = Field(...)


class WallGetExtended(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[objects.WallWallpostFull] = Field(...)
    profiles: List[objects.UsersUserFull] = Field(...)
    groups: List[objects.GroupsGroupFull] = Field(...)


class WallGet(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[objects.WallWallpostFull] = Field(...)


class WallPostAdsStealth(BaseModel):
    post_id: int = Field(..., description="Created post ID")


class WallPost(BaseModel):
    post_id: int = Field(..., description="Created post ID")


class WallRepost(BaseModel):
    success: int = Field(...)
    post_id: int = Field(..., description="Created post ID")
    reposts_count: int = Field(..., description="Reposts number")
    likes_count: int = Field(..., description="Reposts number")


class WallSearchExtended(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[objects.WallWallpostFull] = Field(...)
    profiles: List[objects.UsersUserFull] = Field(...)
    groups: List[objects.GroupsGroupFull] = Field(...)


class WallSearch(BaseModel):
    count: int = Field(..., description="Total number")
    items: List[objects.WallWallpostFull] = Field(...)


class WidgetsGetComments(BaseModel):
    count: int = Field(..., description="Total number")
    posts: List[objects.WidgetsWidgetComment] = Field(...)


class WidgetsGetPages(BaseModel):
    count: int = Field(..., description="Total number")
    pages: List[objects.WidgetsWidgetPage] = Field(...)
