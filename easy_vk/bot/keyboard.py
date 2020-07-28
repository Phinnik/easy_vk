from typing import List
from enum import Enum
import json


class ActionType(Enum):
    TEXT = 'text'
    OPEN_LINK = 'open_link'
    LOCATION = 'location'
    VKPAY = 'vkpay'
    OPEN_APP = 'open_app'
    CALLBACK = 'callback'


class Action:
    def __init__(self, type_: ActionType, label: str = None, link: str = None, payload: str = None, app_id: int = None,
                 owner_id: int = None, hash_: str = None):

        if type_ == ActionType.TEXT:
            assert label is not None
        elif type_ == ActionType.OPEN_LINK:
            assert label is not None
            assert link is not None
        elif type_ == ActionType.LOCATION:
            pass
        elif type_ == ActionType.VKPAY:
            assert hash_ is not None
        elif type_ == ActionType.OPEN_APP:
            assert app_id is not None
            assert label is not None
        elif type_ == ActionType.CALLBACK:
            assert label is not None

        self.type = type_
        self.label = label
        self.link = link
        self.payload = payload
        self.app_id = app_id
        self.owner_id = owner_id
        self.hash = hash_

    def generate(self):
        action_dict = {k: v for k, v in self.__dict__.items() if v}
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

    def generate(self):
        button_dict = {'action': self.action.generate()}
        if self.color:
            button_dict['color'] = self.color.value
        return button_dict

    @classmethod
    def from_template(cls, tmpl: str):
        parameters = tmpl.replace('||', '').split('|')
        action_dict = {'type_': parameters[0]}
        color = None

        for p in parameters[1:]:
            key, value = p.split('::')
            if key == 'color':
                color = Color(value)
            else:
                action_dict[key] = value

        action = Action(**action_dict)
        return cls(action, color)


class Row:
    def __init__(self, buttons: List[Button]):
        self.buttons = buttons

    def add_button(self, button: Button):
        self.buttons.append(button)

    def generate(self):
        return [b.generate() for b in self.buttons]

    @classmethod
    def from_template(cls, row: str):
        buttons = [Button.from_template(b) for b in row.split('  ')]
        return cls(buttons)


class Keyboard:
    def __init__(self, one_time: bool = False, inline: bool = False, rows: List[Row] = None):
        self.one_time = one_time
        self.inline = inline
        self.rows = rows

    def to_json(self):
        keyboard_dict = {'buttons': [r.generate() for r in self.rows]}
        if self.one_time:
            keyboard_dict['one_time'] = True
        if self.inline:
            keyboard_dict['inline'] = True

        return json.dumps(keyboard_dict)

    @classmethod
    def from_template(cls, tmpl: str):
        tmpl_rows = tmpl.split('\n')

        one_time = False
        inline = False

        if 'one_time' in tmpl_rows[0]:
            one_time = True
        if 'inline' in tmpl_rows[0]:
            inline = True

        rows = [Row.from_template(r) for r in tmpl_rows[2:] if r]

        return cls(one_time, inline, rows)

# template = """one_time
# ___
# ||open_link|link::https://www.youtube.com/watch?v=LMkwooZ8-dE||  ||text|label::Hello, world!|color::negative||
# ||location||
# """
#
#
# kb = Keyboard.from_template(template).to_json()
# print(kb)
