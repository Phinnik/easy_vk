from easy_vk.bot import api
from easy_vk.bot.api_options import APIOptions
import requests
from ctypes import c_longdouble
from easy_vk.bot.lonpoll import Longpoll
from easy_vk.bot.handlers import Handlers
from easy_vk.settings import VK_API_VERSION

class Bot:
    def __init__(self, access_token: str, group_id: int, v=VK_API_VERSION, session=None, delay=0.08, auto_retry=True,
                 max_retries=2, timeout=2, debug_mode: bool = False, owner_id: int = None):
        """

        :param access_token: bot access token. Get it in your group - Управление - Работа с API - Создать ключ
        :param group_id: id of your group
        :param v: api version (current - VK_API_VERSION)
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

        options = APIOptions(
            session=session,
            access_token=access_token,
            v=v,
            last_call_timer=last_call_timer,
            delay=delay,
            auto_retry=auto_retry,
            max_retries=max_retries,
            timeout=timeout,
        )
        self.photos = api.Photos(options)
        self.wall = api.Wall(options)
        self.board = api.Board(options)
        self.groups = api.Groups(options)
        self.users = api.Users(options)
        self.appWidgets = api.Appwidgets(options)
        self.stories = api.Stories(options)
        self.messages = api.Messages(options)
        self.storage = api.Storage(options)
        self.docs = api.Docs(options)
        self.utils = api.Utils(options)

        self._longpoll = Longpoll(self.groups.get_long_poll_server, session, group_id, debug_mode=debug_mode)
        self.handler = Handlers()

    def run(self):
        """
        Infinite loop of bot
        """
        for update in self._longpoll.run():
            self.handler.handle(update)
