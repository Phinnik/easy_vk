from typing import List

import requests
import re
import logging

from .longpoll import GroupLongpoll
from .handlers import Handlers
from ..objects.objects import BotMessage
from ..methods import Messages

logger = logging.getLogger('easy_vk.bot')
logger.setLevel(logging.DEBUG)


class GroupBot:
    def __init__(self, owner_access_token: str,
                 group_access_token: str,
                 group_id: int,
                 wait: int = 25,
                 debug_mode: bool = False,
                 owner_id: int = None):
        self._owner_access_token = owner_access_token
        self._group_access_token = group_access_token
        self._group_id = group_id
        self._wait = wait
        self._debug_mode = debug_mode
        self._owner_id = owner_id

        self.handlers: Handlers = Handlers(debug_mode=self._debug_mode, owner_id=self._owner_id)

        self._longpoll = GroupLongpoll(owner_access_token, group_id, wait)

        # api methods
        session = requests.Session()
        self.messages = Messages(session, group_access_token, '5.120', 25)

    def _handle(self, update):
        for handler in self.handlers._handlers_list:
            handler.notify(update)

    def run(self):
        logger.debug(f'Run bot for group https://vk.com/public{self._group_id}\n')
        for updates in self._longpoll.listen():
            for update in updates:
                self._handle(update)
