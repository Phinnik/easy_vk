from typing import List, Union

import requests
import re

from .longpoll import GroupLongpoll
from .handlers import UpdateHandler
from .objects import Message
from ..methods import Messages


class GroupBot:
    def __init__(self, owner_access_token: str,
                 group_access_token: str,
                 group_id: int,
                 wait: int = 25):
        self._owner_access_token = owner_access_token
        self._group_access_token = group_access_token
        self._group_id = group_id
        self._wait = wait

        self._handlers: List[UpdateHandler] = []

        self.longpoll = GroupLongpoll(owner_access_token, group_id, wait)

        # api methods
        session = requests.Session()
        self.messages = Messages(session, group_access_token, '5.120', 25)

    ############################# Handlers
    def message_typing_state_handler(self, user_id: int = None,
                                     user_ids: List[int] = None):
        def decorator(function):
            update_type = 'message_typing_state'
            filters = []
            if user_id:
                filters.append(lambda x: x['from_id'] == user_id)
            if user_ids:
                filters.append(lambda x: x['from_id'] in user_ids)

            handler = UpdateHandler(update_type, filters, function)
            self._handlers.append(handler)
            return function

        return decorator

    def message_new_handler(self, regexp: str = None,
                            user_id: int = None,
                            user_ids: List[int] = None,
                            attachment_type: str = None):
        def decorator(function):
            update_type = 'message_new'
            filters = []
            if regexp:
                filters.append(lambda x: True if re.fullmatch(regexp, x.get('text', '')) else None)
            if user_id:
                filters.append(lambda x: x['from_id'] == user_id)
            if user_ids:
                filters.append(lambda x: x['from_id'] in user_ids)
            if attachment_type:
                filters.append(lambda x: attachment_type in [a['type'] for a in x['attachments']])


            handler = UpdateHandler(update_type, filters, function, handled_object_type=Message)
            self._handlers.append(handler)
            return function

        return decorator

    ####################################################

    def _handle(self, update):
        for handler in self._handlers:
            handler.notify(update)

    def run(self):
        for updates in self.longpoll.listen():
            for update in updates:
                self._handle(update)
