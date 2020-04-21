# easy_vk
Ну, что, пацаны, погнали.

## Оглавление
1. [Установка библиотеки](https://github.com/Phinnik/easy_vk#установка-библиотеки)
1. [Примеры спользования](https://github.com/Phinnik/easy_vk#Примеры-спользования)
    - [Для пользователя](https://github.com/Phinnik/easy_vk#Для-пользователя)
    - [Для ботов](https://github.com/Phinnik/easy_vk#Для-ботов)
1. [Планы на будущее](https://github.com/Phinnik/easy_vk#Планы-на-будущее)
1. [Мем](https://github.com/Phinnik/easy_vk#Мем)


### Установка библиотеки:
```shell script
pip install easy_vk
```

## Примеры спользования
### Для пользователей
```python
from easy_vk import VK

access_token = 'YOUR ACCESS_TOKEN'
vk = VK(access_token=access_token)
vk.friends_get(user_id=1, count=1)

# >>> {'count': 0, 'items': []} 
```

### Для ботов:
```python
# Пример простого эхобота

from easy_vk import Bot
import time

bot = Bot(access_token='GROUP ACCESS_TOKEN', group_id='GROUP_ID')

@bot.message_new_handler(regexp='^test$')
def test(message):
    bot.messages_send(user_id=message['from_id'], random_id=time.time(), message=message['test'])
    print(message)

bot.run()
```

## Планы по поводу этой библиотеки
- [ ] Зафигачить классные штуки дрюки для парсинга
- [ ] Намутить Сallback api
- [ ] Забабахать очень крутые приколямбы для чат-ботов
- [ ] Хорошенечко отдохнуть

## Мем
<img src="https://sun9-67.userapi.com/dUc3jo42I-uAB5m9pRNM37xDF3LtofvvnpQriw/sQkfjjtF0iI.jpg" width="60%">
