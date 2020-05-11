import threading
from typing import List
import asyncio
import aiohttp
import time
import math


class Parser:
    """
    Класс для удобного парсинга данных
    """

    def __init__(self, tokens: List[str], v='5.101'):
        self.tokens = tokens
        self.v = v

    async def call(self, token, code):
        ts = time.time()

        url = 'https://api.vk.com/method/execute'
        params = {'access_token': token, 'code': code, 'v': self.v}
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, params=params) as resp:
                response = await resp.json()

        delay = 1 / 2.9 - (time.time() - ts)
        if delay > 0:
            await asyncio.sleep(delay)
        return response['response']

    async def parse_pack(self, token, method, pack):
        code = """var items = {};
        var i = 0;
        var result = [];
        while ((i < 25) && (i < items.length)) {{
            result = result + {};
            i = i + 1;
        }}
        return result;
        """.format(pack, method)
        return await self.call(token, code)

    def form_packs(self, items, pack_size=25):
        packs = [items[i:i+pack_size] for i in range(0, len(items), pack_size)]
        return packs

    async def parse_items(self, token, method, items):
        packs = self.form_packs(items)
        result = []
        for p in packs:
            r = await self.parse_pack(token, method, p)
            result.extend(r)
        return result

    def parse(self, method, items):
        items_per_acc = math.ceil(len(items) / len(self.tokens))
        account_items = [items[i:i+items_per_acc] for i in range(0, len(items), items_per_acc)]


        ioloop = asyncio.new_event_loop()
        tasks = [ioloop.create_task(self.parse_items(t, method, i)) for t, i in zip(self.tokens, account_items)]
        ioloop.run_until_complete(asyncio.wait(tasks))
        ioloop.close()

        result = []
        for t in tasks:
            result.extend(t.result())
        return result
