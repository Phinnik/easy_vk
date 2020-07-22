from typing import List, Union, Optional
from easy_vk.types import objects, responses
from .base import BaseCategory


class Prettycards(BaseCategory):
    def __init__(self, session, access_token: str, v: str, delay: float, auto_retry: bool, max_retries: int, timeout: float):
        super().__init__(session, access_token, v, delay, auto_retry, max_retries, timeout)

    def create(self, owner_id: int = None, photo: str = None, title: str = None, link: str = None, price: str = None, price_old: str = None, button: str = None) -> responses.PrettyCardsCreate:
        """
        :param owner_id: 
        :param photo: 
        :param title: 
        :param link: 
        :param price: 
        :param price_old: 
        :param button: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'prettyCards.create'
        param_aliases = []
        response_type = responses.PrettyCardsCreate
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def delete(self, owner_id: int = None, card_id: int = None) -> responses.PrettyCardsDelete:
        """
        :param owner_id: 
        :param card_id: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'prettyCards.delete'
        param_aliases = []
        response_type = responses.PrettyCardsDelete
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def edit(self, owner_id: int = None, card_id: int = None, photo: str = None, title: str = None, link: str = None, price: str = None, price_old: str = None, button: str = None) -> responses.PrettyCardsEdit:
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
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'prettyCards.edit'
        param_aliases = []
        response_type = responses.PrettyCardsEdit
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get(self, owner_id: int = None, offset: int = None, count: int = None) -> responses.PrettyCardsGet:
        """
        :param owner_id: 
        :param offset: 
        :param count: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'prettyCards.get'
        param_aliases = []
        response_type = responses.PrettyCardsGet
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_by_id(self, owner_id: int = None, card_ids: List[int] = None) -> responses.PrettyCardsGetById:
        """
        :param owner_id: 
        :param card_ids: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'prettyCards.getById'
        param_aliases = []
        response_type = responses.PrettyCardsGetById
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_upload_url(self) -> responses.PrettyCardsGetUploadUrl:
        
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'prettyCards.getUploadURL'
        param_aliases = []
        response_type = responses.PrettyCardsGetUploadUrl
        return self._call(method_name, method_parameters, param_aliases, response_type)

