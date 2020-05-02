from typing import List, Dict, Optional, Union
import time


class ApiMethod:
    def __init__(self, access_token, v, session, calls_per_second):
        self._session = session
        self._calls_per_second = calls_per_second
        self._required_params = {
            'v': v,
            'access_token': access_token
        }

    def _call(self, method_name: str, params: dict) -> Union[dict, int, list]:
        url = 'https://api.vk.com/method/{}'.format(method_name)
        params.update(self._required_params)
        params.pop('self')
        params = {p: params[p] for p in params if params[p]}
        time_start = time.time()
        r = self._session.post(url, params=params)
        delay = 1 / (self._calls_per_second - 0.2) - (time.time() - time_start)
        if delay > 0:
            time.sleep(delay)
        try:
            r = r.json()['response']
        except Exception as e:
            print(r.json())
            raise e
        return r
