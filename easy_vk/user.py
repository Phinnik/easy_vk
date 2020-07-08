from . import methods
from requests import Session


class User:
    def __init__(self, access_token):
        requests_per_s = 3
        v = '5.120'
        session = Session()

        self._access_token = access_token
        self._v = v
        self._requests_per_s = requests_per_s
        self._session = session

        self.ads = methods.Ads(session, access_token, v, requests_per_s)
        self.stories = methods.Stories(session, access_token, v, requests_per_s)
        self.video = methods.Video(session, access_token, v, requests_per_s)
        self.docs = methods.Docs(session, access_token, v, requests_per_s)
        self.photos = methods.Photos(session, access_token, v, requests_per_s)
        self.notes = methods.Notes(session, access_token, v, requests_per_s)
        self.widgets = methods.Widgets(session, access_token, v, requests_per_s)
        self.market = methods.Market(session, access_token, v, requests_per_s)
        self.wall = methods.Wall(session, access_token, v, requests_per_s)
        self.newsfeed = methods.Newsfeed(session, access_token, v, requests_per_s)
        self.fave = methods.Fave(session, access_token, v, requests_per_s)
        self.account = methods.Account(session, access_token, v, requests_per_s)
        self.auth = methods.Auth(session, access_token, v, requests_per_s)
        self.groups = methods.Groups(session, access_token, v, requests_per_s)
        self.status = methods.Status(session, access_token, v, requests_per_s)
        self.appwidgets = methods.Appwidgets(session, access_token, v, requests_per_s)
        self.polls = methods.Polls(session, access_token, v, requests_per_s)
        self.utils = methods.Utils(session, access_token, v, requests_per_s)
        self.messages = methods.Messages(session, access_token, v, requests_per_s)
        self.apps = methods.Apps(session, access_token, v, requests_per_s)
        self.orders = methods.Orders(session, access_token, v, requests_per_s)
        self.pages = methods.Pages(session, access_token, v, requests_per_s)
        self.search = methods.Search(session, access_token, v, requests_per_s)
        self.notifications = methods.Notifications(session, access_token, v, requests_per_s)
        self.stats = methods.Stats(session, access_token, v, requests_per_s)
        self.board = methods.Board(session, access_token, v, requests_per_s)
        self.secure = methods.Secure(session, access_token, v, requests_per_s)
        self.leads = methods.Leads(session, access_token, v, requests_per_s)
        self.streaming = methods.Streaming(session, access_token, v, requests_per_s)
        self.likes = methods.Likes(session, access_token, v, requests_per_s)
        self.prettycards = methods.Prettycards(session, access_token, v, requests_per_s)
        self.users = methods.Users(session, access_token, v, requests_per_s)
        self.friends = methods.Friends(session, access_token, v, requests_per_s)
        self.database = methods.Database(session, access_token, v, requests_per_s)
        self.storage = methods.Storage(session, access_token, v, requests_per_s)
        self.gifts = methods.Gifts(session, access_token, v, requests_per_s)
        self.execute = methods.Execute(session, access_token, v, requests_per_s).execute
