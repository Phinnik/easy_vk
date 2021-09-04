import asyncio
import math
import time
from typing import List

import aiohttp

from easy_vk.settings import VK_API_URL, VK_API_VERSION


def get_items_packs(items: list, pack_size: int):
    items_packs = [items[i:i + pack_size] for i in range(0, len(items), pack_size)]
    return items_packs


class Parser:
    def __init__(self, access_tokens: List[str]):
        self._access_tokens = access_tokens
        self.current_response = None

    async def _execute(self, code: str, access_token: str):
        time_start = time.time()

        url = f'{VK_API_URL}/execute'
        params = {'access_token': access_token, 'v': VK_API_VERSION, 'code': code}
        async with aiohttp.ClientSession() as session:
            response = await session.post(url, params=params)
            response = await response.json()

        delay = 1 / 2.8 - (time.time() - time_start)
        if delay > 0:
            time.sleep(delay)
        if 'response' in response:
            return response['response']
        else:
            raise TimeoutError(response)

    async def _parse_single_pack(self, items_pack: list, parse_method, access_token: str, ):
        code = """
        var items = {};
        var i = 0;
        var result = [];
        
        while (i < 25 && i < items.length) {{
            var r = {};
            result = result + r;
            i = i + 1;
        }}
        return result;
        """.format(items_pack, parse_method)
        response = await self._execute(code, access_token)
        return response

    async def _parse_items(self, items: list, pack_size: int, parse_method: str, access_token: str):
        result = []
        items_packs = get_items_packs(items, pack_size)
        for items_pack in items_packs:
            r = await self._parse_single_pack(items_pack, parse_method, access_token)
            result.extend(r)
        return result

    def fast_items_parse(self, items: list, parse_method: str, pack_size: int = 25):
        items_per_acc = math.ceil(len(items) / len(self._access_tokens))
        accounts_items = get_items_packs(items, items_per_acc)

        loop = asyncio.get_event_loop()
        tasks = [
            loop.create_task(
                self._parse_items(ai, pack_size, parse_method, at)
            ) for ai, at in zip(accounts_items, self._access_tokens)
        ]

        loop.run_until_complete(asyncio.wait(tasks))
        # loop.close()

        result = []
        for t in tasks:
            result.extend(t.result())
        return result
