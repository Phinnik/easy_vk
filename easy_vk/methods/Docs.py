from ._ApiMethod import ApiMethod
from typing import List


class Docs(ApiMethod):
    def __init__(self, session, access_token, v, requests_per_s):
        super().__init__(session, access_token, v, requests_per_s)

    def add(self, owner_id: int, doc_id: int, access_key: str = None):
        """
        Copies a document to a user's or community's document list.
        
        :param owner_id: ID of the user or community that owns the document. Use a negative value to designate a community ID.
        :param doc_id: Document ID.
        :param access_key: Access key. This parameter is required if 'access_key' was returned with the document's data.
        """
    
        method_name = 'docs.add'
        return self._call(method_name, locals())

    def delete(self, owner_id: int, doc_id: int):
        """
        Deletes a user or community document.
        
        :param owner_id: ID of the user or community that owns the document. Use a negative value to designate a community ID.
        :param doc_id: Document ID.
        """
    
        method_name = 'docs.delete'
        return self._call(method_name, locals())

    def edit(self, owner_id: int, doc_id: int, title: str = None, tags: List[str] = None):
        """
        Edits a document.
        
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param doc_id: Document ID.
        :param title: Document title.
        :param tags: Document tags.
        """
    
        if tags:
            tags = ','.join(tags)
        
        method_name = 'docs.edit'
        return self._call(method_name, locals())

    def get(self, count: int = None, offset: int = None, type_: int = None, owner_id: int = None, return_tags: bool = None):
        """
        Returns detailed information about user or community documents.
        
        :param count: Number of documents to return. By default, all documents.
        :param offset: Offset needed to return a specific subset of documents.
        :param type_: 
        :param owner_id: ID of the user or community that owns the documents. Use a negative value to designate a community ID.
        :param return_tags: 
        """
    
        param_alias_dict = {'type_': 'type'}
        method_name = 'docs.get'
        return self._call(method_name, locals())

    def get_by_id(self, docs: List[str], return_tags: bool = None):
        """
        Returns information about documents by their IDs.
        
        :param docs: Document IDs. Example: , "66748_91488,66748_91455",
        :param return_tags: 
        """
    
        if docs:
            docs = ','.join(docs)
        
        method_name = 'docs.getById'
        return self._call(method_name, locals())

    def get_messages_upload_server(self, type_: str = None, peer_id: int = None):
        """
        Returns the server address for document upload.
        
        :param type_: Document type.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'Chat ID', e.g. '2000000001'. For community: '- Community ID', e.g. '-12345'. "
        """
    
        param_alias_dict = {'type_': 'type'}
        method_name = 'docs.getMessagesUploadServer'
        return self._call(method_name, locals())

    def get_types(self, owner_id: int):
        """
        Returns documents types available for current user.
        
        :param owner_id: ID of the user or community that owns the documents. Use a negative value to designate a community ID.
        """
    
        method_name = 'docs.getTypes'
        return self._call(method_name, locals())

    def get_upload_server(self, group_id: int = None):
        """
        Returns the server address for document upload.
        
        :param group_id: Community ID (if the document will be uploaded to the community).
        """
    
        method_name = 'docs.getUploadServer'
        return self._call(method_name, locals())

    def get_wall_upload_server(self, group_id: int = None):
        """
        Returns the server address for document upload onto a user's or community's wall.
        
        :param group_id: Community ID (if the document will be uploaded to the community).
        """
    
        method_name = 'docs.getWallUploadServer'
        return self._call(method_name, locals())

    def save(self, file: str, title: str = None, tags: str = None, return_tags: bool = None):
        """
        Saves a document after [vk.com/dev/upload_files_2|uploading it to a server].
        
        :param file: This parameter is returned when the file is [vk.com/dev/upload_files_2|uploaded to the server].
        :param title: Document title.
        :param tags: Document tags.
        :param return_tags: 
        """
    
        method_name = 'docs.save'
        return self._call(method_name, locals())

    def search(self, q: str, search_own: bool = None, count: int = None, offset: int = None, return_tags: bool = None):
        """
        Returns a list of documents matching the search criteria.
        
        :param q: Search query string.
        :param search_own: 
        :param count: Number of results to return.
        :param offset: Offset needed to return a specific subset of results.
        :param return_tags: 
        """
    
        method_name = 'docs.search'
        return self._call(method_name, locals())

