from typing import List, Union, Optional
from easy_vk.types import objects, responses
from .base import BaseCategory


class Docs(BaseCategory):
    def __init__(self, session, access_token: str, v: str, delay: float, auto_retry: bool, max_retries: int, timeout: float):
        super().__init__(session, access_token, v, delay, auto_retry, max_retries, timeout)

    def add(self, owner_id: int = None, doc_id: int = None, access_key: str = None) -> responses.DocsAdd:
        """
        Copies a document to a user's or community's document list.
        
        :param owner_id: ID of the user or community that owns the document. Use a negative value to designate a community ID.
        :param doc_id: Document ID.
        :param access_key: Access key. This parameter is required if 'access_key' was returned with the document's data.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'docs.add'
        param_aliases = []
        response_type = responses.DocsAdd
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def delete(self, owner_id: int = None, doc_id: int = None) -> responses.BaseOk:
        """
        Deletes a user or community document.
        
        :param owner_id: ID of the user or community that owns the document. Use a negative value to designate a community ID.
        :param doc_id: Document ID.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'docs.delete'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def edit(self, owner_id: int = None, doc_id: int = None, title: str = None, tags: List[str] = None) -> responses.BaseOk:
        """
        Edits a document.
        
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param doc_id: Document ID.
        :param title: Document title.
        :param tags: Document tags.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'docs.edit'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get(self, count: int = None, offset: int = None, type_: int = None, owner_id: int = None, return_tags: bool = None) -> responses.DocsGet:
        """
        Returns detailed information about user or community documents.
        
        :param count: Number of documents to return. By default, all documents.
        :param offset: Offset needed to return a specific subset of documents.
        :param type_: 
        :param owner_id: ID of the user or community that owns the documents. Use a negative value to designate a community ID.
        :param return_tags: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'docs.get'
        param_aliases = [('type_', 'type')]
        response_type = responses.DocsGet
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_by_id(self, docs: List[str] = None, return_tags: bool = None) -> responses.DocsGetById:
        """
        Returns information about documents by their IDs.
        
        :param docs: Document IDs. Example: , "66748_91488,66748_91455",
        :param return_tags: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'docs.getById'
        param_aliases = []
        response_type = responses.DocsGetById
        return self._call(method_name, method_parameters, param_aliases, response_type)

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

    def get_types(self, owner_id: int = None) -> responses.DocsGetTypes:
        """
        Returns documents types available for current user.
        
        :param owner_id: ID of the user or community that owns the documents. Use a negative value to designate a community ID.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'docs.getTypes'
        param_aliases = []
        response_type = responses.DocsGetTypes
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_upload_server(self, group_id: int = None) -> responses.DocsGetUploadServer:
        """
        Returns the server address for document upload.
        
        :param group_id: Community ID (if the document will be uploaded to the community).
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'docs.getUploadServer'
        param_aliases = []
        response_type = responses.DocsGetUploadServer
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

