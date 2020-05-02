from ApiMethod import ApiMethod


class Apps(ApiMethod):
    def __init__(self, access_token, v, session, calls_per_second):
        super(Apps, self).__init__(access_token, v, session, calls_per_second)
        self._base_method = 'apps.'
