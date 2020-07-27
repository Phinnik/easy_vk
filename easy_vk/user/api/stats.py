# This file was autogenerated from vk-api json schema

from typing import List, Union, Optional, Literal, overload
from easy_vk.types import objects
from easy_vk.types import responses
from easy_vk.api_category import BaseCategory


class Stats(BaseCategory):
    def __init__(self, session, access_token: str, v: str, last_call_timer, delay: float, auto_retry: bool, max_retries: int, timeout: float):
        super().__init__(session, access_token, v, last_call_timer, delay, auto_retry, max_retries, timeout)

    def get(self, group_id: Optional[int] = None, app_id: Optional[int] = None, timestamp_from: Optional[int] = None, timestamp_to: Optional[int] = None, interval: Optional[str] = None, intervals_count: Optional[int] = None, filters: Optional[List[str]] = None, stats_groups: Optional[List[str]] = None, extended: Optional[bool] = None) -> responses.StatsGet:
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
        param_aliases = []
        method_name = 'stats.get'
        response_type = responses.StatsGet
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_post_reach(self, owner_id: str, post_ids: List[int]) -> responses.StatsGetPostReach:
        """
        Returns stats for a wall post.
        
        :param owner_id: post owner community id. Specify with "-" sign.
        :param post_ids: wall posts id
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = []
        method_name = 'stats.getPostReach'
        response_type = responses.StatsGetPostReach
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def track_visitor(self, id_: str) -> responses.BaseOk:
        """
        :param id_:
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        param_aliases = [('id_', 'id')]
        method_name = 'stats.trackVisitor'
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)
