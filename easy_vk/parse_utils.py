from .easy_vk import VK
from . import api_utils


class Parser:
    def __init__(self, vk: VK):
        self.vk = vk

    def form_packs(self, items, pack_len=20):
        packs = [items[i:i + pack_len] for i in range(0, len(items), pack_len)]
        return packs

    @api_utils.delay
    def execute_from_pack(self, pack, method):
        code = """
        var items = {};
        var i = 0;
        var result = [];
        
        while ((i < 20) && (i < items.length)) {{
            var r = {};
            result = result + r;
            i = i + 1;
        }}
        return result;
        """
        code = code.format(pack, method)
        return self.vk.execute(code)

    def parse(self, items, method, pack_len=20):
        packs = self.form_packs(items, pack_len=pack_len)
        result = []
        for pack in packs:
            r = self.execute_from_pack(pack, method)
            result.append(r)
        return result
