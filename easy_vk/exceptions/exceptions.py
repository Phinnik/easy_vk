class Unknown(Exception):
    def __init__(self, message=''):
        """Unknown error occurred"""
        super().__init__(message)


class Disabled(Exception):
    def __init__(self, message=''):
        """Application is disabled. Enable your application or use test mode"""
        super().__init__(message)


class Method(Exception):
    def __init__(self, message=''):
        """Unknown method passed"""
        super().__init__(message)


class Signature(Exception):
    def __init__(self, message=''):
        """Incorrect signature"""
        super().__init__(message)


class Auth(Exception):
    def __init__(self, message=''):
        """User authorization failed"""
        super().__init__(message)


class TooMany(Exception):
    def __init__(self, message=''):
        """Too many requests per second"""
        super().__init__(message)


class Permission(Exception):
    def __init__(self, message=''):
        """Permission to perform this action is denied"""
        super().__init__(message)


class Request(Exception):
    def __init__(self, message=''):
        """Invalid request"""
        super().__init__(message)


class Flood(Exception):
    def __init__(self, message=''):
        """Flood control"""
        super().__init__(message)


class Server(Exception):
    def __init__(self, message=''):
        """Internal server error"""
        super().__init__(message)


class EnabledInTest(Exception):
    def __init__(self, message=''):
        """In test mode application should be disabled or user should be authorized"""
        super().__init__(message)


class Compile(Exception):
    def __init__(self, message=''):
        """Unable to compile code"""
        super().__init__(message)


class Runtime(Exception):
    def __init__(self, message=''):
        """Runtime error occurred during code invocation"""
        super().__init__(message)


class Captcha(Exception):
    def __init__(self, message=''):
        """Captcha needed"""
        super().__init__(message)


class Access(Exception):
    def __init__(self, message=''):
        """Access denied"""
        super().__init__(message)


class AuthHttps(Exception):
    def __init__(self, message=''):
        """HTTP authorization failed"""
        super().__init__(message)


class AuthValidation(Exception):
    def __init__(self, message=''):
        """Validation required"""
        super().__init__(message)


class UserDeleted(Exception):
    def __init__(self, message=''):
        """User was deleted or banned"""
        super().__init__(message)


class Blocked(Exception):
    def __init__(self, message=''):
        """Content blocked"""
        super().__init__(message)


class MethodPermission(Exception):
    def __init__(self, message=''):
        """Permission to perform this action is denied for non-standalone applications"""
        super().__init__(message)


class MethodAds(Exception):
    def __init__(self, message=''):
        """Permission to perform this action is allowed only for standalone and OpenAPI applications"""
        super().__init__(message)


class Upload(Exception):
    def __init__(self, message=''):
        """Upload error"""
        super().__init__(message)


class MethodDisabled(Exception):
    def __init__(self, message=''):
        """This method was disabled"""
        super().__init__(message)


class NeedConfirmation(Exception):
    def __init__(self, message=''):
        """Confirmation required"""
        super().__init__(message)


class NeedTokenConfirmation(Exception):
    def __init__(self, message=''):
        """Token confirmation required"""
        super().__init__(message)


class GroupAuth(Exception):
    def __init__(self, message=''):
        """Group authorization failed"""
        super().__init__(message)


class AppAuth(Exception):
    def __init__(self, message=''):
        """Application authorization failed"""
        super().__init__(message)


class RateLimit(Exception):
    def __init__(self, message=''):
        """Rate limit reached"""
        super().__init__(message)


class PrivateProfile(Exception):
    def __init__(self, message=''):
        """This profile is private"""
        super().__init__(message)


class NotImplementedYet(Exception):
    def __init__(self, message=''):
        """Not implemented yet"""
        super().__init__(message)


class ClientUpdateNeeded(Exception):
    def __init__(self, message=''):
        """Client update needed"""
        super().__init__(message)


class Param(Exception):
    def __init__(self, message=''):
        """One of the parameters specified was missing or invalid"""
        super().__init__(message)


class ParamApiId(Exception):
    def __init__(self, message=''):
        """Invalid application API ID"""
        super().__init__(message)


class Limits(Exception):
    def __init__(self, message=''):
        """Out of limits"""
        super().__init__(message)


class NotFound(Exception):
    def __init__(self, message=''):
        """Not found"""
        super().__init__(message)


class SaveFile(Exception):
    def __init__(self, message=''):
        """Couldn't save file"""
        super().__init__(message)


class ActionFailed(Exception):
    def __init__(self, message=''):
        """Unable to process action"""
        super().__init__(message)


class ParamUserId(Exception):
    def __init__(self, message=''):
        """Invalid user id"""
        super().__init__(message)


class ParamAlbumId(Exception):
    def __init__(self, message=''):
        """Invalid album id"""
        super().__init__(message)


class ParamServer(Exception):
    def __init__(self, message=''):
        """Invalid server"""
        super().__init__(message)


class ParamTitle(Exception):
    def __init__(self, message=''):
        """Invalid title"""
        super().__init__(message)


class ParamHash(Exception):
    def __init__(self, message=''):
        """Invalid hash"""
        super().__init__(message)


class ParamPhotos(Exception):
    def __init__(self, message=''):
        """Invalid photos"""
        super().__init__(message)


class ParamGroupId(Exception):
    def __init__(self, message=''):
        """Invalid group id"""
        super().__init__(message)


class ParamPhoto(Exception):
    def __init__(self, message=''):
        """Invalid photo"""
        super().__init__(message)


class ParamPageId(Exception):
    def __init__(self, message=''):
        """Page not found"""
        super().__init__(message)


class AccessPage(Exception):
    def __init__(self, message=''):
        """Access to page denied"""
        super().__init__(message)


class MobileNotActivated(Exception):
    def __init__(self, message=''):
        """The mobile number of the user is unknown"""
        super().__init__(message)


class InsufficientFunds(Exception):
    def __init__(self, message=''):
        """Application has insufficient funds"""
        super().__init__(message)


class AccessMenu(Exception):
    def __init__(self, message=''):
        """Access to the menu of the user denied"""
        super().__init__(message)


class ParamTimestamp(Exception):
    def __init__(self, message=''):
        """Invalid timestamp"""
        super().__init__(message)


class FriendsListId(Exception):
    def __init__(self, message=''):
        """Invalid list id"""
        super().__init__(message)


class FriendsListLimit(Exception):
    def __init__(self, message=''):
        """Reached the maximum number of lists"""
        super().__init__(message)


class FriendsAddYourself(Exception):
    def __init__(self, message=''):
        """Cannot add user himself as friend"""
        super().__init__(message)


class FriendsAddInEnemy(Exception):
    def __init__(self, message=''):
        """Cannot add this user to friends as they have put you on their blacklist"""
        super().__init__(message)


class FriendsAddEnemy(Exception):
    def __init__(self, message=''):
        """Cannot add this user to friends as you put him on blacklist"""
        super().__init__(message)


class FriendsAddNotFound(Exception):
    def __init__(self, message=''):
        """Cannot add this user to friends as user not found"""
        super().__init__(message)


class ParamNoteId(Exception):
    def __init__(self, message=''):
        """Note not found"""
        super().__init__(message)


class AccessNote(Exception):
    def __init__(self, message=''):
        """Access to note denied"""
        super().__init__(message)


class AccessNoteComment(Exception):
    def __init__(self, message=''):
        """You can't comment this note"""
        super().__init__(message)


class AccessComment(Exception):
    def __init__(self, message=''):
        """Access to comment denied"""
        super().__init__(message)


class AccessAlbum(Exception):
    def __init__(self, message=''):
        """Access denied"""
        super().__init__(message)


class AccessAudio(Exception):
    def __init__(self, message=''):
        """Access denied"""
        super().__init__(message)


class AccessGroup(Exception):
    def __init__(self, message=''):
        """Access to group denied"""
        super().__init__(message)


class AccessVideo(Exception):
    def __init__(self, message=''):
        """Access denied"""
        super().__init__(message)


class AccessMarket(Exception):
    def __init__(self, message=''):
        """Access denied"""
        super().__init__(message)


class WallAccessPost(Exception):
    def __init__(self, message=''):
        """Access to wall's post denied"""
        super().__init__(message)


class WallAccessComment(Exception):
    def __init__(self, message=''):
        """Access to wall's comment denied"""
        super().__init__(message)


class WallAccessReplies(Exception):
    def __init__(self, message=''):
        """Access to post comments denied"""
        super().__init__(message)


class WallAccessAddReply(Exception):
    def __init__(self, message=''):
        """Access to status replies denied"""
        super().__init__(message)


class WallAddPost(Exception):
    def __init__(self, message=''):
        """Access to adding post denied"""
        super().__init__(message)


class WallAdsPublished(Exception):
    def __init__(self, message=''):
        """Advertisement post was recently added"""
        super().__init__(message)


class WallTooManyRecipients(Exception):
    def __init__(self, message=''):
        """Too many recipients"""
        super().__init__(message)


class StatusNoAudio(Exception):
    def __init__(self, message=''):
        """User disabled track name broadcast"""
        super().__init__(message)


class WallLinksForbidden(Exception):
    def __init__(self, message=''):
        """Hyperlinks are forbidden"""
        super().__init__(message)


class WallReplyOwnerFlood(Exception):
    def __init__(self, message=''):
        """Too many replies"""
        super().__init__(message)


class WallAdsPostLimitReached(Exception):
    def __init__(self, message=''):
        """Too many ads posts"""
        super().__init__(message)


class PollsAccess(Exception):
    def __init__(self, message=''):
        """Access to poll denied"""
        super().__init__(message)


class PollsPollId(Exception):
    def __init__(self, message=''):
        """Invalid poll id"""
        super().__init__(message)


class PollsAnswerId(Exception):
    def __init__(self, message=''):
        """Invalid answer id"""
        super().__init__(message)


class PollsAccessWithoutVote(Exception):
    def __init__(self, message=''):
        """Access denied, please vote first"""
        super().__init__(message)


class AccessGroups(Exception):
    def __init__(self, message=''):
        """Access to the groups list is denied due to the user's privacy settings"""
        super().__init__(message)


class AlbumFull(Exception):
    def __init__(self, message=''):
        """This album is full"""
        super().__init__(message)


class AlbumsLimit(Exception):
    def __init__(self, message=''):
        """Albums number limit is reached"""
        super().__init__(message)


class VotesPermission(Exception):
    def __init__(self, message=''):
        """Permission denied. You must enable votes processing in application settings"""
        super().__init__(message)


class Votes(Exception):
    def __init__(self, message=''):
        """Not enough votes"""
        super().__init__(message)


class AdsPermission(Exception):
    def __init__(self, message=''):
        """Permission denied. You have no access to operations specified with given object(s)"""
        super().__init__(message)


class WeightedFlood(Exception):
    def __init__(self, message=''):
        """Permission denied. You have requested too many actions this day. Try later."""
        super().__init__(message)


class AdsPartialSuccess(Exception):
    def __init__(self, message=''):
        """Some part of the request has not been completed"""
        super().__init__(message)


class AdsSpecific(Exception):
    def __init__(self, message=''):
        """Some ads error occured"""
        super().__init__(message)


class AdsObjectDeleted(Exception):
    def __init__(self, message=''):
        """Object deleted"""
        super().__init__(message)


class GroupChangeCreator(Exception):
    def __init__(self, message=''):
        """Cannot edit creator role"""
        super().__init__(message)


class GroupNotInClub(Exception):
    def __init__(self, message=''):
        """User should be in club"""
        super().__init__(message)


class GroupTooManyOfficers(Exception):
    def __init__(self, message=''):
        """Too many officers in club"""
        super().__init__(message)


class GroupNeed2Fa(Exception):
    def __init__(self, message=''):
        """You need to enable 2FA for this action"""
        super().__init__(message)


class GroupHostNeed2Fa(Exception):
    def __init__(self, message=''):
        """User needs to enable 2FA for this action"""
        super().__init__(message)


class GroupTooManyAddresses(Exception):
    def __init__(self, message=''):
        """Too many addresses in club"""
        super().__init__(message)


class GroupAppIsNotInstalledInCommunity(Exception):
    def __init__(self, message=''):
        """Application is not installed in community"""
        super().__init__(message)


class GroupInviteLinksNotValid(Exception):
    def __init__(self, message=''):
        """Invite link is invalid - expired, deleted or not exists"""
        super().__init__(message)


class VideoAlreadyAdded(Exception):
    def __init__(self, message=''):
        """This video is already added"""
        super().__init__(message)


class VideoCommentsClosed(Exception):
    def __init__(self, message=''):
        """Comments for this video are closed"""
        super().__init__(message)


class MessagesUserBlocked(Exception):
    def __init__(self, message=''):
        """Can't send messages for users from blacklist"""
        super().__init__(message)


class MessagesDenySend(Exception):
    def __init__(self, message=''):
        """Can't send messages for users without permission"""
        super().__init__(message)


class MessagesPrivacy(Exception):
    def __init__(self, message=''):
        """Can't send messages to this user due to their privacy settings"""
        super().__init__(message)


class MessagesTooOldPts(Exception):
    def __init__(self, message=''):
        """Value of ts or pts is too old"""
        super().__init__(message)


class MessagesTooNewPts(Exception):
    def __init__(self, message=''):
        """Value of ts or pts is too new"""
        super().__init__(message)


class MessagesEditExpired(Exception):
    def __init__(self, message=''):
        """Can't edit this message, because it's too old"""
        super().__init__(message)


class MessagesTooBig(Exception):
    def __init__(self, message=''):
        """Can't sent this message, because it's too big"""
        super().__init__(message)


class MessagesKeyboardInvalid(Exception):
    def __init__(self, message=''):
        """Keyboard format is invalid"""
        super().__init__(message)


class MessagesChatBotFeature(Exception):
    def __init__(self, message=''):
        """This is a chat bot feature, change this status in settings"""
        super().__init__(message)


class MessagesTooLongForwards(Exception):
    def __init__(self, message=''):
        """Too many forwarded messages"""
        super().__init__(message)


class MessagesTooLongMessage(Exception):
    def __init__(self, message=''):
        """Message is too long"""
        super().__init__(message)


class MessagesChatUserNoAccess(Exception):
    def __init__(self, message=''):
        """You don't have access to this chat"""
        super().__init__(message)


class MessagesCantSeeInviteLink(Exception):
    def __init__(self, message=''):
        """You can't see invite link for this chat"""
        super().__init__(message)


class MessagesEditKindDisallowed(Exception):
    def __init__(self, message=''):
        """Can't edit this kind of message"""
        super().__init__(message)


class MessagesCantFwd(Exception):
    def __init__(self, message=''):
        """Can't forward these messages"""
        super().__init__(message)


class MessagesCantDeleteForAll(Exception):
    def __init__(self, message=''):
        """Can't delete this message for everybody"""
        super().__init__(message)


class MessagesChatNotAdmin(Exception):
    def __init__(self, message=''):
        """You are not admin of this chat"""
        super().__init__(message)


class MessagesChatNotExist(Exception):
    def __init__(self, message=''):
        """Chat does not exist"""
        super().__init__(message)


class MessagesCantChangeInviteLink(Exception):
    def __init__(self, message=''):
        """You can't change invite link for this chat"""
        super().__init__(message)


class MessagesGroupPeerAccess(Exception):
    def __init__(self, message=''):
        """Your community can't interact with this peer"""
        super().__init__(message)


class MessagesChatUserNotInChat(Exception):
    def __init__(self, message=''):
        """User not found in chat"""
        super().__init__(message)


class MessagesContactNotFound(Exception):
    def __init__(self, message=''):
        """Contact not found"""
        super().__init__(message)


class MessagesMessageRequestAlreadySent(Exception):
    def __init__(self, message=''):
        """Message request already sent"""
        super().__init__(message)


class MessagesTooManyPosts(Exception):
    def __init__(self, message=''):
        """Too many posts in messages"""
        super().__init__(message)


class MessagesCantPinOneTimeStory(Exception):
    def __init__(self, message=''):
        """Cannot pin one-time story"""
        super().__init__(message)


class MessagesIntentCantUse(Exception):
    def __init__(self, message=''):
        """Cannot use this intent"""
        super().__init__(message)


class MessagesIntentLimitOverflow(Exception):
    def __init__(self, message=''):
        """Limits overflow for this intent"""
        super().__init__(message)


class MessagesChatDisabled(Exception):
    def __init__(self, message=''):
        """Chat was disabled"""
        super().__init__(message)


class MessagesChatUnsupported(Exception):
    def __init__(self, message=''):
        """Chat not supported"""
        super().__init__(message)


class MessagesMemberAccessToGroupDenied(Exception):
    def __init__(self, message=''):
        """Can't add user to chat, because user has no access to group"""
        super().__init__(message)


class MessagesCantEditPinnedYet(Exception):
    def __init__(self, message=''):
        """Can't edit pinned message yet"""
        super().__init__(message)


class MessagesPeerBlockedReasonByTime(Exception):
    def __init__(self, message=''):
        """Can't send message, reply timed out"""
        super().__init__(message)


class ParamPhone(Exception):
    def __init__(self, message=''):
        """Invalid phone number"""
        super().__init__(message)


class PhoneAlreadyUsed(Exception):
    def __init__(self, message=''):
        """This phone number is used by another user"""
        super().__init__(message)


class AuthFloodError(Exception):
    def __init__(self, message=''):
        """Too many auth attempts, try again later"""
        super().__init__(message)


class AuthDelay(Exception):
    def __init__(self, message=''):
        """Processing.. Try later"""
        super().__init__(message)


class ParamDocId(Exception):
    def __init__(self, message=''):
        """Invalid document id"""
        super().__init__(message)


class ParamDocDeleteAccess(Exception):
    def __init__(self, message=''):
        """Access to document deleting is denied"""
        super().__init__(message)


class ParamDocTitle(Exception):
    def __init__(self, message=''):
        """Invalid document title"""
        super().__init__(message)


class ParamDocAccess(Exception):
    def __init__(self, message=''):
        """Access to document is denied"""
        super().__init__(message)


class PhotoChanged(Exception):
    def __init__(self, message=''):
        """Original photo was changed"""
        super().__init__(message)


class TooManyLists(Exception):
    def __init__(self, message=''):
        """Too many feed lists"""
        super().__init__(message)


class AppsAlreadyUnlocked(Exception):
    def __init__(self, message=''):
        """This achievement is already unlocked"""
        super().__init__(message)


class AppsSubscriptionNotFound(Exception):
    def __init__(self, message=''):
        """Subscription not found"""
        super().__init__(message)


class AppsSubscriptionInvalidStatus(Exception):
    def __init__(self, message=''):
        """Subscription is in invalid status"""
        super().__init__(message)


class InvalidAddress(Exception):
    def __init__(self, message=''):
        """Invalid screen name"""
        super().__init__(message)


class CommunitiesCatalogDisabled(Exception):
    def __init__(self, message=''):
        """Catalog is not available for this user"""
        super().__init__(message)


class CommunitiesCategoriesDisabled(Exception):
    def __init__(self, message=''):
        """Catalog categories are not available for this user"""
        super().__init__(message)


class MarketRestoreTooLate(Exception):
    def __init__(self, message=''):
        """Too late for restore"""
        super().__init__(message)


class MarketCommentsClosed(Exception):
    def __init__(self, message=''):
        """Comments for this market are closed"""
        super().__init__(message)


class MarketAlbumNotFound(Exception):
    def __init__(self, message=''):
        """Album not found"""
        super().__init__(message)


class MarketItemNotFound(Exception):
    def __init__(self, message=''):
        """Item not found"""
        super().__init__(message)


class MarketItemAlreadyAdded(Exception):
    def __init__(self, message=''):
        """Item already added to album"""
        super().__init__(message)


class MarketTooManyItems(Exception):
    def __init__(self, message=''):
        """Too many items"""
        super().__init__(message)


class MarketTooManyItemsInAlbum(Exception):
    def __init__(self, message=''):
        """Too many items in album"""
        super().__init__(message)


class MarketTooManyAlbums(Exception):
    def __init__(self, message=''):
        """Too many albums"""
        super().__init__(message)


class MarketItemHasBadLinks(Exception):
    def __init__(self, message=''):
        """Item has bad links in description"""
        super().__init__(message)


class StoryExpired(Exception):
    def __init__(self, message=''):
        """Story has already expired"""
        super().__init__(message)


class StoryIncorrectReplyPrivacy(Exception):
    def __init__(self, message=''):
        """Incorrect reply privacy"""
        super().__init__(message)


class PrettyCardsCardNotFound(Exception):
    def __init__(self, message=''):
        """Card not found"""
        super().__init__(message)


class PrettyCardsTooManyCards(Exception):
    def __init__(self, message=''):
        """Too many cards"""
        super().__init__(message)


class PrettyCardsCardIsConnectedToPost(Exception):
    def __init__(self, message=''):
        """Card is connected to post"""
        super().__init__(message)


class CallbackApiServersLimit(Exception):
    def __init__(self, message=''):
        """Servers number limit is reached"""
        super().__init__(message)


class Recaptcha(Exception):
    def __init__(self, message=''):
        """Recaptcha needed"""
        super().__init__(message)


class PhoneValidationNeed(Exception):
    def __init__(self, message=''):
        """Phone validation needed"""
        super().__init__(message)


class PasswordValidationNeed(Exception):
    def __init__(self, message=''):
        """Password validation needed"""
        super().__init__(message)


class OtpValidationNeed(Exception):
    def __init__(self, message=''):
        """Otp app validation needed"""
        super().__init__(message)


class EmailConfirmationNeed(Exception):
    def __init__(self, message=''):
        """Email confirmation needed"""
        super().__init__(message)


class AssertVotes(Exception):
    def __init__(self, message=''):
        """Assert votes"""
        super().__init__(message)


class TokenExtensionRequired(Exception):
    def __init__(self, message=''):
        """Token extension required"""
        super().__init__(message)


class UserDeactivated(Exception):
    def __init__(self, message=''):
        """User is deactivated"""
        super().__init__(message)


class UserServiceDeactivated(Exception):
    def __init__(self, message=''):
        """Service is deactivated for user"""
        super().__init__(message)


class FaveAliexpressTag(Exception):
    def __init__(self, message=''):
        """Can't set AliExpress tag to this type of object"""
        super().__init__(message)


error_dict = {
    1: Unknown,
    2: Disabled,
    3: Method,
    4: Signature,
    5: Auth,
    6: TooMany,
    7: Permission,
    8: Request,
    9: Flood,
    10: Server,
    11: EnabledInTest,
    12: Compile,
    13: Runtime,
    14: Captcha,
    15: Access,
    16: AuthHttps,
    17: AuthValidation,
    18: UserDeleted,
    19: Blocked,
    20: MethodPermission,
    21: MethodAds,
    22: Upload,
    23: MethodDisabled,
    24: NeedConfirmation,
    25: NeedTokenConfirmation,
    27: GroupAuth,
    28: AppAuth,
    29: RateLimit,
    30: PrivateProfile,
    33: NotImplementedYet,
    35: ClientUpdateNeeded,
    100: Param,
    101: ParamApiId,
    103: Limits,
    104: NotFound,
    105: SaveFile,
    106: ActionFailed,
    113: ParamUserId,
    114: ParamAlbumId,
    118: ParamServer,
    119: ParamTitle,
    121: ParamHash,
    122: ParamPhotos,
    125: ParamGroupId,
    129: ParamPhoto,
    140: ParamPageId,
    141: AccessPage,
    146: MobileNotActivated,
    147: InsufficientFunds,
    148: AccessMenu,
    150: ParamTimestamp,
    171: FriendsListId,
    173: FriendsListLimit,
    174: FriendsAddYourself,
    175: FriendsAddInEnemy,
    176: FriendsAddEnemy,
    177: FriendsAddNotFound,
    180: ParamNoteId,
    181: AccessNote,
    182: AccessNoteComment,
    183: AccessComment,
    200: AccessAlbum,
    201: AccessAudio,
    203: AccessGroup,
    204: AccessVideo,
    205: AccessMarket,
    210: WallAccessPost,
    211: WallAccessComment,
    212: WallAccessReplies,
    213: WallAccessAddReply,
    214: WallAddPost,
    219: WallAdsPublished,
    220: WallTooManyRecipients,
    221: StatusNoAudio,
    222: WallLinksForbidden,
    223: WallReplyOwnerFlood,
    224: WallAdsPostLimitReached,
    250: PollsAccess,
    251: PollsPollId,
    252: PollsAnswerId,
    253: PollsAccessWithoutVote,
    260: AccessGroups,
    300: AlbumFull,
    302: AlbumsLimit,
    500: VotesPermission,
    503: Votes,
    600: AdsPermission,
    601: WeightedFlood,
    602: AdsPartialSuccess,
    603: AdsSpecific,
    629: AdsObjectDeleted,
    700: GroupChangeCreator,
    701: GroupNotInClub,
    702: GroupTooManyOfficers,
    703: GroupNeed2Fa,
    704: GroupHostNeed2Fa,
    706: GroupTooManyAddresses,
    711: GroupAppIsNotInstalledInCommunity,
    714: GroupInviteLinksNotValid,
    800: VideoAlreadyAdded,
    801: VideoCommentsClosed,
    900: MessagesUserBlocked,
    901: MessagesDenySend,
    902: MessagesPrivacy,
    907: MessagesTooOldPts,
    908: MessagesTooNewPts,
    909: MessagesEditExpired,
    910: MessagesTooBig,
    911: MessagesKeyboardInvalid,
    912: MessagesChatBotFeature,
    913: MessagesTooLongForwards,
    914: MessagesTooLongMessage,
    917: MessagesChatUserNoAccess,
    919: MessagesCantSeeInviteLink,
    920: MessagesEditKindDisallowed,
    921: MessagesCantFwd,
    924: MessagesCantDeleteForAll,
    925: MessagesChatNotAdmin,
    927: MessagesChatNotExist,
    931: MessagesCantChangeInviteLink,
    932: MessagesGroupPeerAccess,
    935: MessagesChatUserNotInChat,
    936: MessagesContactNotFound,
    939: MessagesMessageRequestAlreadySent,
    940: MessagesTooManyPosts,
    942: MessagesCantPinOneTimeStory,
    943: MessagesIntentCantUse,
    944: MessagesIntentLimitOverflow,
    945: MessagesChatDisabled,
    946: MessagesChatUnsupported,
    947: MessagesMemberAccessToGroupDenied,
    949: MessagesCantEditPinnedYet,
    950: MessagesPeerBlockedReasonByTime,
    1000: ParamPhone,
    1004: PhoneAlreadyUsed,
    1105: AuthFloodError,
    1112: AuthDelay,
    1150: ParamDocId,
    1151: ParamDocDeleteAccess,
    1152: ParamDocTitle,
    1153: ParamDocAccess,
    1160: PhotoChanged,
    1170: TooManyLists,
    1251: AppsAlreadyUnlocked,
    1256: AppsSubscriptionNotFound,
    1257: AppsSubscriptionInvalidStatus,
    1260: InvalidAddress,
    1310: CommunitiesCatalogDisabled,
    1311: CommunitiesCategoriesDisabled,
    1400: MarketRestoreTooLate,
    1401: MarketCommentsClosed,
    1402: MarketAlbumNotFound,
    1403: MarketItemNotFound,
    1404: MarketItemAlreadyAdded,
    1405: MarketTooManyItems,
    1406: MarketTooManyItemsInAlbum,
    1407: MarketTooManyAlbums,
    1408: MarketItemHasBadLinks,
    1600: StoryExpired,
    1602: StoryIncorrectReplyPrivacy,
    1900: PrettyCardsCardNotFound,
    1901: PrettyCardsTooManyCards,
    1902: PrettyCardsCardIsConnectedToPost,
    2000: CallbackApiServersLimit,
    3300: Recaptcha,
    3301: PhoneValidationNeed,
    3302: PasswordValidationNeed,
    3303: OtpValidationNeed,
    3304: EmailConfirmationNeed,
    3305: AssertVotes,
    3609: TokenExtensionRequired,
    3610: UserDeactivated,
    3611: UserServiceDeactivated,
    3800: FaveAliexpressTag
}


def raise_exception(code: int, message):
    """raises exception with message by code """
    raise error_dict.get(code, Unknown)(message)
