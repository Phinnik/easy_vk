from _ApiMethod import ApiMethod
from typing import List


class Secure(ApiMethod):
    def __init__(self, session, access_token, v, requests_per_s):
        super().__init__(session, access_token, v, requests_per_s)

    def add_app_event(self, user_id: int, activity_id: int, value: int = None):
        """
        Adds user activity information to an application
        
        :param user_id: ID of a user to save the data
        :param activity_id: there are 2 default activities: , * 1 – level. Works similar to ,, * 2 – points, saves points amount, Any other value is for saving completed missions
        :param value: depends on activity_id: * 1 – number, current level number,, * 2 – number, current user's points amount, , Any other value is ignored
        """
    
        method_name = 'secure.addAppEvent'
        return self.call(method_name, locals())

    def check_token(self, token: str = None, ip: str = None):
        """
        Checks the user authentication in 'IFrame' and 'Flash' apps using the 'access_token' parameter.
        
        :param token: client 'access_token'
        :param ip: user 'ip address'. Note that user may access using the 'ipv6' address, in this case it is required to transmit the 'ipv6' address. If not transmitted, the address will not be checked.
        """
    
        method_name = 'secure.checkToken'
        return self.call(method_name, locals())

    def get_app_balance(self):
        """
        Returns payment balance of the application in hundredth of a vote.
        
        """
    
        method_name = 'secure.getAppBalance'
        return self.call(method_name, locals())

    def get_sm_shistory(self, user_id: int = None, date_from: int = None, date_to: int = None, limit: int = None):
        """
        Shows a list of SMS notifications sent by the application using [vk.com/dev/secure.sendSMSNotification|secure.sendSMSNotification] method.
        
        :param user_id: 
        :param date_from: filter by start date. It is set as UNIX-time.
        :param date_to: filter by end date. It is set as UNIX-time.
        :param limit: number of returned posts. By default — 1000.
        """
    
        method_name = 'secure.getSMSHistory'
        return self.call(method_name, locals())

    def get_transactions_history(self, type_: int = None, uid_from: int = None, uid_to: int = None, date_from: int = None, date_to: int = None, limit: int = None):
        """
        Shows history of votes transaction between users and the application.
        
        :param type_: 
        :param uid_from: 
        :param uid_to: 
        :param date_from: 
        :param date_to: 
        :param limit: 
        """
    
        param_alias_dict = {'type_': 'type'}
        method_name = 'secure.getTransactionsHistory'
        return self.call(method_name, locals())

    def get_user_level(self, user_ids: List[int]):
        """
        Returns one of the previously set game levels of one or more users in the application.
        
        :param user_ids: 
        """
    
        if user_ids:
            user_ids = [str(u) for u in user_ids]
            user_ids = ','.join(user_ids)
        
        method_name = 'secure.getUserLevel'
        return self.call(method_name, locals())

    def give_event_sticker(self, user_ids: List[int], achievement_id: int):
        """
        Opens the game achievement and gives the user a sticker
        
        :param user_ids: 
        :param achievement_id: 
        """
    
        if user_ids:
            user_ids = [str(u) for u in user_ids]
            user_ids = ','.join(user_ids)
        
        method_name = 'secure.giveEventSticker'
        return self.call(method_name, locals())

    def send_notification(self, message: str, user_ids: List[int] = None, user_id: int = None):
        """
        Sends notification to the user.
        
        :param message: notification text which should be sent in 'UTF-8' encoding ('254' characters maximum).
        :param user_ids: 
        :param user_id: 
        """
    
        if user_ids:
            user_ids = [str(u) for u in user_ids]
            user_ids = ','.join(user_ids)
        
        method_name = 'secure.sendNotification'
        return self.call(method_name, locals())

    def send_sm_snotification(self, user_id: int, message: str):
        """
        Sends 'SMS' notification to a user's mobile device.
        
        :param user_id: ID of the user to whom SMS notification is sent. The user shall allow the application to send him/her notifications (, +1).
        :param message: 'SMS' text to be sent in 'UTF-8' encoding. Only Latin letters and numbers are allowed. Maximum size is '160' characters.
        """
    
        method_name = 'secure.sendSMSNotification'
        return self.call(method_name, locals())

    def set_counter(self, counters: List[str] = None, user_id: int = None, counter: int = None, increment: bool = None):
        """
        Sets a counter which is shown to the user in bold in the left menu.
        
        :param counters: 
        :param user_id: 
        :param counter: counter value.
        :param increment: 
        """
    
        if counters:
            counters = ','.join(counters)
        
        method_name = 'secure.setCounter'
        return self.call(method_name, locals())

