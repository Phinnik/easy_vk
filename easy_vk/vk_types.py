# -*- coding: utf-8 -*-


########################################
# Base objects:

class User:
    def __init__(self, j):
        # Base fields
        self.id = j.get('id')
        self.first_name = j.get('first_name')
        self.last_name = j.get('last_name')
        self.deactivated = j.get('deactivated')
        self.is_closed = j.get('is_closed')
        self.can_access_closed = j.get('can_access_closed')

        # Optional fields
        for f in ['id', 'first_name', 'last_name', 'deactivated', 'is_closed', 'can_access_closed']:
            j.pop(f, None)
        self.optional = j


class Group:
    def __init__(self, j):
        # Base fields
        self.id = j.get('id')
        self.name = j.get('name')
        self.screen_name = j.get('screen_name')
        self.is_closed = j.get('is_closed')
        self.deactivated = j.get('deactivated')
        self.is_admin = j.get('is_admin')
        self.admin_level = j.get('admin_level')
        self.is_member = j.get('is_member')
        self.is_advertiser = j.get('is_advertiser')
        self.invited_by = j.get('invited_by')
        self.type = j.get('type')
        self.photo_50 = j.get('photo_50')
        self.photo_100 = j.get('photo_100')
        self.photo_200 = j.get('photo_200')

        # Optional fields
        for f in ['id', 'name', 'screen_name', 'is_closed', 'deactivated', 'is_admin', 'admin_level', 'is_member',
                  'is_advertiser', 'invited_by', 'type', 'photo_50', 'photo_100', 'photo_200']:
            j.pop(f, None)
        self.optional = j


class Wall_post:
    def __init__(self, j):
        # Base fields
        self.id = j.get('id')
        self.owner_id = j.get('owner_id')
        self.from_id = j.get('from_id')
        self.created_by = j.get('created_by')
        self.date = j.get('date')
        self.text = j.get('text')
        self.reply_owner_id = j.get('reply_owner_id')
        self.reply_post_id = j.get('reply_post_id')
        self.friends_only = j.get('friends_only')
        self.comments = j.get('comments')
        self.likes = j.get('likes')
        self.reposts = j.get('reposts')
        self.views = j.get('views')
        self.post_type = j.get('post_type')
        self.post_source = j.get('post_source')
        self.attachments = j.get('attachments')
        self.geo = j.get('geo')
        self.signer_id = j.get('signer_id')
        self.copy_history = j.get('copy_history')
        self.can_pin = j.get('can_pin')
        self.can_delete = j.get('can_delete')
        self.can_edit = j.get('can_edit')
        self.is_pinned = j.get('is_pinned')
        self.marked_as_ads = j.get('marked_as_ads')
        self.is_favorite = j.get('is_favorite')
        self.postponed_id = j.get('postponed_id')

        # Optional fields
        for f in ['id', 'owner_id', 'from_id', 'created_by', 'date', 'text', 'reply_owner_id', 'reply_post_id',
                  'friends_only', 'comments', 'likes', 'reposts', 'views', 'post_type', 'post_source', 'attachments',
                  'geo', 'signer_id', 'copy_history', 'can_pin', 'can_delete', 'can_edit', 'is_pinned', 'marked_as_ads',
                  'is_favorite', 'postponed_id']:
            j.pop(f, None)
        self.optional = j


class Message:
    def __init__(self, j, m_type='message_new'):
        # Base fields
        self.id = j.get('id')
        self.date = j.get('date')
        self.peer_id = j.get('peer_id')
        self.from_id = j.get('from_id')
        self.text = j.get('text')
        self.random_id = j.get('random_id')
        self.ref = j.get('ref')
        self.ref_source = j.get('ref_source')
        self.attachments = j.get('attachments')
        self.important = j.get('important')
        self.geo = j.get('geo')
        self.payload = j.get('payload')
        self.keyboard = j.get('keyboard')
        self.fwd_messages = j.get('fwd_messages')
        self.reply_message = j.get('reply_message')
        self.action = j.get('action')

        # Optional fields
        for f in ['id', 'date', 'peer_id', 'from_id', 'text', 'random_id', 'ref', 'ref_source', 'attachments',
                  'important', 'geo', 'payload', 'keyboard', 'fwd_messages', 'reply_message', 'action']:
            j.pop(f, None)
        self.optional = j


class Wall_comment:
    def __init__(self, j):
        # Base fields
        self.id = j.get('id')
        self.from_id = j.get('from_id')
        self.date = j.get('date')
        self.text = j.get('text')
        self.reply_to_user = j.get('reply_to_user')
        self.reply_to_comment = j.get('reply_to_comment')
        self.attachments = j.get('attachments')
        self.parents_stack = j.get('parents_stack')
        self.thread = j.get('thread')

        # Optional fields
        for f in ['id', 'from_id', 'date', 'text', 'reply_to_user', 'reply_to_comment', 'attachments', 'parents_stack',
                  'thread']:
            j.pop(f, None)
        self.optional = j


class Conversation:
    def __init__(self, j):
        # Base fields
        self.peer = j.get('peer')
        self.in_read = j.get('in_read')
        self.out_read = j.get('out_read')
        self.unread_count = j.get('unread_count')
        self.important = j.get('important')
        self.unanswered = j.get('unanswered')
        self.push_settings = j.get('push_settings')
        self.can_write = j.get('can_write')
        self.chat_settings = j.get('chat_settings')

        # Optional fields
        for f in ['peer', 'in_read', 'out_read', 'unread_count', 'important', 'unanswered', 'push_settings',
                  'can_write', 'chat_settings']:
            j.pop(f, None)
        self.optional = j


class Chat:
    def __init__(self, j):
        # Base fields
        self.id = j.get('id')
        self.type = j.get('type')
        self.title = j.get('title')
        self.admin_id = j.get('admin_id')
        self.users = j.get('users')
        self.push_settings = j.get('push_settings')
        self.photo_50 = j.get('photo_50')
        self.photo_100 = j.get('photo_100')
        self.photo_200 = j.get('photo_200')
        self.left = j.get('left')
        self.kicked = j.get('kicked')

        # Optional fields
        for f in ['id', 'type', 'title', 'admin_id', 'users', 'push_settings', 'photo_50', 'photo_100', 'photo_200',
                  'left', 'kicked']:
            j.pop(f, None)
        self.optional = j


class Note:
    def __init__(self, j):
        # Base fields
        self.id = j.get('id')
        self.owner_id = j.get('owner_id')
        self.title = j.get('title')
        self.text = j.get('text')
        self.date = j.get('date')
        self.comments = j.get('comments')
        self.read_comments = j.get('read_comments')
        self.view_url = j.get('view_url')

        # Optional fields
        for f in ['id', 'owner_id', 'title', 'text', 'date', 'comments', 'read_comments', 'view_url']:
            j.pop(f, None)
        self.optional = j


class Page:
    def __init__(self, j):
        # Base fields
        self.id = j.get('id')
        self.group_id = j.get('group_id')
        self.creator_id = j.get('creator_id')
        self.title = j.get('title')
        self.current_user_can_edit = j.get('current_user_can_edit')
        self.current_user_can_edit_access = j.get('current_user_can_edit_access')
        self.who_can_view = j.get('who_can_view')
        self.who_can_edit = j.get('who_can_edit')
        self.edited = j.get('edited')
        self.created = j.get('created')
        self.editor_id = j.get('editor_id')
        self.views = j.get('views')
        self.parent = j.get('parent')
        self.parent2 = j.get('parent2')
        self.source = j.get('source')
        self.html = j.get('html')
        self.view_url = j.get('view_url')

        # Optional fields
        for f in ['id', 'group_id', 'creator_id', 'title', 'current_user_can_edit', 'current_user_can_edit_access',
                  'who_can_view', 'who_can_edit', 'edited', 'created', 'editor_id', 'views', 'parent', 'parent2',
                  'source', 'html', 'view_url']:
            j.pop(f, None)
        self.optional = j


class Market_item:
    def __init__(self, j):
        # Base fields
        self.id = j.get('id')
        self.owner_id = j.get('owner_id')
        self.title = j.get('title')
        self.description = j.get('description')
        self.price = j.get('price')
        self.category = j.get('category')
        self.thumb_photo = j.get('thumb_photo')
        self.date = j.get('date')
        self.availability = j.get('availability')
        self.is_favorite = j.get('is_favorite')

        # Optional fields
        for f in ['id', 'owner_id', 'title', 'description', 'price', 'category', 'thumb_photo', 'date', 'availability',
                  'is_favorite']:
            j.pop(f, None)
        self.optional = j


class Market_album:
    def __init__(self, j):
        # Base fields
        self.id = j.get('id')
        self.owner_id = j.get('owner_id')
        self.title = j.get('title')
        self.photo = j.get('photo')
        self.count = j.get('count')
        self.updated_time = j.get('updated_time')

        # Optional fields
        for f in ['id', 'owner_id', 'title', 'photo', 'count', 'updated_time']:
            j.pop(f, None)
        self.optional = j


class Board:
    def __init__(self, j):
        self.id = j.get('id')
        self.title = j.get('title')
        self.created = j.get('created')
        self.created_by = j.get('created_by')
        self.updated = j.get('updated')
        self.updated_by = j.get('updated_by')
        self.is_closed = j.get('is_closed')
        self.is_fixed = j.get('is_fixed')
        self.comments = j.get('comments')
        self.first_comment = j.get('first_comment')
        self.last_comment = j.get('last_comment')

        # Optional fields
        for f in ['id', 'title', 'created', 'created_by', 'updated', 'updated_by', 'is_closed', 'is_fixed', 'comments',
                  'first_comment', 'last_comment']:
            j.pop(f, None)
        self.optional = j


class Board_comment:
    def __init__(self, j):
        # Base fields
        self.id = j.get('id')
        self.from_id = j.get('from_id')
        self.date = j.get('date')
        self.text = j.get('text')
        self.attachments = j.get('attachments')
        self.likes = j.get('likes')

        # Optional fields
        for f in ['id', 'from_id', 'date', 'text', 'attachments', 'likes']:
            j.pop(f, None)
        self.optional = j


class VK_app:
    def __init__(self, j):
        # Base fields
        self.id = j.get('id')
        self.title = j.get('title')
        self.icon_278 = j.get('icon_278')
        self.icon_139 = j.get('icon_139')
        self.icon_150 = j.get('icon_150')
        self.icon_75 = j.get('icon_75')
        self.banner_560 = j.get('banner_560')
        self.banner_1120 = j.get('banner_1120')
        self.type = j.get('type')
        self.section = j.get('section')
        self.author_url = j.get('author_url')
        self.author_id = j.get('author_id')
        self.author_group = j.get('author_group')
        self.members_count = j.get('members_count')
        self.published_date = j.get('published_date')
        self.catalog_position = j.get('catalog_position')
        self.international = j.get('international')
        self.leaderboard_type = j.get('leaderboard_type')
        self.genre_id = j.get('genre_id')
        self.genre = j.get('genre')
        self.platform_id = j.get('platform_id')
        self.is_in_catalog = j.get('is_in_catalog')
        self.friends = j.get('friends')
        self.installed = j.get('installed')
        self.is_html5_app = j.get('is_html5_app')
        self.screen_orientation = j.get('screen_orientation')
        self.mobile_controls_type = j.get('mobile_controls_type')
        self.mobile_view_support_type = j.get('mobile_view_support_type')

        # Optional fields
        for f in ['id', 'title', 'icon_278', 'icon_139', 'icon_150', 'icon_75', 'banner_560', 'banner_1120', 'type',
                  'section', 'author_url', 'author_id', 'author_group', 'members_count', 'published_date',
                  'catalog_position', 'international', 'leaderboard_type', 'genre_id', 'genre', 'platform_id',
                  'is_in_catalog', 'friends', 'installed', 'is_html5_app', 'screen_orientation', 'mobile_controls_type',
                  'mobile_view_support_type']:
            j.pop(f, None)
        self.optional = j


class Polls:
    def __init__(self, j):
        # Base fields
        self.id = j.get('id')
        self.owner_id = j.get('owner_id')
        self.created = j.get('created')
        self.question = j.get('question')
        self.votes = j.get('votes')
        self.answers = j.get('answers')
        self.anonymous = j.get('anonymous')
        self.multiple = j.get('multiple')
        self.answer_ids = j.get('answer_ids')
        self.end_date = j.get('end_date')
        self.closed = j.get('closed')
        self.is_board = j.get('is_board')
        self.can_edit = j.get('can_edit')
        self.can_vote = j.get('can_vote')
        self.can_report = j.get('can_report')
        self.can_share = j.get('can_share')
        self.author_id = j.get('author_id')
        self.photo = j.get('photo')
        self.background = j.get('background')
        self.friends = j.get('friends')

        # Optional fields
        for f in ['id', 'owner_id', 'created', 'question', 'votes', 'answers', 'anonymous', 'multiple', 'answer_ids',
                  'end_date', 'closed', 'is_board', 'can_edit', 'can_vote', 'can_report', 'can_share', 'author_id',
                  'photo', 'background', 'friends']:
            j.pop(f, None)
        self.optional = j


class Stats:
    def __init__(self, j):
        # Base fields
        self.period_from = j.get('period_from')
        self.period_to = j.get('period_to')
        self.visitors = j.get('visitors')
        self.reach = j.get('reach')

        # Optional fields
        for f in ['period_from', 'period_to', 'visitors', 'reach']:
            j.pop(f, None)
        self.optional = j


class Adress:
    def __init__(self, j):
        # Base fields
        self.id = j.get('id')
        self.country_id = j.get('country_id')
        self.city_id = j.get('city_id')
        self.title = j.get('title')
        self.address = j.get('address')
        self.additional_address = j.get('additional_address')
        self.latitude = j.get('latitude')
        self.longitude = j.get('longitude')
        self.metro_station_id = j.get('metro_station_id')
        self.work_info_status = j.get('work_info_status')
        self.timetable = j.get('timetable')

        # Optional fields
        for f in ['id', 'country_id', 'city_id', 'title', 'address', 'additional_address', 'latitude', 'longitude',
                  'metro_station_id', 'work_info_status', 'timetable']:
            j.pop(f, None)
        self.optional = j



########################################
# Media content and attachments:

def get_attachment_type(attachment):
    attachment_type = attachment.get('type')
    if attachment_type == 'photo':
        return Photo(attachment['photo'])


class Photo:
    def __init__(self, photo):
        pass


class Audio:
    def __init__(self):
        pass


class Video:
    def __init__(self):
        pass


class Document:
    def __init__(self):
        pass


class Url:
    def __init__(self):
        pass


class Sticker:
    def __init__(self):
        pass


class Present:
    def __init__(self):
        pass


class App_widget:
    def __init__(self):
        pass


class Stories:
    def __init__(self):
        pass


class Stories_sticker:
    def __init__(self):
        pass

