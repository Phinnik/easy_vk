from typing import List, Union, Optional
from easy_vk.types import objects, responses
from .base import BaseCategory


class Orders(BaseCategory):
    def __init__(self, session, access_token: str, v: str, delay: float, auto_retry: bool, max_retries: int, timeout: float):
        super().__init__(session, access_token, v, delay, auto_retry, max_retries, timeout)

    def cancel_subscription(self, user_id: int = None, subscription_id: int = None, pending_cancel: bool = None) -> responses.OrdersCancelSubscription:
        """
        :param user_id: 
        :param subscription_id: 
        :param pending_cancel: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'orders.cancelSubscription'
        param_aliases = []
        response_type = responses.OrdersCancelSubscription
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def change_state(self, order_id: int = None, action: str = None, app_order_id: int = None, test_mode: bool = None) -> responses.OrdersChangeState:
        """
        Changes order status.
        
        :param order_id: order ID.
        :param action: action to be done with the order. Available actions: *cancel — to cancel unconfirmed order. *charge — to confirm unconfirmed order. Applies only if processing of [vk.com/dev/payments_status|order_change_state] notification failed. *refund — to cancel confirmed order.
        :param app_order_id: internal ID of the order in the application.
        :param test_mode: if this parameter is set to 1, this method returns a list of test mode orders. By default — 0.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'orders.changeState'
        param_aliases = []
        response_type = responses.OrdersChangeState
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get(self, offset: int = None, count: int = None, test_mode: bool = None) -> responses.OrdersGet:
        """
        Returns a list of orders.
        
        :param offset: 
        :param count: number of returned orders.
        :param test_mode: if this parameter is set to 1, this method returns a list of test mode orders. By default — 0.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'orders.get'
        param_aliases = []
        response_type = responses.OrdersGet
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_amount(self, user_id: int = None, votes: List[str] = None) -> responses.OrdersGetAmount:
        """
        :param user_id: 
        :param votes: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'orders.getAmount'
        param_aliases = []
        response_type = responses.OrdersGetAmount
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_by_id(self, order_id: int = None, order_ids: List[int] = None, test_mode: bool = None) -> responses.OrdersGetById:
        """
        Returns information about orders by their IDs.
        
        :param order_id: order ID.
        :param order_ids: order IDs (when information about several orders is requested).
        :param test_mode: if this parameter is set to 1, this method returns a list of test mode orders. By default — 0.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'orders.getById'
        param_aliases = []
        response_type = responses.OrdersGetById
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_user_subscription_by_id(self, user_id: int = None, subscription_id: int = None) -> responses.OrdersGetUserSubscriptionById:
        """
        :param user_id: 
        :param subscription_id: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'orders.getUserSubscriptionById'
        param_aliases = []
        response_type = responses.OrdersGetUserSubscriptionById
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_user_subscriptions(self, user_id: int = None) -> responses.OrdersGetUserSubscriptions:
        """
        :param user_id: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'orders.getUserSubscriptions'
        param_aliases = []
        response_type = responses.OrdersGetUserSubscriptions
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def update_subscription(self, user_id: int = None, subscription_id: int = None, price: int = None) -> responses.OrdersUpdateSubscription:
        """
        :param user_id: 
        :param subscription_id: 
        :param price: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'orders.updateSubscription'
        param_aliases = []
        response_type = responses.OrdersUpdateSubscription
        return self._call(method_name, method_parameters, param_aliases, response_type)

