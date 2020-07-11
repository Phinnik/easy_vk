import time
from ..exceptions  import raise_exception, Server


class ApiMethod:
    def __init__(self, session, access_token, v, requests_per_s):
        self._session = session
        self._access_token = access_token
        self._v = v
        self._requests_per_s = requests_per_s

    def _call(self, method_name, method_locals):
        try:
            time_start = time.time()

            api_url = f'https://api.vk.com/method/{method_name}'

            params = method_locals
            param_alias_dict = params.get('param_alias_dict')
            if param_alias_dict:
                for alias in param_alias_dict:
                    params[param_alias_dict[alias]] = params.pop(alias)
                params.pop('param_alias_dict')

            params.pop('self')
            params = {p: params[p] for p in params if params[p] is not None}
            params['access_token'] = self._access_token
            params['v'] = self._v

            response = self._session.post(url=api_url, params=params).json()
            if 'error' in response:
                # print(response)
                error_code =  response['error']['error_code']
                error_message = response['error']['error_msg']
                raise_exception(error_code, error_message)
            else:
                response = response['response']

            delay = 1 / self._requests_per_s - (time.time() - time_start)
            if delay > 0:
                time.sleep(delay)

        except Server as e:
            response = self._call(method_name, method_locals)


        return response
