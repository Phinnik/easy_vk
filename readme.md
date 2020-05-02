# easy_vk
Ну, что, пацаны, погнали.

## Оглавление
1. [Установка библиотеки](https://github.com/Phinnik/easy_vk#установка-библиотеки)
1. [Примеры спользования](https://github.com/Phinnik/easy_vk#Примеры-спользования)
    - [Для пользователей](https://github.com/Phinnik/easy_vk#Для-пользователей)
    - [Для ботов](https://github.com/Phinnik/easy_vk#Для-ботов)
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

## Планы на будущее
- [ ] Сделать аннотирование типов
- [ ] Написать классы для объектов
- [ ] Написать классы для медиа
- [ ] Зафигачить классные штуки дрюки для парсинга
- [ ] Намутить штуки для ботов
- [ ] Хорошенечко отдохнуть

## Мем
<img src="https://sun9-67.userapi.com/dUc3jo42I-uAB5m9pRNM37xDF3LtofvvnpQriw/sQkfjjtF0iI.jpg" width="60%">
