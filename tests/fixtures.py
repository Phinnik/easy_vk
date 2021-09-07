from unittest.mock import patch

import pytest

from easy_vk.bot import Bot


@pytest.fixture()
def bot_fixture():
    with patch('requests.Session.request') as mock_get:
        mock_get.return_value.json.return_value = {
            'response': {'key': 'test_key', 'server': 'test_server',
                         'ts': '22'}}

        return Bot('bot_access_token', 0)


@pytest.fixture()
def ping_data_fixture():
    return {'ts': '22', 'updates': [{'type': 'message_new', 'object': {
        'message': {'date': 1630797055, 'from_id': 505540783, 'id': 24, 'out': 0, 'peer_id': 505540783,
                    'text': 'Hello', 'conversation_message_id': 24, 'fwd_messages': [], 'important': False,
                    'random_id': 0, 'attachments': [], 'is_hidden': False}, 'client_info': {
            'button_actions': ['text', 'vkpay', 'open_app', 'location', 'open_link', 'callback', 'intent_subscribe',
                               'intent_unsubscribe'], 'keyboard': True, 'inline_keyboard': True, 'carousel': True,
            'lang_id': 0}}, 'group_id': 0, 'event_id': '554fb5408759e7cc793f20e871fedcc4833ce12f'}]}
