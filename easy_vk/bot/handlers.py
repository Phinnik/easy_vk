from typing import List, Callable, Sequence
from easy_vk.bot import update_types
import re


class UpdateHandlerBase:
    def __init__(self, update_type: str, update_object, filters: List[Callable], function: Callable):
        self.update_type = update_type
        self.update_object = update_object
        self.filters = filters
        self.function = function

    def check(self, update):
        if update['type'] != self.update_type:
            return False
        update = self.update_object(**update['object'])
        for f in self.filters:
            if not f(update):
                return False
        return True

    def handle(self, update):
        update = self.update_object(**update['object'])
        self.function(update)


class Handlers:
    def __init__(self):
        self._handler_list: List[UpdateHandlerBase] = []

    def message_new(self,
                    regexp: str = None,
                    user_id: int = None,
                    user_ids: List[int] = None,
                    user_black_list: List[int] = None):

        if user_id:
            user_ids = [user_id]

        def decorator(function):
            filters = []

            # adding filters
            if regexp:
                filters.append(lambda update: re.fullmatch(regexp, update.message.text, flags=re.MULTILINE))
            if user_ids:
                filters.append(lambda update: update.message.from_id in user_ids)
            if user_black_list:
                filters.append(lambda update: not update.message.from_id in user_black_list)

            self._handler_list.append(UpdateHandlerBase('message_new', update_types.MessageNew, filters, function))
            return function
        return decorator




    def _handle(self, update):
        for handler in self._handler_list:
            if handler.check(update):
                handler.handle(update)
