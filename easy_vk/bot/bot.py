from easy_vk.bot import api
import requests
from ctypes import c_longdouble
from easy_vk.bot.lonpoll import Longpoll
from easy_vk.bot.handlers import Handlers


class Bot:
    def __init__(self, access_token: str, group_id: int, v='5.120', session=None, delay=0.08, auto_retry=True,
                 max_retries=2, timeout=2, debug_mode: bool = False, owner_id: int = None):
        """

        :param access_token: bot access token. Get it in your group - Управление - Работа с API - Создать ключ
        :param group_id: id of your group
        :param v: api version (current - '5.120')
        :param session: requests session
        :param delay: delay between api calls
        :param auto_retry: enable auto retries
        :param max_retries: maximum retries count. Works only if auto retry enabled
        :param timeout: time between retries. Works only if auto retry enabled
        :param debug_mode: - Not implemented yet
        :param owner_id: - Not implemented yet
        """
        last_call_timer = c_longdouble(0)
        if session is None:
            session = requests.session()

        self.photos = api.Photos(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)
        self.wall = api.Wall(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)
        self.board = api.Board(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)
        self.groups = api.Groups(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)
        self.users = api.Users(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)
        self.appWidgets = api.Appwidgets(session, access_token, v, last_call_timer, delay, auto_retry, max_retries,
                                         timeout)
        self.stories = api.Stories(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)
        self.messages = api.Messages(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)
        self.storage = api.Storage(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)
        self.docs = api.Docs(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)
        self.utils = api.Utils(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)

        self._longpoll = Longpoll(self.groups.get_long_poll_server, session, group_id)
        self.handler = Handlers()

    def run(self):
        """
        Infinite loop of bot
        """
        for update in self._longpoll.run():
            self.handler.handle(update)
