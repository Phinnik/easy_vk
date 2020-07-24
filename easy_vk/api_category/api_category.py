import time
from easy_vk.exceptions.exceptions import raise_exception, Server
from typing import Optional, Tuple, List, Dict, Any


def preprocess_parameter(parameter):
    if isinstance(parameter, dict) or isinstance(parameter, str):
        return parameter
    if isinstance(parameter, int) or isinstance(parameter, float):
        return str(parameter)
    if isinstance(parameter, list):
        parameter = [preprocess_parameter(p) for p in parameter]
        parameter = ','.join(parameter)
        return parameter

    if hasattr(parameter, '__dict__'):
        if hasattr(parameter, 'value'):
            return parameter.value
        elif hasattr(parameter, 'Config'):
            return parameter.json(exclude_none=True)
        else:
            ValueError(f'Unknown parameter type passed ({parameter}).\n'
                       f'Parameters can be only builtin types or objects, defined in easy_vk.types.objects.')


class BaseCategory:
    def __init__(self, session, access_token: str, v: str, delay: float, auto_retry: bool, max_retries: int, timeout: float):
        """
        Base api category class

        :param session: api session
        :param access_token: api access_token
        :param v: api version
        :param delay: delay between api calls
        :param auto_retry: enables auto retry in calling methods if specific errors occurred
            e.g. easy_vk.exceptions.exceptions.Server
        :param max_retries: maximum value of retries. Works only if auto_retry is True
        :param timeout: time to sleep between retries. Works only if auto_retry is True
        """

        self._session = session
        self._access_token = access_token
        self._v = v
        self._delay = delay
        self._auto_retry = auto_retry
        self._max_retries = max_retries
        self._timeout = timeout

    def _call(self, method_name: str, method_parameters: Dict[str, Any], param_aliases: Optional[List[Tuple[str, str]]], response_type, retries_count: int = 0):
        """
        Call method "method_name" with parameters and return json or object response

        :param method_name: full name of the method.  e.g. friends.get
        :param method_parameters: locals, containing method parameters
        :param param_aliases: Optional[List[Tuple[str, str]]] e.g [('type_', 'type'), ('global_', 'global')]
        :param response_type: response object which method should return
            e.g easy_vk.types.responses.FriendsGetResponse
        :param retries_count: current retries counter
        """

        time_start = time.time()

        api_url = f'https://api.vk.com/method/{method_name}'

        if param_aliases:
            for name, alias in param_aliases:
                method_parameters[alias] = method_parameters.pop(name, None)

        params = {parameter: value for parameter, value in method_parameters.items() if value is not None}
        params = {p: preprocess_parameter(params[p]) for p in params}
        params['access_token'] = self._access_token
        params['v'] = self._v

        try:
            # post request type to have larger size requests
            response = self._session.post(url=api_url, params=params).json()

            if 'response' in response:
                response = response

            # error
            else:
                error_code = response['error']['error_code']
                error_message = response['error']['error_msg']
                raise_exception(error_code, error_message)

            delay = self._delay - (time.time() - time_start)
            if delay > 0:
                time.sleep(delay)

        except Server as e:
            if self._auto_retry and retries_count < self._max_retries:
                time.sleep(self._timeout)
                response = self._call(method_name, method_parameters,
                                      param_aliases, response_type, retries_count=retries_count + 1)
            else:
                raise e

        response = response_type(**response)
        return response
