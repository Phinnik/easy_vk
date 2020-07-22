from typing import List, Union, Optional
from easy_vk.types import objects, responses
from .base import BaseCategory


class Docs(BaseCategory):
    def __init__(self, session, access_token: str, v: str, delay: float, auto_retry: bool, max_retries: int, timeout: float):
        super().__init__(session, access_token, v, delay, auto_retry, max_retries, timeout)

    def get_messages_upload_server(self, type_: str = None, peer_id: int = None) -> responses.BaseGetUploadServer:
        """
        Returns the server address for document upload.
        
        :param type_: Document type.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'Chat ID', e.g. '2000000001'. For community: '- Community ID', e.g. '-12345'. "
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'docs.getMessagesUploadServer'
        param_aliases = [('type_', 'type')]
        response_type = responses.BaseGetUploadServer
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_wall_upload_server(self, group_id: int = None) -> responses.BaseGetUploadServer:
        """
        Returns the server address for document upload onto a user's or community's wall.
        
        :param group_id: Community ID (if the document will be uploaded to the community).
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'docs.getWallUploadServer'
        param_aliases = []
        response_type = responses.BaseGetUploadServer
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def save(self, file: str = None, title: str = None, tags: str = None, return_tags: bool = None) -> responses.DocsSave:
        """
        Saves a document after [vk.com/dev/upload_files_2|uploading it to a server].
        
        :param file: This parameter is returned when the file is [vk.com/dev/upload_files_2|uploaded to the server].
        :param title: Document title.
        :param tags: Document tags.
        :param return_tags: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'docs.save'
        param_aliases = []
        response_type = responses.DocsSave
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def search(self, q: str = None, search_own: bool = None, count: int = None, offset: int = None, return_tags: bool = None) -> responses.DocsSearch:
        """
        Returns a list of documents matching the search criteria.
        
        :param q: Search query string.
        :param search_own: 
        :param count: Number of results to return.
        :param offset: Offset needed to return a specific subset of results.
        :param return_tags: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'docs.search'
        param_aliases = []
        response_type = responses.DocsSearch
        return self._call(method_name, method_parameters, param_aliases, response_type)

