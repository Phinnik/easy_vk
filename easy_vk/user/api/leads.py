from typing import List, Union, Optional
from easy_vk.types import objects, responses
from .base import BaseCategory


class Leads(BaseCategory):
    def __init__(self, session, access_token: str, v: str, delay: float, auto_retry: bool, max_retries: int, timeout: float):
        super().__init__(session, access_token, v, delay, auto_retry, max_retries, timeout)

    def check_user(self, lead_id: int = None, test_result: int = None, test_mode: bool = None, auto_start: bool = None, age: int = None, country: str = None) -> responses.LeadsCheckUser:
        """
        Checks if the user can start the lead.
        
        :param lead_id: Lead ID.
        :param test_result: Value to be return in 'result' field when test mode is used.
        :param test_mode: 
        :param auto_start: 
        :param age: User age.
        :param country: User country code.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'leads.checkUser'
        param_aliases = []
        response_type = responses.LeadsCheckUser
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def complete(self, vk_sid: str = None, secret: str = None, comment: str = None) -> responses.LeadsComplete:
        """
        Completes the lead started by user.
        
        :param vk_sid: Session obtained as GET parameter when session started.
        :param secret: Secret key from the lead testing interface.
        :param comment: Comment text.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'leads.complete'
        param_aliases = []
        response_type = responses.LeadsComplete
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_stats(self, lead_id: int = None, secret: str = None, date_start: str = None, date_end: str = None) -> responses.LeadsGetStats:
        """
        Returns lead stats data.
        
        :param lead_id: Lead ID.
        :param secret: Secret key obtained from the lead testing interface.
        :param date_start: Day to start stats from (YYYY_MM_DD, e.g.2011-09-17).
        :param date_end: Day to finish stats (YYYY_MM_DD, e.g.2011-09-17).
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'leads.getStats'
        param_aliases = []
        response_type = responses.LeadsGetStats
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_users(self, offer_id: int = None, secret: str = None, offset: int = None, count: int = None, status: int = None, reverse: bool = None) -> responses.LeadsGetUsers:
        """
        Returns a list of last user actions for the offer.
        
        :param offer_id: Offer ID.
        :param secret: Secret key obtained in the lead testing interface.
        :param offset: Offset needed to return a specific subset of results.
        :param count: Number of results to return.
        :param status: Action type. Possible values: *'0' — start,, *'1' — finish,, *'2' — blocking users,, *'3' — start in a test mode,, *'4' — finish in a test mode.
        :param reverse: Sort order. Possible values: *'1' — chronological,, *'0' — reverse chronological.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'leads.getUsers'
        param_aliases = []
        response_type = responses.LeadsGetUsers
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def metric_hit(self, data: str = None) -> responses.LeadsMetricHit:
        """
        Counts the metric event.
        
        :param data: Metric data obtained in the lead interface.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'leads.metricHit'
        param_aliases = []
        response_type = responses.LeadsMetricHit
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def start(self, lead_id: int = None, secret: str = None, uid: int = None, aid: int = None, test_mode: bool = None, force: bool = None) -> responses.LeadsStart:
        """
        Creates new session for the user passing the offer.
        
        :param lead_id: Lead ID.
        :param secret: Secret key from the lead testing interface.
        :param uid: 
        :param aid: 
        :param test_mode: 
        :param force: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'leads.start'
        param_aliases = []
        response_type = responses.LeadsStart
        return self._call(method_name, method_parameters, param_aliases, response_type)

