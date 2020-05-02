from .ApiMethod import ApiMethod


class Podcasts(ApiMethod):
    def __init__(self, access_token, v, session, calls_per_second):
        super(Podcasts, self).__init__(access_token, v, session, calls_per_second)
        self._base_method = 'podcasts.'