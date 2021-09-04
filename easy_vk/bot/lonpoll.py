import sys
from typing import Callable

from loguru import logger
from requests.sessions import Session

logger.remove()


class Longpoll:
    def __init__(self, get_longpoll: Callable, session: Session, group_id: int, key: str = None, ts: int = None,
                 server=None, debug_mode: bool = False):
        if debug_mode:
            logger.add(sys.stdout, format="{time} {file} {module} {function}: {message}", level="DEBUG")
        self._get_longpoll = get_longpoll
        self.session = session
        self._group_id = group_id

        self.key = key
        self.ts = ts
        self.server = server

        if not self.key:
            self._update_longpoll()

    def _update_longpoll(self):
        lp = self._get_longpoll(self._group_id)
        self.key = lp.key
        self.ts = lp.ts
        self.server = lp.server

    def check_updates(self, ts_update=True):
        params = {
            'act': 'a_check',
            'key': self.key,
            'ts': self.ts,
            'wait': 25
        }
        updates = self.session.get(self.server, params=params).json()

        if 'failed' in updates:
            if updates['failed'] == 1:
                self.ts = updates['ts']
            else:
                self._update_longpoll()
            return self.check_updates(ts_update=True)

        else:
            if ts_update:
                self.ts = updates['ts']
        logger.debug(f'new update: {updates}')
        return updates['updates']

    def run(self):
        while True:
            updates = self.check_updates()
            for u in updates:
                yield u

    def __repr__(self):
        return f'LONGPOLL INFO\n' \
               f'key: {self.key}\n' \
               f'ts: {self.ts}\n' \
               f'server: {self.server}'
