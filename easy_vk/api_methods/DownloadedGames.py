from .ApiMethod import ApiMethod


class DownloadedGames(ApiMethod):
    def __init__(self, access_token, v, session, calls_per_second):
        super(DownloadedGames, self).__init__(access_token, v, session, calls_per_second)
        self._base_method = 'downloadedGames.'
