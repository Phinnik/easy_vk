# easy_vk


### Установка библиотеки:
`pip install easy_vk`

### Использование
```python
from easy_vk.easy_vk import VK

access_token = 'YOUR ACCESS_TOKEN'
vk = VK(access_token=access_token)
vk.friends_get(user_id=1, count=1)

# >>> {'count': 0, 'items': []} 
```

### Использование для ботов:
```python
# Пример простого эхобота

from easy_vk.bots import Bot
import time

bot = Bot(access_token='GROUP ACCESS_TOKEN', group_id='GROUP_ID')

@bot.message_new_handler('test')
def test(message):
    bot.messages_send(user_id=message['from_id'], random_id=time.time(), message=message['test'])
    print(message)
```

## Планы по поводу этой библиотеки
- [x] Cделать то
- [ ] Cделать се
- [ ] Cделать то самое
- [ ] Cделать это самое

