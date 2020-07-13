# easy_vk
Библиотека в стадии разработки

## Оглавление
1. [Установка библиотеки](https://github.com/Phinnik/easy_vk#установка-библиотеки)
1. [Примеры использования](https://github.com/Phinnik/easy_vk#Примеры-использования)
    - [Для пользователей](https://github.com/Phinnik/easy_vk#Для-пользователей)
    - [Для ботов](https://github.com/Phinnik/easy_vk#Для-ботов)
1. [Планы на будущее](https://github.com/Phinnik/easy_vk#Планы-на-будущее)


## Установка библиотеки:
```shell script
pip install easy_vk
```

## Примеры использования
### Для пользователей
```python

from easy_vk import User

access_token = 'YOUR ACCESS_TOKEN'
vk = User(access_token=access_token)
vk.friends.get(user_id=1, count=1)

# >>> {'count': 0, 'items': []} 
```

### Для ботов:
```python

import time
from easy_vk.bot import GroupBot
from easy_vk.objects.objects import BotMessage

bot = GroupBot(owner_access_token='owner_access_token', 
               group_access_token='group_access_token',
               group_id=1, 
               debug_mode=True, 
               owner_id=1)

@bot.handlers.message_new(regexp='Hello')
def response(message: BotMessage):
    bot.messages.send(user_id = message.message.from_id,
                     message = 'world',
                     random_id = time.time())

bot.run()
```


## Планы на будущее
- [ ] Создание модуля для парсинга данных
- [ ] Типизация данных VK API
- [ ] Типизация ответов VK API
- [ ] Создание модуля базы данных
- [ ] Создание модуля для ботов
- [ ] Написание документации
- [ ] Логирование каждого модуля
- [ ] Написание полезных утилит

