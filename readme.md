# easy_vk
Ну, что, пацаны, погнали.

## Оглавление
1. [Установка библиотеки](https://github.com/Phinnik/easy_vk#установка-библиотеки)
1. [Примеры спользования](https://github.com/Phinnik/easy_vk#Примеры-спользования)
    - [Для пользователей](https://github.com/Phinnik/easy_vk#Для-пользователей)
    - [Для ботов](https://github.com/Phinnik/easy_vk#Для-ботов)
    - [Для парсина](https://github.com/Phinnik/easy_vk#Для-парсинга)
1. [Планы на будущее](https://github.com/Phinnik/easy_vk#Планы-на-будущее)
1. [Мем](https://github.com/Phinnik/easy_vk#Мем)


## Установка библиотеки:
```shell script
pip install easy_vk
```

## Примеры спользования
### Для пользователей
```python
from easy_vk import VK

access_token = 'YOUR ACCESS_TOKEN'
vk = VK(access_token=access_token)
vk.friends.get(user_id=1, count=1)

# >>> {'count': 0, 'items': []} 
```

### Для ботов:
```python
# Модуль для ботов удален из-за угрозы восстания машин
"""
Прошу прощения за неудобства у всех людей, коих бесчисленное 
количество, за предоставленные неудобства
""" 
```

### Для парсинга:
#### Получение словаря друзей своих друзей
```python
# Быстро получить всех друзей своих друзей:

from easy_vk import VK, Parser


vk = VK(access_token='YOUR ACCESS_TOKEN')
parser = Parser()
my_friends = vk.friends.get()['items']
parsing_method = '[API.friends.get({"user_id": items[i]})["items"]]'
friends_friends = parser.process_parsing(vk, parsing_method, my_friends)
friends_friends = {friend: friends_friends[i] for i, friend in enumerate(my_friends)}

"""
friends_friends = {
    123: [1, 234, 453234, ... ],
    14543: [23, 5543],
    ...
}
"""
```

#### Получение всех участников группы с помощью нескольких аккаунтов
```python
# Быстро получить всех участников группы с помощью нескольких аккаунтов

from easy_vk import VK, Parser

vk = VK('ACCESS_TOKEN_1')
vk1 = VK('ACCESS_TOKEN_2')

parser = Parser([vk, vk1])
group_members_count = vk.groups.getMembers(group_id=84926122)['count']
offsets = list(range(0, group_members_count, 1000))
parsing_method = 'API.groups.getMembers({"group_id": 84926122, "count": 1000, "offset": items[i]})["items"]'
group_members = parser.parse_threaded(parsing_method, offsets)

# group_members = [1, 223434, 2341, 23432, ...]
# group_members_count = 233677
```

## Планы на будущее
- [ ] Сделать аннотирование типов
- [ ] Написать классы для объектов
- [ ] Написать классы для медиа
- [x] Зафигачить классные штуки дрюки для парсинга
- [ ] Намутить штуки для ботов
- [ ] Хорошенечко отдохнуть

## Мем
<img src="https://sun9-67.userapi.com/dUc3jo42I-uAB5m9pRNM37xDF3LtofvvnpQriw/sQkfjjtF0iI.jpg" width="60%">
