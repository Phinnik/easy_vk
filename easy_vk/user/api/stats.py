from typing import List, Union, Optional
from easy_vk.types import objects, responses
from .base import BaseCategory


class Stats(BaseCategory):
    def __init__(self, session, access_token: str, v: str, delay: float, auto_retry: bool, max_retries: int, timeout: float):
        super().__init__(session, access_token, v, delay, auto_retry, max_retries, timeout)

    def get(self, group_id: int = None, app_id: int = None, timestamp_from: int = None, timestamp_to: int = None, interval: str = None, intervals_count: int = None, filters: List[str] = None, stats_groups: List[str] = None, extended: bool = None) -> responses.StatsGet:
        """
        Returns statistics of a community or an application.
        
        :param group_id: Community ID.
        :param app_id: Application ID.
        :param timestamp_from: 
        :param timestamp_to: 
        :param interval: 
        :param intervals_count: 
        :param filters: 
        :param stats_groups: 
        :param extended: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'stats.get'
        param_aliases = []
        response_type = responses.StatsGet
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_post_reach(self, owner_id: str = None, post_ids: List[int] = None) -> responses.StatsGetPostReach:
        """
        Returns stats for a wall post.
        
        :param owner_id: post owner community id. Specify with "-" sign.
        :param post_ids: wall posts id
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'stats.getPostReach'
        param_aliases = []
        response_type = responses.StatsGetPostReach
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def track_visitor(self, id_: str = None) -> responses.BaseOk:
        """
        :param id_: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'stats.trackVisitor'
        param_aliases = [('id_', 'id')]
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

