from _ApiMethod import ApiMethod
from typing import List


class Prettycards(ApiMethod):
    def __init__(self, session, access_token, v, requests_per_s):
        super().__init__(session, access_token, v, requests_per_s)

    def create(self, owner_id: int, photo: str, title: str, link: str, price: str = None, price_old: str = None, button: str = None):
        """
        
        :param owner_id: 
        :param photo: 
        :param title: 
        :param link: 
        :param price: 
        :param price_old: 
        :param button: 
        """
    
        method_name = 'prettyCards.create'
        return self.call(method_name, locals())

    def delete(self, owner_id: int, card_id: int):
        """
        
        :param owner_id: 
        :param card_id: 
        """
    
        method_name = 'prettyCards.delete'
        return self.call(method_name, locals())

    def edit(self, owner_id: int, card_id: int, photo: str = None, title: str = None, link: str = None, price: str = None, price_old: str = None, button: str = None):
        """
        
        :param owner_id: 
        :param card_id: 
        :param photo: 
        :param title: 
        :param link: 
        :param price: 
        :param price_old: 
        :param button: 
        """
    
        method_name = 'prettyCards.edit'
        return self.call(method_name, locals())

    def get(self, owner_id: int, offset: int = None, count: int = None):
        """
        
        :param owner_id: 
        :param offset: 
        :param count: 
        """
    
        method_name = 'prettyCards.get'
        return self.call(method_name, locals())

    def get_by_id(self, owner_id: int, card_ids: List[int]):
        """
        
        :param owner_id: 
        :param card_ids: 
        """
    
        if card_ids:
            card_ids = [str(c) for c in card_ids]
            card_ids = ','.join(card_ids)
        
        method_name = 'prettyCards.getById'
        return self.call(method_name, locals())

    def get_upload_ur_l(self):
        """
        
        """
    
        method_name = 'prettyCards.getUploadURL'
        return self.call(method_name, locals())

