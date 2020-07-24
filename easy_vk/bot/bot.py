from . import api
import requests


class Bot:
    def __init__(self, access_token: str, group_id: int, v='5.120', session=None, delay=0.08, auto_retry=True,
                 max_retries=2, timeout=2):
        if session is None:
            session = requests.session()

        self.photos = api.Photos(session, access_token, v, delay, auto_retry, max_retries, timeout)
        self.wall = api.Wall(session, access_token, v, delay, auto_retry, max_retries, timeout)
        self.board = api.Board(session, access_token, v, delay, auto_retry, max_retries, timeout)
        self.groups = api.Groups(session, access_token, v, delay, auto_retry, max_retries, timeout)
        self.users = api.Users(session, access_token, v, delay, auto_retry, max_retries, timeout)
        self.appWidgets = api.Appwidgets(session, access_token, v, delay, auto_retry, max_retries, timeout)
        self.stories = api.Stories(session, access_token, v, delay, auto_retry, max_retries, timeout)
        self.messages = api.Messages(session, access_token, v, delay, auto_retry, max_retries, timeout)
        self.storage = api.Storage(session, access_token, v, delay, auto_retry, max_retries, timeout)
        self.docs = api.Docs(session, access_token, v, delay, auto_retry, max_retries, timeout)
        self.utils = api.Utils(session, access_token, v, delay, auto_retry, max_retries, timeout)

        self.messages.get_long_poll_server()