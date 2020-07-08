from ._ApiMethod import ApiMethod
from typing import List


class Video(ApiMethod):
    def __init__(self, session, access_token, v, requests_per_s):
        super().__init__(session, access_token, v, requests_per_s)

    def add(self, video_id: int, owner_id: int, target_id: int = None):
        """
        Adds a video to a user or community page.
        
        :param video_id: Video ID.
        :param owner_id: ID of the user or community that owns the video. Use a negative value to designate a community ID.
        :param target_id: identifier of a user or community to add a video to. Use a negative value to designate a community ID.
        """
    
        method_name = 'video.add'
        return self._call(method_name, locals())

    def add_album(self, group_id: int = None, title: str = None, privacy: List[str] = None):
        """
        Creates an empty album for videos.
        
        :param group_id: Community ID (if the album will be created in a community).
        :param title: Album title.
        :param privacy: new access permissions for the album. Possible values: , *'0' – all users,, *'1' – friends only,, *'2' – friends and friends of friends,, *'3' – "only me".
        """
    
        if privacy:
            privacy = ','.join(privacy)
        
        method_name = 'video.addAlbum'
        return self._call(method_name, locals())

    def add_to_album(self, owner_id: int, video_id: int, target_id: int = None, album_id: int = None, album_ids: List[int] = None):
        """
        
        :param owner_id: 
        :param video_id: 
        :param target_id: 
        :param album_id: 
        :param album_ids: 
        """
    
        if album_ids:
            album_ids = [str(a) for a in album_ids]
            album_ids = ','.join(album_ids)
        
        method_name = 'video.addToAlbum'
        return self._call(method_name, locals())

    def create_comment(self, video_id: int, owner_id: int = None, message: str = None, attachments: List[str] = None, from_group: bool = None, reply_to_comment: int = None, sticker_id: int = None, guid: str = None):
        """
        Adds a new comment on a video.
        
        :param video_id: Video ID.
        :param owner_id: ID of the user or community that owns the video.
        :param message: New comment text.
        :param attachments: List of objects attached to the comment, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media attachment owner. '<media_id>' — Media attachment ID. Example: "photo100172_166443618,photo66748_265827614"
        :param from_group: '1' — to post the comment from a community name (only if 'owner_id'<0)
        :param reply_to_comment: 
        :param sticker_id: 
        :param guid: 
        """
    
        if attachments:
            attachments = ','.join(attachments)
        
        method_name = 'video.createComment'
        return self._call(method_name, locals())

    def delete(self, video_id: int, owner_id: int = None, target_id: int = None):
        """
        Deletes a video from a user or community page.
        
        :param video_id: Video ID.
        :param owner_id: ID of the user or community that owns the video.
        :param target_id: 
        """
    
        method_name = 'video.delete'
        return self._call(method_name, locals())

    def delete_album(self, album_id: int, group_id: int = None):
        """
        Deletes a video album.
        
        :param album_id: Album ID.
        :param group_id: Community ID (if the album is owned by a community).
        """
    
        method_name = 'video.deleteAlbum'
        return self._call(method_name, locals())

    def delete_comment(self, comment_id: int, owner_id: int = None):
        """
        Deletes a comment on a video.
        
        :param comment_id: ID of the comment to be deleted.
        :param owner_id: ID of the user or community that owns the video.
        """
    
        method_name = 'video.deleteComment'
        return self._call(method_name, locals())

    def edit(self, video_id: int, owner_id: int = None, name: str = None, desc: str = None, privacy_view: List[str] = None, privacy_comment: List[str] = None, no_comments: bool = None, repeat: bool = None):
        """
        Edits information about a video on a user or community page.
        
        :param video_id: Video ID.
        :param owner_id: ID of the user or community that owns the video.
        :param name: New video title.
        :param desc: New video description.
        :param privacy_view: Privacy settings in a [vk.com/dev/privacy_setting|special format]. Privacy setting is available for videos uploaded to own profile by user.
        :param privacy_comment: Privacy settings for comments in a [vk.com/dev/privacy_setting|special format].
        :param no_comments: Disable comments for the group video.
        :param repeat: '1' — to repeat the playback of the video, '0' — to play the video once,
        """
    
        if privacy_view:
            privacy_view = ','.join(privacy_view)
        if privacy_comment:
            privacy_comment = ','.join(privacy_comment)
        
        method_name = 'video.edit'
        return self._call(method_name, locals())

    def edit_album(self, album_id: int, title: str, group_id: int = None, privacy: List[str] = None):
        """
        Edits the title of a video album.
        
        :param album_id: Album ID.
        :param title: New album title.
        :param group_id: Community ID (if the album edited is owned by a community).
        :param privacy: new access permissions for the album. Possible values: , *'0' – all users,, *'1' – friends only,, *'2' – friends and friends of friends,, *'3' – "only me".
        """
    
        if privacy:
            privacy = ','.join(privacy)
        
        method_name = 'video.editAlbum'
        return self._call(method_name, locals())

    def edit_comment(self, comment_id: int, owner_id: int = None, message: str = None, attachments: List[str] = None):
        """
        Edits the text of a comment on a video.
        
        :param comment_id: Comment ID.
        :param owner_id: ID of the user or community that owns the video.
        :param message: New comment text.
        :param attachments: List of objects attached to the comment, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media attachment owner. '<media_id>' — Media attachment ID. Example: "photo100172_166443618,photo66748_265827614"
        """
    
        if attachments:
            attachments = ','.join(attachments)
        
        method_name = 'video.editComment'
        return self._call(method_name, locals())

    def get(self, owner_id: int = None, videos: List[str] = None, album_id: int = None, count: int = None, offset: int = None, extended: bool = None):
        """
        Returns detailed information about videos.
        
        :param owner_id: ID of the user or community that owns the video(s).
        :param videos: Video IDs, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", Use a negative value to designate a community ID. Example: "-4363_136089719,13245770_137352259"
        :param album_id: ID of the album containing the video(s).
        :param count: Number of videos to return.
        :param offset: Offset needed to return a specific subset of videos.
        :param extended: '1' — to return an extended response with additional fields
        """
    
        if videos:
            videos = ','.join(videos)
        
        method_name = 'video.get'
        return self._call(method_name, locals())

    def get_album_by_id(self, album_id: int, owner_id: int = None):
        """
        Returns video album info
        
        :param album_id: Album ID.
        :param owner_id: identifier of a user or community to add a video to. Use a negative value to designate a community ID.
        """
    
        method_name = 'video.getAlbumById'
        return self._call(method_name, locals())

    def get_albums(self, owner_id: int = None, offset: int = None, count: int = None, extended: bool = None, need_system: bool = None):
        """
        Returns a list of video albums owned by a user or community.
        
        :param owner_id: ID of the user or community that owns the video album(s).
        :param offset: Offset needed to return a specific subset of video albums.
        :param count: Number of video albums to return.
        :param extended: '1' — to return additional information about album privacy settings for the current user
        :param need_system: 
        """
    
        method_name = 'video.getAlbums'
        return self._call(method_name, locals())

    def get_albums_by_video(self, owner_id: int, video_id: int, target_id: int = None, extended: bool = None):
        """
        
        :param owner_id: 
        :param video_id: 
        :param target_id: 
        :param extended: 
        """
    
        method_name = 'video.getAlbumsByVideo'
        return self._call(method_name, locals())

    def get_comments(self, video_id: int, owner_id: int = None, need_likes: bool = None, start_comment_id: int = None, offset: int = None, count: int = None, sort: str = None, extended: bool = None, fields: List[str] = None):
        """
        Returns a list of comments on a video.
        
        :param video_id: Video ID.
        :param owner_id: ID of the user or community that owns the video.
        :param need_likes: '1' — to return an additional 'likes' field
        :param start_comment_id: 
        :param offset: Offset needed to return a specific subset of comments.
        :param count: Number of comments to return.
        :param sort: Sort order: 'asc' — oldest comment first, 'desc' — newest comment first
        :param extended: 
        :param fields: 
        """
    
        if fields:
            fields = ','.join(fields)
        
        method_name = 'video.getComments'
        return self._call(method_name, locals())

    def remove_from_album(self, owner_id: int, video_id: int, target_id: int = None, album_id: int = None, album_ids: List[int] = None):
        """
        
        :param owner_id: 
        :param video_id: 
        :param target_id: 
        :param album_id: 
        :param album_ids: 
        """
    
        if album_ids:
            album_ids = [str(a) for a in album_ids]
            album_ids = ','.join(album_ids)
        
        method_name = 'video.removeFromAlbum'
        return self._call(method_name, locals())

    def reorder_albums(self, album_id: int, owner_id: int = None, before: int = None, after: int = None):
        """
        Reorders the album in the list of user video albums.
        
        :param album_id: Album ID.
        :param owner_id: ID of the user or community that owns the albums..
        :param before: ID of the album before which the album in question shall be placed.
        :param after: ID of the album after which the album in question shall be placed.
        """
    
        method_name = 'video.reorderAlbums'
        return self._call(method_name, locals())

    def reorder_videos(self, owner_id: int, video_id: int, target_id: int = None, album_id: int = None, before_owner_id: int = None, before_video_id: int = None, after_owner_id: int = None, after_video_id: int = None):
        """
        Reorders the video in the video album.
        
        :param owner_id: ID of the user or community that owns the video.
        :param video_id: ID of the video.
        :param target_id: ID of the user or community that owns the album with videos.
        :param album_id: ID of the video album.
        :param before_owner_id: ID of the user or community that owns the video before which the video in question shall be placed.
        :param before_video_id: ID of the video before which the video in question shall be placed.
        :param after_owner_id: ID of the user or community that owns the video after which the photo in question shall be placed.
        :param after_video_id: ID of the video after which the photo in question shall be placed.
        """
    
        method_name = 'video.reorderVideos'
        return self._call(method_name, locals())

    def report(self, owner_id: int, video_id: int, reason: int = None, comment: str = None, search_query: str = None):
        """
        Reports (submits a complaint about) a video.
        
        :param owner_id: ID of the user or community that owns the video.
        :param video_id: Video ID.
        :param reason: Reason for the complaint: '0' – spam, '1' – child pornography, '2' – extremism, '3' – violence, '4' – drug propaganda, '5' – adult material, '6' – insult, abuse
        :param comment: Comment describing the complaint.
        :param search_query: (If the video was found in search results.) Search query string.
        """
    
        method_name = 'video.report'
        return self._call(method_name, locals())

    def report_comment(self, owner_id: int, comment_id: int, reason: int = None):
        """
        Reports (submits a complaint about) a comment on a video.
        
        :param owner_id: ID of the user or community that owns the video.
        :param comment_id: ID of the comment being reported.
        :param reason: Reason for the complaint: , 0 – spam , 1 – child pornography , 2 – extremism , 3 – violence , 4 – drug propaganda , 5 – adult material , 6 – insult, abuse
        """
    
        method_name = 'video.reportComment'
        return self._call(method_name, locals())

    def restore(self, video_id: int, owner_id: int = None):
        """
        Restores a previously deleted video.
        
        :param video_id: Video ID.
        :param owner_id: ID of the user or community that owns the video.
        """
    
        method_name = 'video.restore'
        return self._call(method_name, locals())

    def restore_comment(self, comment_id: int, owner_id: int = None):
        """
        Restores a previously deleted comment on a video.
        
        :param comment_id: ID of the deleted comment.
        :param owner_id: ID of the user or community that owns the video.
        """
    
        method_name = 'video.restoreComment'
        return self._call(method_name, locals())

    def save(self, name: str = None, description: str = None, is_private: bool = None, wallpost: bool = None, link: str = None, group_id: int = None, album_id: int = None, privacy_view: List[str] = None, privacy_comment: List[str] = None, no_comments: bool = None, repeat: bool = None, compression: bool = None):
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
    
        if privacy_view:
            privacy_view = ','.join(privacy_view)
        if privacy_comment:
            privacy_comment = ','.join(privacy_comment)
        
        method_name = 'video.save'
        return self._call(method_name, locals())

    def search(self, q: str, sort: int = None, hd: int = None, adult: bool = None, filters: List[str] = None, search_own: bool = None, offset: int = None, longer: int = None, shorter: int = None, count: int = None, extended: bool = None):
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
    
        if filters:
            filters = ','.join(filters)
        
        method_name = 'video.search'
        return self._call(method_name, locals())

