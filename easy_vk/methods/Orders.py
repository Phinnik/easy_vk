from _ApiMethod import ApiMethod
from typing import List


class Orders(ApiMethod):
    def __init__(self, session, access_token, v, requests_per_s):
        super().__init__(session, access_token, v, requests_per_s)

    def cancel_subscription(self, user_id: int, subscription_id: int, pending_cancel: bool = None):
        """
        
        :param user_id: 
        :param subscription_id: 
        :param pending_cancel: 
        """
    
        method_name = 'orders.cancelSubscription'
        return self.call(method_name, locals())

    def change_state(self, order_id: int, action: str, app_order_id: int = None, test_mode: bool = None):
        """
        Changes order status.
        
        :param order_id: order ID.
        :param action: action to be done with the order. Available actions: *cancel — to cancel unconfirmed order. *charge — to confirm unconfirmed order. Applies only if processing of [vk.com/dev/payments_status|order_change_state] notification failed. *refund — to cancel confirmed order.
        :param app_order_id: internal ID of the order in the application.
        :param test_mode: if this parameter is set to 1, this method returns a list of test mode orders. By default — 0.
        """
    
        method_name = 'orders.changeState'
        return self.call(method_name, locals())

    def get(self, offset: int = None, count: int = None, test_mode: bool = None):
        """
        Returns a list of orders.
        
        :param offset: 
        :param count: number of returned orders.
        :param test_mode: if this parameter is set to 1, this method returns a list of test mode orders. By default — 0.
        """
    
        method_name = 'orders.get'
        return self.call(method_name, locals())

    def get_amount(self, user_id: int, votes: List[str]):
        """
        
        :param user_id: 
        :param votes: 
        """
    
        if votes:
            votes = ','.join(votes)
        
        method_name = 'orders.getAmount'
        return self.call(method_name, locals())

    def get_by_id(self, order_id: int = None, order_ids: List[int] = None, test_mode: bool = None):
        """
        Returns information about orders by their IDs.
        
        :param order_id: order ID.
        :param order_ids: order IDs (when information about several orders is requested).
        :param test_mode: if this parameter is set to 1, this method returns a list of test mode orders. By default — 0.
        """
    
        if order_ids:
            order_ids = [str(o) for o in order_ids]
            order_ids = ','.join(order_ids)
        
        method_name = 'orders.getById'
        return self.call(method_name, locals())

    def get_user_subscription_by_id(self, user_id: int, subscription_id: int):
        """
        
        :param user_id: 
        :param subscription_id: 
        """
    
        method_name = 'orders.getUserSubscriptionById'
        return self.call(method_name, locals())

    def get_user_subscriptions(self, user_id: int):
        """
        
        :param user_id: 
        """
    
        method_name = 'orders.getUserSubscriptions'
        return self.call(method_name, locals())

    def update_subscription(self, user_id: int, subscription_id: int, price: int):
        """
        
        :param user_id: 
        :param subscription_id: 
        :param price: 
        """
    
        method_name = 'orders.updateSubscription'
        return self.call(method_name, locals())

