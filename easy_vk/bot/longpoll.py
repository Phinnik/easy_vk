from ..methods.Groups import Groups
import requests

import logging

logger = logging.getLogger('easy_vk.bot.longpoll')
logger.setLevel(logging.DEBUG)


class GroupLongpoll:
    def __init__(self, owner_access_token: str, group_id: int, wait: int = 25, ts: int = None):
        self._access_token = owner_access_token
        self._group_id = group_id
        self._wait = wait

        self._session = requests.Session()

        lp = self.get_lp()
        self._key = lp['key']
        self._server = lp['server']
        self._ts = ts or lp['ts']
        logger.debug(f'Initialise GroupLongpoll class with parameters:\n'
                     f'\towner_access_token = {owner_access_token}'
                     f'\tgroup_id = {group_id}'
                     f'\twait = {wait}'
                     f'\tts = {ts}'
                     )

    def get_lp(self):
        lp = Groups(self._session, self._access_token, '5.120', 3).get_long_poll_server(self._group_id)
        logger.debug(f'Got new longpoll: {lp}')
        return lp

    def update_lp(self):
        lp = self.get_lp()
        self._key = lp['key']
        self._server = lp['server']
        self._ts = lp['ts']
        logger.debug(f'Updated new lonpoll with parameters:\n'
                     f'\tself._key = {lp["key"]}\n'
                     f'\tself._server = {lp["server"]}\n'
                     f'\tself._ts = {lp["ts"]}')

    def get_updates(self, ts_update=True):
        logger.debug('Getting new updates...')
        url = self._server
        params = {
            'act': 'a_check',
            'key': self._key,
            'ts': self._ts,
            'wait': self._wait
        }
        response = self._session.get(url, params=params).json()

        if 'failed' in response:
            if response['failed'] == 1:
                self._ts = response['ts']
                logger.debug(f'Got "fail" = 1 when getting updates. Changing self._ts = {response["ts"]}')
            elif response['failed'] == 2:
                logger.debug(f'Got "fail" = 2 when getting updates. Updating lonpoll...')
                self.update_lp()
            elif response['failed'] == 3:
                logger.debug(f'Got "fail" = 2 when getting updates. Updating lonpoll...')
                self.update_lp()
            return self.get_updates(ts_update)

        if ts_update and response:
            self._ts = response['ts']
            logger.debug(f'Changed ts: self._ts = {response["ts"]}')

        logger.debug(f'Got updates: {response["updates"]}')
        return response['updates']

    def listen(self):
        logger.debug(f'Started listening')
        while True:
            updates = self.get_updates(ts_update=True)
            yield updates
