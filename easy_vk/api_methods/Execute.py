from .ApiMethod import ApiMethod


class Execute(ApiMethod):
    def __init__(self, access_token, v, session, calls_per_second):
        super(Execute, self).__init__(access_token, v, session, calls_per_second)
        self._base_method = 'execute'

    def __call__(self, code):
        params = locals()
        return self._call(self._base_method, params)
