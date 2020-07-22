from typing import List, Union, Optional
from easy_vk.types import objects, responses
from .base import BaseCategory


class Photos(BaseCategory):
    def __init__(self, session, access_token: str, v: str, delay: float, auto_retry: bool, max_retries: int, timeout: float):
        super().__init__(session, access_token, v, delay, auto_retry, max_retries, timeout)

    def get_messages_upload_server(self, peer_id: int = None) -> responses.PhotosGetMessagesUploadServer:
        """
        Returns the server address for photo upload in a private message for a user.
        
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'Chat ID', e.g. '2000000001'. For community: '- Community ID', e.g. '-12345'. "
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'photos.getMessagesUploadServer'
        param_aliases = []
        response_type = responses.PhotosGetMessagesUploadServer
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_owner_cover_photo_upload_server(self, group_id: int = None, crop_x: int = None, crop_y: int = None, crop_x2: int = None, crop_y2: int = None) -> responses.BaseGetUploadServer:
        """
        Returns the server address for owner cover upload.
        
        :param group_id: ID of community that owns the album (if the photo will be uploaded to a community album).
        :param crop_x: X coordinate of the left-upper corner
        :param crop_y: Y coordinate of the left-upper corner
        :param crop_x2: X coordinate of the right-bottom corner
        :param crop_y2: Y coordinate of the right-bottom corner
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'photos.getOwnerCoverPhotoUploadServer'
        param_aliases = []
        response_type = responses.BaseGetUploadServer
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def save_messages_photo(self, photo: str = None, server: int = None, hash_: str = None) -> responses.PhotosSaveMessagesPhoto:
        """
        Saves a photo after being successfully uploaded. URL obtained with [vk.com/dev/photos.getMessagesUploadServer|photos.getMessagesUploadServer] method.
        
        :param photo: Parameter returned when the photo is [vk.com/dev/upload_files|uploaded to the server].
        :param server: 
        :param hash_: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'photos.saveMessagesPhoto'
        param_aliases = [('hash_', 'hash')]
        response_type = responses.PhotosSaveMessagesPhoto
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def save_owner_cover_photo(self, hash_: str = None, photo: str = None) -> responses.PhotosSaveOwnerCoverPhoto:
        """
        Saves cover photo after successful uploading.
        
        :param hash_: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param photo: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'photos.saveOwnerCoverPhoto'
        param_aliases = [('hash_', 'hash')]
        response_type = responses.PhotosSaveOwnerCoverPhoto
        return self._call(method_name, method_parameters, param_aliases, response_type)

