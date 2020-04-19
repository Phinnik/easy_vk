from easy_vk import VK
# from bots_types import Message
import requests
import re


class Bot(VK):
    def __init__(self, access_token, group_id, v=5.101):
        super().__init__(access_token, v)
        self.group_id = group_id

        lp = self.get_lp()
        self.key = lp['key']
        self.server = lp['server']
        self.ts = lp['ts']

        self.message_new_handlers = []

        self.listening = False

    def get_lp(self):
        lp = self.groups_getLongPollServer(self.group_id)
        return lp

    def check(self, wait=25):
        params = {'act': 'a_check',
                  'key': self.key,
                  'ts': self.ts,
                  'wait': wait}
        response = requests.get(self.server, params=params).json()
        if 'failed' in response:
            if response['failed'] == 1:
                self.ts = response['ts']
            else:
                lp = self.get_lp()
                self.key = lp['key']
                self.server = lp['server']
            response = requests.get(self.server, params=params).json()
        return response

    def listen(self):
        self.listening = True
        while self.listening:
            r = self.check()

            self.ts = r['ts']
            updates = r['updates']

            if len(updates) != 0:
                yield updates[0]

    def run(self):
        for update in self.listen():
            self.process_handlers(update)

    def process_handlers(self, update):
        if update['type'] == 'message_new':
            self.notify_message_new_handlers(update['object'])
        else:
            pass

    def notify_message_new_handlers(self, message):
        for handler in self.message_new_handlers:
            if self.check_message_new_handler(handler, message):
                self.exec_handler(handler, message)

    def check_message_new_handler(self, handler, message):
        for handler_filter, value in handler['filters']:
            test_cases = {
                'regexp': lambda msg: 'text' in msg and re.search(value, msg['text'])
            }
            if not test_cases[handler_filter](message):
                return False
        return True

    def exec_handler(self, handler, message):
        handler['function'](message)

    def message_new_handler(self, regexp=None):
        def wrapper(function):
            self.message_new_handlers.append({'filters': [('regexp', regexp)],
                                              'function': function})
            return function

        return wrapper
