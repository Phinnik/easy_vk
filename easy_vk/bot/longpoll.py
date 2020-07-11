from ..methods.Groups import Groups
import requests


class GroupLongpoll:
    def __init__(self, owner_access_token: str, group_id: int, wait: int = 25):
        self._access_token = owner_access_token
        self._group_id = group_id
        self._wait = wait

        self._session = requests.Session()

        lp = self.get_lp()
        self._key = lp['key']
        self._server = lp['server']
        self._ts = lp['ts']

    def get_lp(self):
        lp = Groups(self._session, self._access_token, '5.120', 3).get_long_poll_server(self._group_id)
        return lp

    def update_lp(self):
        lp = self.get_lp()
        self._key = lp['key']
        self._server = lp['server']
        self._ts = lp['ts']

    def get_updates(self, ts_update=True):
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
            elif response['failed'] == 2:
                self.update_lp()
            elif response['failed'] == 3:
                self.update_lp()
            response = self.get_updates(ts_update)

        if ts_update and response:
            self._ts = response['ts']
        return response['updates']

    def listen(self):
        while True:
            updates = self.get_updates(ts_update=True)
            yield updates
