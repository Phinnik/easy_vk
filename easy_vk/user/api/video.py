from typing import List, Union, Optional
from easy_vk.types import objects, responses
from .base import BaseCategory


class Video(BaseCategory):
    def __init__(self, session, access_token: str, v: str, delay: float, auto_retry: bool, max_retries: int, timeout: float):
        super().__init__(session, access_token, v, delay, auto_retry, max_retries, timeout)

    def add(self, target_id: int = None, video_id: int = None, owner_id: int = None) -> responses.BaseOk:
        """
        Adds a video to a user or community page.
        
        :param target_id: identifier of a user or community to add a video to. Use a negative value to designate a community ID.
        :param video_id: Video ID.
        :param owner_id: ID of the user or community that owns the video. Use a negative value to designate a community ID.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'video.add'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def add_album(self, group_id: int = None, title: str = None, privacy: List[str] = None) -> responses.VideoAddAlbum:
        """
        Creates an empty album for videos.
        
        :param group_id: Community ID (if the album will be created in a community).
        :param title: Album title.
        :param privacy: new access permissions for the album. Possible values: , *'0' – all users,, *'1' – friends only,, *'2' – friends and friends of friends,, *'3' – "only me".
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'video.addAlbum'
        param_aliases = []
        response_type = responses.VideoAddAlbum
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def add_to_album(self, target_id: int = None, album_id: int = None, album_ids: List[int] = None, owner_id: int = None, video_id: int = None) -> responses.BaseOk:
        """
        :param target_id: 
        :param album_id: 
        :param album_ids: 
        :param owner_id: 
        :param video_id: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'video.addToAlbum'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def create_comment(self, owner_id: int = None, video_id: int = None, message: str = None, attachments: List[str] = None, from_group: bool = None, reply_to_comment: int = None, sticker_id: int = None, guid: str = None) -> responses.VideoCreateComment:
        """
        Adds a new comment on a video.
        
        :param owner_id: ID of the user or community that owns the video.
        :param video_id: Video ID.
        :param message: New comment text.
        :param attachments: List of objects attached to the comment, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media attachment owner. '<media_id>' — Media attachment ID. Example: "photo100172_166443618,photo66748_265827614"
        :param from_group: '1' — to post the comment from a community name (only if 'owner_id'<0)
        :param reply_to_comment: 
        :param sticker_id: 
        :param guid: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'video.createComment'
        param_aliases = []
        response_type = responses.VideoCreateComment
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def delete(self, video_id: int = None, owner_id: int = None, target_id: int = None) -> responses.BaseOk:
        """
        Deletes a video from a user or community page.
        
        :param video_id: Video ID.
        :param owner_id: ID of the user or community that owns the video.
        :param target_id: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'video.delete'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def delete_album(self, group_id: int = None, album_id: int = None) -> responses.BaseOk:
        """
        Deletes a video album.
        
        :param group_id: Community ID (if the album is owned by a community).
        :param album_id: Album ID.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'video.deleteAlbum'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def delete_comment(self, owner_id: int = None, comment_id: int = None) -> responses.BaseOk:
        """
        Deletes a comment on a video.
        
        :param owner_id: ID of the user or community that owns the video.
        :param comment_id: ID of the comment to be deleted.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'video.deleteComment'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def edit(self, owner_id: int = None, video_id: int = None, name: str = None, desc: str = None, privacy_view: List[str] = None, privacy_comment: List[str] = None, no_comments: bool = None, repeat: bool = None) -> responses.BaseOk:
        """
        Edits information about a video on a user or community page.
        
        :param owner_id: ID of the user or community that owns the video.
        :param video_id: Video ID.
        :param name: New video title.
        :param desc: New video description.
        :param privacy_view: Privacy settings in a [vk.com/dev/privacy_setting|special format]. Privacy setting is available for videos uploaded to own profile by user.
        :param privacy_comment: Privacy settings for comments in a [vk.com/dev/privacy_setting|special format].
        :param no_comments: Disable comments for the group video.
        :param repeat: '1' — to repeat the playback of the video, '0' — to play the video once,
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'video.edit'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def edit_album(self, group_id: int = None, album_id: int = None, title: str = None, privacy: List[str] = None) -> responses.BaseOk:
        """
        Edits the title of a video album.
        
        :param group_id: Community ID (if the album edited is owned by a community).
        :param album_id: Album ID.
        :param title: New album title.
        :param privacy: new access permissions for the album. Possible values: , *'0' – all users,, *'1' – friends only,, *'2' – friends and friends of friends,, *'3' – "only me".
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'video.editAlbum'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def edit_comment(self, owner_id: int = None, comment_id: int = None, message: str = None, attachments: List[str] = None) -> responses.BaseOk:
        """
        Edits the text of a comment on a video.
        
        :param owner_id: ID of the user or community that owns the video.
        :param comment_id: Comment ID.
        :param message: New comment text.
        :param attachments: List of objects attached to the comment, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media attachment owner. '<media_id>' — Media attachment ID. Example: "photo100172_166443618,photo66748_265827614"
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'video.editComment'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get(self, owner_id: int = None, videos: List[str] = None, album_id: int = None, count: int = None, offset: int = None, extended: bool = None) -> Union[responses.VideoGet, responses.VideoGetExtended]:
        """
        Returns detailed information about videos.
        
        :param owner_id: ID of the user or community that owns the video(s).
        :param videos: Video IDs, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", Use a negative value to designate a community ID. Example: "-4363_136089719,13245770_137352259"
        :param album_id: ID of the album containing the video(s).
        :param count: Number of videos to return.
        :param offset: Offset needed to return a specific subset of videos.
        :param extended: '1' — to return an extended response with additional fields
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'video.get'
        param_aliases = []
        if not extended:
            response_type = responses.VideoGet
        else:
            response_type = responses.VideoGetExtended
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_album_by_id(self, owner_id: int = None, album_id: int = None) -> responses.VideoGetAlbumById:
        """
        Returns video album info
        
        :param owner_id: identifier of a user or community to add a video to. Use a negative value to designate a community ID.
        :param album_id: Album ID.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'video.getAlbumById'
        param_aliases = []
        response_type = responses.VideoGetAlbumById
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_albums(self, owner_id: int = None, offset: int = None, count: int = None, extended: bool = None, need_system: bool = None) -> Union[responses.VideoGetAlbums, responses.VideoGetAlbumsExtended]:
        """
        Returns a list of video albums owned by a user or community.
        
        :param owner_id: ID of the user or community that owns the video album(s).
        :param offset: Offset needed to return a specific subset of video albums.
        :param count: Number of video albums to return.
        :param extended: '1' — to return additional information about album privacy settings for the current user
        :param need_system: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'video.getAlbums'
        param_aliases = []
        if not extended:
            response_type = responses.VideoGetAlbums
        else:
            response_type = responses.VideoGetAlbumsExtended
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_albums_by_video(self, target_id: int = None, owner_id: int = None, video_id: int = None, extended: bool = None) -> Union[responses.VideoGetAlbumsByVideo, responses.VideoGetAlbumsByVideoExtended]:
        """
        :param target_id: 
        :param owner_id: 
        :param video_id: 
        :param extended: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'video.getAlbumsByVideo'
        param_aliases = []
        if not extended:
            response_type = responses.VideoGetAlbumsByVideo
        else:
            response_type = responses.VideoGetAlbumsByVideoExtended
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_comments(self, owner_id: int = None, video_id: int = None, need_likes: bool = None, start_comment_id: int = None, offset: int = None, count: int = None, sort: str = None, extended: bool = None, fields: List[str] = None) -> Union[responses.VideoGetComments, responses.VideoGetCommentsExtended]:
        """
        Returns a list of comments on a video.
        
        :param owner_id: ID of the user or community that owns the video.
        :param video_id: Video ID.
        :param need_likes: '1' — to return an additional 'likes' field
        :param start_comment_id: 
        :param offset: Offset needed to return a specific subset of comments.
        :param count: Number of comments to return.
        :param sort: Sort order: 'asc' — oldest comment first, 'desc' — newest comment first
        :param extended: 
        :param fields: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'video.getComments'
        param_aliases = []
        if not extended:
            response_type = responses.VideoGetComments
        else:
            response_type = responses.VideoGetCommentsExtended
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def remove_from_album(self, target_id: int = None, album_id: int = None, album_ids: List[int] = None, owner_id: int = None, video_id: int = None) -> responses.BaseOk:
        """
        :param target_id: 
        :param album_id: 
        :param album_ids: 
        :param owner_id: 
        :param video_id: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'video.removeFromAlbum'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def reorder_albums(self, owner_id: int = None, album_id: int = None, before: int = None, after: int = None) -> responses.BaseOk:
        """
        Reorders the album in the list of user video albums.
        
        :param owner_id: ID of the user or community that owns the albums..
        :param album_id: Album ID.
        :param before: ID of the album before which the album in question shall be placed.
        :param after: ID of the album after which the album in question shall be placed.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'video.reorderAlbums'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def reorder_videos(self, target_id: int = None, album_id: int = None, owner_id: int = None, video_id: int = None, before_owner_id: int = None, before_video_id: int = None, after_owner_id: int = None, after_video_id: int = None) -> responses.BaseOk:
        """
        Reorders the video in the video album.
        
        :param target_id: ID of the user or community that owns the album with videos.
        :param album_id: ID of the video album.
        :param owner_id: ID of the user or community that owns the video.
        :param video_id: ID of the video.
        :param before_owner_id: ID of the user or community that owns the video before which the video in question shall be placed.
        :param before_video_id: ID of the video before which the video in question shall be placed.
        :param after_owner_id: ID of the user or community that owns the video after which the photo in question shall be placed.
        :param after_video_id: ID of the video after which the photo in question shall be placed.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'video.reorderVideos'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def report(self, owner_id: int = None, video_id: int = None, reason: int = None, comment: str = None, search_query: str = None) -> responses.BaseOk:
        """
        Reports (submits a complaint about) a video.
        
        :param owner_id: ID of the user or community that owns the video.
        :param video_id: Video ID.
        :param reason: Reason for the complaint: '0' – spam, '1' – child pornography, '2' – extremism, '3' – violence, '4' – drug propaganda, '5' – adult material, '6' – insult, abuse
        :param comment: Comment describing the complaint.
        :param search_query: (If the video was found in search results.) Search query string.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'video.report'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def report_comment(self, owner_id: int = None, comment_id: int = None, reason: int = None) -> responses.BaseOk:
        """
        Reports (submits a complaint about) a comment on a video.
        
        :param owner_id: ID of the user or community that owns the video.
        :param comment_id: ID of the comment being reported.
        :param reason: Reason for the complaint: , 0 – spam , 1 – child pornography , 2 – extremism , 3 – violence , 4 – drug propaganda , 5 – adult material , 6 – insult, abuse
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'video.reportComment'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def restore(self, video_id: int = None, owner_id: int = None) -> responses.BaseOk:
        """
        Restores a previously deleted video.
        
        :param video_id: Video ID.
        :param owner_id: ID of the user or community that owns the video.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'video.restore'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def restore_comment(self, owner_id: int = None, comment_id: int = None) -> responses.VideoRestoreComment:
        """
        Restores a previously deleted comment on a video.
        
        :param owner_id: ID of the user or community that owns the video.
        :param comment_id: ID of the deleted comment.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'video.restoreComment'
        param_aliases = []
        response_type = responses.VideoRestoreComment
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def save(self, name: str = None, description: str = None, is_private: bool = None, wallpost: bool = None, link: str = None, group_id: int = None, album_id: int = None, privacy_view: List[str] = None, privacy_comment: List[str] = None, no_comments: bool = None, repeat: bool = None, compression: bool = None) -> responses.VideoSave:
        """
        Returns a server address (required for upload) and video data.
        
        :param name: Name of the video.
        :param description: Description of the video.
        :param is_private: '1' — to designate the video as private (send it via a private message), the video will not appear on the user's video list and will not be available by ID for other users, '0' — not to designate the video as private
        :param wallpost: '1' — to post the saved video on a user's wall, '0' — not to post the saved video on a user's wall
        :param link: URL for embedding the video from an external website.
        :param group_id: ID of the community in which the video will be saved. By default, the current user's page.
        :param album_id: ID of the album to which the saved video will be added.
        :param privacy_view: 
        :param privacy_comment: 
        :param no_comments: 
        :param repeat: '1' — to repeat the playback of the video, '0' — to play the video once,
        :param compression: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'video.save'
        param_aliases = []
        response_type = responses.VideoSave
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def search(self, q: str = None, sort: int = None, hd: int = None, adult: bool = None, filters: List[str] = None, search_own: bool = None, offset: int = None, longer: int = None, shorter: int = None, count: int = None, extended: bool = None) -> Union[responses.VideoSearch, responses.VideoSearchExtended]:
        """
        Returns a list of videos under the set search criterion.
        
        :param q: Search query string (e.g., 'The Beatles').
        :param sort: Sort order: '1' — by duration, '2' — by relevance, '0' — by date added
        :param hd: If not null, only searches for high-definition videos.
        :param adult: '1' — to disable the Safe Search filter, '0' — to enable the Safe Search filter
        :param filters: Filters to apply: 'youtube' — return YouTube videos only, 'vimeo' — return Vimeo videos only, 'short' — return short videos only, 'long' — return long videos only
        :param search_own: 
        :param offset: Offset needed to return a specific subset of videos.
        :param longer: 
        :param shorter: 
        :param count: Number of videos to return.
        :param extended: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'video.search'
        param_aliases = []
        if not extended:
            response_type = responses.VideoSearch
        else:
            response_type = responses.VideoSearchExtended
        return self._call(method_name, method_parameters, param_aliases, response_type)
