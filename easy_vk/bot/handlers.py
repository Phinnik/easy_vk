import re
from ..objects.objects import BotMessage


class UpdateHandler:
    def __init__(self,
                 update_type: str,
                 filters,
                 function,
                 handled_object_type=None,
                 handler_name: str = None):

        self.update_type = update_type  # str of update type
        self.filters = filters  # list of lambda functions
        self.function = function  # function which will be executed if handler is triggered
        self.handled_object_type = handled_object_type
        self.handler_name = handler_name

    def is_triggered(self, update):
        """ checks all handler filters """
        if update['type'] != self.update_type:
            return False

        handled_object = update['object']
        for f in self.filters:
            if not f(handled_object):
                return False

        return True

    def handle(self, handled_object):
        self.function(handled_object)

    def notify(self, update, handled_object_type=None):
        if self.is_triggered(update):
            handled_object = update['object']
            if self.handled_object_type:
                handled_object = self.handled_object_type(**handled_object)
            self.handle(handled_object)


class Handlers:
    def __init__(self, debug_mode: bool, owner_id: int):
        self._debug_mode = debug_mode
        self._owner_id = owner_id
        self._handlers_list = []

    def message_new(self,
                    regexp: str = None,
                    user_id: int = None,
                    user_ids: int = None,
                    attachment_type: str = None):

        if self._debug_mode:
            user_id = self._owner_id

        def decorator(function):
            update_type = 'message_new'
            filters = []
            if regexp:
                filters.append(lambda x: True if re.fullmatch(regexp, x['message'].get('text', '')) else False)
            if user_id:
                filters.append(lambda x: x['message']['from_id'] == user_id)
            if user_ids:
                filters.append(lambda x: x['message']['from_id'] in user_ids)
            if attachment_type:
                filters.append(lambda x: attachment_type in [a['type'] for a in x['message']['attachments']])

            handler = UpdateHandler(update_type, filters, function, handled_object_type=BotMessage)
            self._handlers_list.append(handler)
            return function

        return decorator

    def message_typing_state(self,
                             user_id: int = None,
                             user_ids=None):

        if self._debug_mode:
            user_id = self._owner_id

        def decorator(function):
            update_type = 'message_typing_state'
            filters = []
            if user_id:
                filters.append(lambda x: x['from_id'] == user_id)
            if user_ids:
                filters.append(lambda x: x['from_id'] in user_ids)

            handler = UpdateHandler(update_type, filters, function)
            self._handlers_list.append(handler)
            return function

        return decorator

    def group_leave(self,
                    user_id: int = None,
                    user_ids: int = None,
                    self_: bool = None):

        if self._debug_mode:
            user_id = self._owner_id

        def decorator(function):
            update_type = 'group_leave'
            filters = []
            if user_id:
                filters.append(lambda x: x['user_id'] == user_id)
            if user_ids:
                filters.append(lambda x: x['user_id'] in user_ids)
            if self_ is not None:
                filters.append(lambda x: x['self'] == self_)

            handler = UpdateHandler(update_type, filters, function)
            self._handlers_list.append(handler)
            return function

        return decorator

    def group_join(self,
                   user_id: int = None,
                   user_ids: int = None,
                   join_type: bool = None):

        if self._debug_mode:
            user_id = self._owner_id

        def decorator(function):
            update_type = 'group_join'
            filters = []
            if user_id:
                filters.append(lambda x: x['user_id'] == user_id)
            if user_ids:
                filters.append(lambda x: x['user_id'] in user_ids)
            if join_type:
                filters.append(lambda x: x['join_type'] == join_type)

            handler = UpdateHandler(update_type, filters, function)
            self._handlers_list.append(handler)
            return function

        return decorator
