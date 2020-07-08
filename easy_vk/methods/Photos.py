from ._ApiMethod import ApiMethod
from typing import List


class Photos(ApiMethod):
    def __init__(self, session, access_token, v, requests_per_s):
        super().__init__(session, access_token, v, requests_per_s)

    def confirm_tag(self, photo_id: str, tag_id: int, owner_id: int = None):
        """
        Confirms a tag on a photo.
        
        :param photo_id: Photo ID.
        :param tag_id: Tag ID.
        :param owner_id: ID of the user or community that owns the photo.
        """
    
        method_name = 'photos.confirmTag'
        return self._call(method_name, locals())

    def copy(self, owner_id: int, photo_id: int, access_key: str = None):
        """
        Allows to copy a photo to the "Saved photos" album
        
        :param owner_id: photo's owner ID
        :param photo_id: photo ID
        :param access_key: for private photos
        """
    
        method_name = 'photos.copy'
        return self._call(method_name, locals())

    def create_album(self, title: str, group_id: int = None, description: str = None, privacy_view: List[str] = None, privacy_comment: List[str] = None, upload_by_admins_only: bool = None, comments_disabled: bool = None):
        """
        Creates an empty photo album.
        
        :param title: Album title.
        :param group_id: ID of the community in which the album will be created.
        :param description: Album description.
        :param privacy_view: 
        :param privacy_comment: 
        :param upload_by_admins_only: 
        :param comments_disabled: 
        """
    
        if privacy_view:
            privacy_view = ','.join(privacy_view)
        if privacy_comment:
            privacy_comment = ','.join(privacy_comment)
        
        method_name = 'photos.createAlbum'
        return self._call(method_name, locals())

    def create_comment(self, photo_id: int, owner_id: int = None, message: str = None, attachments: List[str] = None, from_group: bool = None, reply_to_comment: int = None, sticker_id: int = None, access_key: str = None, guid: str = None):
        """
        Adds a new comment on the photo.
        
        :param photo_id: Photo ID.
        :param owner_id: ID of the user or community that owns the photo.
        :param message: Comment text.
        :param attachments: (Required if 'message' is not set.) List of objects attached to the post, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — Media attachment owner ID. '<media_id>' — Media attachment ID. Example: "photo100172_166443618,photo66748_265827614"
        :param from_group: '1' — to post a comment from the community
        :param reply_to_comment: 
        :param sticker_id: 
        :param access_key: 
        :param guid: 
        """
    
        if attachments:
            attachments = ','.join(attachments)
        
        method_name = 'photos.createComment'
        return self._call(method_name, locals())

    def delete(self, photo_id: int, owner_id: int = None):
        """
        Deletes a photo.
        
        :param photo_id: Photo ID.
        :param owner_id: ID of the user or community that owns the photo.
        """
    
        method_name = 'photos.delete'
        return self._call(method_name, locals())

    def delete_album(self, album_id: int, group_id: int = None):
        """
        Deletes a photo album belonging to the current user.
        
        :param album_id: Album ID.
        :param group_id: ID of the community that owns the album.
        """
    
        method_name = 'photos.deleteAlbum'
        return self._call(method_name, locals())

    def delete_comment(self, comment_id: int, owner_id: int = None):
        """
        Deletes a comment on the photo.
        
        :param comment_id: Comment ID.
        :param owner_id: ID of the user or community that owns the photo.
        """
    
        method_name = 'photos.deleteComment'
        return self._call(method_name, locals())

    def edit(self, photo_id: int, owner_id: int = None, caption: str = None, latitude: float = None, longitude: float = None, place_str: str = None, foursquare_id: str = None, delete_place: bool = None):
        """
        Edits the caption of a photo.
        
        :param photo_id: Photo ID.
        :param owner_id: ID of the user or community that owns the photo.
        :param caption: New caption for the photo. If this parameter is not set, it is considered to be equal to an empty string.
        :param latitude: 
        :param longitude: 
        :param place_str: 
        :param foursquare_id: 
        :param delete_place: 
        """
    
        method_name = 'photos.edit'
        return self._call(method_name, locals())

    def edit_album(self, album_id: int, title: str = None, description: str = None, owner_id: int = None, privacy_view: List[str] = None, privacy_comment: List[str] = None, upload_by_admins_only: bool = None, comments_disabled: bool = None):
        """
        Edits information about a photo album.
        
        :param album_id: ID of the photo album to be edited.
        :param title: New album title.
        :param description: New album description.
        :param owner_id: ID of the user or community that owns the album.
        :param privacy_view: 
        :param privacy_comment: 
        :param upload_by_admins_only: 
        :param comments_disabled: 
        """
    
        if privacy_view:
            privacy_view = ','.join(privacy_view)
        if privacy_comment:
            privacy_comment = ','.join(privacy_comment)
        
        method_name = 'photos.editAlbum'
        return self._call(method_name, locals())

    def edit_comment(self, comment_id: int, owner_id: int = None, message: str = None, attachments: List[str] = None):
        """
        Edits a comment on a photo.
        
        :param comment_id: Comment ID.
        :param owner_id: ID of the user or community that owns the photo.
        :param message: New text of the comment.
        :param attachments: (Required if 'message' is not set.) List of objects attached to the post, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — Media attachment owner ID. '<media_id>' — Media attachment ID. Example: "photo100172_166443618,photo66748_265827614"
        """
    
        if attachments:
            attachments = ','.join(attachments)
        
        method_name = 'photos.editComment'
        return self._call(method_name, locals())

    def get(self, owner_id: int = None, album_id: str = None, photo_ids: List[str] = None, rev: bool = None, extended: bool = None, feed_type: str = None, feed: int = None, photo_sizes: bool = None, offset: int = None, count: int = None):
        """
        Returns a list of a user's or community's photos.
        
        :param owner_id: ID of the user or community that owns the photos. Use a negative value to designate a community ID.
        :param album_id: Photo album ID. To return information about photos from service albums, use the following string values: 'profile, wall, saved'.
        :param photo_ids: Photo IDs.
        :param rev: Sort order: '1' — reverse chronological, '0' — chronological
        :param extended: '1' — to return additional 'likes', 'comments', and 'tags' fields, '0' — (default)
        :param feed_type: Type of feed obtained in 'feed' field of the method.
        :param feed: unixtime, that can be obtained with [vk.com/dev/newsfeed.get|newsfeed.get] method in date field to get all photos uploaded by the user on a specific day, or photos the user has been tagged on. Also, 'uid' parameter of the user the event happened with shall be specified.
        :param photo_sizes: '1' — to return photo sizes in a [vk.com/dev/photo_sizes|special format]
        :param offset: 
        :param count: 
        """
    
        if photo_ids:
            photo_ids = ','.join(photo_ids)
        
        method_name = 'photos.get'
        return self._call(method_name, locals())

    def get_albums(self, owner_id: int = None, album_ids: List[int] = None, offset: int = None, count: int = None, need_system: bool = None, need_covers: bool = None, photo_sizes: bool = None):
        """
        Returns a list of a user's or community's photo albums.
        
        :param owner_id: ID of the user or community that owns the albums.
        :param album_ids: Album IDs.
        :param offset: Offset needed to return a specific subset of albums.
        :param count: Number of albums to return.
        :param need_system: '1' — to return system albums with negative IDs
        :param need_covers: '1' — to return an additional 'thumb_src' field, '0' — (default)
        :param photo_sizes: '1' — to return photo sizes in a
        """
    
        if album_ids:
            album_ids = [str(a) for a in album_ids]
            album_ids = ','.join(album_ids)
        
        method_name = 'photos.getAlbums'
        return self._call(method_name, locals())

    def get_albums_count(self, user_id: int = None, group_id: int = None):
        """
        Returns the number of photo albums belonging to a user or community.
        
        :param user_id: User ID.
        :param group_id: Community ID.
        """
    
        method_name = 'photos.getAlbumsCount'
        return self._call(method_name, locals())

    def get_all(self, owner_id: int = None, extended: bool = None, offset: int = None, count: int = None, photo_sizes: bool = None, no_service_albums: bool = None, need_hidden: bool = None, skip_hidden: bool = None):
        """
        Returns a list of photos belonging to a user or community, in reverse chronological order.
        
        :param owner_id: ID of a user or community that owns the photos. Use a negative value to designate a community ID.
        :param extended: '1' — to return detailed information about photos
        :param offset: Offset needed to return a specific subset of photos. By default, '0'.
        :param count: Number of photos to return.
        :param photo_sizes: '1' – to return image sizes in [vk.com/dev/photo_sizes|special format].
        :param no_service_albums: '1' – to return photos only from standard albums, '0' – to return all photos including those in service albums, e.g., 'My wall photos' (default)
        :param need_hidden: '1' – to show information about photos being hidden from the block above the wall.
        :param skip_hidden: '1' – not to return photos being hidden from the block above the wall. Works only with owner_id>0, no_service_albums is ignored.
        """
    
        method_name = 'photos.getAll'
        return self._call(method_name, locals())

    def get_all_comments(self, owner_id: int = None, album_id: int = None, need_likes: bool = None, offset: int = None, count: int = None):
        """
        Returns a list of comments on a specific photo album or all albums of the user sorted in reverse chronological order.
        
        :param owner_id: ID of the user or community that owns the album(s).
        :param album_id: Album ID. If the parameter is not set, comments on all of the user's albums will be returned.
        :param need_likes: '1' — to return an additional 'likes' field, '0' — (default)
        :param offset: Offset needed to return a specific subset of comments. By default, '0'.
        :param count: Number of comments to return. By default, '20'. Maximum value, '100'.
        """
    
        method_name = 'photos.getAllComments'
        return self._call(method_name, locals())

    def get_by_id(self, photos: List[str], extended: bool = None, photo_sizes: bool = None):
        """
        Returns information about photos by their IDs.
        
        :param photos: IDs separated with a comma, that are IDs of users who posted photos and IDs of photos themselves with an underscore character between such IDs. To get information about a photo in the group album, you shall specify group ID instead of user ID. Example: "1_129207899,6492_135055734, , -20629724_271945303"
        :param extended: '1' — to return additional fields, '0' — (default)
        :param photo_sizes: '1' — to return photo sizes in a
        """
    
        if photos:
            photos = ','.join(photos)
        
        method_name = 'photos.getById'
        return self._call(method_name, locals())

    def get_chat_upload_server(self, chat_id: int, crop_x: int = None, crop_y: int = None, crop_width: int = None):
        """
        Returns an upload link for chat cover pictures.
        
        :param chat_id: ID of the chat for which you want to upload a cover photo.
        :param crop_x: 
        :param crop_y: 
        :param crop_width: Width (in pixels) of the photo after cropping.
        """
    
        method_name = 'photos.getChatUploadServer'
        return self._call(method_name, locals())

    def get_comments(self, photo_id: int, owner_id: int = None, need_likes: bool = None, start_comment_id: int = None, offset: int = None, count: int = None, sort: str = None, access_key: str = None, extended: bool = None, fields: List[str] = None):
        """
        Returns a list of comments on a photo.
        
        :param photo_id: Photo ID.
        :param owner_id: ID of the user or community that owns the photo.
        :param need_likes: '1' — to return an additional 'likes' field, '0' — (default)
        :param start_comment_id: 
        :param offset: Offset needed to return a specific subset of comments. By default, '0'.
        :param count: Number of comments to return.
        :param sort: Sort order: 'asc' — old first, 'desc' — new first
        :param access_key: 
        :param extended: 
        :param fields: 
        """
    
        if fields:
            fields = ','.join(fields)
        
        method_name = 'photos.getComments'
        return self._call(method_name, locals())

    def get_market_album_upload_server(self, group_id: int):
        """
        Returns the server address for market album photo upload.
        
        :param group_id: Community ID.
        """
    
        method_name = 'photos.getMarketAlbumUploadServer'
        return self._call(method_name, locals())

    def get_market_upload_server(self, group_id: int, main_photo: bool = None, crop_x: int = None, crop_y: int = None, crop_width: int = None):
        """
        Returns the server address for market photo upload.
        
        :param group_id: Community ID.
        :param main_photo: '1' if you want to upload the main item photo.
        :param crop_x: X coordinate of the crop left upper corner.
        :param crop_y: Y coordinate of the crop left upper corner.
        :param crop_width: Width of the cropped photo in px.
        """
    
        method_name = 'photos.getMarketUploadServer'
        return self._call(method_name, locals())

    def get_messages_upload_server(self, peer_id: int = None):
        """
        Returns the server address for photo upload in a private message for a user.
        
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'Chat ID', e.g. '2000000001'. For community: '- Community ID', e.g. '-12345'. "
        """
    
        method_name = 'photos.getMessagesUploadServer'
        return self._call(method_name, locals())

    def get_new_tags(self, offset: int = None, count: int = None):
        """
        Returns a list of photos with tags that have not been viewed.
        
        :param offset: Offset needed to return a specific subset of photos.
        :param count: Number of photos to return.
        """
    
        method_name = 'photos.getNewTags'
        return self._call(method_name, locals())

    def get_owner_cover_photo_upload_server(self, group_id: int, crop_x: int = None, crop_y: int = None, crop_x2: int = None, crop_y2: int = None):
        """
        Returns the server address for owner cover upload.
        
        :param group_id: ID of community that owns the album (if the photo will be uploaded to a community album).
        :param crop_x: X coordinate of the left-upper corner
        :param crop_y: Y coordinate of the left-upper corner
        :param crop_x2: X coordinate of the right-bottom corner
        :param crop_y2: Y coordinate of the right-bottom corner
        """
    
        method_name = 'photos.getOwnerCoverPhotoUploadServer'
        return self._call(method_name, locals())

    def get_owner_photo_upload_server(self, owner_id: int = None):
        """
        Returns an upload server address for a profile or community photo.
        
        :param owner_id: identifier of a community or current user. "Note that community id must be negative. 'owner_id=1' – user, 'owner_id=-1' – community, "
        """
    
        method_name = 'photos.getOwnerPhotoUploadServer'
        return self._call(method_name, locals())

    def get_tags(self, photo_id: int, owner_id: int = None, access_key: str = None):
        """
        Returns a list of tags on a photo.
        
        :param photo_id: Photo ID.
        :param owner_id: ID of the user or community that owns the photo.
        :param access_key: 
        """
    
        method_name = 'photos.getTags'
        return self._call(method_name, locals())

    def get_upload_server(self, group_id: int = None, album_id: int = None):
        """
        Returns the server address for photo upload.
        
        :param group_id: ID of community that owns the album (if the photo will be uploaded to a community album).
        :param album_id: 
        """
    
        method_name = 'photos.getUploadServer'
        return self._call(method_name, locals())

    def get_user_photos(self, user_id: int = None, offset: int = None, count: int = None, extended: bool = None, sort: str = None):
        """
        Returns a list of photos in which a user is tagged.
        
        :param user_id: User ID.
        :param offset: Offset needed to return a specific subset of photos. By default, '0'.
        :param count: Number of photos to return. Maximum value is 1000.
        :param extended: '1' — to return an additional 'likes' field, '0' — (default)
        :param sort: Sort order: '1' — by date the tag was added in ascending order, '0' — by date the tag was added in descending order
        """
    
        method_name = 'photos.getUserPhotos'
        return self._call(method_name, locals())

    def get_wall_upload_server(self, group_id: int = None):
        """
        Returns the server address for photo upload onto a user's wall.
        
        :param group_id: ID of community to whose wall the photo will be uploaded.
        """
    
        method_name = 'photos.getWallUploadServer'
        return self._call(method_name, locals())

    def make_cover(self, photo_id: int, owner_id: int = None, album_id: int = None):
        """
        Makes a photo into an album cover.
        
        :param photo_id: Photo ID.
        :param owner_id: ID of the user or community that owns the photo.
        :param album_id: Album ID.
        """
    
        method_name = 'photos.makeCover'
        return self._call(method_name, locals())

    def move(self, target_album_id: int, photo_id: int, owner_id: int = None):
        """
        Moves a photo from one album to another.
        
        :param target_album_id: ID of the album to which the photo will be moved.
        :param photo_id: Photo ID.
        :param owner_id: ID of the user or community that owns the photo.
        """
    
        method_name = 'photos.move'
        return self._call(method_name, locals())

    def put_tag(self, photo_id: int, user_id: int, owner_id: int = None, x: float = None, y: float = None, x2: float = None, y2: float = None):
        """
        Adds a tag on the photo.
        
        :param photo_id: Photo ID.
        :param user_id: ID of the user to be tagged.
        :param owner_id: ID of the user or community that owns the photo.
        :param x: Upper left-corner coordinate of the tagged area (as a percentage of the photo's width).
        :param y: Upper left-corner coordinate of the tagged area (as a percentage of the photo's height).
        :param x2: Lower right-corner coordinate of the tagged area (as a percentage of the photo's width).
        :param y2: Lower right-corner coordinate of the tagged area (as a percentage of the photo's height).
        """
    
        method_name = 'photos.putTag'
        return self._call(method_name, locals())

    def remove_tag(self, photo_id: int, tag_id: int, owner_id: int = None):
        """
        Removes a tag from a photo.
        
        :param photo_id: Photo ID.
        :param tag_id: Tag ID.
        :param owner_id: ID of the user or community that owns the photo.
        """
    
        method_name = 'photos.removeTag'
        return self._call(method_name, locals())

    def reorder_albums(self, album_id: int, owner_id: int = None, before: int = None, after: int = None):
        """
        Reorders the album in the list of user albums.
        
        :param album_id: Album ID.
        :param owner_id: ID of the user or community that owns the album.
        :param before: ID of the album before which the album in question shall be placed.
        :param after: ID of the album after which the album in question shall be placed.
        """
    
        method_name = 'photos.reorderAlbums'
        return self._call(method_name, locals())

    def reorder_photos(self, photo_id: int, owner_id: int = None, before: int = None, after: int = None):
        """
        Reorders the photo in the list of photos of the user album.
        
        :param photo_id: Photo ID.
        :param owner_id: ID of the user or community that owns the photo.
        :param before: ID of the photo before which the photo in question shall be placed.
        :param after: ID of the photo after which the photo in question shall be placed.
        """
    
        method_name = 'photos.reorderPhotos'
        return self._call(method_name, locals())

    def report(self, owner_id: int, photo_id: int, reason: int = None):
        """
        Reports (submits a complaint about) a photo.
        
        :param owner_id: ID of the user or community that owns the photo.
        :param photo_id: Photo ID.
        :param reason: Reason for the complaint: '0' – spam, '1' – child pornography, '2' – extremism, '3' – violence, '4' – drug propaganda, '5' – adult material, '6' – insult, abuse
        """
    
        method_name = 'photos.report'
        return self._call(method_name, locals())

    def report_comment(self, owner_id: int, comment_id: int, reason: int = None):
        """
        Reports (submits a complaint about) a comment on a photo.
        
        :param owner_id: ID of the user or community that owns the photo.
        :param comment_id: ID of the comment being reported.
        :param reason: Reason for the complaint: '0' – spam, '1' – child pornography, '2' – extremism, '3' – violence, '4' – drug propaganda, '5' – adult material, '6' – insult, abuse
        """
    
        method_name = 'photos.reportComment'
        return self._call(method_name, locals())

    def restore(self, photo_id: int, owner_id: int = None):
        """
        Restores a deleted photo.
        
        :param photo_id: Photo ID.
        :param owner_id: ID of the user or community that owns the photo.
        """
    
        method_name = 'photos.restore'
        return self._call(method_name, locals())

    def restore_comment(self, comment_id: int, owner_id: int = None):
        """
        Restores a deleted comment on a photo.
        
        :param comment_id: ID of the deleted comment.
        :param owner_id: ID of the user or community that owns the photo.
        """
    
        method_name = 'photos.restoreComment'
        return self._call(method_name, locals())

    def save(self, album_id: int = None, group_id: int = None, server: int = None, photos_list: str = None, hash_: str = None, latitude: float = None, longitude: float = None, caption: str = None):
        """
        Saves photos after successful uploading.
        
        :param album_id: ID of the album to save photos to.
        :param group_id: ID of the community to save photos to.
        :param server: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param photos_list: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param hash_: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param latitude: Geographical latitude, in degrees (from '-90' to '90').
        :param longitude: Geographical longitude, in degrees (from '-180' to '180').
        :param caption: Text describing the photo. 2048 digits max.
        """
    
        param_alias_dict = {'hash_': 'hash'}
        method_name = 'photos.save'
        return self._call(method_name, locals())

    def save_market_album_photo(self, group_id: int, photo: str, server: int, hash_: str):
        """
        Saves market album photos after successful uploading.
        
        :param group_id: Community ID.
        :param photo: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param server: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param hash_: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        """
    
        param_alias_dict = {'hash_': 'hash'}
        method_name = 'photos.saveMarketAlbumPhoto'
        return self._call(method_name, locals())

    def save_market_photo(self, photo: str, server: int, hash_: str, group_id: int = None, crop_data: str = None, crop_hash: str = None):
        """
        Saves market photos after successful uploading.
        
        :param photo: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param server: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param hash_: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param group_id: Community ID.
        :param crop_data: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param crop_hash: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        """
    
        param_alias_dict = {'hash_': 'hash'}
        method_name = 'photos.saveMarketPhoto'
        return self._call(method_name, locals())

    def save_messages_photo(self, photo: str, server: int = None, hash_: str = None):
        """
        Saves a photo after being successfully uploaded. URL obtained with [vk.com/dev/photos.getMessagesUploadServer|photos.getMessagesUploadServer] method.
        
        :param photo: Parameter returned when the photo is [vk.com/dev/upload_files|uploaded to the server].
        :param server: 
        :param hash_: 
        """
    
        param_alias_dict = {'hash_': 'hash'}
        method_name = 'photos.saveMessagesPhoto'
        return self._call(method_name, locals())

    def save_owner_cover_photo(self, hash_: str, photo: str):
        """
        Saves cover photo after successful uploading.
        
        :param hash_: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param photo: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        """
    
        param_alias_dict = {'hash_': 'hash'}
        method_name = 'photos.saveOwnerCoverPhoto'
        return self._call(method_name, locals())

    def save_owner_photo(self, server: str = None, hash_: str = None, photo: str = None):
        """
        Saves a profile or community photo. Upload URL can be got with the [vk.com/dev/photos.getOwnerPhotoUploadServer|photos.getOwnerPhotoUploadServer] method.
        
        :param server: parameter returned after [vk.com/dev/upload_files|photo upload].
        :param hash_: parameter returned after [vk.com/dev/upload_files|photo upload].
        :param photo: parameter returned after [vk.com/dev/upload_files|photo upload].
        """
    
        param_alias_dict = {'hash_': 'hash'}
        method_name = 'photos.saveOwnerPhoto'
        return self._call(method_name, locals())

    def save_wall_photo(self, photo: str, user_id: int = None, group_id: int = None, server: int = None, hash_: str = None, latitude: float = None, longitude: float = None, caption: str = None):
        """
        Saves a photo to a user's or community's wall after being uploaded.
        
        :param photo: Parameter returned when the the photo is [vk.com/dev/upload_files|uploaded to the server].
        :param user_id: ID of the user on whose wall the photo will be saved.
        :param group_id: ID of community on whose wall the photo will be saved.
        :param server: 
        :param hash_: 
        :param latitude: Geographical latitude, in degrees (from '-90' to '90').
        :param longitude: Geographical longitude, in degrees (from '-180' to '180').
        :param caption: Text describing the photo. 2048 digits max.
        """
    
        param_alias_dict = {'hash_': 'hash'}
        method_name = 'photos.saveWallPhoto'
        return self._call(method_name, locals())

    def search(self, q: str = None, lat: float = None, long: float = None, start_time: int = None, end_time: int = None, sort: int = None, offset: int = None, count: int = None, radius: int = None):
        """
        Returns a list of photos.
        
        :param q: Search query string.
        :param lat: Geographical latitude, in degrees (from '-90' to '90').
        :param long: Geographical longitude, in degrees (from '-180' to '180').
        :param start_time: 
        :param end_time: 
        :param sort: Sort order:
        :param offset: Offset needed to return a specific subset of photos.
        :param count: Number of photos to return.
        :param radius: Radius of search in meters (works very approximately). Available values: '10', '100', '800', '6000', '50000'.
        """
    
        method_name = 'photos.search'
        return self._call(method_name, locals())

