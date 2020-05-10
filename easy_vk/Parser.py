import threading
from typing import List
from .VK import VK
import concurrent.futures
import math


class Parser:
    """
    Класс для удобного парсинга данных
    """

    def __init__(self, vk_accounts: List[VK] = []):
        """
        :param vk_accounts: список классов VK. Нужен для парсинга несколькими аккаунтами.
        """

        self.accounts = vk_accounts

    @staticmethod
    def form_packs(items: list, pack_size: int = 25) -> List[list]:
        """
        Преобразует список items в список списков List[List], каждый длиной pack_size или меньше

        :param items: список объектов
        :param pack_size: размер внутренних массивов

        :example:
        >>> p = Parser()
        >>> p.form_packs([1,2,3,4,5], 2)
        [[1,2], [3,4], [5]]
        """

        packs = [items[i:i+pack_size] for i in range(0, len(items), pack_size)]
        return packs

    @staticmethod
    def _parse_one_pack(vk: VK, method: str, pack: list = []):
        code = '''var i = 0;
        var items = {};
        var result = [];
        
        while ((i < 25) && (i < items.length)) {{
            result = result + {};
            i = i + 1;
        }}
        return result;
        '''.format(pack, method)

        return vk.execute(code=code)

    def parse_single_iter(self, vk: VK, method: str, packs: List[list]):
        """
        Использует один аккаунт для парсинга

        :param vk: класс VK
        :param method:
        :param packs:
        :return:

        :example:
        >>> vk = VK('access_token')
        >>> p = Parser()
        >>> friends = vk.friends.get()['items']
        >>> packs = p.form_packs(friends, 25)
        >>> results = []
        >>> for r in p.parse_single_iter(vk, "API.friends.get('user_id': items[i])", packs):
        >>>     results.append(r)
        """
        for p in packs:
            yield self._parse_one_pack(vk, method, p)

    def parse_single(self, vk: VK, method: str, packs: List[list]):
        result = []
        for r in self.parse_single_iter(vk, method, packs):
            result.extend(r)
        return result

    def process_parsing(self, vk: VK, method: str, items: list, pack_size: int = 25):
        packs = self.form_packs(items, pack_size)
        result = self.parse_single(vk, method, packs)
        return result

    def parse_threaded(self, method, items: list, pack_size: int = 25):
        items_per_account = math.ceil(len(items) / len(self.accounts))
        account_items = [items[items_per_account*i:items_per_account*(i+1)] for i in range(len(self.accounts))]

        result = []

        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = [executor.submit(self.process_parsing,
                                       a,
                                       method,
                                       account_items[i],
                                       pack_size) for i, a in enumerate(self.accounts)]

        for f in concurrent.futures.as_completed(results):
            result.extend(f.result())

        return result

