from pydantic import BaseModel, Field
from typing import List, Union, Optional
from enum import Enum


class AccountAccountCounters(BaseModel):
    app_requests: Optional[int] = Field(None, description="New app requests number")
    events: Optional[int] = Field(None, description="New events number")
    faves: Optional[int] = Field(None, description="New faves number")
    friends: Optional[int] = Field(None, description="New friends requests number")
    friends_suggestions: Optional[int] = Field(None, description="New friends suggestions number")
    friends_recommendations: Optional[int] = Field(None, description="New friends recommendations number")
    gifts: Optional[int] = Field(None, description="New gifts number")
    groups: Optional[int] = Field(None, description="New groups number")
    menu_discover_badge: Optional[int] = Field(None)
    messages: Optional[int] = Field(None, description="New messages number")
    memories: Optional[int] = Field(None, description="New memories number")
    notes: Optional[int] = Field(None, description="New notes number")
    notifications: Optional[int] = Field(None, description="New notifications number")
    photos: Optional[int] = Field(None, description="New photo tags number")
    sdk: Optional[int] = Field(None, description="New sdk number")


class AccountNameRequestStatus(Enum):
    """Request status"""

    SUCCESS = 'success'
    PROCESSING = 'processing'
    DECLINED = 'declined'
    WAS_ACCEPTED = 'was_accepted'
    WAS_DECLINED = 'was_declined'
    DECLINED_WITH_LINK = 'declined_with_link'
    RESPONSE = 'response'
    RESPONSE_WITH_LINK = 'response_with_link'


class AccountOffer(BaseModel):
    description: Optional[str] = Field(None, description="Offer description")
    id_: Optional[int] = Field(None, alias='id', description="Offer ID")
    img: Optional[str] = Field(None, description="URL of the preview image")
    instruction: Optional[str] = Field(None, description="Instruction how to process the offer")
    instruction_html: Optional[str] = Field(None, description="Instruction how to process the offer (HTML format)")
    price: Optional[int] = Field(None, description="Offer price")
    short_description: Optional[str] = Field(None, description="Offer short description")
    tag: Optional[str] = Field(None, description="Offer tag")
    title: Optional[str] = Field(None, description="Offer title")
    currency_amount: Optional[float] = Field(None, description="Currency amount")
    link_id: Optional[int] = Field(None, description="Link id")
    link_type: Optional[str] = Field(None, description="Link type")


class AccountPushParamsMode(Enum):
    """Settings parameters"""

    ON = 'on'
    OFF = 'off'
    NO_SOUND = 'no_sound'
    NO_TEXT = 'no_text'


class AccountPushParamsOnoff(Enum):
    """Settings parameters"""

    ON = 'on'
    OFF = 'off'


class AccountPushParamsSettings(Enum):
    """Settings parameters"""

    ON = 'on'
    OFF = 'off'
    FR_OF_FR = 'fr_of_fr'


class AccountUserSettingsInterest(BaseModel):
    title: str = Field(...)
    value: str = Field(...)


class AddressesFields(Enum):
    ID = 'id'
    TITLE = 'title'
    ADDRESS = 'address'
    ADDITIONAL_ADDRESS = 'additional_address'
    COUNTRY_ID = 'country_id'
    CITY_ID = 'city_id'
    METRO_STATION_ID = 'metro_station_id'
    LATITUDE = 'latitude'
    LONGITUDE = 'longitude'
    DISTANCE = 'distance'
    WORK_INFO_STATUS = 'work_info_status'
    TIMETABLE = 'timetable'
    PHONE = 'phone'
    TIME_OFFSET = 'time_offset'


class AdsAccessRole(Enum):
    """Current user's role"""

    ADMIN = 'admin'
    MANAGER = 'manager'
    REPORTS = 'reports'


class AdsAccountType(Enum):
    """Account type"""

    GENERAL = 'general'
    AGENCY = 'agency'


class AdsAdApproved(Enum):
    """Review status"""

    NOT_MODERATED = 0
    PENDING_MODERATION = 1
    APPROVED = 2
    REJECTED = 3


class AdsAdCostType(Enum):
    """Cost type"""

    PER_CLICKS = 0
    PER_IMPRESSIONS = 1
    PER_ACTIONS = 2
    PER_IMPRESSIONS_OPTIMIZED = 3


class AdsAdStatus(Enum):
    """Ad atatus"""

    STOPPED = 0
    STARTED = 1
    DELETED = 2


class AdsCampaignStatus(Enum):
    """Campaign status"""

    STOPPED = 0
    STARTED = 1
    DELETED = 2


class AdsCampaignType(Enum):
    """Campaign type"""

    NORMAL = 'normal'
    VK_APPS_MANAGED = 'vk_apps_managed'
    MOBILE_APPS = 'mobile_apps'
    PROMOTED_POSTS = 'promoted_posts'


class AdsClient(BaseModel):
    all_limit: str = Field(..., description="Client's total limit, rubles")
    day_limit: str = Field(..., description="Client's day limit, rubles")
    id_: int = Field(..., alias='id', description="Client ID")
    name: str = Field(..., description="Client name")


class AdsCriteriaSex(Enum):
    """Sex"""

    ANY = 0
    MALE = 1
    FEMALE = 2


class AdsFloodStats(BaseModel):
    left: int = Field(..., description="Requests left")
    refresh: int = Field(..., description="Time to refresh in seconds")


class AdsLinkStatus(BaseModel):
    description: str = Field(..., description="Reject reason")
    redirect_url: str = Field(..., description="URL")
    status: str = Field(..., description="Link status")


class AdsLookalikeRequestSaveAudienceLevel(BaseModel):
    level: Optional[int] = Field(None, description="Save audience level id, which is used in save audience queries")
    audience_count: Optional[int] = Field(None, description="Saved audience audience size for according level")


class AdsMusician(BaseModel):
    id_: int = Field(..., alias='id', description="Targeting music artist ID")
    name: str = Field(..., description="Music artist name")


class AdsObjectType(Enum):
    """Object type"""

    AD = 'ad'
    CAMPAIGN = 'campaign'
    CLIENT = 'client'
    OFFICE = 'office'


class AdsParagraphs(BaseModel):
    paragraph: Optional[str] = Field(None, description="Rules paragraph")


class AdsPromotedPostReach(BaseModel):
    hide: int = Field(..., description="Hides amount")
    id_: int = Field(..., alias='id', description="Object ID from 'ids' parameter")
    join_group: int = Field(..., description="Community joins")
    links: int = Field(..., description="Link clicks")
    reach_subscribers: int = Field(..., description="Subscribers reach")
    reach_total: int = Field(..., description="Total reach")
    report: int = Field(..., description="Reports amount")
    to_group: int = Field(..., description="Community clicks")
    unsubscribe: int = Field(..., description="'Unsubscribe' events amount")
    video_views_100p: Optional[int] = Field(None, description="Video views for 100 percent")
    video_views_25p: Optional[int] = Field(None, description="Video views for 25 percent")
    video_views_3s: Optional[int] = Field(None, description="Video views for 3 seconds")
    video_views_50p: Optional[int] = Field(None, description="Video views for 50 percent")
    video_views_75p: Optional[int] = Field(None, description="Video views for 75 percent")
    video_views_start: Optional[int] = Field(None, description="Video starts")


class AdsStatsAge(BaseModel):
    clicks_rate: Optional[float] = Field(None, description="Clicks rate")
    impressions_rate: Optional[float] = Field(None, description="Impressions rate")
    value: Optional[str] = Field(None, description="Age interval")


class AdsStatsCities(BaseModel):
    clicks_rate: Optional[float] = Field(None, description="Clicks rate")
    impressions_rate: Optional[float] = Field(None, description="Impressions rate")
    name: Optional[str] = Field(None, description="City name")
    value: Optional[int] = Field(None, description="City ID")


class AdsStatsFormat(BaseModel):
    clicks: Optional[int] = Field(None, description="Clicks number")
    day: Optional[str] = Field(None, description="Day as YYYY-MM-DD")
    impressions: Optional[int] = Field(None, description="Impressions number")
    join_rate: Optional[int] = Field(None, description="Events number")
    month: Optional[str] = Field(None, description="Month as YYYY-MM")
    overall: Optional[int] = Field(None, description="1 if period=overall")
    reach: Optional[int] = Field(None, description="Reach ")
    spent: Optional[int] = Field(None, description="Spent funds")
    video_clicks_site: Optional[int] = Field(None, description="Clickthoughs to the advertised site")
    video_views: Optional[int] = Field(None, description="Video views number")
    video_views_full: Optional[int] = Field(None, description="Video views (full video)")
    video_views_half: Optional[int] = Field(None, description="Video views (half of video)")


class AdsStatsSexAge(BaseModel):
    clicks_rate: Optional[float] = Field(None, description="Clicks rate")
    impressions_rate: Optional[float] = Field(None, description="Impressions rate")
    value: Optional[str] = Field(None, description="Sex and age interval")


class AdsStatsSexValue(Enum):
    """Sex"""

    FEMALE = 'f'
    MALE = 'm'


class AdsStatsViewsTimes(BaseModel):
    views_ads_times_1: Optional[int] = Field(None)
    views_ads_times_2: Optional[int] = Field(None)
    views_ads_times_3: Optional[int] = Field(None)
    views_ads_times_4: Optional[int] = Field(None)
    views_ads_times_5: Optional[str] = Field(None)
    views_ads_times_6: Optional[int] = Field(None)
    views_ads_times_7: Optional[int] = Field(None)
    views_ads_times_8: Optional[int] = Field(None)
    views_ads_times_9: Optional[int] = Field(None)
    views_ads_times_10: Optional[int] = Field(None)
    views_ads_times_11_plus: Optional[int] = Field(None)


class AdsTargStats(BaseModel):
    audience_count: int = Field(..., description="Audience")
    recommended_cpc: Optional[float] = Field(None, description="Recommended CPC value for 50% reach (old format)")
    recommended_cpm: Optional[float] = Field(None, description="Recommended CPM value for 50% reach (old format)")
    recommended_cpc_50: Optional[float] = Field(None, description="Recommended CPC value for 50% reach")
    recommended_cpm_50: Optional[float] = Field(None, description="Recommended CPM value for 50% reach")
    recommended_cpc_70: Optional[float] = Field(None, description="Recommended CPC value for 70% reach")
    recommended_cpm_70: Optional[float] = Field(None, description="Recommended CPM value for 70% reach")
    recommended_cpc_90: Optional[float] = Field(None, description="Recommended CPC value for 90% reach")
    recommended_cpm_90: Optional[float] = Field(None, description="Recommended CPM value for 90% reach")


class AdsTargSuggestions(BaseModel):
    id_: Optional[int] = Field(None, alias='id', description="Object ID")
    name: Optional[str] = Field(None, description="Object name")


class AdsTargSuggestionsCities(BaseModel):
    id_: Optional[int] = Field(None, alias='id', description="Object ID")
    name: Optional[str] = Field(None, description="Object name")
    parent: Optional[str] = Field(None, description="Parent object")


class AdsTargSuggestionsRegions(BaseModel):
    id_: Optional[int] = Field(None, alias='id', description="Object ID")
    name: Optional[str] = Field(None, description="Object name")
    type_: Optional[str] = Field(None, alias='type', description="Object type")


class AdsTargSuggestionsSchoolsType(Enum):
    """School type"""

    SCHOOL = 'school'
    UNIVERSITY = 'university'
    FACULTY = 'faculty'
    CHAIR = 'chair'


class AdsTargetGroup(BaseModel):
    audience_count: Optional[int] = Field(None, description="Audience")
    domain: Optional[str] = Field(None, description="Site domain")
    id_: Optional[int] = Field(None, alias='id', description="Group ID")
    lifetime: Optional[int] = Field(None, description="Number of days for user to be in group")
    name: Optional[str] = Field(None, description="Group name")
    pixel: Optional[str] = Field(None, description="Pixel code")


class AppsAppLeaderboardType(Enum):
    """Leaderboard type"""

    NOT_SUPPORTED = 0
    LEVELS = 1
    POINTS = 2


class AppsAppType(Enum):
    """Application type"""

    APP = 'app'
    GAME = 'game'
    SITE = 'site'
    STANDALONE = 'standalone'
    VK_APP = 'vk_app'
    COMMUNITY_APP = 'community_app'
    HTML5_GAME = 'html5_game'
    MINI_APP = 'mini_app'


class AppsLeaderboard(BaseModel):
    level: Optional[int] = Field(None, description="Level")
    points: Optional[int] = Field(None, description="Points number")
    score: Optional[int] = Field(None, description="Score number")
    user_id: int = Field(..., description="User ID")


class AppsScope(BaseModel):
    """Scope description"""

    name: str = Field(..., description="Scope name")
    title: Optional[str] = Field(None, description="Scope title")


class AudioAudio(BaseModel):
    artist: str = Field(..., description="Artist name")
    id_: int = Field(..., alias='id', description="Audio ID")
    title: str = Field(..., description="Title")
    url: Optional[str] = Field(None, description="URL of mp3 file")
    duration: int = Field(..., description="Duration in seconds")
    date: Optional[int] = Field(None, description="Date when uploaded")
    album_id: Optional[int] = Field(None, description="Album ID")
    genre_id: Optional[int] = Field(None, description="Genre ID")
    performer: Optional[str] = Field(None, description="Performer name")


class BaseBoolInt(Enum):
    NO = 0
    YES = 1


class BaseCity(BaseModel):
    id_: int = Field(..., alias='id', description="City ID")
    title: str = Field(..., description="City title")


class BaseCountry(BaseModel):
    id_: int = Field(..., alias='id', description="Country ID")
    title: str = Field(..., description="Country title")


class BaseGeoCoordinates(BaseModel):
    latitude: float = Field(...)
    longitude: float = Field(...)


class BaseGradientPoint(BaseModel):
    color: str = Field(..., description="Hex color code without #")
    position: float = Field(..., description="Point position")


class BaseImage(BaseModel):
    id_: Optional[str] = Field(None, alias='id')
    height: int = Field(..., description="Image height")
    url: str = Field(..., description="Image url")
    width: int = Field(..., description="Image width")


class BaseLinkApplicationStore(BaseModel):
    id_: Optional[float] = Field(None, alias='id', description="Store Id")
    name: Optional[str] = Field(None, description="Store name")


class BaseLinkButtonActionType(Enum):
    """Action type"""

    OPEN_URL = 'open_url'


# object BaseLinkButtonStyle has error in json-schema


class BaseLinkRating(BaseModel):
    reviews_count: Optional[int] = Field(None, description="Count of reviews")
    stars: Optional[float] = Field(None, description="Count of stars")


class BaseMessageError(BaseModel):
    code: Optional[int] = Field(None, description="Error code")
    description: Optional[str] = Field(None, description="Error message")


class BaseObject(BaseModel):
    id_: int = Field(..., alias='id', description="Object ID")
    title: str = Field(..., description="Object title")


class BaseObjectCount(BaseModel):
    count: Optional[int] = Field(None, description="Items count")


class BaseObjectWithName(BaseModel):
    id_: int = Field(..., alias='id', description="Object ID")
    name: str = Field(..., description="Object name")


class BasePlace(BaseModel):
    address: Optional[str] = Field(None, description="Place address")
    checkins: Optional[int] = Field(None, description="Checkins number")
    city: Optional[str] = Field(None, description="City name")
    country: Optional[str] = Field(None, description="Country name")
    created: Optional[int] = Field(None, description="Date of the place creation in Unixtime")
    icon: Optional[str] = Field(None, description="URL of the place's icon")
    id_: Optional[int] = Field(None, alias='id', description="Place ID")
    latitude: Optional[float] = Field(None, description="Place latitude")
    longitude: Optional[float] = Field(None, description="Place longitude")
    title: Optional[str] = Field(None, description="Place title")
    type_: Optional[str] = Field(None, alias='type', description="Place type")


class BasePropertyExists(Enum):
    PROPERTY_EXISTS = 1


class BaseRepostsInfo(BaseModel):
    count: Optional[int] = Field(None, description="Reposts number")
    user_reposted: Optional[int] = Field(None, description="Information whether current user has reposted the post")


class BaseRequestParam(BaseModel):
    key: Optional[str] = Field(None, description="Parameter name")
    value: Optional[str] = Field(None, description="Parameter value")


class BaseSex(Enum):
    UNKNOWN = 0
    FEMALE = 1
    MALE = 2


class BaseStickerAnimation(BaseModel):
    type_: Optional[str] = Field(None, alias='type', description="Type of animation script")
    url: Optional[str] = Field(None, description="URL of animation script")


class BaseUploadServer(BaseModel):
    upload_url: str = Field(..., description="Upload URL")


class BaseUserGroupFields(Enum):
    ABOUT = 'about'
    ACTION_BUTTON = 'action_button'
    ACTIVITIES = 'activities'
    ACTIVITY = 'activity'
    ADDRESSES = 'addresses'
    ADMIN_LEVEL = 'admin_level'
    AGE_LIMITS = 'age_limits'
    AUTHOR_ID = 'author_id'
    BAN_INFO = 'ban_info'
    BDATE = 'bdate'
    BLACKLISTED = 'blacklisted'
    BLACKLISTED_BY_ME = 'blacklisted_by_me'
    BOOKS = 'books'
    CAN_CREATE_TOPIC = 'can_create_topic'
    CAN_MESSAGE = 'can_message'
    CAN_POST = 'can_post'
    CAN_SEE_ALL_POSTS = 'can_see_all_posts'
    CAN_SEE_AUDIO = 'can_see_audio'
    CAN_SEND_FRIEND_REQUEST = 'can_send_friend_request'
    CAN_UPLOAD_VIDEO = 'can_upload_video'
    CAN_WRITE_PRIVATE_MESSAGE = 'can_write_private_message'
    CAREER = 'career'
    CITY = 'city'
    COMMON_COUNT = 'common_count'
    CONNECTIONS = 'connections'
    CONTACTS = 'contacts'
    COUNTERS = 'counters'
    COUNTRY = 'country'
    COVER = 'cover'
    CROP_PHOTO = 'crop_photo'
    DEACTIVATED = 'deactivated'
    DESCRIPTION = 'description'
    DOMAIN = 'domain'
    EDUCATION = 'education'
    EXPORTS = 'exports'
    FINISH_DATE = 'finish_date'
    FIXED_POST = 'fixed_post'
    FOLLOWERS_COUNT = 'followers_count'
    FRIEND_STATUS = 'friend_status'
    GAMES = 'games'
    HAS_MARKET_APP = 'has_market_app'
    HAS_MOBILE = 'has_mobile'
    HAS_PHOTO = 'has_photo'
    HOME_TOWN = 'home_town'
    ID = 'id'
    INTERESTS = 'interests'
    IS_ADMIN = 'is_admin'
    IS_CLOSED = 'is_closed'
    IS_FAVORITE = 'is_favorite'
    IS_FRIEND = 'is_friend'
    IS_HIDDEN_FROM_FEED = 'is_hidden_from_feed'
    IS_MEMBER = 'is_member'
    IS_MESSAGES_BLOCKED = 'is_messages_blocked'
    CAN_SEND_NOTIFY = 'can_send_notify'
    IS_SUBSCRIBED = 'is_subscribed'
    LAST_SEEN = 'last_seen'
    LINKS = 'links'
    LISTS = 'lists'
    MAIDEN_NAME = 'maiden_name'
    MAIN_ALBUM_ID = 'main_album_id'
    MAIN_SECTION = 'main_section'
    MARKET = 'market'
    MEMBER_STATUS = 'member_status'
    MEMBERS_COUNT = 'members_count'
    MILITARY = 'military'
    MOVIES = 'movies'
    MUSIC = 'music'
    NAME = 'name'
    NICKNAME = 'nickname'
    OCCUPATION = 'occupation'
    ONLINE = 'online'
    ONLINE_STATUS = 'online_status'
    PERSONAL = 'personal'
    PHONE = 'phone'
    PHOTO_100 = 'photo_100'
    PHOTO_200 = 'photo_200'
    PHOTO_200_ORIG = 'photo_200_orig'
    PHOTO_400_ORIG = 'photo_400_orig'
    PHOTO_50 = 'photo_50'
    PHOTO_ID = 'photo_id'
    PHOTO_MAX = 'photo_max'
    PHOTO_MAX_ORIG = 'photo_max_orig'
    QUOTES = 'quotes'
    RELATION = 'relation'
    RELATIVES = 'relatives'
    SCHOOLS = 'schools'
    SCREEN_NAME = 'screen_name'
    SEX = 'sex'
    SITE = 'site'
    START_DATE = 'start_date'
    STATUS = 'status'
    TIMEZONE = 'timezone'
    TRENDING = 'trending'
    TV = 'tv'
    TYPE = 'type'
    UNIVERSITIES = 'universities'
    VERIFIED = 'verified'
    WALL_COMMENTS = 'wall_comments'
    WIKI_PAGE = 'wiki_page'
    VK_ADMIN_STATUS = 'vk_admin_status'


class BaseUserId(BaseModel):
    user_id: Optional[int] = Field(None, description="User ID")


class BoardDefaultOrder(Enum):
    """Sort type"""

    DESC_UPDATED = 1
    DESC_CREATED = 2
    ASC_UPDATED = -1
    ASC_CREATED = -2


class CallbackBoardPostDelete(BaseModel):
    topic_owner_id: int = Field(...)
    topic_id: int = Field(...)
    id_: int = Field(..., alias='id')


class CallbackGroupJoinType(Enum):
    JOIN = 'join'
    UNSURE = 'unsure'
    ACCEPTED = 'accepted'
    APPROVED = 'approved'
    REQUEST = 'request'


class CallbackGroupMarket(Enum):
    DISABLED = 0
    OPEN = 1


class CallbackGroupOfficerRole(Enum):
    NONE = 0
    MODERATOR = 1
    EDITOR = 2
    ADMINISTRATOR = 3


class CallbackLikeAddRemove(BaseModel):
    liker_id: int = Field(...)
    object_type: str = Field(...)
    object_owner_id: int = Field(...)
    object_id: int = Field(...)
    post_id: int = Field(...)
    thread_reply_id: Optional[int] = Field(None)


class CallbackMarketComment(BaseModel):
    id_: int = Field(..., alias='id')
    from_id: int = Field(...)
    date: int = Field(...)
    text: Optional[str] = Field(None)
    market_owner_od: Optional[int] = Field(None)
    photo_id: Optional[int] = Field(None)


class CallbackMarketCommentDelete(BaseModel):
    owner_id: int = Field(...)
    id_: int = Field(..., alias='id')
    user_id: int = Field(...)
    item_id: int = Field(...)


class CallbackMessageAllow(BaseModel):
    user_id: int = Field(...)
    key: str = Field(...)


class CallbackMessageDeny(BaseModel):
    user_id: int = Field(...)


class CallbackMessageType(Enum):
    CONFIRMATION = 'confirmation'
    GROUP_CHANGE_PHOTO = 'group_change_photo'
    GROUP_CHANGE_SETTINGS = 'group_change_settings'
    GROUP_OFFICERS_EDIT = 'group_officers_edit'
    LEAD_FORMS_NEW = 'lead_forms_new'
    MARKET_COMMENT_DELETE = 'market_comment_delete'
    MARKET_COMMENT_EDIT = 'market_comment_edit'
    MARKET_COMMENT_RESTORE = 'market_comment_restore'
    MESSAGE_ALLOW = 'message_allow'
    MESSAGE_DENY = 'message_deny'
    MESSAGE_READ = 'message_read'
    MESSAGE_REPLY = 'message_reply'
    MESSAGE_TYPING_STATE = 'message_typing_state'
    MESSAGES_EDIT = 'messages_edit'
    PHOTO_COMMENT_DELETE = 'photo_comment_delete'
    PHOTO_COMMENT_EDIT = 'photo_comment_edit'
    PHOTO_COMMENT_RESTORE = 'photo_comment_restore'
    POLL_VOTE_NEW = 'poll_vote_new'
    USER_BLOCK = 'user_block'
    USER_UNBLOCK = 'user_unblock'
    VIDEO_COMMENT_DELETE = 'video_comment_delete'
    VIDEO_COMMENT_EDIT = 'video_comment_edit'
    VIDEO_COMMENT_RESTORE = 'video_comment_restore'
    WALL_REPLY_DELETE = 'wall_reply_delete'
    WALL_REPLY_RESTORE = 'wall_reply_restore'
    WALL_REPOST = 'wall_repost'


class CallbackPhotoComment(BaseModel):
    id_: int = Field(..., alias='id')
    from_id: int = Field(...)
    date: int = Field(...)
    text: str = Field(...)
    photo_owner_od: int = Field(...)


class CallbackPhotoCommentDelete(BaseModel):
    id_: int = Field(..., alias='id')
    owner_id: int = Field(...)
    user_id: int = Field(...)
    photo_id: int = Field(...)


class CallbackPollVoteNew(BaseModel):
    owner_id: int = Field(...)
    poll_id: int = Field(...)
    option_id: int = Field(...)
    user_id: int = Field(...)


class CallbackQrScan(BaseModel):
    user_id: int = Field(...)
    data: str = Field(...)
    type_: str = Field(..., alias='type')
    subtype: str = Field(...)
    reread: bool = Field(...)


class CallbackUserBlock(BaseModel):
    admin_id: int = Field(...)
    user_id: int = Field(...)
    unblock_date: int = Field(...)
    reason: int = Field(...)
    comment: Optional[str] = Field(None)


class CallbackUserUnblock(BaseModel):
    admin_id: int = Field(...)
    user_id: int = Field(...)
    by_end_date: int = Field(...)


class CallbackVideoComment(BaseModel):
    id_: int = Field(..., alias='id')
    from_id: int = Field(...)
    date: int = Field(...)
    text: str = Field(...)
    video_owner_od: int = Field(...)


class CallbackVideoCommentDelete(BaseModel):
    id_: int = Field(..., alias='id')
    owner_id: int = Field(...)
    user_id: int = Field(...)
    video_id: int = Field(...)


class CallbackWallCommentDelete(BaseModel):
    owner_id: int = Field(...)
    id_: int = Field(..., alias='id')
    user_id: int = Field(...)
    post_id: int = Field(...)


class DatabaseFaculty(BaseModel):
    id_: Optional[int] = Field(None, alias='id', description="Faculty ID")
    title: Optional[str] = Field(None, description="Faculty title")


class DatabaseRegion(BaseModel):
    id_: Optional[int] = Field(None, alias='id', description="Region ID")
    title: Optional[str] = Field(None, description="Region title")


class DatabaseSchool(BaseModel):
    id_: Optional[int] = Field(None, alias='id', description="School ID")
    title: Optional[str] = Field(None, description="School title")


class DatabaseStation(BaseModel):
    city_id: Optional[int] = Field(None, description="City ID")
    color: Optional[str] = Field(None, description="Hex color code without #")
    id_: int = Field(..., alias='id', description="Station ID")
    name: str = Field(..., description="Station name")


class DatabaseUniversity(BaseModel):
    id_: Optional[int] = Field(None, alias='id', description="University ID")
    title: Optional[str] = Field(None, description="University title")


class DocsDocAttachmentType(Enum):
    """Doc attachment type"""

    DOC = 'doc'
    GRAFFITI = 'graffiti'
    AUDIO_MESSAGE = 'audio_message'


class DocsDocPreviewAudioMsg(BaseModel):
    duration: int = Field(..., description="Audio message duration in seconds")
    link_mp3: str = Field(..., description="MP3 file URL")
    link_ogg: str = Field(..., description="OGG file URL")
    waveform: List[int] = Field(...)


class DocsDocPreviewGraffiti(BaseModel):
    src: str = Field(..., description="Graffiti file URL")
    width: int = Field(..., description="Graffiti width")
    height: int = Field(..., description="Graffiti height")


class DocsDocPreviewVideo(BaseModel):
    src: str = Field(..., description="Video URL")
    width: int = Field(..., description="Video's width in pixels")
    height: int = Field(..., description="Video's height in pixels")
    file_size: int = Field(..., description="Video file size in bites")


class DocsDocTypes(BaseModel):
    id_: int = Field(..., alias='id', description="Doc type ID")
    name: str = Field(..., description="Doc type title")
    count: int = Field(..., description="Number of docs")


class DocsDocUploadResponse(BaseModel):
    file: Optional[str] = Field(None, description="Uploaded file data")


class FaveBookmarkType(Enum):
    POST = 'post'
    VIDEO = 'video'
    PRODUCT = 'product'
    ARTICLE = 'article'
    LINK = 'link'


class FavePageType(Enum):
    USER = 'user'
    GROUP = 'group'
    HINTS = 'hints'


class FaveTag(BaseModel):
    id_: Optional[int] = Field(None, alias='id', description="Tag id")
    name: Optional[str] = Field(None, description="Tag name")


class FriendsFriendStatusStatus(Enum):
    """Friend status with the user"""

    NOT_A_FRIEND = 0
    OUTCOMING_REQUEST = 1
    INCOMING_REQUEST = 2
    IS_FRIEND = 3


class FriendsFriendsList(BaseModel):
    id_: int = Field(..., alias='id', description="List ID")
    name: str = Field(..., description="List title")


class FriendsMutualFriend(BaseModel):
    common_count: Optional[int] = Field(None, description="Total mutual friends number")
    common_friends: Optional[List[int]] = Field(None)
    id_: Optional[int] = Field(None, alias='id', description="User ID")


class FriendsRequestsMutual(BaseModel):
    count: Optional[int] = Field(None, description="Total mutual friends number")
    users: Optional[List[int]] = Field(None)


class GiftsGiftPrivacy(Enum):
    """Gift privacy"""

    NAME_AND_MESSAGE_FOR_ALL = 0
    NAME_FOR_ALL = 1
    NAME_AND_MESSAGE_FOR_RECIPIENT_ONLY = 2


class GiftsLayout(BaseModel):
    id_: Optional[int] = Field(None, alias='id', description="Gift ID")
    thumb_512: Optional[str] = Field(None, description="URL of the preview image with 512 px in width")
    thumb_256: Optional[str] = Field(None, description="URL of the preview image with 256 px in width")
    thumb_48: Optional[str] = Field(None, description="URL of the preview image with 48 px in width")
    thumb_96: Optional[str] = Field(None, description="URL of the preview image with 96 px in width")
    stickers_product_id: Optional[int] = Field(None,
                                               description="ID of the sticker pack, if the gift is representing one")
    build_id: Optional[str] = Field(None, description="ID of the build of constructor gift")
    keywords: Optional[str] = Field(None, description="Keywords used for search")


class GroupsAddressTimetableDay(BaseModel):
    """Timetable for one day"""

    break_close_time: Optional[int] = Field(None, description="Close time of the break in minutes")
    break_open_time: Optional[int] = Field(None, description="Start time of the break in minutes")
    close_time: int = Field(..., description="Close time in minutes")
    open_time: int = Field(..., description="Open time in minutes")


class GroupsAddressWorkInfoStatus(Enum):
    """Status of information about timetable"""

    NO_INFORMATION = 'no_information'
    TEMPORARILY_CLOSED = 'temporarily_closed'
    ALWAYS_OPENED = 'always_opened'
    TIMETABLE = 'timetable'
    FOREVER_CLOSED = 'forever_closed'


class GroupsAddressesInfo(BaseModel):
    is_enabled: bool = Field(..., description="Information whether addresses is enabled")
    main_address_id: Optional[int] = Field(None, description="Main address id for group")


class GroupsBanInfoReason(Enum):
    """Ban reason"""

    OTHER = 0
    SPAM = 1
    VERBAL_ABUSE = 2
    STRONG_LANGUAGE = 3
    FLOOD = 4


class GroupsCallbackServer(BaseModel):
    id_: int = Field(..., alias='id')
    title: str = Field(...)
    creator_id: int = Field(...)
    url: str = Field(...)
    secret_key: str = Field(...)
    status: str = Field(...)


class GroupsContactsItem(BaseModel):
    desc: Optional[str] = Field(None, description="Contact description")
    email: Optional[str] = Field(None, description="Contact email")
    phone: Optional[str] = Field(None, description="Contact phone")
    user_id: Optional[int] = Field(None, description="User ID")


class GroupsCountersGroup(BaseModel):
    addresses: Optional[int] = Field(None, description="Addresses number")
    albums: Optional[int] = Field(None, description="Photo albums number")
    audios: Optional[int] = Field(None, description="Audios number")
    audio_playlists: Optional[int] = Field(None, description="Audio playlists number")
    docs: Optional[int] = Field(None, description="Docs number")
    market: Optional[int] = Field(None, description="Market items number")
    photos: Optional[int] = Field(None, description="Photos number")
    topics: Optional[int] = Field(None, description="Topics number")
    videos: Optional[int] = Field(None, description="Videos number")


class GroupsFields(Enum):
    MARKET = 'market'
    MEMBER_STATUS = 'member_status'
    IS_FAVORITE = 'is_favorite'
    IS_SUBSCRIBED = 'is_subscribed'
    CITY = 'city'
    COUNTRY = 'country'
    VERIFIED = 'verified'
    DESCRIPTION = 'description'
    WIKI_PAGE = 'wiki_page'
    MEMBERS_COUNT = 'members_count'
    COUNTERS = 'counters'
    COVER = 'cover'
    CAN_POST = 'can_post'
    CAN_SEE_ALL_POSTS = 'can_see_all_posts'
    ACTIVITY = 'activity'
    FIXED_POST = 'fixed_post'
    CAN_CREATE_TOPIC = 'can_create_topic'
    CAN_UPLOAD_VIDEO = 'can_upload_video'
    HAS_PHOTO = 'has_photo'
    STATUS = 'status'
    MAIN_ALBUM_ID = 'main_album_id'
    LINKS = 'links'
    CONTACTS = 'contacts'
    SITE = 'site'
    MAIN_SECTION = 'main_section'
    TRENDING = 'trending'
    CAN_MESSAGE = 'can_message'
    IS_MARKET_CART_ENABLED = 'is_market_cart_enabled'
    IS_MESSAGES_BLOCKED = 'is_messages_blocked'
    CAN_SEND_NOTIFY = 'can_send_notify'
    ONLINE_STATUS = 'online_status'
    START_DATE = 'start_date'
    FINISH_DATE = 'finish_date'
    AGE_LIMITS = 'age_limits'
    BAN_INFO = 'ban_info'
    ACTION_BUTTON = 'action_button'
    AUTHOR_ID = 'author_id'
    PHONE = 'phone'
    HAS_MARKET_APP = 'has_market_app'
    ADDRESSES = 'addresses'
    LIVE_COVERS = 'live_covers'
    IS_ADULT = 'is_adult'
    CAN_SUBSCRIBE_POSTS = 'can_subscribe_posts'
    WARNING_NOTIFICATION = 'warning_notification'
    MSG_PUSH_ALLOWED = 'msg_push_allowed'
    STORIES_ARCHIVE_COUNT = 'stories_archive_count'
    VIDEO_LIVE_LEVEL = 'video_live_level'
    VIDEO_LIVE_COUNT = 'video_live_count'
    CLIPS_COUNT = 'clips_count'


class GroupsFilter(Enum):
    ADMIN = 'admin'
    EDITOR = 'editor'
    MODER = 'moder'
    ADVERTISER = 'advertiser'
    GROUPS = 'groups'
    PUBLICS = 'publics'
    EVENTS = 'events'
    HAS_ADDRESSES = 'has_addresses'


class GroupsGroupAccess(Enum):
    OPEN = 0
    CLOSED = 1
    PRIVATE = 2


class GroupsGroupAdminLevel(Enum):
    """Level of current user's credentials as manager"""

    MODERATOR = 1
    EDITOR = 2
    ADMINISTRATOR = 3


class GroupsGroupAgeLimits(Enum):
    UNLIMITED = 1
    SIXTEEN_PLUS = 2
    EIGHTEEN_PLUS = 3


class GroupsGroupAttach(BaseModel):
    id_: int = Field(..., alias='id', description="group ID")
    text: str = Field(..., description="text of attach")
    status: str = Field(..., description="activity or category of group")
    size: int = Field(..., description="size of group")
    is_favorite: bool = Field(..., description="is favorite")


class GroupsGroupAudio(Enum):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2


class GroupsGroupCategoryType(BaseModel):
    id_: int = Field(..., alias='id')
    name: str = Field(...)


class GroupsGroupDocs(Enum):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2


class GroupsGroupFullAgeLimits(Enum):
    NO = 1
    OVER_16 = 2
    OVER_18 = 3


class GroupsGroupFullMainSection(Enum):
    """Main section of community"""

    ABSENT = 0
    PHOTOS = 1
    TOPICS = 2
    AUDIO = 3
    VIDEO = 4
    MARKET = 5


class GroupsGroupFullMemberStatus(Enum):
    NOT_A_MEMBER = 0
    MEMBER = 1
    NOT_SURE = 2
    DECLINED = 3
    HAS_SENT_A_REQUEST = 4
    INVITED = 5


class GroupsGroupIsClosed(Enum):
    """Information whether community is closed"""

    OPEN = 0
    CLOSED = 1
    PRIVATE = 2


class GroupsGroupMarketCurrency(Enum):
    RUSSIAN_RUBLES = 643
    UKRAINIAN_HRYVNIA = 980
    KAZAKH_TENGE = 398
    EURO = 978
    US_DOLLARS = 840


class GroupsGroupPhotos(Enum):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2


class GroupsGroupRole(Enum):
    MODERATOR = 'moderator'
    EDITOR = 'editor'
    ADMINISTRATOR = 'administrator'


class GroupsGroupSubject(Enum):
    AUTO = 1
    ACTIVITY_HOLIDAYS = 2
    BUSINESS = 3
    PETS = 4
    HEALTH = 5
    DATING_AND_COMMUNICATION = 6
    GAMES = 7
    IT = 8
    CINEMA = 9
    BEAUTY_AND_FASHION = 10
    COOKING = 11
    ART_AND_CULTURE = 12
    LITERATURE = 13
    MOBILE_SERVICES_AND_INTERNET = 14
    MUSIC = 15
    SCIENCE_AND_TECHNOLOGY = 16
    REAL_ESTATE = 17
    NEWS_AND_MEDIA = 18
    SECURITY = 19
    EDUCATION = 20
    HOME_AND_RENOVATIONS = 21
    POLITICS = 22
    FOOD = 23
    INDUSTRY = 24
    TRAVEL = 25
    WORK = 26
    ENTERTAINMENT = 27
    RELIGION = 28
    FAMILY = 29
    SPORTS = 30
    INSURANCE = 31
    TELEVISION = 32
    GOODS_AND_SERVICES = 33
    HOBBIES = 34
    FINANCE = 35
    PHOTO = 36
    ESOTERICS = 37
    ELECTRONICS_AND_APPLIANCES = 38
    EROTIC = 39
    HUMOR = 40
    SOCIETY_HUMANITIES = 41
    DESIGN_AND_GRAPHICS = 42


class GroupsGroupTopics(Enum):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2


class GroupsGroupType(Enum):
    """Community type"""

    GROUP = 'group'
    PAGE = 'page'
    EVENT = 'event'


class GroupsGroupVideo(Enum):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2


class GroupsGroupWall(Enum):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2
    CLOSED = 3


class GroupsGroupWiki(Enum):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2


class GroupsGroupXtrInvitedByAdminLevel(Enum):
    """Level of current user's credentials as manager"""

    MODERATOR = 1
    EDITOR = 2
    ADMINISTRATOR = 3


class GroupsGroupXtrInvitedByType(Enum):
    """Community type"""

    GROUP = 'group'
    PAGE = 'page'
    EVENT = 'event'


class GroupsGroupsArray(BaseModel):
    count: int = Field(..., description="Communities number")
    items: List[int] = Field(...)


class GroupsLongPollServer(BaseModel):
    key: str = Field(..., description="Long Poll key")
    server: str = Field(..., description="Long Poll server address")
    ts: str = Field(..., description="Number of the last event")


class GroupsMemberRolePermission(Enum):
    ADS = 'ads'


class GroupsMemberRoleStatus(Enum):
    """User's credentials as community admin"""

    MODERATOR = 'moderator'
    EDITOR = 'editor'
    ADMINISTRATOR = 'administrator'
    CREATOR = 'creator'


class GroupsOnlineStatusType(Enum):
    """Type of online status of group"""

    NONE = 'none'
    ONLINE = 'online'
    ANSWER_MARK = 'answer_mark'


class GroupsOwnerXtrBanInfoType(Enum):
    """Owner type"""

    GROUP = 'group'
    PROFILE = 'profile'


class GroupsRoleOptions(Enum):
    """User's credentials as community admin"""

    MODERATOR = 'moderator'
    EDITOR = 'editor'
    ADMINISTRATOR = 'administrator'
    CREATOR = 'creator'


class GroupsSettingsTwitter(BaseModel):
    status: str = Field(...)
    name: Optional[str] = Field(None)


class GroupsSubjectItem(BaseModel):
    id_: int = Field(..., alias='id', description="Subject ID")
    name: str = Field(..., description="Subject title")


class GroupsTokenPermissionSetting(BaseModel):
    name: str = Field(...)
    setting: int = Field(...)


class LeadsCheckedResult(Enum):
    """Information whether user can start the lead"""

    TRUE = 'true'
    FALSE = 'false'


class LeadsLeadDays(BaseModel):
    completed: Optional[int] = Field(None, description="Completed offers number")
    impressions: Optional[int] = Field(None, description="Impressions number")
    spent: Optional[int] = Field(None, description="Amount of spent votes")
    started: Optional[int] = Field(None, description="Started offers number")


class LikesType(Enum):
    POST = 'post'
    COMMENT = 'comment'
    PHOTO = 'photo'
    AUDIO = 'audio'
    VIDEO = 'video'
    NOTE = 'note'
    MARKET = 'market'
    PHOTO_COMMENT = 'photo_comment'
    VIDEO_COMMENT = 'video_comment'
    TOPIC_COMMENT = 'topic_comment'
    MARKET_COMMENT = 'market_comment'
    SITEPAGE = 'sitepage'


class LinkTargetObject(BaseModel):
    type_: Optional[str] = Field(None, alias='type', description="Object type")
    owner_id: Optional[int] = Field(None, description="Owner ID")
    item_id: Optional[int] = Field(None, description="Item ID")


class MarketCurrency(BaseModel):
    id_: int = Field(..., alias='id', description="Currency ID")
    name: str = Field(..., description="Currency sign")


class MarketMarketItemAvailability(Enum):
    """Information whether the item is available"""

    AVAILABLE = 0
    REMOVED = 1
    UNAVAILABLE = 2


class MarketSection(BaseModel):
    id_: int = Field(..., alias='id', description="Section ID")
    name: str = Field(..., description="Section name")


class MessageChatPreview(BaseModel):
    admin_id: Optional[int] = Field(None)
    joined: Optional[bool] = Field(None)
    local_id: Optional[int] = Field(None)
    members: Optional[List[int]] = Field(None)
    members_count: Optional[int] = Field(None)
    title: Optional[str] = Field(None)


class MessagesAudioMessage(BaseModel):
    access_key: Optional[str] = Field(None, description="Access key for audio message")
    duration: int = Field(..., description="Audio message duration in seconds")
    id_: int = Field(..., alias='id', description="Audio message ID")
    link_mp3: str = Field(..., description="MP3 file URL")
    link_ogg: str = Field(..., description="OGG file URL")
    owner_id: int = Field(..., description="Audio message owner ID")
    waveform: List[int] = Field(...)


class MessagesChatRestrictions(BaseModel):
    admins_promote_users: Optional[bool] = Field(None, description="Only admins can promote users to admins")
    only_admins_edit_info: Optional[bool] = Field(None, description="Only admins can change chat info")
    only_admins_edit_pin: Optional[bool] = Field(None, description="Only admins can edit pinned message")
    only_admins_invite: Optional[bool] = Field(None, description="Only admins can invite users to this chat")
    only_admins_kick: Optional[bool] = Field(None, description="Only admins can kick users from this chat")


class MessagesConversationMember(BaseModel):
    can_kick: Optional[bool] = Field(None, description="Is it possible for user to kick this member")
    invited_by: Optional[int] = Field(None)
    is_admin: Optional[bool] = Field(None)
    is_owner: Optional[bool] = Field(None)
    is_message_request: Optional[bool] = Field(None)
    join_date: Optional[int] = Field(None)
    request_date: Optional[int] = Field(None, description="Message request date")
    member_id: int = Field(...)


class MessagesConversationPeerType(Enum):
    """Peer type"""

    CHAT = 'chat'
    EMAIL = 'email'
    USER = 'user'
    GROUP = 'group'


class MessagesGraffiti(BaseModel):
    access_key: Optional[str] = Field(None, description="Access key for graffiti")
    height: int = Field(..., description="Graffiti height")
    id_: int = Field(..., alias='id', description="Graffiti ID")
    owner_id: int = Field(..., description="Graffiti owner ID")
    url: str = Field(..., description="Graffiti URL")
    width: int = Field(..., description="Graffiti width")


class MessagesHistoryMessageAttachmentType(Enum):
    """Attachments type"""

    PHOTO = 'photo'
    VIDEO = 'video'
    AUDIO = 'audio'
    DOC = 'doc'
    LINK = 'link'
    MARKET = 'market'
    WALL = 'wall'
    SHARE = 'share'
    GRAFFITI = 'graffiti'
    AUDIO_MESSAGE = 'audio_message'


class MessagesLongpollParams(BaseModel):
    key: Optional[str] = Field(None, description="Key")
    pts: Optional[int] = Field(None, description="Persistent timestamp")
    server: Optional[str] = Field(None, description="Server URL")
    ts: Optional[str] = Field(None, description="Timestamp")


class MessagesMessageActionPhoto(BaseModel):
    photo_100: str = Field(..., description="URL of the preview image with 100px in width")
    photo_200: str = Field(..., description="URL of the preview image with 200px in width")
    photo_50: str = Field(..., description="URL of the preview image with 50px in width")


class MessagesMessageActionStatus(Enum):
    """Action status"""

    CHAT_PHOTO_UPDATE = 'chat_photo_update'
    CHAT_PHOTO_REMOVE = 'chat_photo_remove'
    CHAT_CREATE = 'chat_create'
    CHAT_TITLE_UPDATE = 'chat_title_update'
    CHAT_INVITE_USER = 'chat_invite_user'
    CHAT_KICK_USER = 'chat_kick_user'
    CHAT_PIN_MESSAGE = 'chat_pin_message'
    CHAT_UNPIN_MESSAGE = 'chat_unpin_message'
    CHAT_INVITE_USER_BY_LINK = 'chat_invite_user_by_link'


class MessagesMessageAttachmentType(Enum):
    """Attachment type"""

    PHOTO = 'photo'
    AUDIO = 'audio'
    VIDEO = 'video'
    DOC = 'doc'
    LINK = 'link'
    MARKET = 'market'
    MARKET_ALBUM = 'market_album'
    GIFT = 'gift'
    STICKER = 'sticker'
    WALL = 'wall'
    WALL_REPLY = 'wall_reply'
    ARTICLE = 'article'
    GRAFFITI = 'graffiti'
    AUDIO_MESSAGE = 'audio_message'


class MessagesMessageRequestData(BaseModel):
    status: Optional[str] = Field(None, description="Status of message request")
    inviter_id: Optional[int] = Field(None, description="Message request sender id")
    request_date: Optional[int] = Field(None, description="Message request date")


class MessagesTemplateActionTypeNames(Enum):
    """Template action type names"""

    TEXT = 'text'
    START = 'start'
    LOCATION = 'location'
    VKPAY = 'vkpay'
    OPEN_APP = 'open_app'
    OPEN_PHOTO = 'open_photo'
    OPEN_LINK = 'open_link'


class NewsfeedCommentsFilters(Enum):
    POST = 'post'
    PHOTO = 'photo'
    VIDEO = 'video'
    TOPIC = 'topic'
    NOTE = 'note'


class NewsfeedFilters(Enum):
    POST = 'post'
    PHOTO = 'photo'
    PHOTO_TAG = 'photo_tag'
    WALL_PHOTO = 'wall_photo'
    FRIEND = 'friend'
    RECOMMENDED_GROUPS = 'recommended_groups'
    NOTE = 'note'
    AUDIO = 'audio'
    VIDEO = 'video'
    AUDIO_PLAYLIST = 'audio_playlist'
    CLIP = 'clip'


class NewsfeedIgnoreItemType(Enum):
    POST_ON_THE_WALL = 'wall'
    TAG_ON_A_PHOTO = 'tag'
    PROFILE_PHOTO = 'profilephoto'
    VIDEO = 'video'
    PHOTO = 'photo'
    AUDIO = 'audio'


class NewsfeedItemPromoButtonAction(BaseModel):
    url: Optional[str] = Field(None)
    type_: Optional[str] = Field(None, alias='type')
    target: Optional[str] = Field(None)


class NewsfeedItemPromoButtonImage(BaseModel):
    width: Optional[int] = Field(None)
    height: Optional[int] = Field(None)
    url: Optional[str] = Field(None)


class NewsfeedItemWallpostFeedbackAnswer(BaseModel):
    title: str = Field(...)
    id_: str = Field(..., alias='id')


class NewsfeedItemWallpostFeedbackType(Enum):
    BUTTONS = 'buttons'
    STARS = 'stars'


class NewsfeedItemWallpostType(Enum):
    """Post type"""

    POST = 'post'
    COPY = 'copy'
    REPLY = 'reply'


class NewsfeedList(BaseModel):
    id_: int = Field(..., alias='id', description="List ID")
    title: str = Field(..., description="List title")


class NewsfeedNewsfeedItemType(Enum):
    """Item type"""

    POST = 'post'
    PHOTO = 'photo'
    PHOTO_TAG = 'photo_tag'
    WALL_PHOTO = 'wall_photo'
    FRIEND = 'friend'
    NOTE = 'note'
    AUDIO = 'audio'
    VIDEO = 'video'
    TOPIC = 'topic'
    DIGEST = 'digest'
    STORIES = 'stories'
    TAGS_SUGGESTIONS = 'tags_suggestions'


class NewsfeedNewsfeedNote(BaseModel):
    comments: Optional[int] = Field(None, description="Comments Number")
    id_: Optional[int] = Field(None, alias='id', description="Note ID")
    owner_id: Optional[int] = Field(None, description="integer")
    title: Optional[str] = Field(None, description="Note title")


class NotesNoteComment(BaseModel):
    date: int = Field(..., description="Date when the comment has beed added in Unixtime")
    id_: int = Field(..., alias='id', description="Comment ID")
    message: str = Field(..., description="Comment text")
    nid: int = Field(..., description="Note ID")
    oid: int = Field(..., description="Note ID")
    reply_to: Optional[int] = Field(None, description="ID of replied comment ")
    uid: int = Field(..., description="Comment author's ID")


# object NotificationsNotificationItem has error in json-schema


class NotificationsReply(BaseModel):
    date: Optional[int] = Field(None, description="Date when the reply has been created in Unixtime")
    id_: Optional[int] = Field(None, alias='id', description="Reply ID")
    text: Optional[int] = Field(None, description="Reply text")


class NotificationsSendMessageError(BaseModel):
    code: Optional[int] = Field(None, description="Error code")
    description: Optional[str] = Field(None, description="Error description")


class OauthError(BaseModel):
    error: str = Field(..., description="Error type")
    error_description: str = Field(..., description="Error description")
    redirect_uri: Optional[str] = Field(None, description="URI for validation")


class OrdersAmountItem(BaseModel):
    amount: Optional[int] = Field(None, description="Votes amount in user's currency")
    description: Optional[str] = Field(None, description="Amount description")
    votes: Optional[str] = Field(None, description="Votes number")


class OrdersOrder(BaseModel):
    amount: Optional[int] = Field(None, description="Amount")
    app_order_id: Optional[int] = Field(None, description="App order ID")
    cancel_transaction_id: Optional[int] = Field(None, description="Cancel transaction ID")
    date: Optional[int] = Field(None, description="Date of creation in Unixtime")
    id_: Optional[int] = Field(None, alias='id', description="Order ID")
    item: Optional[str] = Field(None, description="Order item")
    receiver_id: Optional[int] = Field(None, description="Receiver ID")
    status: Optional[str] = Field(None, description="Order status")
    transaction_id: Optional[int] = Field(None, description="Transaction ID")
    user_id: Optional[int] = Field(None, description="User ID")


class OrdersSubscription(BaseModel):
    cancel_reason: Optional[str] = Field(None, description="Cancel reason")
    create_time: int = Field(..., description="Date of creation in Unixtime")
    id_: int = Field(..., alias='id', description="Subscription ID")
    item_id: str = Field(..., description="Subscription order item")
    next_bill_time: Optional[int] = Field(None, description="Date of next bill in Unixtime")
    pending_cancel: Optional[bool] = Field(None, description="Pending cancel state")
    period: int = Field(..., description="Subscription period")
    period_start_time: int = Field(..., description="Date of last period start in Unixtime")
    price: int = Field(..., description="Subscription price")
    status: str = Field(..., description="Subscription status")
    test_mode: Optional[bool] = Field(None, description="Is test subscription")
    trial_expire_time: Optional[int] = Field(None, description="Date of trial expire in Unixtime")
    update_time: int = Field(..., description="Date of last change in Unixtime")


class OwnerState(BaseModel):
    state: Optional[int] = Field(None)
    description: Optional[str] = Field(None, description="wiki text to describe user state")


class PagesPrivacySettings(Enum):
    COMMUNITY_MANAGERS_ONLY = 0
    COMMUNITY_MEMBERS_ONLY = 1
    EVERYONE = 2


class PagesWikipageHistory(BaseModel):
    id_: int = Field(..., alias='id', description="Version ID")
    length: int = Field(..., description="Page size in bytes")
    date: int = Field(..., description="Date when the page has been edited in Unixtime")
    editor_id: int = Field(..., description="Last editor ID")
    editor_name: str = Field(..., description="Last editor name")


class PhotosImageType(Enum):
    """Photo's type."""

    S = 's'
    M = 'm'
    X = 'x'
    L = 'l'
    O = 'o'
    P = 'p'
    Q = 'q'
    R = 'r'
    Y = 'y'
    Z = 'z'
    W = 'w'


class PhotosMarketAlbumUploadResponse(BaseModel):
    gid: Optional[int] = Field(None, description="Community ID")
    hash_: Optional[str] = Field(None, alias='hash', description="Uploading hash")
    photo: Optional[str] = Field(None, description="Uploaded photo data")
    server: Optional[int] = Field(None, description="Upload server number")


class PhotosMarketUploadResponse(BaseModel):
    crop_data: Optional[str] = Field(None, description="Crop data")
    crop_hash: Optional[str] = Field(None, description="Crop hash")
    group_id: Optional[int] = Field(None, description="Community ID")
    hash_: Optional[str] = Field(None, alias='hash', description="Uploading hash")
    photo: Optional[str] = Field(None, description="Uploaded photo data")
    server: Optional[int] = Field(None, description="Upload server number")


class PhotosMessageUploadResponse(BaseModel):
    hash_: Optional[str] = Field(None, alias='hash', description="Uploading hash")
    photo: Optional[str] = Field(None, description="Uploaded photo data")
    server: Optional[int] = Field(None, description="Upload server number")


class PhotosOwnerUploadResponse(BaseModel):
    hash_: Optional[str] = Field(None, alias='hash', description="Uploading hash")
    photo: Optional[str] = Field(None, description="Uploaded photo data")
    server: Optional[int] = Field(None, description="Upload server number")


class PhotosPhotoSizesType(Enum):
    """Size type"""

    S = 's'
    M = 'm'
    X = 'x'
    O = 'o'
    P = 'p'
    Q = 'q'
    R = 'r'
    K = 'k'
    L = 'l'
    Y = 'y'
    Z = 'z'
    C = 'c'
    W = 'w'


class PhotosPhotoUpload(BaseModel):
    album_id: int = Field(..., description="Album ID")
    upload_url: str = Field(..., description="URL to upload photo")
    fallback_upload_url: Optional[str] = Field(None, description="Fallback URL if upload_url returned error")
    user_id: int = Field(..., description="User ID")
    group_id: Optional[int] = Field(None, description="Group ID")


class PhotosPhotoUploadResponse(BaseModel):
    aid: Optional[int] = Field(None, description="Album ID")
    hash_: Optional[str] = Field(None, alias='hash', description="Uploading hash")
    photos_list: Optional[str] = Field(None, description="Uploaded photos data")
    server: Optional[int] = Field(None, description="Upload server number")


class PhotosTagsSuggestionItemButton(BaseModel):
    title: Optional[str] = Field(None)
    action: Optional[str] = Field(None)
    style: Optional[str] = Field(None)


class PhotosWallUploadResponse(BaseModel):
    hash_: Optional[str] = Field(None, alias='hash', description="Uploading hash")
    photo: Optional[str] = Field(None, description="Uploaded photo data")
    server: Optional[int] = Field(None, description="Upload server number")


class PollsAnswer(BaseModel):
    id_: int = Field(..., alias='id', description="Answer ID")
    rate: float = Field(..., description="Answer rate in percents")
    text: str = Field(..., description="Answer text")
    votes: int = Field(..., description="Votes number")


class PollsFriend(BaseModel):
    id_: int = Field(..., alias='id')


# object PollsPollAnonymous has error in json-schema


class PollsVotersUsers(BaseModel):
    count: Optional[int] = Field(None, description="Votes number")
    items: Optional[List[int]] = Field(None)


class SearchHintSection(Enum):
    """Section title"""

    GROUPS = 'groups'
    EVENTS = 'events'
    PUBLICS = 'publics'
    CORRESPONDENTS = 'correspondents'
    PEOPLE = 'people'
    FRIENDS = 'friends'
    MUTUAL_FRIENDS = 'mutual_friends'


class SearchHintType(Enum):
    """Object type"""

    GROUP = 'group'
    PROFILE = 'profile'
    VK_APP = 'vk_app'
    APP = 'app'
    HTML5_GAME = 'html5_game'


class SecureLevel(BaseModel):
    level: Optional[int] = Field(None, description="Level")
    uid: Optional[int] = Field(None, description="User ID")


class SecureSmsNotification(BaseModel):
    app_id: Optional[str] = Field(None, description="Application ID")
    date: Optional[str] = Field(None, description="Date when message has been sent in Unixtime")
    id_: Optional[str] = Field(None, alias='id', description="Notification ID")
    message: Optional[str] = Field(None, description="Messsage text")
    user_id: Optional[str] = Field(None, description="User ID")


class SecureTokenChecked(BaseModel):
    date: Optional[int] = Field(None, description="Date when access_token has been generated in Unixtime")
    expire: Optional[int] = Field(None, description="Date when access_token will expire in Unixtime")
    success: Optional[int] = Field(None, description="Returns if successfully processed")
    user_id: Optional[int] = Field(None, description="User ID")


class SecureTransaction(BaseModel):
    date: Optional[int] = Field(None, description="Transaction date in Unixtime")
    id_: Optional[int] = Field(None, alias='id', description="Transaction ID")
    uid_from: Optional[int] = Field(None, description="From ID")
    uid_to: Optional[int] = Field(None, description="To ID")
    votes: Optional[int] = Field(None, description="Votes number")


class StatsActivity(BaseModel):
    """Activity stats"""

    comments: Optional[int] = Field(None, description="Comments number")
    copies: Optional[int] = Field(None, description="Reposts number")
    hidden: Optional[int] = Field(None, description="Hidden from news count")
    likes: Optional[int] = Field(None, description="Likes number")
    subscribed: Optional[int] = Field(None, description="New subscribers count")
    unsubscribed: Optional[int] = Field(None, description="Unsubscribed count")


class StatsCity(BaseModel):
    count: Optional[int] = Field(None, description="Visitors number")
    name: Optional[str] = Field(None, description="City name")
    value: Optional[int] = Field(None, description="City ID")


class StatsCountry(BaseModel):
    code: Optional[str] = Field(None, description="Country code")
    count: Optional[int] = Field(None, description="Visitors number")
    name: Optional[str] = Field(None, description="Country name")
    value: Optional[int] = Field(None, description="Country ID")


class StatsSexAge(BaseModel):
    count: Optional[int] = Field(None, description="Visitors number")
    value: str = Field(..., description="Sex/age value")
    reach: Optional[int] = Field(None)
    reach_subscribers: Optional[int] = Field(None)
    count_subscribers: Optional[int] = Field(None)


class StorageValue(BaseModel):
    key: str = Field(...)
    value: str = Field(...)


class StoriesClickableArea(BaseModel):
    x: Optional[int] = Field(None)
    y: Optional[int] = Field(None)


class StoriesPromoBlock(BaseModel):
    """Additional data for promo stories"""

    name: str = Field(..., description="Promo story title")
    photo_50: str = Field(..., description="RL of square photo of the story with 50 pixels in width")
    photo_100: str = Field(..., description="RL of square photo of the story with 100 pixels in width")
    not_animated: bool = Field(..., description="Hide animation for promo story")


class StoriesReplies(BaseModel):
    count: int = Field(..., description="Replies number.")
    new: Optional[int] = Field(None, description="New replies number.")


class StoriesStatLine(BaseModel):
    name: str = Field(...)
    counter: Optional[int] = Field(None)
    is_unavailable: Optional[bool] = Field(None)


class StoriesStoryLink(BaseModel):
    text: str = Field(..., description="Link text")
    url: str = Field(..., description="Link URL")


class StoriesStoryStatsState(Enum):
    """Statistic state"""

    ON = 'on'
    OFF = 'off'
    HIDDEN = 'hidden'


class StoriesStoryType(Enum):
    """Story type."""

    PHOTO = 'photo'
    VIDEO = 'video'
    LIVE_ACTIVE = 'live_active'
    LIVE_FINISHED = 'live_finished'


class StoriesUploadLinkText(Enum):
    TO_STORE = 'to_store'
    VOTE = 'vote'
    MORE = 'more'
    BOOK = 'book'
    ORDER = 'order'
    ENROLL = 'enroll'
    FILL = 'fill'
    SIGNUP = 'signup'
    BUY = 'buy'
    TICKET = 'ticket'
    WRITE = 'write'
    OPEN = 'open'
    LEARN_MORE = 'learn_more'
    VIEW = 'view'
    GO_TO = 'go_to'
    CONTACT = 'contact'
    WATCH = 'watch'
    PLAY = 'play'
    INSTALL = 'install'
    READ = 'read'
    CALENDAR = 'calendar'


class UsersCareer(BaseModel):
    city_id: Optional[int] = Field(None, description="City ID")
    company: Optional[str] = Field(None, description="Company name")
    country_id: Optional[int] = Field(None, description="Country ID")
    from_: Optional[int] = Field(None, alias='from', description="From year")
    group_id: Optional[int] = Field(None, description="Community ID")
    id_: Optional[int] = Field(None, alias='id', description="Career ID")
    position: Optional[str] = Field(None, description="Position")
    until: Optional[int] = Field(None, description="Till year")


class UsersCropPhotoCrop(BaseModel):
    x: Optional[float] = Field(None, description="Coordinate X of the left upper corner")
    x2: Optional[float] = Field(None, description="Coordinate X of the right lower corner")
    y: Optional[float] = Field(None, description="Coordinate Y of the left upper corner")
    y2: Optional[float] = Field(None, description="Coordinate Y of the right lower corner")


class UsersCropPhotoRect(BaseModel):
    x: Optional[float] = Field(None, description="Coordinate X of the left upper corner")
    x2: Optional[float] = Field(None, description="Coordinate X of the right lower corner")
    y: Optional[float] = Field(None, description="Coordinate Y of the left upper corner")
    y2: Optional[float] = Field(None, description="Coordinate Y of the right lower corner")


class UsersExports(BaseModel):
    facebook: Optional[int] = Field(None)
    livejournal: Optional[int] = Field(None)
    twitter: Optional[int] = Field(None)


class UsersFields(Enum):
    PHOTO_ID = 'photo_id'
    VERIFIED = 'verified'
    SEX = 'sex'
    BDATE = 'bdate'
    CITY = 'city'
    COUNTRY = 'country'
    HOME_TOWN = 'home_town'
    HAS_PHOTO = 'has_photo'
    PHOTO_50 = 'photo_50'
    PHOTO_100 = 'photo_100'
    PHOTO_200_ORIG = 'photo_200_orig'
    PHOTO_200 = 'photo_200'
    PHOTO_400_ORIG = 'photo_400_orig'
    PHOTO_MAX = 'photo_max'
    PHOTO_MAX_ORIG = 'photo_max_orig'
    ONLINE = 'online'
    LISTS = 'lists'
    DOMAIN = 'domain'
    HAS_MOBILE = 'has_mobile'
    CONTACTS = 'contacts'
    SITE = 'site'
    EDUCATION = 'education'
    UNIVERSITIES = 'universities'
    SCHOOLS = 'schools'
    STATUS = 'status'
    LAST_SEEN = 'last_seen'
    FOLLOWERS_COUNT = 'followers_count'
    COUNTERS = 'counters'
    COMMON_COUNT = 'common_count'
    OCCUPATION = 'occupation'
    NICKNAME = 'nickname'
    RELATIVES = 'relatives'
    RELATION = 'relation'
    PERSONAL = 'personal'
    CONNECTIONS = 'connections'
    EXPORTS = 'exports'
    WALL_COMMENTS = 'wall_comments'
    ACTIVITIES = 'activities'
    INTERESTS = 'interests'
    MUSIC = 'music'
    MOVIES = 'movies'
    TV = 'tv'
    BOOKS = 'books'
    GAMES = 'games'
    ABOUT = 'about'
    QUOTES = 'quotes'
    CAN_POST = 'can_post'
    CAN_SEE_ALL_POSTS = 'can_see_all_posts'
    CAN_SEE_AUDIO = 'can_see_audio'
    CAN_WRITE_PRIVATE_MESSAGE = 'can_write_private_message'
    CAN_SEND_FRIEND_REQUEST = 'can_send_friend_request'
    IS_FAVORITE = 'is_favorite'
    IS_HIDDEN_FROM_FEED = 'is_hidden_from_feed'
    TIMEZONE = 'timezone'
    SCREEN_NAME = 'screen_name'
    MAIDEN_NAME = 'maiden_name'
    CROP_PHOTO = 'crop_photo'
    IS_FRIEND = 'is_friend'
    FRIEND_STATUS = 'friend_status'
    CAREER = 'career'
    MILITARY = 'military'
    BLACKLISTED = 'blacklisted'
    BLACKLISTED_BY_ME = 'blacklisted_by_me'
    CAN_SUBSCRIBE_POSTS = 'can_subscribe_posts'
    DESCRIPTIONS = 'descriptions'
    TRENDING = 'trending'
    MUTUAL = 'mutual'
    FRIENDSHIP_WEEKS = 'friendship_weeks'
    CAN_INVITE_TO_CHATS = 'can_invite_to_chats'
    STORIES_ARCHIVE_COUNT = 'stories_archive_count'
    VIDEO_LIVE_LEVEL = 'video_live_level'
    VIDEO_LIVE_COUNT = 'video_live_count'
    CLIPS_COUNT = 'clips_count'


class UsersLastSeen(BaseModel):
    platform: Optional[int] = Field(None, description="Type of the platform that used for the last authorization")
    time: Optional[int] = Field(None, description="Last visit date (in Unix time)")


class UsersMilitary(BaseModel):
    country_id: int = Field(..., description="Country ID")
    from_: Optional[int] = Field(None, alias='from', description="From year")
    id_: Optional[int] = Field(None, alias='id', description="Military ID")
    unit: str = Field(..., description="Unit name")
    unit_id: int = Field(..., description="Unit ID")
    until: Optional[int] = Field(None, description="Till year")


class UsersOccupation(BaseModel):
    id_: Optional[int] = Field(None, alias='id', description="ID of school, university, company group")
    name: Optional[str] = Field(None, description="Name of occupation")
    type_: Optional[str] = Field(None, alias='type', description="Type of occupation")


class UsersPersonal(BaseModel):
    alcohol: Optional[int] = Field(None, description="User's views on alcohol")
    inspired_by: Optional[str] = Field(None, description="User's inspired by")
    langs: Optional[List[str]] = Field(None)
    life_main: Optional[int] = Field(None, description="User's personal priority in life")
    people_main: Optional[int] = Field(None, description="User's personal priority in people")
    political: Optional[int] = Field(None, description="User's political views")
    religion: Optional[str] = Field(None, description="User's religion")
    religion_id: Optional[int] = Field(None, description="User's religion id")
    smoking: Optional[int] = Field(None, description="User's views on smoking")


class UsersRelative(BaseModel):
    birth_date: Optional[str] = Field(None, description="Date of child birthday (format dd.mm.yyyy)")
    id_: Optional[int] = Field(None, alias='id', description="Relative ID")
    name: Optional[str] = Field(None, description="Name of relative")
    type_: str = Field(..., alias='type', description="Relative type")


class UsersSchool(BaseModel):
    city: Optional[int] = Field(None, description="City ID")
    class_: Optional[str] = Field(None, alias='class', description="School class letter")
    country: Optional[int] = Field(None, description="Country ID")
    id_: Optional[str] = Field(None, alias='id', description="School ID")
    name: Optional[str] = Field(None, description="School name")
    type_: Optional[int] = Field(None, alias='type', description="School type ID")
    type_str: Optional[str] = Field(None, description="School type name")
    year_from: Optional[int] = Field(None, description="Year the user started to study")
    year_graduated: Optional[int] = Field(None, description="Graduation year")
    year_to: Optional[int] = Field(None, description="Year the user finished to study")


class UsersUniversity(BaseModel):
    chair: Optional[int] = Field(None, description="Chair ID")
    chair_name: Optional[str] = Field(None, description="Chair name")
    city: Optional[int] = Field(None, description="City ID")
    country: Optional[int] = Field(None, description="Country ID")
    education_form: Optional[str] = Field(None, description="Education form")
    education_status: Optional[str] = Field(None, description="Education status")
    faculty: Optional[int] = Field(None, description="Faculty ID")
    faculty_name: Optional[str] = Field(None, description="Faculty name")
    graduation: Optional[int] = Field(None, description="Graduation year")
    id_: Optional[int] = Field(None, alias='id', description="University ID")
    name: Optional[str] = Field(None, description="University name")


class UsersUserConnections(BaseModel):
    skype: str = Field(..., description="User's Skype nickname")
    facebook: str = Field(..., description="User's Facebook account")
    facebook_name: Optional[str] = Field(None, description="User's Facebook name")
    twitter: str = Field(..., description="User's Twitter account")
    livejournal: Optional[str] = Field(None, description="User's Livejournal account")
    instagram: str = Field(..., description="User's Instagram account")


class UsersUserCounters(BaseModel):
    albums: Optional[int] = Field(None, description="Albums number")
    audios: Optional[int] = Field(None, description="Audios number")
    followers: Optional[int] = Field(None, description="Followers number")
    friends: Optional[int] = Field(None, description="Friends number")
    gifts: Optional[int] = Field(None, description="Gifts number")
    groups: Optional[int] = Field(None, description="Communities number")
    notes: Optional[int] = Field(None, description="Notes number")
    online_friends: Optional[int] = Field(None, description="Online friends number")
    pages: Optional[int] = Field(None, description="Public pages number")
    photos: Optional[int] = Field(None, description="Photos number")
    subscriptions: Optional[int] = Field(None, description="Subscriptions number")
    user_photos: Optional[int] = Field(None, description="Number of photos with user")
    user_videos: Optional[int] = Field(None, description="Number of videos with user")
    videos: Optional[int] = Field(None, description="Videos number")


class UsersUserMin(BaseModel):
    deactivated: Optional[str] = Field(None, description="Returns if a profile is deleted or blocked")
    first_name: str = Field(..., description="User first name")
    hidden: Optional[int] = Field(None, description="Returns if a profile is hidden.")
    id_: int = Field(..., alias='id', description="User ID")
    last_name: str = Field(..., description="User last name")
    can_access_closed: Optional[bool] = Field(None)
    is_closed: Optional[bool] = Field(None)


class UsersUserRelation(Enum):
    NOT_SPECIFIED = 0
    SINGLE = 1
    IN_A_RELATIONSHIP = 2
    ENGAGED = 3
    MARRIED = 4
    COMPLICATED = 5
    ACTIVELY_SEARCHING = 6
    IN_LOVE = 7
    IN_A_CIVIL_UNION = 8


class UsersUserType(Enum):
    """Object type"""

    PROFILE = 'profile'


class UsersUsersArray(BaseModel):
    count: int = Field(..., description="Users number")
    items: List[int] = Field(...)


class UtilsDomainResolvedType(Enum):
    """Object type"""

    USER = 'user'
    GROUP = 'group'
    APPLICATION = 'application'
    PAGE = 'page'


class UtilsLastShortenedLink(BaseModel):
    access_key: Optional[str] = Field(None, description="Access key for private stats")
    key: Optional[str] = Field(None, description="Link key (characters after vk.cc/)")
    short_url: Optional[str] = Field(None, description="Short link URL")
    timestamp: Optional[int] = Field(None, description="Creation time in Unixtime")
    url: Optional[str] = Field(None, description="Full URL")
    views: Optional[int] = Field(None, description="Total views number")


class UtilsLinkCheckedStatus(Enum):
    """Link status"""

    NOT_BANNED = 'not_banned'
    BANNED = 'banned'
    PROCESSING = 'processing'


class UtilsShortLink(BaseModel):
    access_key: Optional[str] = Field(None, description="Access key for private stats")
    key: Optional[str] = Field(None, description="Link key (characters after vk.cc/)")
    short_url: Optional[str] = Field(None, description="Short link URL")
    url: Optional[str] = Field(None, description="Full URL")


class UtilsStats(BaseModel):
    timestamp: Optional[int] = Field(None, description="Start time")
    views: Optional[int] = Field(None, description="Total views number")


class UtilsStatsCity(BaseModel):
    city_id: Optional[int] = Field(None, description="City ID")
    views: Optional[int] = Field(None, description="Views number")


class UtilsStatsCountry(BaseModel):
    country_id: Optional[int] = Field(None, description="Country ID")
    views: Optional[int] = Field(None, description="Views number")


class UtilsStatsSexAge(BaseModel):
    age_range: Optional[str] = Field(None, description="Age denotation")
    female: Optional[int] = Field(None, description=" Views by female users")
    male: Optional[int] = Field(None, description=" Views by male users")


class VideoRestrictionButton(BaseModel):
    """Video restriction button"""

    action: Optional[str] = Field(None)
    title: Optional[str] = Field(None)


class VideoSaveResult(BaseModel):
    access_key: Optional[str] = Field(None, description="Video access key")
    description: Optional[str] = Field(None, description="Video description")
    owner_id: Optional[int] = Field(None, description="Video owner ID")
    title: Optional[str] = Field(None, description="Video title")
    upload_url: Optional[str] = Field(None, description="URL for the video uploading")
    video_id: Optional[int] = Field(None, description="Video ID")


class VideoVideoFiles(BaseModel):
    external: Optional[str] = Field(None, description="URL of the external player")
    mp4_240: Optional[str] = Field(None, description="URL of the mpeg4 file with 240p quality")
    mp4_360: Optional[str] = Field(None, description="URL of the mpeg4 file with 360p quality")
    mp4_480: Optional[str] = Field(None, description="URL of the mpeg4 file with 480p quality")
    mp4_720: Optional[str] = Field(None, description="URL of the mpeg4 file with 720p quality")
    mp4_1080: Optional[str] = Field(None, description="URL of the mpeg4 file with 1080p quality")
    flv_320: Optional[str] = Field(None, description="URL of the flv file with 320p quality")


class WallAppPost(BaseModel):
    id_: Optional[int] = Field(None, alias='id', description="Application ID")
    name: Optional[str] = Field(None, description="Application name")
    photo_130: Optional[str] = Field(None, description="URL of the preview image with 130 px in width")
    photo_604: Optional[str] = Field(None, description="URL of the preview image with 604 px in width")


class WallAttachedNote(BaseModel):
    comments: int = Field(..., description="Comments number")
    date: int = Field(..., description="Date when the note has been created in Unixtime")
    id_: int = Field(..., alias='id', description="Note ID")
    owner_id: int = Field(..., description="Note owner's ID")
    read_comments: int = Field(..., description="Read comments number")
    title: str = Field(..., description="Note title")
    view_url: str = Field(..., description="URL of the page with note preview")


class WallCarouselBase(BaseModel):
    carousel_offset: Optional[int] = Field(None, description="Index of current carousel element")


class WallCommentAttachmentType(Enum):
    """Attachment type"""

    PHOTO = 'photo'
    AUDIO = 'audio'
    VIDEO = 'video'
    DOC = 'doc'
    LINK = 'link'
    NOTE = 'note'
    PAGE = 'page'
    MARKET_MARKET_ALBUM = 'market_market_album'
    MARKET = 'market'
    STICKER = 'sticker'


class WallGraffiti(BaseModel):
    id_: Optional[int] = Field(None, alias='id', description="Graffiti ID")
    owner_id: Optional[int] = Field(None, description="Graffiti owner's ID")
    photo_200: Optional[str] = Field(None, description="URL of the preview image with 200 px in width")
    photo_586: Optional[str] = Field(None, description="URL of the preview image with 586 px in width")


class WallPostCopyright(BaseModel):
    id_: Optional[int] = Field(None, alias='id')
    link: str = Field(...)
    name: str = Field(...)
    type_: str = Field(..., alias='type')


class WallPostSourceType(Enum):
    """Type of post source"""

    VK = 'vk'
    WIDGET = 'widget'
    API = 'api'
    RSS = 'rss'
    SMS = 'sms'


class WallPostType(Enum):
    """Post type"""

    POST = 'post'
    COPY = 'copy'
    REPLY = 'reply'
    POSTPONE = 'postpone'
    SUGGEST = 'suggest'


class WallPostedPhoto(BaseModel):
    id_: Optional[int] = Field(None, alias='id', description="Photo ID")
    owner_id: Optional[int] = Field(None, description="Photo owner's ID")
    photo_130: Optional[str] = Field(None, description="URL of the preview image with 130 px in width")
    photo_604: Optional[str] = Field(None, description="URL of the preview image with 604 px in width")


class WallViews(BaseModel):
    count: Optional[int] = Field(None, description="Count")


class WallWallpostAttachmentType(Enum):
    """Attachment type"""

    PHOTO = 'photo'
    POSTED_PHOTO = 'posted_photo'
    AUDIO = 'audio'
    VIDEO = 'video'
    DOC = 'doc'
    LINK = 'link'
    GRAFFITI = 'graffiti'
    NOTE = 'note'
    APP = 'app'
    POLL = 'poll'
    PAGE = 'page'
    ALBUM = 'album'
    PHOTOS_LIST = 'photos_list'
    MARKET_MARKET_ALBUM = 'market_market_album'
    MARKET = 'market'
    EVENT = 'event'


class WidgetsCommentMediaType(Enum):
    """Media type"""

    AUDIO = 'audio'
    PHOTO = 'photo'
    VIDEO = 'video'


class WidgetsWidgetLikes(BaseModel):
    count: Optional[int] = Field(None, description="Likes number")


class AccountInfo(BaseModel):
    wishlists_ae_promo_banner_show: Optional[BaseBoolInt] = Field(None)
    two_fa_required: Optional[BaseBoolInt] = Field(None, alias='2fa_required',
                                                   description="Two factor authentication is enabled")
    country: Optional[str] = Field(None, description="Country code")
    https_required: Optional[BaseBoolInt] = Field(None, description="Information whether HTTPS-only is enabled")
    intro: Optional[BaseBoolInt] = Field(None, description="Information whether user has been processed intro")
    show_vk_apps_intro: Optional[bool] = Field(None)
    mini_apps_ads_slot_id: Optional[int] = Field(None, description="Ads slot id for MyTarget")
    qr_promotion: Optional[int] = Field(None)
    link_redirects: Optional[str] = Field(None)
    lang: Optional[int] = Field(None, description="Language ID")
    no_wall_replies: Optional[BaseBoolInt] = Field(None,
                                                   description="Information whether wall comments should be hidden")
    own_posts_default: Optional[BaseBoolInt] = Field(None,
                                                     description="Information whether only owners posts should be "
                                                                 "shown")
    subscriptions: Optional[List[int]] = Field(None)


class AccountNameRequest(BaseModel):
    first_name: Optional[str] = Field(None, description="First name in request")
    id_: Optional[int] = Field(None, alias='id', description="Request ID needed to cancel the request")
    last_name: Optional[str] = Field(None, description="Last name in request")
    status: Optional[AccountNameRequestStatus] = Field(None)
    lang: Optional[str] = Field(None, description="Text to display to user")
    link_href: Optional[str] = Field(None, description="href for link in lang field")
    link_label: Optional[str] = Field(None, description="label to display for link in lang field")


class AccountPushConversationsItem(BaseModel):
    disabled_until: int = Field(..., description="Time until that notifications are disabled in seconds")
    peer_id: int = Field(..., description="Peer ID")
    sound: BaseBoolInt = Field(..., description="Information whether the sound are enabled")


class AccountPushParams(BaseModel):
    msg: Optional[List[AccountPushParamsMode]] = Field(None)
    chat: Optional[List[AccountPushParamsMode]] = Field(None)
    like: Optional[List[AccountPushParamsSettings]] = Field(None)
    repost: Optional[List[AccountPushParamsSettings]] = Field(None)
    comment: Optional[List[AccountPushParamsSettings]] = Field(None)
    mention: Optional[List[AccountPushParamsSettings]] = Field(None)
    reply: Optional[List[AccountPushParamsOnoff]] = Field(None)
    new_post: Optional[List[AccountPushParamsOnoff]] = Field(None)
    wall_post: Optional[List[AccountPushParamsOnoff]] = Field(None)
    wall_publish: Optional[List[AccountPushParamsOnoff]] = Field(None)
    friend: Optional[List[AccountPushParamsOnoff]] = Field(None)
    friend_found: Optional[List[AccountPushParamsOnoff]] = Field(None)
    friend_accepted: Optional[List[AccountPushParamsOnoff]] = Field(None)
    group_invite: Optional[List[AccountPushParamsOnoff]] = Field(None)
    group_accepted: Optional[List[AccountPushParamsOnoff]] = Field(None)
    birthday: Optional[List[AccountPushParamsOnoff]] = Field(None)
    event_soon: Optional[List[AccountPushParamsOnoff]] = Field(None)
    app_request: Optional[List[AccountPushParamsOnoff]] = Field(None)
    sdk_open: Optional[List[AccountPushParamsOnoff]] = Field(None)


class AccountUserSettingsInterests(BaseModel):
    activities: Optional[AccountUserSettingsInterest] = Field(None)
    interests: Optional[AccountUserSettingsInterest] = Field(None)
    music: Optional[AccountUserSettingsInterest] = Field(None)
    tv: Optional[AccountUserSettingsInterest] = Field(None)
    movies: Optional[AccountUserSettingsInterest] = Field(None)
    books: Optional[AccountUserSettingsInterest] = Field(None)
    games: Optional[AccountUserSettingsInterest] = Field(None)
    quotes: Optional[AccountUserSettingsInterest] = Field(None)
    about: Optional[AccountUserSettingsInterest] = Field(None)


class AdsAccesses(BaseModel):
    client_id: Optional[str] = Field(None, description="Client ID")
    role: Optional[AdsAccessRole] = Field(None)


class AdsAccount(BaseModel):
    access_role: AdsAccessRole = Field(...)
    account_id: int = Field(..., description="Account ID")
    account_status: BaseBoolInt = Field(..., description="Information whether account is active")
    account_type: AdsAccountType = Field(...)


class AdsAd(BaseModel):
    ad_format: int = Field(..., description="Ad format")
    ad_platform: Optional[Union[int, str]] = Field(None, description="Ad platform")
    all_limit: int = Field(..., description="Total limit")
    approved: AdsAdApproved = Field(...)
    campaign_id: int = Field(..., description="Campaign ID")
    category1_id: Optional[int] = Field(None, description="Category ID")
    category2_id: Optional[int] = Field(None, description="Additional category ID")
    cost_type: AdsAdCostType = Field(...)
    cpc: Optional[int] = Field(None, description="Cost of a click, kopecks")
    cpm: Optional[int] = Field(None, description="Cost of 1000 impressions, kopecks")
    cpa: Optional[int] = Field(None, description="Cost of an action, kopecks")
    ocpm: Optional[int] = Field(None, description="Cost of 1000 impressions optimized, kopecks")
    autobidding_max_cost: Optional[int] = Field(None, description="Max cost of target actions for autobidding, kopecks")
    disclaimer_medical: Optional[BaseBoolInt] = Field(None, description="Information whether disclaimer is enabled")
    disclaimer_specialist: Optional[BaseBoolInt] = Field(None, description="Information whether disclaimer is enabled")
    disclaimer_supplements: Optional[BaseBoolInt] = Field(None, description="Information whether disclaimer is enabled")
    id_: int = Field(..., alias='id', description="Ad ID")
    impressions_limit: Optional[int] = Field(None, description="Impressions limit")
    impressions_limited: Optional[BaseBoolInt] = Field(None, description="Information whether impressions are limited")
    name: str = Field(..., description="Ad title")
    status: AdsAdStatus = Field(...)
    video: Optional[BaseBoolInt] = Field(None, description="Information whether the ad is a video")


class AdsAdLayout(BaseModel):
    ad_format: int = Field(..., description="Ad format")
    campaign_id: int = Field(..., description="Campaign ID")
    cost_type: AdsAdCostType = Field(...)
    description: str = Field(..., description="Ad description")
    id_: int = Field(..., alias='id', description="Ad ID")
    image_src: str = Field(..., description="Image URL")
    image_src_2x: Optional[str] = Field(None, description="URL of the preview image in double size")
    link_domain: Optional[str] = Field(None, description="Domain of advertised object")
    link_url: str = Field(..., description="URL of advertised object")
    preview_link: Optional[Union[int, str]] = Field(None,
                                                    description="link to preview an ad as it is shown on the website")
    title: str = Field(..., description="Ad title")
    video: Optional[BaseBoolInt] = Field(None, description="Information whether the ad is a video")


class AdsCampaign(BaseModel):
    all_limit: str = Field(..., description="Campaign's total limit, rubles")
    day_limit: str = Field(..., description="Campaign's day limit, rubles")
    id_: int = Field(..., alias='id', description="Campaign ID")
    name: str = Field(..., description="Campaign title")
    start_time: int = Field(..., description="Campaign start time, as Unixtime")
    status: AdsCampaignStatus = Field(...)
    stop_time: int = Field(..., description="Campaign stop time, as Unixtime")
    type_: AdsCampaignType = Field(..., alias='type')


class AdsCategory(BaseModel):
    id_: int = Field(..., alias='id', description="Category ID")
    name: str = Field(..., description="Category name")
    subcategories: Optional[List[BaseObjectWithName]] = Field(None)


class AdsCriteria(BaseModel):
    age_from: Optional[int] = Field(None, description="Age from")
    age_to: Optional[int] = Field(None, description="Age to")
    apps: Optional[str] = Field(None, description="Apps IDs")
    apps_not: Optional[str] = Field(None, description="Apps IDs to except")
    birthday: Optional[int] = Field(None, description="Days to birthday")
    cities: Optional[str] = Field(None, description="Cities IDs")
    cities_not: Optional[str] = Field(None, description="Cities IDs to except")
    country: Optional[int] = Field(None, description="Country ID")
    districts: Optional[str] = Field(None, description="Districts IDs")
    groups: Optional[str] = Field(None, description="Communities IDs")
    interest_categories: Optional[str] = Field(None, description="Interests categories IDs")
    interests: Optional[str] = Field(None, description="Interests")
    paying: Optional[BaseBoolInt] = Field(None,
                                          description="Information whether the user has proceeded VK payments before")
    positions: Optional[str] = Field(None, description="Positions IDs")
    religions: Optional[str] = Field(None, description="Religions IDs")
    retargeting_groups: Optional[str] = Field(None, description="Retargeting groups IDs")
    retargeting_groups_not: Optional[str] = Field(None, description="Retargeting groups IDs to except")
    school_from: Optional[int] = Field(None, description="School graduation year from")
    school_to: Optional[int] = Field(None, description="School graduation year to")
    schools: Optional[str] = Field(None, description="Schools IDs")
    sex: Optional[AdsCriteriaSex] = Field(None)
    stations: Optional[str] = Field(None, description="Stations IDs")
    statuses: Optional[str] = Field(None, description="Relationship statuses")
    streets: Optional[str] = Field(None, description="Streets IDs")
    travellers: Optional[BasePropertyExists] = Field(None, description="Travellers only")
    uni_from: Optional[int] = Field(None, description="University graduation year from")
    uni_to: Optional[int] = Field(None, description="University graduation year to")
    user_browsers: Optional[str] = Field(None, description="Browsers")
    user_devices: Optional[str] = Field(None, description="Devices")
    user_os: Optional[str] = Field(None, description="Operating systems")


class AdsLookalikeRequest(BaseModel):
    id_: int = Field(..., alias='id', description="Lookalike request ID")
    create_time: int = Field(..., description="Lookalike request create time, as Unixtime")
    update_time: int = Field(..., description="Lookalike request update time, as Unixtime")
    scheduled_delete_time: Optional[int] = Field(None,
                                                 description="Time by which lookalike request would be deleted, "
                                                             "as Unixtime")
    status: str = Field(..., description="Lookalike request status")
    source_type: str = Field(..., description="Lookalike request source type")
    source_retargeting_group_id: Optional[int] = Field(None,
                                                       description="Retargeting group id, which was used as lookalike "
                                                                   "seed")
    source_name: Optional[str] = Field(None, description="Lookalike request seed name (retargeting group name)")
    audience_count: Optional[int] = Field(None, description="Lookalike request seed audience size")
    save_audience_levels: Optional[List[AdsLookalikeRequestSaveAudienceLevel]] = Field(None)


class AdsRules(BaseModel):
    paragraphs: Optional[List[AdsParagraphs]] = Field(None)
    title: Optional[str] = Field(None, description="Comment")


class AdsStats(BaseModel):
    id_: Optional[int] = Field(None, alias='id', description="Object ID")
    stats: Optional[AdsStatsFormat] = Field(None)
    type_: Optional[AdsObjectType] = Field(None, alias='type')
    views_times: Optional[AdsStatsViewsTimes] = Field(None)


class AdsStatsSex(BaseModel):
    clicks_rate: Optional[float] = Field(None, description="Clicks rate")
    impressions_rate: Optional[float] = Field(None, description="Impressions rate")
    value: Optional[AdsStatsSexValue] = Field(None)


class AdsTargSuggestionsSchools(BaseModel):
    desc: Optional[str] = Field(None, description="Full school title")
    id_: Optional[int] = Field(None, alias='id', description="School ID")
    name: Optional[str] = Field(None, description="School title")
    parent: Optional[str] = Field(None, description="City name")
    type_: Optional[AdsTargSuggestionsSchoolsType] = Field(None, alias='type')


class AppsAppMin(BaseModel):
    type_: AppsAppType = Field(..., alias='type')
    id_: int = Field(..., alias='id', description="Application ID")
    title: str = Field(..., description="Application title")
    author_owner_id: Optional[int] = Field(None, description="Application author's ID")
    is_installed: Optional[bool] = Field(None, description="Is application installed")
    icon_139: Optional[str] = Field(None, description="URL of the app icon with 139 px in width")
    icon_150: Optional[str] = Field(None, description="URL of the app icon with 150 px in width")
    icon_278: Optional[str] = Field(None, description="URL of the app icon with 278 px in width")
    icon_576: Optional[str] = Field(None, description="URL of the app icon with 576 px in width")
    background_loader_color: Optional[str] = Field(None, description="Hex color code without hash sign")
    loader_icon: Optional[str] = Field(None, description="SVG data")
    icon_75: Optional[str] = Field(None, description="URL of the app icon with 75 px in width")


class BaseCommentsInfo(BaseModel):
    can_post: Optional[BaseBoolInt] = Field(None, description="Information whether current user can comment the post")
    count: Optional[int] = Field(None, description="Comments number")
    groups_can_post: Optional[bool] = Field(None, description="Information whether groups can comment the post")


class BaseError(BaseModel):
    error_code: Optional[int] = Field(None, description="Error code")
    error_msg: Optional[str] = Field(None, description="Error message")
    request_params: Optional[List[BaseRequestParam]] = Field(None)


class BaseGeo(BaseModel):
    coordinates: Optional[BaseGeoCoordinates] = Field(None)
    place: Optional[BasePlace] = Field(None)
    showmap: Optional[int] = Field(None, description="Information whether a map is showed")
    type_: Optional[str] = Field(None, alias='type', description="Place type")


class BaseLikes(BaseModel):
    count: Optional[int] = Field(None, description="Likes number")
    user_likes: Optional[BaseBoolInt] = Field(None, description="Information whether current user likes the photo")


class BaseLikesInfo(BaseModel):
    can_like: BaseBoolInt = Field(..., description="Information whether current user can like the post")
    can_publish: Optional[BaseBoolInt] = Field(None, description="Information whether current user can repost")
    count: int = Field(..., description="Likes number")
    user_likes: int = Field(..., description="Information whether current uer has liked the post")


class BaseLinkApplication(BaseModel):
    app_id: Optional[float] = Field(None, description="Application Id")
    store: Optional[BaseLinkApplicationStore] = Field(None)


class BaseLinkButtonAction(BaseModel):
    type_: Optional[BaseLinkButtonActionType] = Field(None, alias='type')
    url: Optional[str] = Field(None, description="Action URL")
    consume_reason: Optional[str] = Field(None)


class BaseSticker(BaseModel):
    sticker_id: Optional[int] = Field(None, description="Sticker ID")
    product_id: Optional[int] = Field(None, description="Pack ID")
    images: Optional[List[BaseImage]] = Field(None)
    images_with_background: Optional[List[BaseImage]] = Field(None)
    animation_url: Optional[str] = Field(None, description="URL of sticker animation script")
    animations: Optional[List[BaseStickerAnimation]] = Field(None,
                                                             description="Array of sticker animation script objects")
    is_allowed: Optional[bool] = Field(None, description="Information whether the sticker is allowed")


class BoardTopic(BaseModel):
    comments: Optional[int] = Field(None, description="Comments number")
    created: Optional[int] = Field(None, description="Date when the topic has been created in Unixtime")
    created_by: Optional[int] = Field(None, description="Creator ID")
    id_: Optional[int] = Field(None, alias='id', description="Topic ID")
    is_closed: Optional[BaseBoolInt] = Field(None, description="Information whether the topic is closed")
    is_fixed: Optional[BaseBoolInt] = Field(None, description="Information whether the topic is fixed")
    title: Optional[str] = Field(None, description="Topic title")
    updated: Optional[int] = Field(None, description="Date when the topic has been updated in Unixtime")
    updated_by: Optional[int] = Field(None, description="ID of user who updated the topic")


class BoardTopicPoll(BaseModel):
    answer_id: int = Field(..., description="Current user's answer ID")
    answers: List[PollsAnswer] = Field(...)
    created: int = Field(..., description="Date when poll has been created in Unixtime")
    is_closed: Optional[BaseBoolInt] = Field(None, description="Information whether the poll is closed")
    owner_id: int = Field(..., description="Poll owner's ID")
    poll_id: int = Field(..., description="Poll ID")
    question: str = Field(..., description="Poll question")
    votes: str = Field(..., description="Votes number")


class CallbackConfirmationMessage(BaseModel):
    type_: CallbackMessageType = Field(..., alias='type')
    group_id: int = Field(...)
    secret: str = Field(...)


class CallbackGroupChangeSettings(BaseModel):
    user_id: int = Field(...)
    self: BaseBoolInt = Field(...)


class CallbackGroupJoin(BaseModel):
    user_id: int = Field(...)
    join_type: CallbackGroupJoinType = Field(...)


class CallbackGroupLeave(BaseModel):
    user_id: Optional[int] = Field(None)
    self: Optional[BaseBoolInt] = Field(None)


class CallbackGroupOfficersEdit(BaseModel):
    admin_id: int = Field(...)
    user_id: int = Field(...)
    level_old: CallbackGroupOfficerRole = Field(...)
    level_new: CallbackGroupOfficerRole = Field(...)


class CallbackGroupSettingsChanges(BaseModel):
    title: Optional[str] = Field(None)
    description: Optional[str] = Field(None)
    access: Optional[GroupsGroupIsClosed] = Field(None)
    screen_name: Optional[str] = Field(None)
    public_category: Optional[int] = Field(None)
    public_subcategory: Optional[int] = Field(None)
    age_limits: Optional[GroupsGroupFullAgeLimits] = Field(None)
    website: Optional[str] = Field(None)
    enable_status_default: Optional[GroupsGroupWall] = Field(None)
    enable_audio: Optional[GroupsGroupAudio] = Field(None)
    enable_video: Optional[GroupsGroupVideo] = Field(None)
    enable_photo: Optional[GroupsGroupPhotos] = Field(None)
    enable_market: Optional[CallbackGroupMarket] = Field(None)


class CallbackMessageBase(BaseModel):
    type_: CallbackMessageType = Field(..., alias='type')
    object_: str = Field(..., alias='object')
    group_id: int = Field(...)


class DatabaseCity(BaseObject):
    area: Optional[str] = Field(None, description="Area title")
    region: Optional[str] = Field(None, description="Region title")
    important: Optional[BaseBoolInt] = Field(None,
                                             description="Information whether the city is included in important "
                                                         "cities list")


class DocsDocPreviewPhotoSizes(BaseModel):
    src: str = Field(..., description="URL of the image")
    width: int = Field(..., description="Width in px")
    height: int = Field(..., description="Height in px")
    type_: PhotosPhotoSizesType = Field(..., alias='type')


class EventsEventAttach(BaseModel):
    address: Optional[str] = Field(None, description="address of event")
    button_text: str = Field(..., description="text of attach")
    friends: List[int] = Field(..., description="array of friends ids")
    id_: int = Field(..., alias='id', description="event ID")
    is_favorite: bool = Field(..., description="is favorite")
    member_status: Optional[GroupsGroupFullMemberStatus] = Field(None, description="Current user's member status")
    text: str = Field(..., description="text of attach")
    time: Optional[int] = Field(None, description="event start time")


class FriendsFriendStatus(BaseModel):
    friend_status: FriendsFriendStatusStatus = Field(...)
    sign: Optional[str] = Field(None, description="MD5 hash for the result validation")
    user_id: int = Field(..., description="User ID")


class FriendsRequests(BaseModel):
    from_: Optional[str] = Field(None, alias='from', description="ID of the user by whom friend has been suggested")
    mutual: Optional[FriendsRequestsMutual] = Field(None)
    user_id: Optional[int] = Field(None, description="User ID")


class FriendsRequestsXtrMessage(BaseModel):
    from_: Optional[str] = Field(None, alias='from', description="ID of the user by whom friend has been suggested")
    message: Optional[str] = Field(None, description="Message sent with a request")
    mutual: Optional[FriendsRequestsMutual] = Field(None)
    user_id: Optional[int] = Field(None, description="User ID")


class GiftsGift(BaseModel):
    date: Optional[int] = Field(None, description="Date when gist has been sent in Unixtime")
    from_id: Optional[int] = Field(None, description="Gift sender ID")
    gift: Optional[GiftsLayout] = Field(None)
    gift_hash: Optional[str] = Field(None, description="Hash")
    id_: Optional[int] = Field(None, alias='id', description="Gift ID")
    message: Optional[str] = Field(None, description="Comment text")
    privacy: Optional[GiftsGiftPrivacy] = Field(None)


class GroupsAddressTimetable(BaseModel):
    """Timetable for a week"""

    fri: Optional[GroupsAddressTimetableDay] = Field(None, description="Timetable for friday")
    mon: Optional[GroupsAddressTimetableDay] = Field(None, description="Timetable for monday")
    sat: Optional[GroupsAddressTimetableDay] = Field(None, description="Timetable for saturday")
    sun: Optional[GroupsAddressTimetableDay] = Field(None, description="Timetable for sunday")
    thu: Optional[GroupsAddressTimetableDay] = Field(None, description="Timetable for thursday")
    tue: Optional[GroupsAddressTimetableDay] = Field(None, description="Timetable for tuesday")
    wed: Optional[GroupsAddressTimetableDay] = Field(None, description="Timetable for wednesday")


class GroupsBanInfo(BaseModel):
    admin_id: Optional[int] = Field(None, description="Administrator ID")
    comment: Optional[str] = Field(None, description="Comment for a ban")
    comment_visible: Optional[bool] = Field(None, description="Show comment for user")
    is_closed: Optional[bool] = Field(None)
    date: Optional[int] = Field(None, description="Date when user has been added to blacklist in Unixtime")
    end_date: Optional[int] = Field(None, description="Date when user will be removed from blacklist in Unixtime")
    reason: Optional[GroupsBanInfoReason] = Field(None)


class GroupsCover(BaseModel):
    enabled: BaseBoolInt = Field(..., description="Information whether cover is enabled")
    images: Optional[List[BaseImage]] = Field(None)


class GroupsGroup(BaseModel):
    admin_level: Optional[GroupsGroupAdminLevel] = Field(None)
    deactivated: Optional[str] = Field(None, description="Information whether community is banned")
    finish_date: Optional[int] = Field(None, description="Finish date in Unixtime format")
    id_: Optional[int] = Field(None, alias='id', description="Community ID")
    is_admin: Optional[BaseBoolInt] = Field(None, description="Information whether current user is administrator")
    is_advertiser: Optional[BaseBoolInt] = Field(None, description="Information whether current user is advertiser")
    is_closed: Optional[GroupsGroupIsClosed] = Field(None)
    is_member: Optional[BaseBoolInt] = Field(None, description="Information whether current user is member")
    name: Optional[str] = Field(None, description="Community name")
    photo_100: Optional[str] = Field(None, description="URL of square photo of the community with 100 pixels in width")
    photo_200: Optional[str] = Field(None, description="URL of square photo of the community with 200 pixels in width")
    photo_50: Optional[str] = Field(None, description="URL of square photo of the community with 50 pixels in width")
    screen_name: Optional[str] = Field(None, description="Domain of the community page")
    start_date: Optional[int] = Field(None, description="Start date in Unixtime format")
    type_: Optional[GroupsGroupType] = Field(None, alias='type')


class GroupsGroupBanInfo(BaseModel):
    comment: Optional[str] = Field(None, description="Ban comment")
    end_date: Optional[int] = Field(None, description="End date of ban in Unixtime")
    reason: Optional[GroupsBanInfoReason] = Field(None)


class GroupsGroupCategory(BaseModel):
    id_: int = Field(..., alias='id', description="Category ID")
    name: str = Field(..., description="Category name")
    subcategories: Optional[List[BaseObjectWithName]] = Field(None)


class GroupsGroupLink(BaseModel):
    name: Optional[str] = Field(None, description="Link label")
    desc: Optional[str] = Field(None, description="Link description")
    edit_title: Optional[BaseBoolInt] = Field(None, description="Information whether the title can be edited")
    id_: Optional[int] = Field(None, alias='id', description="Link ID")
    image_processing: Optional[BaseBoolInt] = Field(None, description="Information whether the image on processing")
    url: Optional[str] = Field(None, description="Link URL")


class GroupsGroupPublicCategoryList(BaseModel):
    id_: Optional[int] = Field(None, alias='id')
    name: Optional[str] = Field(None)
    subcategories: Optional[List[GroupsGroupCategoryType]] = Field(None)


class GroupsGroupXtrInvitedBy(BaseModel):
    admin_level: Optional[GroupsGroupXtrInvitedByAdminLevel] = Field(None)
    id_: Optional[int] = Field(None, alias='id', description="Community ID")
    invited_by: Optional[int] = Field(None, description="Inviter ID")
    is_admin: Optional[BaseBoolInt] = Field(None, description="Information whether current user is manager")
    is_advertiser: Optional[BaseBoolInt] = Field(None, description="Information whether current user is advertiser")
    is_closed: Optional[BaseBoolInt] = Field(None, description="Information whether community is closed")
    is_member: Optional[BaseBoolInt] = Field(None, description="Information whether current user is member")
    name: Optional[str] = Field(None, description="Community name")
    photo_100: Optional[str] = Field(None, description="URL of square photo of the community with 100 pixels in width")
    photo_200: Optional[str] = Field(None, description="URL of square photo of the community with 200 pixels in width")
    photo_50: Optional[str] = Field(None, description="URL of square photo of the community with 50 pixels in width")
    screen_name: Optional[str] = Field(None, description="Domain of the community page")
    type_: Optional[GroupsGroupXtrInvitedByType] = Field(None, alias='type')


class GroupsLinksItem(BaseModel):
    desc: Optional[str] = Field(None, description="Link description")
    edit_title: Optional[BaseBoolInt] = Field(None, description="Information whether the link title can be edited")
    id_: Optional[int] = Field(None, alias='id', description="Link ID")
    name: Optional[str] = Field(None, description="Link title")
    photo_100: Optional[str] = Field(None, description="URL of square image of the link with 100 pixels in width")
    photo_50: Optional[str] = Field(None, description="URL of square image of the link with 50 pixels in width")
    url: Optional[str] = Field(None, description="Link URL")


class GroupsLongPollEvents(BaseModel):
    audio_new: BaseBoolInt = Field(...)
    board_post_delete: BaseBoolInt = Field(...)
    board_post_edit: BaseBoolInt = Field(...)
    board_post_new: BaseBoolInt = Field(...)
    board_post_restore: BaseBoolInt = Field(...)
    group_change_photo: BaseBoolInt = Field(...)
    group_change_settings: BaseBoolInt = Field(...)
    group_join: BaseBoolInt = Field(...)
    group_leave: BaseBoolInt = Field(...)
    group_officers_edit: BaseBoolInt = Field(...)
    lead_forms_new: Optional[BaseBoolInt] = Field(None)
    market_comment_delete: BaseBoolInt = Field(...)
    market_comment_edit: BaseBoolInt = Field(...)
    market_comment_new: BaseBoolInt = Field(...)
    market_comment_restore: BaseBoolInt = Field(...)
    message_allow: BaseBoolInt = Field(...)
    message_deny: BaseBoolInt = Field(...)
    message_new: BaseBoolInt = Field(...)
    message_read: BaseBoolInt = Field(...)
    message_reply: BaseBoolInt = Field(...)
    message_typing_state: BaseBoolInt = Field(...)
    message_edit: BaseBoolInt = Field(...)
    photo_comment_delete: BaseBoolInt = Field(...)
    photo_comment_edit: BaseBoolInt = Field(...)
    photo_comment_new: BaseBoolInt = Field(...)
    photo_comment_restore: BaseBoolInt = Field(...)
    photo_new: BaseBoolInt = Field(...)
    poll_vote_new: BaseBoolInt = Field(...)
    user_block: BaseBoolInt = Field(...)
    user_unblock: BaseBoolInt = Field(...)
    video_comment_delete: BaseBoolInt = Field(...)
    video_comment_edit: BaseBoolInt = Field(...)
    video_comment_new: BaseBoolInt = Field(...)
    video_comment_restore: BaseBoolInt = Field(...)
    video_new: BaseBoolInt = Field(...)
    wall_post_new: BaseBoolInt = Field(...)
    wall_reply_delete: BaseBoolInt = Field(...)
    wall_reply_edit: BaseBoolInt = Field(...)
    wall_reply_new: BaseBoolInt = Field(...)
    wall_reply_restore: BaseBoolInt = Field(...)
    wall_repost: BaseBoolInt = Field(...)


class GroupsMarketInfo(BaseModel):
    contact_id: Optional[int] = Field(None, description="Contact person ID")
    currency: Optional[MarketCurrency] = Field(None)
    currency_text: Optional[str] = Field(None, description="Currency name")
    enabled: Optional[BaseBoolInt] = Field(None, description="Information whether the market is enabled")
    main_album_id: Optional[int] = Field(None, description="Main market album ID")
    price_max: Optional[str] = Field(None, description="Maximum price")
    price_min: Optional[str] = Field(None, description="Minimum price")


class GroupsMemberRole(BaseModel):
    id_: Optional[int] = Field(None, alias='id', description="User ID")
    permissions: Optional[List[GroupsMemberRolePermission]] = Field(None)
    role: Optional[GroupsMemberRoleStatus] = Field(None)


class GroupsMemberStatus(BaseModel):
    member: BaseBoolInt = Field(..., description="Information whether user is a member of the group")
    user_id: int = Field(..., description="User ID")


class GroupsMemberStatusFull(BaseModel):
    can_invite: Optional[BaseBoolInt] = Field(None, description="Information whether user can be invited")
    can_recall: Optional[BaseBoolInt] = Field(None,
                                              description="Information whether user's invite to the group can be "
                                                          "recalled")
    invitation: Optional[BaseBoolInt] = Field(None,
                                              description="Information whether user has been invited to the group")
    member: BaseBoolInt = Field(..., description="Information whether user is a member of the group")
    request: Optional[BaseBoolInt] = Field(None, description="Information whether user has send request to the group")
    user_id: int = Field(..., description="User ID")


class GroupsOnlineStatus(BaseModel):
    """Online status of group"""

    minutes: Optional[int] = Field(None, description="Estimated time of answer (for status = answer_mark)")
    status: GroupsOnlineStatusType = Field(...)


class LeadsChecked(BaseModel):
    reason: Optional[str] = Field(None, description="Reason why user can't start the lead")
    result: Optional[LeadsCheckedResult] = Field(None)
    sid: Optional[str] = Field(None, description="Session ID")
    start_link: Optional[str] = Field(None, description="URL user should open to start the lead")


class LeadsComplete(BaseModel):
    cost: Optional[int] = Field(None, description="Offer cost")
    limit: Optional[int] = Field(None, description="Offer limit")
    spent: Optional[int] = Field(None, description="Amount of spent votes")
    success: Optional[int] = Field(None)
    test_mode: Optional[BaseBoolInt] = Field(None, description="Information whether test mode is enabled")


class LeadsEntry(BaseModel):
    aid: Optional[int] = Field(None, description="Application ID")
    comment: Optional[str] = Field(None, description="Comment text")
    date: Optional[int] = Field(None, description="Date when the action has been started in Unixtime")
    sid: Optional[str] = Field(None, description="Session string ID")
    start_date: Optional[int] = Field(None, description="Start date in Unixtime (for status=2)")
    status: Optional[int] = Field(None, description="Action type")
    test_mode: Optional[BaseBoolInt] = Field(None, description="Information whether test mode is enabled")
    uid: Optional[int] = Field(None, description="User ID")


class LeadsLead(BaseModel):
    completed: Optional[int] = Field(None, description="Completed offers number")
    cost: Optional[int] = Field(None, description="Offer cost")
    days: Optional[LeadsLeadDays] = Field(None)
    impressions: Optional[int] = Field(None, description="Impressions number")
    limit: Optional[int] = Field(None, description="Lead limit")
    spent: Optional[int] = Field(None, description="Amount of spent votes")
    started: Optional[int] = Field(None, description="Started offers number")


class LeadsStart(BaseModel):
    test_mode: Optional[BaseBoolInt] = Field(None, description="Information whether test mode is enabled")
    vk_sid: Optional[str] = Field(None, description="Session data")


class MarketMarketCategory(BaseModel):
    id_: int = Field(..., alias='id', description="Category ID")
    name: str = Field(..., description="Category name")
    section: MarketSection = Field(...)


class MarketPrice(BaseModel):
    amount: Optional[str] = Field(None, description="Amount")
    currency: Optional[MarketCurrency] = Field(None)
    discount_rate: Optional[int] = Field(None)
    old_amount: Optional[str] = Field(None)
    text: Optional[str] = Field(None, description="Text")


class MediaRestriction(BaseModel):
    """Media restrictions"""

    text: Optional[str] = Field(None)
    title: str = Field(...)
    button: Optional[VideoRestrictionButton] = Field(None)
    always_shown: Optional[BaseBoolInt] = Field(None, description="Need show restriction always or not")
    blur: Optional[BaseBoolInt] = Field(None, description="Need blur current video or not")
    can_play: Optional[BaseBoolInt] = Field(None, description="Can play video or not")
    can_preview: Optional[BaseBoolInt] = Field(None, description="Can preview video or not")
    card_icon: Optional[List[BaseImage]] = Field(None)
    list_icon: Optional[List[BaseImage]] = Field(None)


class MessagesChatPushSettings(BaseModel):
    disabled_until: Optional[int] = Field(None, description="Time until that notifications are disabled")
    sound: Optional[BaseBoolInt] = Field(None, description="Information whether the sound is on")


class MessagesConversationPeer(BaseModel):
    id_: int = Field(..., alias='id')
    local_id: Optional[int] = Field(None)
    type_: MessagesConversationPeerType = Field(..., alias='type')


class MessagesKeyboardButtonAction(BaseModel):
    """Description of the action, that should be performed on button click"""

    app_id: Optional[int] = Field(None, description="Fragment value in app link like vk.com/app{app_id}_-654321#hash")
    hash_: Optional[str] = Field(None, alias='hash',
                                 description="Fragment value in app link like vk.com/app123456_-654321#{hash}")
    label: Optional[str] = Field(None, description="Label for button")
    link: Optional[str] = Field(None, description="link for button")
    owner_id: Optional[int] = Field(None,
                                    description="Fragment value in app link like vk.com/app123456_{owner_id}#hash")
    payload: Optional[str] = Field(None,
                                   description="Additional data sent along with message for developer convenience")
    type_: MessagesTemplateActionTypeNames = Field(..., alias='type', description="Button type")


class MessagesLastActivity(BaseModel):
    online: BaseBoolInt = Field(..., description="Information whether user is online")
    time: int = Field(..., description="Time when user was online in Unixtime")


class MessagesMessageAction(BaseModel):
    conversation_message_id: Optional[int] = Field(None, description="Message ID")
    email: Optional[str] = Field(None, description="Email address for chat_invite_user or chat_kick_user actions")
    member_id: Optional[int] = Field(None, description="User or email peer ID")
    message: Optional[str] = Field(None, description="Message body of related message")
    photo: Optional[MessagesMessageActionPhoto] = Field(None)
    text: Optional[str] = Field(None, description="New chat title for chat_create and chat_title_update actions")
    type_: MessagesMessageActionStatus = Field(..., alias='type')


class NewsfeedEventActivity(BaseModel):
    address: Optional[str] = Field(None, description="address of event")
    button_text: str = Field(..., description="text of attach")
    friends: List[int] = Field(..., description="array of friends ids")
    member_status: GroupsGroupFullMemberStatus = Field(..., description="Current user's member status")
    text: str = Field(..., description="text of attach")
    time: Optional[int] = Field(None, description="event start time")


class NewsfeedItemAudioAudio(BaseModel):
    count: Optional[int] = Field(None, description="Audios number")
    items: Optional[List[AudioAudio]] = Field(None)


class NewsfeedItemBase(BaseModel):
    type_: NewsfeedNewsfeedItemType = Field(..., alias='type')
    source_id: int = Field(..., description="Item source ID")
    date: int = Field(..., description="Date when item has been added in Unixtime")


class NewsfeedItemFriendFriends(BaseModel):
    count: Optional[int] = Field(None, description="Number of friends has been added")
    items: Optional[List[BaseUserId]] = Field(None)


class NewsfeedItemNoteNotes(BaseModel):
    count: Optional[int] = Field(None, description="Notes number")
    items: Optional[List[NewsfeedNewsfeedNote]] = Field(None)


class NewsfeedItemWallpostFeedback(BaseModel):
    type_: NewsfeedItemWallpostFeedbackType = Field(..., alias='type')
    question: str = Field(...)
    answers: Optional[List[NewsfeedItemWallpostFeedbackAnswer]] = Field(None)
    stars_count: Optional[int] = Field(None)
    gratitude: Optional[str] = Field(None)


class NewsfeedListFull(NewsfeedList):
    no_reposts: Optional[BaseBoolInt] = Field(None, description="Information whether reposts hiding is enabled")
    source_ids: Optional[List[int]] = Field(None)


class NotesNote(BaseModel):
    read_comments: Optional[int] = Field(None)
    can_comment: Optional[BaseBoolInt] = Field(None,
                                               description="Information whether current user can comment the note")
    comments: int = Field(..., description="Comments number")
    date: int = Field(..., description="Date when the note has been created in Unixtime")
    id_: int = Field(..., alias='id', description="Note ID")
    owner_id: int = Field(..., description="Note owner's ID")
    text: Optional[str] = Field(None, description="Note text")
    text_wiki: Optional[str] = Field(None, description="Note text in wiki format")
    title: str = Field(..., description="Note title")
    view_url: str = Field(..., description="URL of the page with note preview")


class NotificationsSendMessageItem(BaseModel):
    user_id: Optional[int] = Field(None, description="User ID")
    status: Optional[bool] = Field(None, description="Notification status")
    error: Optional[NotificationsSendMessageError] = Field(None)


class OrdersAmount(BaseModel):
    amounts: Optional[List[OrdersAmountItem]] = Field(None)
    currency: Optional[str] = Field(None, description="Currency name")


class PagesWikipage(BaseModel):
    creator_id: Optional[int] = Field(None, description="Page creator ID")
    creator_name: Optional[int] = Field(None, description="Page creator name")
    editor_id: Optional[int] = Field(None, description="Last editor ID")
    editor_name: Optional[str] = Field(None, description="Last editor name")
    group_id: int = Field(..., description="Community ID")
    id_: int = Field(..., alias='id', description="Page ID")
    title: str = Field(..., description="Page title")
    views: int = Field(..., description="Views number")
    who_can_edit: PagesPrivacySettings = Field(..., description="Edit settings of the page")
    who_can_view: PagesPrivacySettings = Field(..., description="View settings of the page")


class PagesWikipageFull(BaseModel):
    created: int = Field(..., description="Date when the page has been created in Unixtime")
    creator_id: Optional[int] = Field(None, description="Page creator ID")
    current_user_can_edit: Optional[BaseBoolInt] = Field(None,
                                                         description="Information whether current user can edit the "
                                                                     "page")
    current_user_can_edit_access: Optional[BaseBoolInt] = Field(None,
                                                                description="Information whether current user can "
                                                                            "edit the page access settings")
    edited: int = Field(..., description="Date when the page has been edited in Unixtime")
    editor_id: Optional[int] = Field(None, description="Last editor ID")
    group_id: int = Field(..., description="Community ID")
    html: Optional[str] = Field(None, description="Page content, HTML")
    id_: int = Field(..., alias='id', description="Page ID")
    source: Optional[str] = Field(None, description="Page content, wiki")
    title: str = Field(..., description="Page title")
    view_url: str = Field(..., description="URL of the page preview")
    views: int = Field(..., description="Views number")
    who_can_edit: PagesPrivacySettings = Field(..., description="Edit settings of the page")
    who_can_view: PagesPrivacySettings = Field(..., description="View settings of the page")


class PhotosImage(BaseModel):
    height: Optional[int] = Field(None, description="Height of the photo in px.")
    type_: Optional[PhotosImageType] = Field(None, alias='type')
    url: Optional[str] = Field(None, description="Photo URL.")
    width: Optional[int] = Field(None, description="Width of the photo in px.")


class PhotosPhotoSizes(BaseModel):
    height: int = Field(..., description="Height in px")
    url: str = Field(..., description="URL of the image")
    src: Optional[str] = Field(None, description="URL of the image")
    type_: PhotosPhotoSizesType = Field(..., alias='type')
    width: int = Field(..., description="Width in px")


class PhotosPhotoTag(BaseModel):
    date: int = Field(..., description="Date when tag has been added in Unixtime")
    id_: int = Field(..., alias='id', description="Tag ID")
    placer_id: int = Field(..., description="ID of the tag creator")
    tagged_name: str = Field(..., description="Tag description")
    user_id: int = Field(..., description="Tagged user ID")
    viewed: BaseBoolInt = Field(..., description="Information whether the tag is reviewed")
    x: float = Field(..., description="Coordinate X of the left upper corner")
    x2: float = Field(..., description="Coordinate X of the right lower corner")
    y: float = Field(..., description="Coordinate Y of the left upper corner")
    y2: float = Field(..., description="Coordinate Y of the right lower corner")


class PollsBackground(BaseModel):
    angle: Optional[int] = Field(None, description="Gradient angle with 0 on positive X axis")
    color: Optional[str] = Field(None, description="Hex color code without #")
    height: Optional[int] = Field(None, description="Original height of pattern tile")
    id_: Optional[int] = Field(None, alias='id')
    name: Optional[str] = Field(None)
    images: Optional[List[BaseImage]] = Field(None, description="Pattern tiles")
    points: Optional[List[BaseGradientPoint]] = Field(None, description="Gradient points")
    type_: Optional[str] = Field(None, alias='type')
    width: Optional[int] = Field(None, description="Original with of pattern tile")


class PollsVoters(BaseModel):
    answer_id: Optional[int] = Field(None, description="Answer ID")
    users: Optional[PollsVotersUsers] = Field(None)


class PrettycardsPrettycard(BaseModel):
    button: Optional[str] = Field(None, description="Button key")
    button_text: Optional[str] = Field(None, description="Button text in current language")
    card_id: str = Field(..., description="Card ID (long int returned as string)")
    images: Optional[List[BaseImage]] = Field(None)
    link_url: str = Field(..., description="Link URL")
    photo: str = Field(..., description="Photo ID (format \"<owner_id>_<media_id>\")")
    price: Optional[str] = Field(None, description="Price if set (decimal number returned as string)")
    price_old: Optional[str] = Field(None, description="Old price if set (decimal number returned as string)")
    title: str = Field(..., description="Title")


class StatsReach(BaseModel):
    """Reach stats"""

    age: Optional[List[StatsSexAge]] = Field(None)
    cities: Optional[List[StatsCity]] = Field(None)
    countries: Optional[List[StatsCountry]] = Field(None)
    mobile_reach: Optional[int] = Field(None, description="Reach count from mobile devices")
    reach: Optional[int] = Field(None, description="Reach count")
    reach_subscribers: Optional[int] = Field(None, description="Subscribers reach count")
    sex: Optional[List[StatsSexAge]] = Field(None)
    sex_age: Optional[List[StatsSexAge]] = Field(None)


class StatsViews(BaseModel):
    """Views stats"""

    age: Optional[List[StatsSexAge]] = Field(None)
    cities: Optional[List[StatsCity]] = Field(None)
    countries: Optional[List[StatsCountry]] = Field(None)
    mobile_views: Optional[int] = Field(None, description="Number of views from mobile devices")
    sex: Optional[List[StatsSexAge]] = Field(None)
    sex_age: Optional[List[StatsSexAge]] = Field(None)
    views: Optional[int] = Field(None, description="Views number")
    visitors: Optional[int] = Field(None, description="Visitors number")


class StatsWallpostStat(BaseModel):
    post_id: Optional[int] = Field(None)
    hide: Optional[int] = Field(None, description="Hidings number")
    join_group: Optional[int] = Field(None, description="People have joined the group")
    links: Optional[int] = Field(None, description="Link clickthrough")
    reach_subscribers: Optional[int] = Field(None, description="Subscribers reach")
    reach_subscribers_count: Optional[int] = Field(None)
    reach_total: Optional[int] = Field(None, description="Total reach")
    reach_total_count: Optional[int] = Field(None)
    reach_viral: Optional[int] = Field(None)
    reach_ads: Optional[int] = Field(None)
    report: Optional[int] = Field(None, description="Reports number")
    to_group: Optional[int] = Field(None, description="Clickthrough to community")
    unsubscribe: Optional[int] = Field(None, description="Unsubscribed members")
    sex_age: Optional[List[StatsSexAge]] = Field(None)


class StatusStatus(BaseModel):
    audio: Optional[AudioAudio] = Field(None)
    text: Optional[str] = Field(None, description="Status text")


class StoriesStoryStatsStat(BaseModel):
    count: Optional[int] = Field(None, description="Stat value")
    state: StoriesStoryStatsState = Field(...)


class UsersUser(UsersUserMin):
    sex: Optional[BaseSex] = Field(None, description="User sex")
    screen_name: Optional[str] = Field(None, description="Domain name of the user's page")
    photo_50: Optional[str] = Field(None, description="URL of square photo of the user with 50 pixels in width")
    photo_100: Optional[str] = Field(None, description="URL of square photo of the user with 100 pixels in width")
    online: Optional[BaseBoolInt] = Field(None, description="Information whether the user is online")
    online_mobile: Optional[BaseBoolInt] = Field(None,
                                                 description="Information whether the user is online in mobile site "
                                                             "or application")
    online_app: Optional[int] = Field(None, description="Application ID")
    verified: Optional[BaseBoolInt] = Field(None, description="Information whether the user is verified")
    trending: Optional[BaseBoolInt] = Field(None, description="Information whether the user has a \"fire\" pictogram.")
    friend_status: Optional[FriendsFriendStatusStatus] = Field(None)
    mutual: Optional[FriendsRequestsMutual] = Field(None)


class UtilsDomainResolved(BaseModel):
    object_id: Optional[int] = Field(None, description="Object ID")
    group_id: Optional[int] = Field(None, description="Group ID")
    type_: Optional[UtilsDomainResolvedType] = Field(None, alias='type')


class UtilsLinkChecked(BaseModel):
    link: Optional[str] = Field(None, description="Link URL")
    status: Optional[UtilsLinkCheckedStatus] = Field(None)


class UtilsLinkStats(BaseModel):
    key: Optional[str] = Field(None, description="Link key (characters after vk.cc/)")
    stats: Optional[List[UtilsStats]] = Field(None)


class UtilsStatsExtended(BaseModel):
    cities: Optional[List[UtilsStatsCity]] = Field(None)
    countries: Optional[List[UtilsStatsCountry]] = Field(None)
    sex_age: Optional[List[UtilsStatsSexAge]] = Field(None)
    timestamp: Optional[int] = Field(None, description="Start time")
    views: Optional[int] = Field(None, description="Total views number")


class VideoLiveSettings(BaseModel):
    """Video live settings"""

    can_rewind: Optional[BaseBoolInt] = Field(None, description="If user car rewind live or not")
    is_endless: Optional[BaseBoolInt] = Field(None, description="If live is endless or not")
    max_duration: Optional[int] = Field(None, description="Max possible time for rewind")


class VideoVideoImage(BaseImage):
    with_padding: Optional[BasePropertyExists] = Field(None)


class WallGeo(BaseModel):
    coordinates: Optional[str] = Field(None, description="Coordinates as string. <latitude> <longtitude>")
    place: Optional[BasePlace] = Field(None)
    showmap: Optional[int] = Field(None, description="Information whether a map is showed")
    type_: Optional[str] = Field(None, alias='type', description="Place type")


class WallPostSource(BaseModel):
    data: Optional[str] = Field(None, description="Additional data")
    platform: Optional[str] = Field(None, description="Platform name")
    type_: Optional[WallPostSourceType] = Field(None, alias='type')
    url: Optional[str] = Field(None, description="URL to an external site used to publish the post")


class WidgetsCommentMedia(BaseModel):
    item_id: Optional[int] = Field(None, description="Media item ID")
    owner_id: Optional[int] = Field(None, description="Media owner's ID")
    thumb_src: Optional[str] = Field(None, description="URL of the preview image (type=photo only)")
    type_: Optional[WidgetsCommentMediaType] = Field(None, alias='type')


class WidgetsWidgetPage(BaseModel):
    comments: Optional[BaseObjectCount] = Field(None)
    date: Optional[int] = Field(None,
                                description="Date when widgets on the page has been initialized firstly in Unixtime")
    description: Optional[str] = Field(None, description="Page description")
    id_: Optional[int] = Field(None, alias='id', description="Page ID")
    likes: Optional[BaseObjectCount] = Field(None)
    page_id: Optional[str] = Field(None, description="page_id parameter value")
    photo: Optional[str] = Field(None, description="URL of the preview image")
    title: Optional[str] = Field(None, description="Page title")
    url: Optional[str] = Field(None, description="Page absolute URL")


class AccountPushConversations(BaseModel):
    count: Optional[int] = Field(None, description="Items count")
    items: Optional[List[AccountPushConversationsItem]] = Field(None)


class AdsDemostatsFormat(BaseModel):
    age: Optional[List[AdsStatsAge]] = Field(None)
    cities: Optional[List[AdsStatsCities]] = Field(None)
    day: Optional[str] = Field(None, description="Day as YYYY-MM-DD")
    month: Optional[str] = Field(None, description="Month as YYYY-MM")
    overall: Optional[int] = Field(None, description="1 if period=overall")
    sex: Optional[List[AdsStatsSex]] = Field(None)
    sex_age: Optional[List[AdsStatsSexAge]] = Field(None)


class AdsRejectReason(BaseModel):
    comment: Optional[str] = Field(None, description="Comment text")
    rules: Optional[List[AdsRules]] = Field(None)


class AdsTargSettings(AdsCriteria):
    id_: Optional[int] = Field(None, alias='id', description="Ad ID")
    campaign_id: Optional[int] = Field(None, description="Campaign ID")


class AdsUsers(BaseModel):
    accesses: List[AdsAccesses] = Field(...)
    user_id: int = Field(..., description="User ID")


class AppsApp(AppsAppMin):
    author_url: Optional[str] = Field(None, description="Application author's URL")
    banner_1120: Optional[str] = Field(None, description="URL of the app banner with 1120 px in width")
    banner_560: Optional[str] = Field(None, description="URL of the app banner with 560 px in width")
    icon_16: Optional[str] = Field(None, description="URL of the app icon with 16 px in width")
    is_new: Optional[BaseBoolInt] = Field(None, description="Is new flag")
    push_enabled: Optional[BaseBoolInt] = Field(None, description="Is push enabled")
    screen_orientation: Optional[int] = Field(None, description="Screen orientation")
    friends: Optional[List[int]] = Field(None)
    catalog_position: Optional[int] = Field(None, description="Catalog position")
    description: Optional[str] = Field(None, description="Application description")
    genre: Optional[str] = Field(None, description="Genre name")
    genre_id: Optional[int] = Field(None, description="Genre ID")
    international: Optional[bool] = Field(None, description="Information whether the application is multilanguage")
    is_in_catalog: Optional[int] = Field(None, description="Information whether application is in mobile catalog")
    leaderboard_type: Optional[AppsAppLeaderboardType] = Field(None)
    members_count: Optional[int] = Field(None, description="Members number")
    platform_id: Optional[str] = Field(None, description="Application ID in store")
    published_date: Optional[int] = Field(None, description="Date when the application has been published in Unixtime")
    screen_name: Optional[str] = Field(None, description="Screen name")
    section: Optional[str] = Field(None, description="Application section name")


class BaseLinkButton(BaseModel):
    action: Optional[BaseLinkButtonAction] = Field(None, description="Button action")
    title: Optional[str] = Field(None, description="Button title")
    block_id: Optional[str] = Field(None, description="Target block id")
    section_id: Optional[str] = Field(None, description="Target section id")
    owner_id: Optional[int] = Field(None, description="Owner id")
    icon: Optional[str] = Field(None, description="Button icon name, e.g. 'phone' or 'gift'")
    # style: Optional[BaseLinkButtonStyle] = Field(None) object BaseLinkButtonStyle has error in json-schema


class BaseLinkProduct(BaseModel):
    price: MarketPrice = Field(...)
    merchant: Optional[str] = Field(None)
    orders_count: Optional[int] = Field(None)


class DocsDocPreviewPhoto(BaseModel):
    sizes: Optional[List[DocsDocPreviewPhotoSizes]] = Field(None)


class FriendsFriendExtendedStatus(FriendsFriendStatus):
    is_request_unread: Optional[bool] = Field(None, description="Is friend request from other user unread")


class GroupsAddress(BaseModel):
    additional_address: Optional[str] = Field(None, description="Additional address to the place (6 floor, left door)")
    address: Optional[str] = Field(None, description="String address to the place (Nevsky, 28)")
    city_id: Optional[int] = Field(None, description="City id of address")
    country_id: Optional[int] = Field(None, description="Country id of address")
    distance: Optional[int] = Field(None, description="Distance from the point")
    id_: int = Field(..., alias='id', description="Address id")
    latitude: Optional[float] = Field(None, description="Address latitude")
    longitude: Optional[float] = Field(None, description="Address longitude")
    metro_station_id: Optional[int] = Field(None, description="Metro id of address")
    phone: Optional[str] = Field(None, description="Address phone")
    time_offset: Optional[int] = Field(None, description="Time offset int minutes from utc time")
    timetable: Optional[GroupsAddressTimetable] = Field(None, description="Week timetable for the address")
    title: Optional[str] = Field(None, description="Title of the place (Zinger, etc)")
    work_info_status: Optional[GroupsAddressWorkInfoStatus] = Field(None,
                                                                    description="Status of information about timetable")


class GroupsCallbackSettings(BaseModel):
    api_version: Optional[str] = Field(None, description="API version used for the events")
    events: Optional[GroupsLongPollEvents] = Field(None)


class GroupsGroupCategoryFull(BaseModel):
    id_: int = Field(..., alias='id', description="Category ID")
    name: str = Field(..., description="Category name")
    page_count: int = Field(..., description="Pages number")
    page_previews: List[GroupsGroup] = Field(...)
    subcategories: Optional[List[GroupsGroupCategory]] = Field(None)


class GroupsGroupFull(GroupsGroup):
    market: Optional[GroupsMarketInfo] = Field(None)
    member_status: Optional[GroupsGroupFullMemberStatus] = Field(None, description="Current user's member status")
    is_adult: Optional[BaseBoolInt] = Field(None, description="Information whether community is adult")
    is_hidden_from_feed: Optional[BaseBoolInt] = Field(None,
                                                       description="Information whether community is hidden from "
                                                                   "current user's newsfeed")
    is_favorite: Optional[BaseBoolInt] = Field(None, description="Information whether community is in faves")
    is_subscribed: Optional[BaseBoolInt] = Field(None, description="Information whether current user is subscribed")
    city: Optional[BaseObject] = Field(None)
    country: Optional[BaseCountry] = Field(None)
    verified: Optional[BaseBoolInt] = Field(None, description="Information whether community is verified")
    description: Optional[str] = Field(None, description="Community description")
    wiki_page: Optional[str] = Field(None, description="Community's main wiki page title")
    members_count: Optional[int] = Field(None, description="Community members number")
    video_live_level: Optional[int] = Field(None, description="Community level live streams achievements")
    video_live_count: Optional[int] = Field(None, description="Number of community's live streams")
    counters: Optional[GroupsCountersGroup] = Field(None)
    cover: Optional[GroupsCover] = Field(None)
    can_post: Optional[BaseBoolInt] = Field(None,
                                            description="Information whether current user can post on community's wall")
    can_see_all_posts: Optional[BaseBoolInt] = Field(None,
                                                     description="Information whether current user can see all posts "
                                                                 "on community's wall")
    activity: Optional[str] = Field(None, description="Type of group, start date of event or category of public page")
    fixed_post: Optional[int] = Field(None, description="Fixed post ID")
    can_create_topic: Optional[BaseBoolInt] = Field(None,
                                                    description="Information whether current user can create topic")
    can_upload_doc: Optional[BaseBoolInt] = Field(None, description="Information whether current user can upload doc")
    can_upload_story: Optional[BaseBoolInt] = Field(None,
                                                    description="Information whether current user can upload story")
    can_upload_video: Optional[BaseBoolInt] = Field(None,
                                                    description="Information whether current user can upload video")
    has_photo: Optional[BaseBoolInt] = Field(None, description="Information whether community has photo")
    status: Optional[str] = Field(None, description="Community status")
    main_album_id: Optional[int] = Field(None, description="Community's main photo album ID")
    links: Optional[List[GroupsLinksItem]] = Field(None)
    contacts: Optional[List[GroupsContactsItem]] = Field(None)
    wall: Optional[int] = Field(None, description="Information about wall status in community")
    site: Optional[str] = Field(None, description="Community's website")
    main_section: Optional[GroupsGroupFullMainSection] = Field(None)
    trending: Optional[BaseBoolInt] = Field(None,
                                            description="Information whether the community has a \"fire\" pictogram.")
    can_message: Optional[BaseBoolInt] = Field(None,
                                               description="Information whether current user can send a message to "
                                                           "community")
    is_messages_blocked: Optional[BaseBoolInt] = Field(None,
                                                       description="Information whether community can send a message "
                                                                   "to current user")
    can_send_notify: Optional[BaseBoolInt] = Field(None,
                                                   description="Information whether community can send notifications "
                                                               "by phone number to current user")
    online_status: Optional[GroupsOnlineStatus] = Field(None, description="Status of replies in community messages")
    age_limits: Optional[GroupsGroupFullAgeLimits] = Field(None, description="Information whether age limit")
    ban_info: Optional[GroupsGroupBanInfo] = Field(None, description="User ban info")
    has_market_app: Optional[bool] = Field(None, description="Information whether community has installed market app")
    addresses: Optional[GroupsAddressesInfo] = Field(None, description="Info about addresses in groups")
    is_subscribed_podcasts: Optional[bool] = Field(None,
                                                   description="Information whether current user is subscribed to "
                                                               "podcasts")
    can_subscribe_podcasts: Optional[bool] = Field(None, description="Owner in whitelist or not")
    can_subscribe_posts: Optional[bool] = Field(None, description="Can subscribe to wall")


class GroupsLongPollSettings(BaseModel):
    api_version: Optional[str] = Field(None, description="API version used for the events")
    events: GroupsLongPollEvents = Field(...)
    is_enabled: bool = Field(..., description="Shows whether Long Poll is enabled")


class GroupsOwnerXtrBanInfo(BaseModel):
    ban_info: Optional[GroupsBanInfo] = Field(None)
    group: Optional[GroupsGroup] = Field(None, description="Information about group if type = group")
    profile: Optional[UsersUser] = Field(None, description="Information about group if type = profile")
    type_: Optional[GroupsOwnerXtrBanInfoType] = Field(None, alias='type')


class MarketMarketItem(BaseModel):
    access_key: Optional[str] = Field(None, description="Access key for the market item")
    availability: MarketMarketItemAvailability = Field(...)
    button_title: Optional[str] = Field(None, description="Title for button for url")
    category: MarketMarketCategory = Field(...)
    date: Optional[int] = Field(None, description="Date when the item has been created in Unixtime")
    description: str = Field(..., description="Item description")
    external_id: Optional[str] = Field(None)
    id_: int = Field(..., alias='id', description="Item ID")
    is_favorite: Optional[bool] = Field(None)
    owner_id: int = Field(..., description="Item owner's ID")
    price: MarketPrice = Field(...)
    thumb_photo: str = Field(..., description="URL of the preview image")
    title: str = Field(..., description="Item title")
    url: Optional[str] = Field(None, description="URL to item")
    variants_grouping_id: Optional[int] = Field(None)
    is_main_variant: Optional[bool] = Field(None)


class MessagesChat(BaseModel):
    admin_id: int = Field(..., description="Chat creator ID")
    id_: int = Field(..., alias='id', description="Chat ID")
    kicked: Optional[BaseBoolInt] = Field(None, description="Shows that user has been kicked from the chat")
    left: Optional[BaseBoolInt] = Field(None, description="Shows that user has been left the chat")
    photo_100: Optional[str] = Field(None, description="URL of the preview image with 100 px in width")
    photo_200: Optional[str] = Field(None, description="URL of the preview image with 200 px in width")
    photo_50: Optional[str] = Field(None, description="URL of the preview image with 50 px in width")
    push_settings: Optional[MessagesChatPushSettings] = Field(None)
    title: Optional[str] = Field(None, description="Chat title")
    type_: str = Field(..., alias='type', description="Chat type")
    users: List[int] = Field(...)
    is_default_photo: Optional[bool] = Field(None, description="If provided photo is default")


class MessagesKeyboardButton(BaseModel):
    action: MessagesKeyboardButtonAction = Field(...)
    color: Optional[str] = Field(None, description="Button color")


class NewsfeedItemAudio(NewsfeedItemBase):
    audio: Optional[NewsfeedItemAudioAudio] = Field(None)
    post_id: Optional[int] = Field(None, description="Post ID")


class NewsfeedItemFriend(NewsfeedItemBase):
    friends: Optional[NewsfeedItemFriendFriends] = Field(None)


class NewsfeedItemHolidayRecommendationsBlockHeader(BaseModel):
    title: Optional[str] = Field(None, description="Title of the header")
    subtitle: Optional[str] = Field(None, description="Subtitle of the header")
    image: Optional[List[BaseImage]] = Field(None)
    action: Optional[BaseLinkButtonAction] = Field(None)


class NewsfeedItemNote(NewsfeedItemBase):
    notes: Optional[NewsfeedItemNoteNotes] = Field(None)


class NewsfeedItemPromoButton(NewsfeedItemBase):
    text: Optional[str] = Field(None)
    title: Optional[str] = Field(None)
    action: Optional[NewsfeedItemPromoButtonAction] = Field(None)
    images: Optional[List[NewsfeedItemPromoButtonImage]] = Field(None)
    track_code: Optional[str] = Field(None)


class NewsfeedItemTopic(NewsfeedItemBase):
    comments: Optional[BaseCommentsInfo] = Field(None)
    likes: Optional[BaseLikesInfo] = Field(None)
    post_id: Optional[int] = Field(None, description="Topic post ID")
    text: Optional[str] = Field(None, description="Post text")


class PhotosPhoto(BaseModel):
    access_key: Optional[str] = Field(None, description="Access key for the photo")
    album_id: int = Field(..., description="Album ID")
    date: int = Field(..., description="Date when uploaded")
    height: Optional[int] = Field(None, description="Original photo height")
    id_: int = Field(..., alias='id', description="Photo ID")
    images: Optional[List[PhotosImage]] = Field(None)
    lat: Optional[float] = Field(None, description="Latitude")
    long: Optional[float] = Field(None, description="Longitude")
    owner_id: int = Field(..., description="Photo owner's ID")
    photo_256: Optional[str] = Field(None, description="URL of image with 2560 px width")
    can_comment: Optional[BaseBoolInt] = Field(None,
                                               description="Information whether current user can comment the photo")
    place: Optional[str] = Field(None)
    post_id: Optional[int] = Field(None, description="Post ID")
    sizes: Optional[List[PhotosPhotoSizes]] = Field(None)
    text: Optional[str] = Field(None, description="Photo caption")
    user_id: Optional[int] = Field(None, description="ID of the user who have uploaded the photo")
    width: Optional[int] = Field(None, description="Original photo width")
    has_tags: bool = Field(..., description="Whether photo has attached tag links")
    restrictions: Optional[MediaRestriction] = Field(None)


class PhotosPhotoAlbumFull(BaseModel):
    can_upload: Optional[BaseBoolInt] = Field(None,
                                              description="Information whether current user can upload photo to the "
                                                          "album")
    comments_disabled: Optional[BaseBoolInt] = Field(None,
                                                     description="Information whether album comments are disabled")
    created: int = Field(..., description="Date when the album has been created in Unixtime")
    description: Optional[str] = Field(None, description="Photo album description")
    id_: int = Field(..., alias='id', description="Photo album ID")
    owner_id: int = Field(..., description="Album owner's ID")
    size: int = Field(..., description="Photos number")
    sizes: Optional[List[PhotosPhotoSizes]] = Field(None)
    thumb_id: Optional[int] = Field(None, description="Thumb photo ID")
    thumb_is_last: Optional[BaseBoolInt] = Field(None, description="Information whether the album thumb is last photo")
    thumb_src: Optional[str] = Field(None, description="URL of the thumb image")
    title: str = Field(..., description="Photo album title")
    updated: int = Field(..., description="Date when the album has been updated last time in Unixtime")
    upload_by_admins_only: Optional[BaseBoolInt] = Field(None,
                                                         description="Information whether only community "
                                                                     "administrators can upload photos")


class PhotosPhotoFull(BaseModel):
    access_key: Optional[str] = Field(None, description="Access key for the photo")
    album_id: int = Field(..., description="Album ID")
    can_comment: Optional[BaseBoolInt] = Field(None,
                                               description="Information whether current user can comment the photo")
    comments: Optional[BaseObjectCount] = Field(None)
    date: int = Field(..., description="Date when uploaded")
    height: Optional[int] = Field(None, description="Original photo height")
    id_: int = Field(..., alias='id', description="Photo ID")
    images: Optional[List[PhotosImage]] = Field(None)
    lat: Optional[float] = Field(None, description="Latitude")
    likes: Optional[BaseLikes] = Field(None)
    long: Optional[float] = Field(None, description="Longitude")
    owner_id: int = Field(..., description="Photo owner's ID")
    post_id: Optional[int] = Field(None, description="Post ID")
    reposts: Optional[BaseObjectCount] = Field(None)
    tags: Optional[BaseObjectCount] = Field(None)
    text: Optional[str] = Field(None, description="Photo caption")
    user_id: Optional[int] = Field(None, description="ID of the user who have uploaded the photo")
    width: Optional[int] = Field(None, description="Original photo width")


class PhotosPhotoFullXtrRealOffset(BaseModel):
    access_key: Optional[str] = Field(None, description="Access key for the photo")
    album_id: int = Field(..., description="Album ID")
    can_comment: Optional[BaseBoolInt] = Field(None)
    comments: Optional[BaseObjectCount] = Field(None)
    date: int = Field(..., description="Date when uploaded")
    height: Optional[int] = Field(None, description="Original photo height")
    hidden: Optional[BasePropertyExists] = Field(None, description="Returns if the photo is hidden above the wall")
    id_: int = Field(..., alias='id', description="Photo ID")
    lat: Optional[float] = Field(None, description="Latitude")
    likes: Optional[BaseLikes] = Field(None)
    long: Optional[float] = Field(None, description="Longitude")
    owner_id: int = Field(..., description="Photo owner's ID")
    photo_1280: Optional[str] = Field(None, description="URL of image with 1280 px width")
    photo_130: Optional[str] = Field(None, description="URL of image with 130 px width")
    photo_2560: Optional[str] = Field(None, description="URL of image with 2560 px width")
    photo_604: Optional[str] = Field(None, description="URL of image with 604 px width")
    photo_75: Optional[str] = Field(None, description="URL of image with 75 px width")
    photo_807: Optional[str] = Field(None, description="URL of image with 807 px width")
    post_id: Optional[int] = Field(None, description="Post ID")
    real_offset: Optional[int] = Field(None, description="Real position of the photo")
    reposts: Optional[BaseObjectCount] = Field(None)
    sizes: Optional[List[PhotosPhotoSizes]] = Field(None)
    tags: Optional[BaseObjectCount] = Field(None)
    text: Optional[str] = Field(None, description="Photo caption")
    user_id: Optional[int] = Field(None, description="ID of the user who have uploaded the photo")
    width: Optional[int] = Field(None, description="Original photo width")


class PhotosPhotoXtrRealOffset(BaseModel):
    access_key: Optional[str] = Field(None, description="Access key for the photo")
    album_id: int = Field(..., description="Album ID")
    date: int = Field(..., description="Date when uploaded")
    height: Optional[int] = Field(None, description="Original photo height")
    hidden: Optional[BasePropertyExists] = Field(None, description="Returns if the photo is hidden above the wall")
    id_: int = Field(..., alias='id', description="Photo ID")
    lat: Optional[float] = Field(None, description="Latitude")
    long: Optional[float] = Field(None, description="Longitude")
    owner_id: int = Field(..., description="Photo owner's ID")
    photo_1280: Optional[str] = Field(None, description="URL of image with 1280 px width")
    photo_130: Optional[str] = Field(None, description="URL of image with 130 px width")
    photo_2560: Optional[str] = Field(None, description="URL of image with 2560 px width")
    photo_604: Optional[str] = Field(None, description="URL of image with 604 px width")
    photo_75: Optional[str] = Field(None, description="URL of image with 75 px width")
    photo_807: Optional[str] = Field(None, description="URL of image with 807 px width")
    post_id: Optional[int] = Field(None, description="Post ID")
    real_offset: Optional[int] = Field(None, description="Real position of the photo")
    sizes: Optional[List[PhotosPhotoSizes]] = Field(None)
    text: Optional[str] = Field(None, description="Photo caption")
    user_id: Optional[int] = Field(None, description="ID of the user who have uploaded the photo")
    width: Optional[int] = Field(None, description="Original photo width")


class PhotosPhotoXtrTagInfo(BaseModel):
    access_key: Optional[str] = Field(None, description="Access key for the photo")
    album_id: int = Field(..., description="Album ID")
    date: int = Field(..., description="Date when uploaded")
    height: Optional[int] = Field(None, description="Original photo height")
    id_: int = Field(..., alias='id', description="Photo ID")
    lat: Optional[float] = Field(None, description="Latitude")
    long: Optional[float] = Field(None, description="Longitude")
    owner_id: int = Field(..., description="Photo owner's ID")
    photo_1280: Optional[str] = Field(None, description="URL of image with 1280 px width")
    photo_130: Optional[str] = Field(None, description="URL of image with 130 px width")
    photo_2560: Optional[str] = Field(None, description="URL of image with 2560 px width")
    photo_604: Optional[str] = Field(None, description="URL of image with 604 px width")
    photo_75: Optional[str] = Field(None, description="URL of image with 75 px width")
    photo_807: Optional[str] = Field(None, description="URL of image with 807 px width")
    placer_id: Optional[int] = Field(None, description="ID of the tag creator")
    post_id: Optional[int] = Field(None, description="Post ID")
    sizes: Optional[List[PhotosPhotoSizes]] = Field(None)
    tag_created: Optional[int] = Field(None, description="Date when tag has been added in Unixtime")
    tag_id: Optional[int] = Field(None, description="Tag ID")
    text: Optional[str] = Field(None, description="Photo caption")
    user_id: Optional[int] = Field(None, description="ID of the user who have uploaded the photo")
    width: Optional[int] = Field(None, description="Original photo width")


class PollsPoll(BaseModel):
    # anonymous: PollsPollAnonymous = Field(...)  object PollsPollAnonymous has error in json-schema
    friends: Optional[List[PollsFriend]] = Field(None)
    multiple: bool = Field(..., description="Information whether the poll with multiple choices")
    answer_id: Optional[int] = Field(None, description="Current user's answer ID")
    end_date: int = Field(...)
    answer_ids: Optional[List[int]] = Field(None, description="Current user's answer IDs")
    closed: bool = Field(...)
    is_board: bool = Field(...)
    can_edit: bool = Field(...)
    can_vote: bool = Field(...)
    can_report: bool = Field(...)
    can_share: bool = Field(...)
    photo: Optional[PollsBackground] = Field(None)
    answers: List[PollsAnswer] = Field(...)
    created: int = Field(..., description="Date when poll has been created in Unixtime")
    id_: int = Field(..., alias='id', description="Poll ID")
    owner_id: int = Field(..., description="Poll owner's ID")
    author_id: Optional[int] = Field(None, description="Poll author's ID")
    question: str = Field(..., description="Poll question")
    background: Optional[PollsBackground] = Field(None)
    votes: int = Field(..., description="Votes number")
    disable_unvote: bool = Field(...)


class StatsPeriod(BaseModel):
    activity: Optional[StatsActivity] = Field(None)
    period_from: Optional[int] = Field(None, description="Unix timestamp")
    period_to: Optional[int] = Field(None, description="Unix timestamp")
    reach: Optional[StatsReach] = Field(None)
    visitors: Optional[StatsViews] = Field(None)


class StoriesStoryStats(BaseModel):
    answer: StoriesStoryStatsStat = Field(...)
    bans: StoriesStoryStatsStat = Field(...)
    open_link: StoriesStoryStatsStat = Field(...)
    replies: StoriesStoryStatsStat = Field(...)
    shares: StoriesStoryStatsStat = Field(...)
    subscribers: StoriesStoryStatsStat = Field(...)
    views: StoriesStoryStatsStat = Field(...)
    likes: StoriesStoryStatsStat = Field(...)


class UsersUserSettingsXtr(BaseModel):
    connections: Optional[UsersUserConnections] = Field(None)
    bdate: Optional[str] = Field(None, description="User's date of birth")
    bdate_visibility: Optional[int] = Field(None, description="Information whether user's birthdate are hidden")
    city: Optional[BaseCity] = Field(None)
    country: Optional[BaseCountry] = Field(None)
    first_name: Optional[str] = Field(None, description="User first name")
    home_town: str = Field(..., description="User's hometown")
    last_name: Optional[str] = Field(None, description="User last name")
    maiden_name: Optional[str] = Field(None, description="User maiden name")
    name_request: Optional[AccountNameRequest] = Field(None)
    personal: Optional[UsersPersonal] = Field(None)
    phone: Optional[str] = Field(None, description="User phone number with some hidden digits")
    relation: Optional[UsersUserRelation] = Field(None, description="User relationship status")
    relation_partner: Optional[UsersUserMin] = Field(None)
    relation_pending: Optional[BaseBoolInt] = Field(None, description="Information whether relation status is pending")
    relation_requests: Optional[List[UsersUserMin]] = Field(None)
    screen_name: Optional[str] = Field(None, description="Domain name of the user's page")
    sex: Optional[BaseSex] = Field(None, description="User sex")
    status: str = Field(..., description="User status")
    status_audio: Optional[AudioAudio] = Field(None)
    interests: Optional[AccountUserSettingsInterests] = Field(None)
    languages: Optional[List[str]] = Field(None)


class UsersUserXtrType(UsersUser):
    type_: Optional[UsersUserType] = Field(None, alias='type')


class UtilsLinkStatsExtended(BaseModel):
    key: Optional[str] = Field(None, description="Link key (characters after vk.cc/)")
    stats: Optional[List[UtilsStatsExtended]] = Field(None)


class VideoVideo(BaseModel):
    access_key: Optional[str] = Field(None, description="Video access key")
    adding_date: Optional[int] = Field(None, description="Date when the video has been added in Unixtime")
    can_comment: Optional[BaseBoolInt] = Field(None,
                                               description="Information whether current user can comment the video")
    can_edit: Optional[BaseBoolInt] = Field(None, description="Information whether current user can edit the video")
    can_like: Optional[BaseBoolInt] = Field(None, description="Information whether current user can like the video")
    can_repost: Optional[BaseBoolInt] = Field(None, description="Information whether current user can repost the video")
    can_subscribe: Optional[BaseBoolInt] = Field(None,
                                                 description="Information whether current user can subscribe to "
                                                             "author of the video")
    can_add_to_faves: Optional[BaseBoolInt] = Field(None,
                                                    description="Information whether current user can add the video "
                                                                "to favourites")
    can_add: Optional[BaseBoolInt] = Field(None, description="Information whether current user can add the video")
    can_attach_link: Optional[BaseBoolInt] = Field(None,
                                                   description="Information whether current user can attach action "
                                                               "button to the video")
    is_private: Optional[BaseBoolInt] = Field(None, description="1 if video is private")
    comments: Optional[int] = Field(None, description="Number of comments")
    date: Optional[int] = Field(None, description="Date when video has been uploaded in Unixtime")
    description: Optional[str] = Field(None, description="Video description")
    duration: Optional[int] = Field(None, description="Video duration in seconds")
    image: Optional[List[VideoVideoImage]] = Field(None)
    first_frame: Optional[List[VideoVideoImage]] = Field(None)
    width: Optional[int] = Field(None, description="Video width")
    height: Optional[int] = Field(None, description="Video height")
    id_: Optional[int] = Field(None, alias='id', description="Video ID")
    owner_id: Optional[int] = Field(None, description="Video owner ID")
    user_id: Optional[int] = Field(None,
                                   description="Id of the user who uploaded the video if it was uploaded to a group "
                                               "by member")
    title: Optional[str] = Field(None, description="Video title")
    is_favorite: Optional[bool] = Field(None, description="Whether video is added to bookmarks")
    player: Optional[str] = Field(None, description="Video embed URL")
    processing: Optional[BasePropertyExists] = Field(None, description="Returns if the video is processing")
    converting: Optional[BaseBoolInt] = Field(None, description="1 if  video is being converted")
    restriction: Optional[MediaRestriction] = Field(None)
    added: Optional[BaseBoolInt] = Field(None, description="1 if video is added to user's albums")
    is_subscribed: Optional[BaseBoolInt] = Field(None, description="1 if user is subscribed to author of the video")
    track_code: Optional[str] = Field(None)
    repeat: Optional[BasePropertyExists] = Field(None, description="Information whether the video is repeated")
    type_: Optional[str] = Field(None, alias='type')
    views: Optional[int] = Field(None, description="Number of views")
    local_views: Optional[int] = Field(None, description="If video is external, number of views on vk")
    content_restricted: Optional[int] = Field(None, description="Restriction code")
    content_restricted_message: Optional[str] = Field(None, description="Restriction text")
    balance: Optional[int] = Field(None, description="Live donations balance")
    live_status: Optional[str] = Field(None, description="Live stream status")
    live: Optional[BasePropertyExists] = Field(None, description="1 if the video is a live stream")
    upcoming: Optional[BasePropertyExists] = Field(None, description="1 if the video is an upcoming stream")
    spectators: Optional[int] = Field(None, description="Number of spectators of the stream")
    platform: Optional[str] = Field(None, description="External platform")
    likes: Optional[BaseLikes] = Field(None)
    reposts: Optional[BaseRepostsInfo] = Field(None)


class VideoVideoAlbumFull(BaseModel):
    count: int = Field(..., description="Total number of videos in album")
    id_: Optional[int] = Field(None, alias='id', description="Album ID")
    image: Optional[List[VideoVideoImage]] = Field(None, description="Album cover image in different sizes")
    image_blur: Optional[BasePropertyExists] = Field(None, description="Need blur album thumb or not")
    is_system: Optional[BasePropertyExists] = Field(None, description="Information whether album is system")
    owner_id: int = Field(..., description="Album owner's ID")
    title: str = Field(..., description="Album title")
    updated_time: int = Field(..., description="Date when the album has been updated last time in Unixtime")


class AccountPushSettings(BaseModel):
    disabled: Optional[BaseBoolInt] = Field(None, description="Information whether notifications are disabled")
    disabled_until: Optional[int] = Field(None, description="Time until that notifications are disabled in Unixtime")
    settings: Optional[AccountPushParams] = Field(None)
    conversations: Optional[AccountPushConversations] = Field(None)


class AccountUserSettings(UsersUserMin, UsersUserSettingsXtr):
    photo_200: Optional[str] = Field(None, description="URL of square photo of the user with 200 pixels in width")
    is_service_account: Optional[bool] = Field(None, description="flag about service account")


class AdsDemoStats(BaseModel):
    id_: Optional[int] = Field(None, alias='id', description="Object ID")
    stats: Optional[AdsDemostatsFormat] = Field(None)
    type_: Optional[AdsObjectType] = Field(None, alias='type')


class BaseLink(BaseModel):
    application: Optional[BaseLinkApplication] = Field(None)
    button: Optional[BaseLinkButton] = Field(None)
    caption: Optional[str] = Field(None, description="Link caption")
    description: Optional[str] = Field(None, description="Link description")
    id_: Optional[str] = Field(None, alias='id', description="Link ID")
    is_favorite: Optional[bool] = Field(None)
    photo: Optional[PhotosPhoto] = Field(None)
    preview_page: Optional[str] = Field(None, description="String ID of the page with article preview")
    preview_url: Optional[str] = Field(None, description="URL of the page with article preview")
    product: Optional[BaseLinkProduct] = Field(None)
    rating: Optional[BaseLinkRating] = Field(None)
    title: Optional[str] = Field(None, description="Link title")
    url: str = Field(..., description="Link URL")
    target_object: Optional[LinkTargetObject] = Field(None)
    is_external: Optional[bool] = Field(None, description="Information whether the current link is external")
    video: Optional[VideoVideo] = Field(None, description="Video from link")


class CallbackGroupChangePhoto(BaseModel):
    user_id: int = Field(...)
    photo: PhotosPhoto = Field(...)


class DocsDocPreview(BaseModel):
    audio_msg: Optional[DocsDocPreviewAudioMsg] = Field(None)
    graffiti: Optional[DocsDocPreviewGraffiti] = Field(None)
    photo: Optional[DocsDocPreviewPhoto] = Field(None)
    video: Optional[DocsDocPreviewVideo] = Field(None)


# object GroupsBannedItem has error in json-schema


class MarketMarketAlbum(BaseModel):
    count: int = Field(..., description="Items number")
    id_: int = Field(..., alias='id', description="Market album ID")
    owner_id: int = Field(..., description="Market album owner's ID")
    photo: Optional[PhotosPhoto] = Field(None)
    title: str = Field(..., description="Market album title")
    updated_time: int = Field(..., description="Date when album has been updated last time in Unixtime")


class MarketMarketItemFull(MarketMarketItem):
    albums_ids: Optional[List[int]] = Field(None)
    photos: Optional[List[PhotosPhoto]] = Field(None)
    can_comment: Optional[BaseBoolInt] = Field(None, description="Information whether current use can comment the item")
    can_repost: Optional[BaseBoolInt] = Field(None, description="Information whether current use can repost the item")
    likes: Optional[BaseLikes] = Field(None)
    reposts: Optional[BaseRepostsInfo] = Field(None)
    views_count: Optional[int] = Field(None, description="Views number")


class MessagesKeyboard(BaseModel):
    author_id: Optional[int] = Field(None, description="Community or bot, which set this keyboard")
    buttons: List[List[MessagesKeyboardButton]] = Field(...)
    one_time: bool = Field(..., description="Should this keyboard disappear on first use")
    inline: Optional[bool] = Field(None)


class MessagesUserXtrInvitedBy(UsersUserXtrType):
    invited_by: Optional[int] = Field(None, description="ID of the inviter")


class NewsfeedItemVideoVideo(BaseModel):
    count: Optional[int] = Field(None, description="Tags number")
    items: Optional[List[VideoVideo]] = Field(None)


class NewsfeedNewsfeedPhoto(PhotosPhoto):
    likes: Optional[BaseLikes] = Field(None)
    comments: Optional[BaseObjectCount] = Field(None)
    can_repost: Optional[BaseBoolInt] = Field(None, description="Information whether current user can repost the photo")


class PhotosPhotoAlbum(BaseModel):
    created: int = Field(..., description="Date when the album has been created in Unixtime")
    description: Optional[str] = Field(None, description="Photo album description")
    id_: int = Field(..., alias='id', description="Photo album ID")
    owner_id: int = Field(..., description="Album owner's ID")
    size: int = Field(..., description="Photos number")
    thumb: Optional[PhotosPhoto] = Field(None)
    title: str = Field(..., description="Photo album title")
    updated: int = Field(..., description="Date when the album has been updated last time in Unixtime")


class PhotosTagsSuggestionItem(BaseModel):
    title: Optional[str] = Field(None)
    type_: Optional[str] = Field(None, alias='type')
    buttons: Optional[List[PhotosTagsSuggestionItemButton]] = Field(None)
    photo: Optional[PhotosPhoto] = Field(None)
    tags: Optional[List[PhotosPhotoTag]] = Field(None)


class SearchHint(BaseModel):
    app: Optional[AppsApp] = Field(None)
    description: str = Field(..., description="Object description")
    global_: Optional[BaseBoolInt] = Field(None, alias='global',
                                           description="Information whether the object has been found globally")
    group: Optional[GroupsGroup] = Field(None)
    profile: Optional[UsersUserMin] = Field(None)
    section: SearchHintSection = Field(...)
    type_: SearchHintType = Field(..., alias='type')


class UsersCropPhoto(BaseModel):
    crop: Optional[UsersCropPhotoCrop] = Field(None)
    photo: Optional[PhotosPhoto] = Field(None)
    rect: Optional[UsersCropPhotoRect] = Field(None)


class UsersSubscriptionsItem(UsersUserXtrType, GroupsGroupFull):
    ...


class VideoVideoFull(VideoVideo):
    files: Optional[VideoVideoFiles] = Field(None)
    live_settings: Optional[VideoLiveSettings] = Field(None, description="Settings for live stream")


class DocsDoc(BaseModel):
    id_: int = Field(..., alias='id', description="Document ID")
    owner_id: int = Field(..., description="Document owner ID")
    title: str = Field(..., description="Document title")
    size: int = Field(..., description="File size in bites")
    ext: str = Field(..., description="File extension")
    url: Optional[str] = Field(None, description="File URL")
    date: int = Field(..., description="Date when file has been uploaded in Unixtime")
    type_: int = Field(..., alias='type', description="Document type")
    preview: Optional[DocsDocPreview] = Field(None)
    is_licensed: Optional[BaseBoolInt] = Field(None)
    access_key: Optional[str] = Field(None, description="Access key for the document")
    tags: Optional[List[str]] = Field(None, description="Document tags")


class MessagesChatFull(BaseModel):
    admin_id: int = Field(..., description="Chat creator ID")
    id_: int = Field(..., alias='id', description="Chat ID")
    kicked: Optional[BaseBoolInt] = Field(None, description="Shows that user has been kicked from the chat")
    left: Optional[BaseBoolInt] = Field(None, description="Shows that user has been left the chat")
    photo_100: Optional[str] = Field(None, description="URL of the preview image with 100 px in width")
    photo_200: Optional[str] = Field(None, description="URL of the preview image with 200 px in width")
    photo_50: Optional[str] = Field(None, description="URL of the preview image with 50 px in width")
    push_settings: Optional[MessagesChatPushSettings] = Field(None)
    title: Optional[str] = Field(None, description="Chat title")
    type_: str = Field(..., alias='type', description="Chat type")
    users: List[MessagesUserXtrInvitedBy] = Field(...)


class MessagesConversation(BaseModel):
    peer: MessagesConversationPeer = Field(...)
    last_message_id: int = Field(..., description="ID of the last message in conversation")
    in_read: int = Field(..., description="Last message user have read")
    out_read: int = Field(..., description="Last outcoming message have been read by the opponent")
    unread_count: Optional[int] = Field(None, description="Unread messages number")
    is_marked_unread: Optional[bool] = Field(None, description="Is this conversation uread")
    important: Optional[bool] = Field(None)
    unanswered: Optional[bool] = Field(None)
    special_service_type: Optional[str] = Field(None)
    message_request_data: Optional[MessagesMessageRequestData] = Field(None)
    mentions: Optional[List[int]] = Field(None, description="Ids of messages with mentions")
    current_keyboard: Optional[MessagesKeyboard] = Field(None)


class NewsfeedItemPhotoPhotos(BaseModel):
    count: Optional[int] = Field(None, description="Photos number")
    items: Optional[List[NewsfeedNewsfeedPhoto]] = Field(None)


class NewsfeedItemPhotoTagPhotoTags(BaseModel):
    count: Optional[int] = Field(None, description="Tags number")
    items: Optional[List[NewsfeedNewsfeedPhoto]] = Field(None)


class NewsfeedItemVideo(WallCarouselBase, NewsfeedItemBase):
    video: Optional[NewsfeedItemVideoVideo] = Field(None)


class StoriesClickableSticker(BaseModel):
    clickable_area: List[StoriesClickableArea] = Field(...)
    id_: int = Field(..., alias='id', description="Clickable sticker ID")
    hashtag: Optional[str] = Field(None)
    link_object: Optional[BaseLink] = Field(None)
    mention: Optional[str] = Field(None)
    tooltip_text: Optional[str] = Field(None)
    owner_id: Optional[int] = Field(None)
    story_id: Optional[int] = Field(None)
    question: Optional[str] = Field(None)
    question_button: Optional[str] = Field(None)
    place_id: Optional[int] = Field(None)
    market_item: Optional[MarketMarketItem] = Field(None)
    audio: Optional[AudioAudio] = Field(None)
    audio_start_time: Optional[int] = Field(None)
    style: Optional[str] = Field(None)
    type_: str = Field(..., alias='type')
    subtype: Optional[str] = Field(None)
    post_owner_id: Optional[int] = Field(None)
    post_id: Optional[int] = Field(None)
    poll: Optional[PollsPoll] = Field(None)
    color: Optional[str] = Field(None, description="Color, hex format")
    sticker_id: Optional[int] = Field(None, description="Sticker ID")
    sticker_pack_id: Optional[int] = Field(None, description="Sticker pack ID")
    app: Optional[AppsAppMin] = Field(None)
    app_context: Optional[str] = Field(None, description="Additional context for app sticker")
    has_new_interactions: Optional[bool] = Field(None,
                                                 description="Whether current user has unread interaction with this "
                                                             "app")
    is_broadcast_notify_allowed: Optional[bool] = Field(None,
                                                        description="Whether current user allowed broadcast notify "
                                                                    "from this app")


class UsersUserFull(UsersUser):
    first_name_nom: Optional[str] = Field(None, description="User's first name in nominative case")
    first_name_gen: Optional[str] = Field(None, description="User's first name in genitive case")
    first_name_dat: Optional[str] = Field(None, description="User's first name in dative case")
    first_name_acc: Optional[str] = Field(None, description="User's first name in accusative case")
    first_name_ins: Optional[str] = Field(None, description="User's first name in instrumental case")
    first_name_abl: Optional[str] = Field(None, description="User's first name in prepositional case")
    last_name_nom: Optional[str] = Field(None, description="User's last name in nominative case")
    last_name_gen: Optional[str] = Field(None, description="User's last name in genitive case")
    last_name_dat: Optional[str] = Field(None, description="User's last name in dative case")
    last_name_acc: Optional[str] = Field(None, description="User's last name in accusative case")
    last_name_ins: Optional[str] = Field(None, description="User's last name in instrumental case")
    last_name_abl: Optional[str] = Field(None, description="User's last name in prepositional case")
    nickname: Optional[str] = Field(None, description="User nickname")
    maiden_name: Optional[str] = Field(None, description="User maiden name")
    domain: Optional[str] = Field(None, description="Domain name of the user's page")
    bdate: Optional[str] = Field(None, description="User's date of birth")
    city: Optional[BaseObject] = Field(None)
    country: Optional[BaseCountry] = Field(None)
    timezone: Optional[int] = Field(None, description="User's timezone")
    owner_state: Optional[OwnerState] = Field(None)
    photo_200: Optional[str] = Field(None, description="URL of square photo of the user with 200 pixels in width")
    photo_max: Optional[str] = Field(None, description="URL of square photo of the user with maximum width")
    photo_200_orig: Optional[str] = Field(None, description="URL of user's photo with 200 pixels in width")
    photo_400_orig: Optional[str] = Field(None, description="URL of user's photo with 400 pixels in width")
    photo_max_orig: Optional[str] = Field(None, description="URL of user's photo of maximum size")
    photo_id: Optional[str] = Field(None, description="ID of the user's main photo")
    has_photo: Optional[BaseBoolInt] = Field(None, description="Information whether the user has main photo")
    has_mobile: Optional[BaseBoolInt] = Field(None,
                                              description="Information whether the user specified his phone number")
    is_friend: Optional[BaseBoolInt] = Field(None,
                                             description="Information whether the user is a friend of current user")
    wall_comments: Optional[BaseBoolInt] = Field(None,
                                                 description="Information whether current user can comment wall posts")
    can_post: Optional[BaseBoolInt] = Field(None,
                                            description="Information whether current user can post on the user's wall")
    can_see_all_posts: Optional[BaseBoolInt] = Field(None,
                                                     description="Information whether current user can see other "
                                                                 "users' audio on the wall")
    can_see_audio: Optional[BaseBoolInt] = Field(None,
                                                 description="Information whether current user can see the user's "
                                                             "audio")
    can_write_private_message: Optional[BaseBoolInt] = Field(None,
                                                             description="Information whether current user can write "
                                                                         "private message")
    can_send_friend_request: Optional[BaseBoolInt] = Field(None,
                                                           description="Information whether current user can send a "
                                                                       "friend request")
    can_be_invited_group: Optional[bool] = Field(None,
                                                 description="Information whether current user can be invited to the "
                                                             "community")
    mobile_phone: Optional[str] = Field(None, description="User's mobile phone number")
    home_phone: Optional[str] = Field(None, description="User's additional phone number")
    site: Optional[str] = Field(None, description="User's website")
    status_audio: Optional[AudioAudio] = Field(None)
    status: Optional[str] = Field(None, description="User's status")
    activity: Optional[str] = Field(None, description="User's status")
    last_seen: Optional[UsersLastSeen] = Field(None)
    exports: Optional[UsersExports] = Field(None)
    crop_photo: Optional[UsersCropPhoto] = Field(None)
    followers_count: Optional[int] = Field(None, description="Number of user's followers")
    video_live_level: Optional[int] = Field(None, description="User level in live streams achievements")
    video_live_count: Optional[int] = Field(None, description="Number of user's live streams")
    blacklisted: Optional[BaseBoolInt] = Field(None,
                                               description="Information whether current user is in the requested "
                                                           "user's blacklist.")
    blacklisted_by_me: Optional[BaseBoolInt] = Field(None,
                                                     description="Information whether the requested user is in "
                                                                 "current user's blacklist")
    is_favorite: Optional[BaseBoolInt] = Field(None,
                                               description="Information whether the requested user is in faves of "
                                                           "current user")
    is_hidden_from_feed: Optional[BaseBoolInt] = Field(None,
                                                       description="Information whether the requested user is hidden "
                                                                   "from current user's newsfeed")
    common_count: Optional[int] = Field(None, description="Number of common friends with current user")
    occupation: Optional[UsersOccupation] = Field(None)
    career: Optional[List[UsersCareer]] = Field(None)
    military: Optional[List[UsersMilitary]] = Field(None)
    university: Optional[int] = Field(None, description="University ID")
    university_name: Optional[str] = Field(None, description="University name")
    faculty: Optional[int] = Field(None, description="Faculty ID")
    faculty_name: Optional[str] = Field(None, description="Faculty name")
    graduation: Optional[int] = Field(None, description="Graduation year")
    education_form: Optional[str] = Field(None, description="Education form")
    education_status: Optional[str] = Field(None, description="User's education status")
    home_town: Optional[str] = Field(None, description="User hometown")
    relation: Optional[UsersUserRelation] = Field(None, description="User relationship status")
    relation_partner: Optional[UsersUserMin] = Field(None)
    personal: Optional[UsersPersonal] = Field(None)
    universities: Optional[List[UsersUniversity]] = Field(None)
    schools: Optional[List[UsersSchool]] = Field(None)
    relatives: Optional[List[UsersRelative]] = Field(None)
    is_subscribed_podcasts: Optional[bool] = Field(None,
                                                   description="Information whether current user is subscribed to "
                                                               "podcasts")
    can_subscribe_podcasts: Optional[bool] = Field(None, description="Owner in whitelist or not")
    can_subscribe_posts: Optional[bool] = Field(None, description="Can subscribe to wall")


class FavePage(BaseModel):
    description: str = Field(..., description="Some info about user or group")
    group: Optional[GroupsGroupFull] = Field(None)
    tags: List[FaveTag] = Field(...)
    type_: FavePageType = Field(..., alias='type', description="Item type")
    updated_date: Optional[int] = Field(None, description="Timestamp, when this page was bookmarked")
    user: Optional[UsersUserFull] = Field(None)


class FriendsUserXtrLists(UsersUserFull):
    lists: Optional[List[int]] = Field(None)


class FriendsUserXtrPhone(UsersUserFull):
    phone: Optional[str] = Field(None, description="User phone")


class GroupsUserXtrRole(UsersUserFull):
    role: Optional[GroupsRoleOptions] = Field(None)


class MessagesHistoryMessageAttachment(BaseModel):
    audio: Optional[AudioAudio] = Field(None)
    audio_message: Optional[MessagesAudioMessage] = Field(None)
    doc: Optional[DocsDoc] = Field(None)
    graffiti: Optional[MessagesGraffiti] = Field(None)
    link: Optional[BaseLink] = Field(None)
    market: Optional[BaseLink] = Field(None)
    photo: Optional[PhotosPhoto] = Field(None)
    share: Optional[BaseLink] = Field(None)
    type_: MessagesHistoryMessageAttachmentType = Field(..., alias='type')
    video: Optional[VideoVideo] = Field(None)
    wall: Optional[BaseLink] = Field(None)


class NewsfeedItemPhoto(WallCarouselBase, NewsfeedItemBase):
    photos: Optional[NewsfeedItemPhotoPhotos] = Field(None)
    post_id: Optional[int] = Field(None, description="Post ID")


class NewsfeedItemPhotoTag(WallCarouselBase, NewsfeedItemBase):
    photo_tags: Optional[NewsfeedItemPhotoTagPhotoTags] = Field(None)
    post_id: Optional[int] = Field(None, description="Post ID")


class StoriesClickableStickers(BaseModel):
    clickable_stickers: List[StoriesClickableSticker] = Field(...)
    original_height: int = Field(...)
    original_width: int = Field(...)


class StoriesViewersItem(BaseModel):
    is_liked: bool = Field(..., description="user has like for this object")
    user_id: int = Field(..., description="user id")
    user: Optional[UsersUserFull] = Field(None)


class UsersUserXtrCounters(UsersUserFull):
    counters: Optional[UsersUserCounters] = Field(None)


class WallCommentAttachment(BaseModel):
    audio: Optional[AudioAudio] = Field(None)
    doc: Optional[DocsDoc] = Field(None)
    link: Optional[BaseLink] = Field(None)
    market: Optional[MarketMarketItem] = Field(None)
    market_market_album: Optional[MarketMarketAlbum] = Field(None)
    note: Optional[WallAttachedNote] = Field(None)
    page: Optional[PagesWikipageFull] = Field(None)
    photo: Optional[PhotosPhoto] = Field(None)
    sticker: Optional[BaseSticker] = Field(None)
    type_: WallCommentAttachmentType = Field(..., alias='type')
    video: Optional[VideoVideo] = Field(None)


class WallWallpostAttachment(BaseModel):
    access_key: Optional[str] = Field(None, description="Access key for the audio")
    album: Optional[PhotosPhotoAlbum] = Field(None)
    app: Optional[WallAppPost] = Field(None)
    audio: Optional[AudioAudio] = Field(None)
    doc: Optional[DocsDoc] = Field(None)
    event: Optional[EventsEventAttach] = Field(None)
    group: Optional[GroupsGroupAttach] = Field(None)
    graffiti: Optional[WallGraffiti] = Field(None)
    link: Optional[BaseLink] = Field(None)
    market: Optional[MarketMarketItem] = Field(None)
    market_album: Optional[MarketMarketAlbum] = Field(None)
    note: Optional[WallAttachedNote] = Field(None)
    page: Optional[PagesWikipageFull] = Field(None)
    photo: Optional[PhotosPhoto] = Field(None)
    photos_list: Optional[List[str]] = Field(None)
    poll: Optional[PollsPoll] = Field(None)
    posted_photo: Optional[WallPostedPhoto] = Field(None)
    type_: WallWallpostAttachmentType = Field(..., alias='type')
    video: Optional[VideoVideo] = Field(None)


class WidgetsCommentRepliesItem(BaseModel):
    cid: Optional[int] = Field(None, description="Comment ID")
    date: Optional[int] = Field(None, description="Date when the comment has been added in Unixtime")
    likes: Optional[WidgetsWidgetLikes] = Field(None)
    text: Optional[str] = Field(None, description="Comment text")
    uid: Optional[int] = Field(None, description="User ID")
    user: Optional[UsersUserFull] = Field(None)


class BoardTopicComment(BaseModel):
    attachments: Optional[List[WallCommentAttachment]] = Field(None)
    date: int = Field(..., description="Date when the comment has been added in Unixtime")
    from_id: int = Field(..., description="Author ID")
    id_: int = Field(..., alias='id', description="Comment ID")
    real_offset: Optional[int] = Field(None, description="Real position of the comment")
    text: str = Field(..., description="Comment text")
    can_edit: Optional[BaseBoolInt] = Field(None, description="Information whether current user can edit the comment")
    likes: Optional[BaseLikesInfo] = Field(None)


class MessagesHistoryAttachment(BaseModel):
    attachment: MessagesHistoryMessageAttachment = Field(...)
    message_id: int = Field(..., description="Message ID")
    from_id: int = Field(..., description="Message author's ID")


class NotificationsFeedback(BaseModel):
    attachments: Optional[List[WallWallpostAttachment]] = Field(None)
    from_id: Optional[int] = Field(None, description="Reply author's ID")
    geo: Optional[BaseGeo] = Field(None)
    id_: Optional[int] = Field(None, alias='id', description="Item ID")
    likes: Optional[BaseLikesInfo] = Field(None)
    text: Optional[str] = Field(None, description="Reply text")
    to_id: Optional[int] = Field(None, description="Wall owner's ID")


class StoriesStory(BaseModel):
    access_key: Optional[str] = Field(None, description="Access key for private object.")
    can_comment: Optional[BaseBoolInt] = Field(None,
                                               description="Information whether current user can comment the story (0 "
                                                           "- no, 1 - yes).")
    can_reply: Optional[BaseBoolInt] = Field(None,
                                             description="Information whether current user can reply to the story (0 "
                                                         "- no, 1 - yes).")
    can_see: Optional[BaseBoolInt] = Field(None,
                                           description="Information whether current user can see the story (0 - no, "
                                                       "1 - yes).")
    can_like: Optional[bool] = Field(None, description="Information whether current user can like the story.")
    can_share: Optional[BaseBoolInt] = Field(None,
                                             description="Information whether current user can share the story (0 - "
                                                         "no, 1 - yes).")
    can_hide: Optional[BaseBoolInt] = Field(None,
                                            description="Information whether current user can hide the story (0 - no, "
                                                        "1 - yes).")
    date: Optional[int] = Field(None, description="Date when story has been added in Unixtime.")
    expires_at: Optional[int] = Field(None, description="Story expiration time. Unixtime.")
    id_: int = Field(..., alias='id', description="Story ID.")
    is_deleted: Optional[bool] = Field(None,
                                       description="Information whether the story is deleted (false - no, true - yes).")
    is_expired: Optional[bool] = Field(None,
                                       description="Information whether the story is expired (false - no, true - yes).")
    link: Optional[StoriesStoryLink] = Field(None)
    owner_id: int = Field(..., description="Story owner's ID.")
    parent_story: Optional["StoriesStory"] = Field(None)
    parent_story_access_key: Optional[str] = Field(None, description="Access key for private object.")
    parent_story_id: Optional[int] = Field(None, description="Parent story ID.")
    parent_story_owner_id: Optional[int] = Field(None, description="Parent story owner's ID.")
    photo: Optional[PhotosPhoto] = Field(None)
    replies: Optional[StoriesReplies] = Field(None, description="Replies counters to current story.")
    seen: Optional[BaseBoolInt] = Field(None,
                                        description="Information whether current user has seen the story or not (0 - "
                                                    "no, 1 - yes).")
    type_: Optional[StoriesStoryType] = Field(None, alias='type')
    clickable_stickers: Optional[StoriesClickableStickers] = Field(None)
    video: Optional[VideoVideo] = Field(None)
    views: Optional[int] = Field(None, description="Views number.")
    can_ask: Optional[BaseBoolInt] = Field(None,
                                           description="Information whether story has question sticker and current "
                                                       "user can send question to the author")
    can_ask_anonymous: Optional[BaseBoolInt] = Field(None,
                                                     description="Information whether story has question sticker and "
                                                                 "current user can send anonymous question to the author")
    narratives_count: Optional[int] = Field(None)
    first_narrative_title: Optional[str] = Field(None)
    birthday_wish_user_id: Optional[int] = Field(None)


StoriesStory.update_forward_refs()


class WallWallComment(BaseModel):
    attachments: Optional[List[WallCommentAttachment]] = Field(None)
    date: int = Field(..., description="Date when the comment has been added in Unixtime")
    from_id: int = Field(..., description="Author ID")
    id_: int = Field(..., alias='id', description="Comment ID")
    likes: Optional[BaseLikesInfo] = Field(None)
    real_offset: Optional[int] = Field(None, description="Real position of the comment")
    reply_to_comment: Optional[int] = Field(None, description="Replied comment ID")
    reply_to_user: Optional[int] = Field(None, description="Replied user ID")
    text: str = Field(..., description="Comment text")
    # thread: Optional[CommentThread] = Field(None)  object CommentThread has error in json-schema
    post_id: Optional[int] = Field(None)
    owner_id: Optional[int] = Field(None)
    parents_stack: Optional[List[int]] = Field(None)
    deleted: Optional[bool] = Field(None)


class WallWallpost(BaseModel):
    access_key: Optional[str] = Field(None, description="Access key to private object")
    attachments: Optional[List[WallWallpostAttachment]] = Field(None)
    copyright_: Optional[WallPostCopyright] = Field(None, alias='copyright',
                                                    description="Information about the source of the post")
    date: Optional[int] = Field(None, description="Date of publishing in Unixtime")
    edited: Optional[int] = Field(None, description="Date of editing in Unixtime")
    from_id: Optional[int] = Field(None, description="Post author ID")
    geo: Optional[WallGeo] = Field(None)
    id_: Optional[int] = Field(None, alias='id', description="Post ID")
    is_archived: Optional[bool] = Field(None, description="Is post archived, only for post owners")
    is_favorite: Optional[bool] = Field(None, description="Information whether the post in favorites list")
    likes: Optional[BaseLikesInfo] = Field(None, description="Count of likes")
    owner_id: Optional[int] = Field(None, description="Wall owner's ID")
    post_source: Optional[WallPostSource] = Field(None)
    post_type: Optional[WallPostType] = Field(None)
    reposts: Optional[BaseRepostsInfo] = Field(None, description="Count of views")
    signer_id: Optional[int] = Field(None, description="Post signer ID")
    text: Optional[str] = Field(None, description="Post text")
    views: Optional[WallViews] = Field(None, description="Count of views")


class WallWallpostToId(BaseModel):
    attachments: Optional[List[WallWallpostAttachment]] = Field(None)
    comments: Optional[BaseCommentsInfo] = Field(None)
    copy_owner_id: Optional[int] = Field(None, description="ID of the source post owner")
    copy_post_id: Optional[int] = Field(None, description="ID of the source post")
    date: Optional[int] = Field(None, description="Date of publishing in Unixtime")
    from_id: Optional[int] = Field(None, description="Post author ID")
    geo: Optional[WallGeo] = Field(None)
    id_: Optional[int] = Field(None, alias='id', description="Post ID")
    is_favorite: Optional[bool] = Field(None, description="Information whether the post in favorites list")
    likes: Optional[BaseLikesInfo] = Field(None)
    post_id: Optional[int] = Field(None, description="wall post ID (if comment)")
    post_source: Optional[WallPostSource] = Field(None)
    post_type: Optional[WallPostType] = Field(None)
    reposts: Optional[BaseRepostsInfo] = Field(None)
    signer_id: Optional[int] = Field(None, description="Post signer ID")
    text: Optional[str] = Field(None, description="Post text")
    to_id: Optional[int] = Field(None, description="Wall owner's ID")


class WidgetsCommentReplies(BaseModel):
    can_post: Optional[BaseBoolInt] = Field(None, description="Information whether current user can comment the post")
    count: Optional[int] = Field(None, description="Comments number")
    replies: Optional[List[WidgetsCommentRepliesItem]] = Field(None)


class CommentThread(BaseModel):
    can_post: Optional[bool] = Field(None, description="Information whether current user can comment the post")
    count: int = Field(..., description="Comments number")
    groups_can_post: Optional[bool] = Field(None, description="Information whether groups can comment the post")
    items: Optional[List[WallWallComment]] = Field(None)
    show_reply_button: Optional[bool] = Field(None,
                                              description="Information whether recommended to display reply button")


class NewsfeedItemDigest(NewsfeedItemBase):
    button_text: Optional[str] = Field(None)
    feed_id: Optional[str] = Field(None, description="id of feed in digest")
    items: Optional[List[WallWallpost]] = Field(None)
    main_post_ids: Optional[List[str]] = Field(None)
    template: Optional[str] = Field(None, description="type of digest")
    title: Optional[str] = Field(None)
    track_code: Optional[str] = Field(None)


class NewsfeedItemWallpost(WallCarouselBase, NewsfeedItemBase):
    activity: Optional[NewsfeedEventActivity] = Field(None)
    attachments: Optional[List[WallWallpostAttachment]] = Field(None)
    comments: Optional[BaseCommentsInfo] = Field(None)
    copy_history: Optional[List[WallWallpost]] = Field(None)
    feedback: Optional[NewsfeedItemWallpostFeedback] = Field(None)
    geo: Optional[BaseGeo] = Field(None)
    is_favorite: Optional[bool] = Field(None, description="Information whether the post in favorites list")
    likes: Optional[BaseLikesInfo] = Field(None)
    marked_as_ads: Optional[BaseBoolInt] = Field(None, description="Information whether the post is marked as ads")
    post_id: Optional[int] = Field(None, description="Post ID")
    post_source: Optional[WallPostSource] = Field(None)
    post_type: Optional[NewsfeedItemWallpostType] = Field(None)
    reposts: Optional[BaseRepostsInfo] = Field(None)
    signer_id: Optional[int] = Field(None, description="Post signer ID")
    text: Optional[str] = Field(None, description="Post text")
    views: Optional[WallViews] = Field(None, description="Count of views")
    short_text_rate: Optional[float] = Field(None, description="Preview length control parameter")


class NotificationsNotificationsComment(BaseModel):
    date: Optional[int] = Field(None, description="Date when the comment has been added in Unixtime")
    id_: Optional[int] = Field(None, alias='id', description="Comment ID")
    owner_id: Optional[int] = Field(None, description="Author ID")
    photo: Optional[PhotosPhoto] = Field(None)
    post: Optional[WallWallpost] = Field(None)
    text: Optional[str] = Field(None, description="Comment text")
    topic: Optional[BoardTopic] = Field(None)
    video: Optional[VideoVideo] = Field(None)


class StoriesFeedItem(BaseModel):
    type_: str = Field(..., alias='type', description="Type of Feed Item")
    stories: Optional[List[StoriesStory]] = Field(None, description="Author stories")
    grouped: Optional[List["StoriesFeedItem"]] = Field(None,
                                                       description="Grouped stories of various authors (for types "
                                                                   "community_grouped_stories/app_grouped_stories type)")
    app: Optional[AppsAppMin] = Field(None,
                                      description="App, which stories has been grouped (for type app_grouped_stories)")
    promo_data: Optional[StoriesPromoBlock] = Field(None,
                                                    description="Additional data for promo stories (for type "
                                                                "promo_stories)")


StoriesFeedItem.update_forward_refs()


class WallWallpostFull(WallCarouselBase, WallWallpost):
    copy_history: Optional[List[WallWallpost]] = Field(None)
    can_edit: Optional[BaseBoolInt] = Field(None, description="Information whether current user can edit the post")
    created_by: Optional[int] = Field(None, description="Post creator ID (if post still can be edited)")
    can_delete: Optional[BaseBoolInt] = Field(None, description="Information whether current user can delete the post")
    can_pin: Optional[BaseBoolInt] = Field(None, description="Information whether current user can pin the post")
    is_pinned: Optional[int] = Field(None, description="Information whether the post is pinned")
    comments: Optional[BaseCommentsInfo] = Field(None)
    marked_as_ads: Optional[BaseBoolInt] = Field(None, description="Information whether the post is marked as ads")
    short_text_rate: Optional[float] = Field(None, description="Preview length control parameter")


class WidgetsWidgetComment(BaseModel):
    attachments: Optional[List[WallCommentAttachment]] = Field(None)
    can_delete: Optional[BaseBoolInt] = Field(None,
                                              description="Information whether current user can delete the comment")
    comments: Optional[WidgetsCommentReplies] = Field(None)
    date: int = Field(..., description="Date when the comment has been added in Unixtime")
    from_id: int = Field(..., description="Comment author ID")
    id_: int = Field(..., alias='id', description="Comment ID")
    likes: Optional[BaseLikesInfo] = Field(None)
    media: Optional[WidgetsCommentMedia] = Field(None)
    post_source: Optional[WallPostSource] = Field(None)
    post_type: int = Field(..., description="Post type")
    reposts: Optional[BaseRepostsInfo] = Field(None)
    text: str = Field(..., description="Comment text")
    to_id: int = Field(..., description="Wall owner")
    user: Optional[UsersUserFull] = Field(None)


class FaveBookmark(BaseModel):
    added_date: int = Field(..., description="Timestamp, when this item was bookmarked")
    link: Optional[BaseLink] = Field(None)
    post: Optional[WallWallpostFull] = Field(None)
    product: Optional[MarketMarketItem] = Field(None)
    seen: bool = Field(..., description="Has user seen this item")
    tags: List[FaveTag] = Field(...)
    type_: FaveBookmarkType = Field(..., alias='type', description="Item type")
    video: Optional[VideoVideo] = Field(None)


class MessagesMessageAttachment(BaseModel):
    audio: Optional[AudioAudio] = Field(None)
    audio_message: Optional[MessagesAudioMessage] = Field(None)
    doc: Optional[DocsDoc] = Field(None)
    gift: Optional[GiftsLayout] = Field(None)
    graffiti: Optional[MessagesGraffiti] = Field(None)
    link: Optional[BaseLink] = Field(None)
    market: Optional[MarketMarketItem] = Field(None)
    market_market_album: Optional[MarketMarketAlbum] = Field(None)
    photo: Optional[PhotosPhoto] = Field(None)
    sticker: Optional[BaseSticker] = Field(None)
    story: Optional[StoriesStory] = Field(None)
    type_: MessagesMessageAttachmentType = Field(..., alias='type')
    video: Optional[VideoVideo] = Field(None)
    wall: Optional[WallWallpostFull] = Field(None)
    wall_reply: Optional[WallWallComment] = Field(None)


class NewsfeedNewsfeedItem(NewsfeedItemWallpost, NewsfeedItemPhoto, NewsfeedItemPhotoTag, NewsfeedItemFriend,
                           NewsfeedItemNote, NewsfeedItemAudio, NewsfeedItemVideo, NewsfeedItemTopic,
                           NewsfeedItemDigest, NewsfeedItemPromoButton):
    ...


class NotificationsNotificationParent(WallWallpostToId, PhotosPhoto, BoardTopic, VideoVideo,
                                      NotificationsNotificationsComment):
    ...


class PhotosCommentXtrPid(BaseModel):
    attachments: Optional[List[WallCommentAttachment]] = Field(None)
    date: int = Field(..., description="Date when the comment has been added in Unixtime")
    from_id: int = Field(..., description="Author ID")
    id_: int = Field(..., alias='id', description="Comment ID")
    likes: Optional[BaseLikesInfo] = Field(None)
    pid: int = Field(..., description="Photo ID")
    reply_to_comment: Optional[int] = Field(None, description="Replied comment ID")
    reply_to_user: Optional[int] = Field(None, description="Replied user ID")
    text: str = Field(..., description="Comment text")
    parents_stack: Optional[List[int]] = Field(None)
    thread: Optional[CommentThread] = Field(None)


class MessagesForeignMessage(BaseModel):
    attachments: Optional[List[MessagesMessageAttachment]] = Field(None)
    conversation_message_id: Optional[int] = Field(None, description="Conversation message ID")
    date: int = Field(..., description="Date when the message was created")
    from_id: int = Field(..., description="Message author's ID")
    fwd_messages: Optional[List["MessagesForeignMessage"]] = Field(None)
    geo: Optional[BaseGeo] = Field(None)
    id_: Optional[int] = Field(None, alias='id', description="Message ID")
    peer_id: Optional[int] = Field(None, description="Peer ID")
    reply_message: Optional["MessagesForeignMessage"] = Field(None)
    text: str = Field(..., description="Message text")
    update_time: Optional[int] = Field(None, description="Date when the message has been updated in Unixtime")
    was_listened: Optional[bool] = Field(None, description="Was the audio message inside already listened by you")
    payload: Optional[str] = Field(None,
                                   description="Additional data sent along with message for developer convenience")


MessagesForeignMessage.update_forward_refs()


class NotificationsNotification(BaseModel):
    date: Optional[int] = Field(None, description="Date when the event has been occurred")
    feedback: Optional[NotificationsFeedback] = Field(None)
    parent: Optional[NotificationsNotificationParent] = Field(None)
    reply: Optional[NotificationsReply] = Field(None)
    type_: Optional[str] = Field(None, alias='type', description="Notification type")


class MessagesMessage(BaseModel):
    action: Optional[MessagesMessageAction] = Field(None)
    admin_author_id: Optional[int] = Field(None,
                                           description="Only for messages from community. Contains user ID of community admin, who sent this message.")
    attachments: Optional[List[MessagesMessageAttachment]] = Field(None)
    conversation_message_id: Optional[int] = Field(None,
                                                   description="Unique auto-incremented number for all messages with this peer")
    date: int = Field(..., description="Date when the message has been sent in Unixtime")
    deleted: Optional[BaseBoolInt] = Field(None, description="Is it an deleted message")
    from_id: int = Field(..., description="Message author's ID")
    fwd_messages: Optional[List[MessagesForeignMessage]] = Field(None, description="Forwarded messages")
    geo: Optional[BaseGeo] = Field(None)
    id_: int = Field(..., alias='id', description="Message ID")
    important: Optional[bool] = Field(None, description="Is it an important message")
    is_hidden: Optional[bool] = Field(None)
    is_cropped: Optional[bool] = Field(None, description="this message is cropped for bot")
    keyboard: Optional[MessagesKeyboard] = Field(None)
    members_count: Optional[int] = Field(None, description="Members number")
    out: BaseBoolInt = Field(..., description="Information whether the message is outcoming")
    payload: Optional[str] = Field(None)
    peer_id: int = Field(..., description="Peer ID")
    random_id: Optional[int] = Field(None,
                                     description="ID used for sending messages. It returned only for outgoing messages")
    ref: Optional[str] = Field(None)
    ref_source: Optional[str] = Field(None)
    reply_message: Optional[MessagesForeignMessage] = Field(None)
    text: str = Field(..., description="Message text")
    update_time: Optional[int] = Field(None, description="Date when the message has been updated in Unixtime")
    was_listened: Optional[bool] = Field(None, description="Was the audio message inside already listened by you")
    pinned_at: Optional[int] = Field(None, description="Date when the message has been pinned in Unixtime")


class MessagesPinnedMessage(BaseModel):
    attachments: Optional[List[MessagesMessageAttachment]] = Field(None)
    conversation_message_id: Optional[int] = Field(None,
                                                   description="Unique auto-incremented number for all messages with this peer")
    date: int = Field(..., description="Date when the message has been sent in Unixtime")
    from_id: int = Field(..., description="Message author's ID")
    fwd_messages: Optional[List[MessagesForeignMessage]] = Field(None, description="Forwarded messages")
    geo: Optional[BaseGeo] = Field(None)
    id_: int = Field(..., alias='id', description="Message ID")
    peer_id: int = Field(..., description="Peer ID")
    reply_message: Optional[MessagesForeignMessage] = Field(None)
    text: str = Field(..., description="Message text")
    keyboard: Optional[MessagesKeyboard] = Field(None)


class MessagesConversationWithMessage(BaseModel):
    conversation: Optional[MessagesConversation] = Field(None)
    last_message: Optional[MessagesMessage] = Field(None)


class MessagesLongpollMessages(BaseModel):
    count: Optional[int] = Field(None, description="Total number")
    items: Optional[List[MessagesMessage]] = Field(None)
