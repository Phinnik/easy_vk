# easy_vk


### Установка библиотеки:
`pip install easy_vk`

### Использование
```python
from easy_vk.easy_vk import VK

access_token = 'YOUR ACCESS TOKEN'
vk = VK(access_token=access_token)
vk.friends_get(user_id=1, count=1)

# >>> {'count': 0, 'items': []} 
```
