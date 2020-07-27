from . import api
import requests
from ctypes import c_longdouble


class User:
    def __init__(self, access_token: str, v='5.120', session=None, delay=0.35,
                 auto_retry=True, max_retries=2, timeout=5):
        last_call_timer = c_longdouble(0)
        if session is None:
            session = requests.session()

        self.search = api.Search(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)
        self.board = api.Board(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)
        self.market = api.Market(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)
        self.users = api.Users(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)
        self.gifts = api.Gifts(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)
        self.docs = api.Docs(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)
        self.stories = api.Stories(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)
        self.stats = api.Stats(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)
        self.wall = api.Wall(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)
        self.ads = api.Ads(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)
        self.utils = api.Utils(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)
        self.newsfeed = api.Newsfeed(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)
        self.status = api.Status(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)
        self.notes = api.Notes(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)
        self.pages = api.Pages(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)
        self.storage = api.Storage(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)
        self.account = api.Account(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)
        self.orders = api.Orders(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)
        self.auth = api.Auth(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)
        self.database = api.Database(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)
        self.streaming = api.Streaming(session, access_token, v, last_call_timer, delay, auto_retry, max_retries,
                                       timeout)
        self.likes = api.Likes(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)
        self.widgets = api.Widgets(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)
        self.apps = api.Apps(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)
        self.downloadedGames = api.Downloadedgames(session, access_token, v, last_call_timer, delay, auto_retry,
                                                   max_retries, timeout)
        self.groups = api.Groups(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)
        self.messages = api.Messages(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)
        self.notifications = api.Notifications(session, access_token, v, last_call_timer, delay, auto_retry,
                                               max_retries, timeout)
        self.fave = api.Fave(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)
        self.photos = api.Photos(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)
        self.friends = api.Friends(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)
        self.video = api.Video(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)
        self.prettyCards = api.Prettycards(session, access_token, v, last_call_timer, delay, auto_retry, max_retries,
                                           timeout)
        self.polls = api.Polls(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)
        self.leads = api.Leads(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)

