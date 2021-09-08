from unittest.mock import patch


def test_get_new_message(bot_fixture, ping_data_fixture):
    with patch('requests.Session.request') as mock_get:
        mock_get.return_value.json.return_value = ping_data_fixture

        @bot_fixture.handler.message_new()
        def response(message):
            assert message.message.text == 'Hello'

        # костыль для перехватывания ровно одного события
        for update in bot_fixture._longpoll.run():
            bot_fixture.handler.handle(update)
            return
