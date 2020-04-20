from .easy_vk import VK
from .vk_types import get_update_type, Message, Message_typing_state
import requests
import re


class Message_handler:
    def __init__(self, h_filters: list, function):
        # h_filters = [('regexp', '123'), ('has_attachments', 'False'), ('fwd_messages', True), ('geo', True)]
        self.h_filters = h_filters
        self.function = function

    def check_filter(self, h_filter, message: Message):
        test_cases = {
            'regexp': lambda msg: msg.text and re.search(h_filter[1], msg.text),
            'has_attachments': lambda msg: len(msg.attachments) != 0,
            'has_fwd_messages': lambda msg: (msg.fwd_messages is not None) == h_filter[1],
            'geo': lambda msg: (msg.geo is not None) == h_filter[1],
            # 'action': ''
        }
        return test_cases[h_filter[0]](message)

    def is_valid(self, message):
        for h_filter in self.h_filters:
            if not self.check_filter(h_filter, message):
                return False
        return True

    def notify(self, message):
        if self.is_valid(message):
            self.function(message)


class Bot(VK):
    def __init__(self, access_token, group_id, v=5.101):
        super().__init__(access_token, v)
        self.group_id = group_id

        lp = self._get_lp()
        self.key = lp['key']
        self.server = lp['server']
        self.ts = lp['ts']

        self.message_handlers = []

        self.listening = False

    def _get_lp(self):
        lp = self.groups_getLongPollServer(self.group_id)
        return lp

    def _check(self, wait=25):
        params = {'act': 'a_check',
                  'key': self.key,
                  'ts': self.ts,
                  'wait': wait}
        response = requests.get(self.server, params=params).json()
        if 'failed' in response:
            if response['failed'] == 1:
                self.ts = response['ts']
            else:
                lp = self._get_lp()
                self.key = lp['key']
                self.server = lp['server']
            response = requests.get(self.server, params=params).json()
        return response

    def listen(self):
        self.listening = True
        while self.listening:
            r = self._check()

            self.ts = r['ts']
            updates = r['updates']

            if len(updates) != 0:
                yield updates[0]

    def run(self):
        for update in self.listen():
            self._process_handlers(get_update_type(update))

    def _process_handlers(self, update):
        if update.type == 'message_new':
            print(update)
            for handler in self.message_handlers:
                handler.notify(update)

    def message_handler(self, regexp=None, has_attachments=None, fwd_messages=None, geo=None):
        h_filters = locals()
        h_filters.pop('self')
        h_filters = [(f, h_filters[f]) for f in h_filters if h_filters[f] is not None]
        def wrapper(function):
            self.message_handlers.append(Message_handler(h_filters, function))
            return function
        return wrapper
