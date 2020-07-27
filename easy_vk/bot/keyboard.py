from typing import List
from enum import Enum
import json


class Action:
    def __init__(self, type_: str, label: str = None, link: str = None, payload: str = None, app_id: int = None,
                 owner_id: int = None, hash_: str = None):

        assert type_ in ['text', 'open_link', 'location', 'vkpay', 'open_app', 'callback']
        if type_ == 'text':
            assert label is not None
        elif type_ == 'open_link':
            assert label is not None
            assert link is not None
        elif type_ == 'location':
            pass
        elif type_ == 'vkpay':
            assert hash_ is not None
        elif type_ == 'open_app':
            assert app_id is not None
            assert label is not None
        elif type_ == 'callback':
            assert label is not None

        self.type = type_
        self.label = label
        self.link = link
        self.payload = payload
        self.app_id = app_id
        self.owner_id = owner_id
        self.hash = hash_

    def to_json(self):
        action_dict = {k:v for k, v in self.__dict__.items() if v}
        return action_dict



class Color(Enum):
    PRIMARY = 'primary'
    SECONDARY = 'secondary'
    NEGATIVE = 'negative'
    POSITIVE = 'positive'


class Button:
    def __init__(self, action: Action, color: Color = None):
        self.action = action
        self.color = color

    def to_json(self):
        button_dict = {'color': self.color.value,
                       'action': self.action.to_json()}
        return button_dict


class Keyboard:
    def __init__(self, one_time: bool = False, inline: bool = False, buttons: List[List[Button]] = None):
        self.one_time = one_time
        self.inline = inline
        self.buttons = buttons

    def add_button(self, button):
        pass

    def to_json(self):
        button_dict = dict()

        button_dict.update({'one_time': True})
        if self.inline:
            button_dict.update({'inline': True})
        button_dict['buttons'] = [[b.to_json() for b in row] for row in self.buttons]
        return json.dumps(button_dict)
