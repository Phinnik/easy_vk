class UpdateHandler:
    def __init__(self, update_type, filters, function, handled_object_type=None):
        self.update_type = update_type  # str of update type
        self.filters = filters          # list of lambda functions
        self.function = function        # function which will be executed if handler is triggered
        self.handled_object_type = handled_object_type

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
