# -*- coding: utf-8 -*-

def get_update_type(update):
    update_type = update.get('type')
    if update_type in ['message_new', 'message_reply']:
        return Message(update['object'], update_type)
    if update_type == 'message_typing_state':
        return Message_typing_state(update['object'])
    else:
        print(update)


class Message:
    def __init__(self, j, type):
        self.type = type
        self.date = j.get('date')
        self.from_id = j.get('from_id')
        self.id = j.get('id')
        self.out = j.get('out')
        self.peer_id = j.get('peer_id')
        self.text = j.get('text')
        self.conversation_message_id = j.get('conversation_message_id')
        self.fwd_messages = j.get('fwd_messages')
        self.important = j.get('important')
        self.random_id = j.get('random_id')
        self.attachments = j.get('attachments')
        self.is_hidden = j.get('is_hidden')
        self.event_id = j.get('event_id')
        self.geo = j.get('geo')
        self.keyboard = j.get('keyboard')
        self.action = j.get('action')
        self.group_id = j.get('group_id')

    def __repr__(self):
        string = '___Message___\nfrom_id: {}\ntext: {}\nattachments: {}\ngeo: {}'.format(self.from_id, self.text,
                                                                                         self.attachments, self.geo)
        return string


class Message_typing_state:
    def __init__(self, j):
        self.type = 'typing_state'
        self.state = j.get('state')
        self.from_id = j.get('from_id')
        self.to_id = j.get('to_id')
        self.group_id = j.get('group_id')
        self.event_id = j.get('event_id')


#####################

def get_attachment_type(attachment):
    attachment_type = attachment.get('type')
    if attachment_type == 'photo':
        return Photo(attachment['photo'])


class Photo:
    def __init__(self, photo):
        pass
