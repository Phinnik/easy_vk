import time
from easy_vk.bot.api_options import APIOptions
from easy_vk.exceptions.exceptions import raise_exception, Server
from typing import Optional, Tuple, List, Dict, Any
from ctypes import c_longdouble
from pydantic import ValidationError

from easy_vk.settings import VK_API_URL


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


def unpack_response(response, response_type):
    if response_type in (int, bool, str, float):
        return response_type(response)
    elif hasattr(response_type, '__origin__'):
        return [unpack_response(r, response_type.__args__[0]) for r in response]
    elif hasattr(response_type, '__fields__'):
        try:
            return response_type(**response)
        except ValidationError as e:
            print(e.json())
            return response
    else:
        pass


class BaseCategory:
    def __init__(self, options: APIOptions):
        """
        Base api category class

        :param options: api options
        """

        self._last_call_timer = options.last_call_timer
        self._session = options.session
        self._access_token = options.access_token
        self._v = options.v
        self._delay = options.delay
        self._auto_retry = options.auto_retry
        self._max_retries = options.max_retries
        self._timeout = options.timeout

    def _call(self, method_name: str, method_parameters: Dict[str, Any], param_aliases: Optional[List[Tuple[str, str]]],
              response_type, retries_count: int = 0):
        """
        Call method "method_name" with parameters and return json or object response

        :param method_name: full name of the method.  e.g. friends.get
        :param method_parameters: locals, containing method parameters
        :param param_aliases: Optional[List[Tuple[str, str]]] e.g [('type_', 'type'), ('global_', 'global')]
        :param response_type: response object which method should return
            e.g easy_vk.types.responses.FriendsGetResponse
        :param retries_count: current retries counter
        """
        api_url = f'{VK_API_URL}/{method_name}'

        if param_aliases:
            for name, alias in param_aliases:
                method_parameters[alias] = method_parameters.pop(name, None)

        params = {parameter: value for parameter, value in method_parameters.items() if value is not None}
        params = {p: preprocess_parameter(params[p]) for p in params}
        params['access_token'] = self._access_token
        params['v'] = self._v

        delay = self._delay - (time.time() - self._last_call_timer.value)
        if delay > 0:
            time.sleep(delay)

        try:
            # post request type to have larger size requests
            response = self._session.post(url=api_url, params=params).json()

            if 'response' in response:
                response = response['response']

            # error
            else:
                error_code = response['error']['error_code']
                error_message = response['error']['error_msg']
                raise_exception(error_code, error_message)

        except Server as e:
            if self._auto_retry and retries_count < self._max_retries:
                time.sleep(self._timeout)
                response = self._call(method_name, method_parameters,
                                      param_aliases, response_type, retries_count=retries_count + 1)
            else:
                raise e

        self._last_call_timer.value = time.time()
        response = unpack_response(response, response_type)

        return response
