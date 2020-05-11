import requests
from .api_methods import *


class VK:
    def __init__(self, access_token, v=5.101, bot=False):
        session = requests.session()

        if bot:
            calls_per_second = 25
        else:
            calls_per_second = 3

        self.access_token = access_token

        self.account = Account(access_token, v, session, calls_per_second)
        self.ads = Ads(access_token, v, session, calls_per_second)
        self.appWidgets = AppWidgets(access_token, v, session, calls_per_second)
        # self.apps = Apps(access_token, v, session, calls_per_second)
        self.auth = Auth(access_token, v, session, calls_per_second)
        self.board = Board(access_token, v, session, calls_per_second)
        self.database = Database(access_token, v, session, calls_per_second)
        self.docs = Docs(access_token, v, session, calls_per_second)
        # self.downloadedGames = DownloadedGames(access_token, v, session, calls_per_second)
        self.docs = Docs(access_token, v, session, calls_per_second)
        self.execute = Execute(access_token, v, session, calls_per_second)
        self.fave = Fave(access_token, v, session, calls_per_second)
        self.friends = Friends(access_token, v, session, calls_per_second)
        self.gifts = Gifts(access_token, v, session, calls_per_second)
        self.groups = Groups(access_token, v, session, calls_per_second)
        self.leadForms = LeadForms(access_token, v, session, calls_per_second)
        self.leads = Leads(access_token, v, session, calls_per_second)
        self.likes = Likes(access_token, v, session, calls_per_second)
        self.market = Market(access_token, v, session, calls_per_second)
        self.messages = Messages(access_token, v, session, calls_per_second)
        self.newsfeed = Newsfeed(access_token, v, session, calls_per_second)
        self.notes = Notes(access_token, v, session, calls_per_second)
        self.notifications = Notifications(access_token, v, session, calls_per_second)
        self.orders = Orders(access_token, v, session, calls_per_second)
        self.pages = Pages(access_token, v, session, calls_per_second)
        self.photos = Photos(access_token, v, session, calls_per_second)
        # self.podcasts = Podcasts(access_token, v, session, calls_per_second)
        self.polls = Polls(access_token, v, session, calls_per_second)
        self.prettyCards = PrettyCards(access_token, v, session, calls_per_second)
        self.search = Search(access_token, v, session, calls_per_second)
        self.secure = Secure(access_token, v, session, calls_per_second)
        self.stats = Stats(access_token, v, session, calls_per_second)
        self.status = Status(access_token, v, session, calls_per_second)
        self.storage = Storage(access_token, v, session, calls_per_second)
        self.stories = Stories(access_token, v, session, calls_per_second)
        self.streaming = Streaming(access_token, v, session, calls_per_second)
        self.users = Users(access_token, v, session, calls_per_second)
        self.utils = Utils(access_token, v, session, calls_per_second)
        self.video = Video(access_token, v, session, calls_per_second)
        self.wall = Wall(access_token, v, session, calls_per_second)
        self.widgets = Widgets(access_token, v, session, calls_per_second)
