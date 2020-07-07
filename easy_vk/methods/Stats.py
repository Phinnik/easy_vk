from _ApiMethod import ApiMethod
from typing import List


class Stats(ApiMethod):
    def __init__(self, session, access_token, v, requests_per_s):
        super().__init__(session, access_token, v, requests_per_s)

    def get(self, group_id: int = None, app_id: int = None, timestamp_from: int = None, timestamp_to: int = None, interval: str = None, intervals_count: int = None, filters: List[str] = None, stats_groups: List[str] = None, extended: bool = None):
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
    
        if filters:
            filters = ','.join(filters)
        if stats_groups:
            stats_groups = ','.join(stats_groups)
        
        method_name = 'stats.get'
        return self.call(method_name, locals())

    def get_post_reach(self, owner_id: str, post_ids: List[int]):
        """
        Returns stats for a wall post.
        
        :param owner_id: post owner community id. Specify with "-" sign.
        :param post_ids: wall posts id
        """
    
        if post_ids:
            post_ids = [str(p) for p in post_ids]
            post_ids = ','.join(post_ids)
        
        method_name = 'stats.getPostReach'
        return self.call(method_name, locals())

    def track_visitor(self, id_: str):
        """
        
        :param id_: 
        """
    
        param_alias_dict = {'id_': 'id'}
        method_name = 'stats.trackVisitor'
        return self.call(method_name, locals())

