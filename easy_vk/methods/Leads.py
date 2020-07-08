from ._ApiMethod import ApiMethod
from typing import List


class Leads(ApiMethod):
    def __init__(self, session, access_token, v, requests_per_s):
        super().__init__(session, access_token, v, requests_per_s)

    def check_user(self, lead_id: int, test_result: int = None, test_mode: bool = None, auto_start: bool = None, age: int = None, country: str = None):
        """
        Checks if the user can start the lead.
        
        :param lead_id: Lead ID.
        :param test_result: Value to be return in 'result' field when test mode is used.
        :param test_mode: 
        :param auto_start: 
        :param age: User age.
        :param country: User country code.
        """
    
        method_name = 'leads.checkUser'
        return self._call(method_name, locals())

    def complete(self, vk_sid: str, secret: str, comment: str = None):
        """
        Completes the lead started by user.
        
        :param vk_sid: Session obtained as GET parameter when session started.
        :param secret: Secret key from the lead testing interface.
        :param comment: Comment text.
        """
    
        method_name = 'leads.complete'
        return self._call(method_name, locals())

    def get_stats(self, lead_id: int, secret: str = None, date_start: str = None, date_end: str = None):
        """
        Returns lead stats data.
        
        :param lead_id: Lead ID.
        :param secret: Secret key obtained from the lead testing interface.
        :param date_start: Day to start stats from (YYYY_MM_DD, e.g.2011-09-17).
        :param date_end: Day to finish stats (YYYY_MM_DD, e.g.2011-09-17).
        """
    
        method_name = 'leads.getStats'
        return self._call(method_name, locals())

    def get_users(self, offer_id: int, secret: str, offset: int = None, count: int = None, status: int = None, reverse: bool = None):
        """
        Returns a list of last user actions for the offer.
        
        :param offer_id: Offer ID.
        :param secret: Secret key obtained in the lead testing interface.
        :param offset: Offset needed to return a specific subset of results.
        :param count: Number of results to return.
        :param status: Action type. Possible values: *'0' — start,, *'1' — finish,, *'2' — blocking users,, *'3' — start in a test mode,, *'4' — finish in a test mode.
        :param reverse: Sort order. Possible values: *'1' — chronological,, *'0' — reverse chronological.
        """
    
        method_name = 'leads.getUsers'
        return self._call(method_name, locals())

    def metric_hit(self, data: str):
        """
        Counts the metric event.
        
        :param data: Metric data obtained in the lead interface.
        """
    
        method_name = 'leads.metricHit'
        return self._call(method_name, locals())

    def start(self, lead_id: int, secret: str, uid: int = None, aid: int = None, test_mode: bool = None, force: bool = None):
        """
        Creates new session for the user passing the offer.
        
        :param lead_id: Lead ID.
        :param secret: Secret key from the lead testing interface.
        :param uid: 
        :param aid: 
        :param test_mode: 
        :param force: 
        """
    
        method_name = 'leads.start'
        return self._call(method_name, locals())

