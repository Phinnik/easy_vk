from _ApiMethod import ApiMethod
from typing import List


class Account(ApiMethod):
    def __init__(self, session, access_token, v, requests_per_s):
        super().__init__(session, access_token, v, requests_per_s)

    def ban(self, owner_id: int = None):
        """
        
        :param owner_id: 
        """
    
        method_name = 'account.ban'
        return self.call(method_name, locals())

    def change_password(self, new_password: str, restore_sid: str = None, change_password_hash: str = None, old_password: str = None):
        """
        Changes a user password after access is successfully restored with the [vk.com/dev/auth.restore|auth.restore] method.
        
        :param new_password: New password that will be set as a current
        :param restore_sid: Session id received after the [vk.com/dev/auth.restore|auth.restore] method is executed. (If the password is changed right after the access was restored)
        :param change_password_hash: Hash received after a successful OAuth authorization with a code got by SMS. (If the password is changed right after the access was restored)
        :param old_password: Current user password.
        """
    
        method_name = 'account.changePassword'
        return self.call(method_name, locals())

    def get_active_offers(self, offset: int = None, count: int = None):
        """
        Returns a list of active ads (offers) which executed by the user will bring him/her respective number of votes to his balance in the application.
        
        :param offset: 
        :param count: Number of results to return.
        """
    
        method_name = 'account.getActiveOffers'
        return self.call(method_name, locals())

    def get_app_permissions(self, user_id: int):
        """
        Gets settings of the user in this application.
        
        :param user_id: User ID whose settings information shall be got. By default: current user.
        """
    
        method_name = 'account.getAppPermissions'
        return self.call(method_name, locals())

    def get_banned(self, offset: int = None, count: int = None):
        """
        Returns a user's blacklist.
        
        :param offset: Offset needed to return a specific subset of results.
        :param count: Number of results to return.
        """
    
        method_name = 'account.getBanned'
        return self.call(method_name, locals())

    def get_counters(self, filter_: List[str] = None):
        """
        Returns non-null values of user counters.
        
        :param filter_: Counters to be returned.
        """
    
        if filter_:
            filter_ = ','.join(filter_)
        
        param_alias_dict = {'filter_': 'filter'}
        method_name = 'account.getCounters'
        return self.call(method_name, locals())

    def get_info(self, fields: List[str] = None):
        """
        Returns current account info.
        
        :param fields: Fields to return. Possible values: *'country' — user country,, *'https_required' — is "HTTPS only" option enabled,, *'own_posts_default' — is "Show my posts only" option is enabled,, *'no_wall_replies' — are wall replies disabled or not,, *'intro' — is intro passed by user or not,, *'lang' — user language. By default: all.
        """
    
        if fields:
            fields = ','.join(fields)
        
        method_name = 'account.getInfo'
        return self.call(method_name, locals())

    def get_profile_info(self):
        """
        Returns the current account info.
        
        """
    
        method_name = 'account.getProfileInfo'
        return self.call(method_name, locals())

    def get_push_settings(self, device_id: str = None):
        """
        Gets settings of push notifications.
        
        :param device_id: Unique device ID.
        """
    
        method_name = 'account.getPushSettings'
        return self.call(method_name, locals())

    def register_device(self, token: str, device_id: str, device_model: str = None, device_year: int = None, system_version: str = None, settings: str = None, sandbox: bool = None):
        """
        Subscribes an iOS/Android/Windows Phone-based device to receive push notifications
        
        :param token: Device token used to send notifications. (for mpns, the token shall be URL for sending of notifications)
        :param device_id: Unique device ID.
        :param device_model: String name of device model.
        :param device_year: Device year.
        :param system_version: String version of device operating system.
        :param settings: Push settings in a [vk.com/dev/push_settings|special format].
        :param sandbox: 
        """
    
        method_name = 'account.registerDevice'
        return self.call(method_name, locals())

    def save_profile_info(self, first_name: str = None, last_name: str = None, maiden_name: str = None, screen_name: str = None, cancel_request_id: int = None, sex: int = None, relation: int = None, relation_partner_id: int = None, bdate: str = None, bdate_visibility: int = None, home_town: str = None, country_id: int = None, city_id: int = None, status: str = None):
        """
        Edits current profile info.
        
        :param first_name: User first name.
        :param last_name: User last name.
        :param maiden_name: User maiden name (female only)
        :param screen_name: User screen name.
        :param cancel_request_id: ID of the name change request to be canceled. If this parameter is sent, all the others are ignored.
        :param sex: User sex. Possible values: , * '1' – female,, * '2' – male.
        :param relation: User relationship status. Possible values: , * '1' – single,, * '2' – in a relationship,, * '3' – engaged,, * '4' – married,, * '5' – it's complicated,, * '6' – actively searching,, * '7' – in love,, * '0' – not specified.
        :param relation_partner_id: ID of the relationship partner.
        :param bdate: User birth date, format: DD.MM.YYYY.
        :param bdate_visibility: Birth date visibility. Returned values: , * '1' – show birth date,, * '2' – show only month and day,, * '0' – hide birth date.
        :param home_town: User home town.
        :param country_id: User country.
        :param city_id: User city.
        :param status: Status text.
        """
    
        method_name = 'account.saveProfileInfo'
        return self.call(method_name, locals())

    def set_info(self, name: str = None, value: str = None):
        """
        Allows to edit the current account info.
        
        :param name: Setting name.
        :param value: Setting value.
        """
    
        method_name = 'account.setInfo'
        return self.call(method_name, locals())

    def set_name_in_menu(self, user_id: int, name: str = None):
        """
        Sets an application screen name (up to 17 characters), that is shown to the user in the left menu.
        
        :param user_id: User ID.
        :param name: Application screen name.
        """
    
        method_name = 'account.setNameInMenu'
        return self.call(method_name, locals())

    def set_offline(self):
        """
        Marks a current user as offline.
        
        """
    
        method_name = 'account.setOffline'
        return self.call(method_name, locals())

    def set_online(self, voip: bool = None):
        """
        Marks the current user as online for 15 minutes.
        
        :param voip: '1' if videocalls are available for current device.
        """
    
        method_name = 'account.setOnline'
        return self.call(method_name, locals())

    def set_push_settings(self, device_id: str, settings: str = None, key: str = None, value: List[str] = None):
        """
        Change push settings.
        
        :param device_id: Unique device ID.
        :param settings: Push settings in a [vk.com/dev/push_settings|special format].
        :param key: Notification key.
        :param value: New value for the key in a [vk.com/dev/push_settings|special format].
        """
    
        if value:
            value = ','.join(value)
        
        method_name = 'account.setPushSettings'
        return self.call(method_name, locals())

    def set_silence_mode(self, device_id: str = None, time: int = None, peer_id: int = None, sound: int = None):
        """
        Mutes push notifications for the set period of time.
        
        :param device_id: Unique device ID.
        :param time: Time in seconds for what notifications should be disabled. '-1' to disable forever.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'Chat ID', e.g. '2000000001'. For community: '- Community ID', e.g. '-12345'. "
        :param sound: '1' — to enable sound in this dialog, '0' — to disable sound. Only if 'peer_id' contains user or community ID.
        """
    
        method_name = 'account.setSilenceMode'
        return self.call(method_name, locals())

    def unban(self, owner_id: int = None):
        """
        
        :param owner_id: 
        """
    
        method_name = 'account.unban'
        return self.call(method_name, locals())

    def unregister_device(self, device_id: str = None, sandbox: bool = None):
        """
        Unsubscribes a device from push notifications.
        
        :param device_id: Unique device ID.
        :param sandbox: 
        """
    
        method_name = 'account.unregisterDevice'
        return self.call(method_name, locals())

