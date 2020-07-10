from pydantic import BaseModel, Field
from typing import List, Union, Optional, Dict


class Place(BaseModel):
    id: int = Field(None)
    title: str = Field(None)
    latitude: float = Field(None)
    longitude: float = Field(None)
    created: int = Field(None)
    icon: str = Field(None)
    country: str = Field(None)
    city: str = Field(None)


class Geo(BaseModel):
    type: str = Field(None)
    coordinates: List[float] = Field(None)
    place: Place = Field(None)


class MessageAction(BaseModel):
    type: str = Field(None)
    member_id: int = Field(None)
    text: str = Field(None)
    email: str = Field(None)
    photo: Dict[str, str] = Field(None)


class PhotoSize(BaseModel):
    url: str = Field(None)
    width: int = Field(None)
    height: int = Field(None)
    type: str = Field(None)


class Photo(BaseModel):
    id: int = Field(None)
    album_id: int = Field(None)
    owner_id: int = Field(None)
    user_id: int = Field(None)
    text: str = Field(None)
    date: int = Field(None)
    sizes: List[PhotoSize] = Field(None)
    width: int = Field(None)
    height: int = Field(None)


class Video(BaseModel):
    id: int = Field(None)
    owner_id: int = Field(None)
    title: str = Field(None)
    description: str = Field(None)
    duration: int = Field(None)
    photo_130: str = Field(None)
    photo_320: str = Field(None)
    photo_640: str = Field(None)
    photo_800: str = Field(None)
    photo_1280: str = Field(None)
    first_frame_130: str = Field(None)
    first_frame_320: str = Field(None)
    first_frame_640: str = Field(None)
    first_frame_800: str = Field(None)
    first_frame_1280: str = Field(None)
    date: int = Field(None)
    adding_date: int = Field(None)
    views: int = Field(None)
    comments: int = Field(None)
    player: str = Field(None)
    platform: str = Field(None)
    can_edit: int = Field(None)
    can_add: int = Field(None)
    is_private: int = Field(None)
    access_key: str = Field(None)
    processing: int = Field(None)
    live: int = Field(None)
    upcoming: int = Field(None)
    is_favorite: bool = Field(None)


class Audio(BaseModel):
    id: int = Field(None)
    owner_id: int = Field(None)
    artist: str = Field(None)
    title: str = Field(None)
    duration: int = Field(None)
    url: str = Field(None)
    lyrics_id: int = Field(None)
    album_id: int = Field(None)
    genre_id: int = Field(None)
    date: int = Field(None)
    no_search: int = Field(None)
    is_hq: int = Field(None)


class Attachment(BaseModel):
    action: Photo = Field(None)
    color: str = Field(None)


class ButtonAction(BaseModel):
    type: str = Field(...)
    label: str = Field(None)
    payload: str = Field(None)
    link: str = Field(None)
    hash: str = Field(None)
    app_id: int = Field(None)
    owner_id: int = Field(None)


class Button(BaseModel):
    action: ButtonAction = Field(...)
    color: str = Field(None)


class Keyboard(BaseModel):
    one_time: bool = Field(None)
    buttons: List[List[Button]] = Field(None)
    inline: bool = Field(None)


class Message(BaseModel):
    id: int = Field(None)
    date: int = Field(None)
    peer_id: int = Field(None)
    from_id: int = Field(None)
    text: str = Field(None)
    random_id: int = Field(None)
    ref: str = Field(None)
    ref_source: str = Field(None)
    attachments: List[Attachment] = Field(None)
    important: bool = Field(None)
    geo: Geo = Field(None)
    payload: str = Field(None)
    # keyboard = Field(None)
    fwd_messages: List["Message"] = Field(None)
    reply_message: "Message" = Field(None)
    action: Union[MessageAction, str] = Field(None)
    chat_id: int = Field(None)
    chat_active: List[int] = Field(None)
    push_settings: dict = Field(None)
    users_count: int = Field(None)
    admin_id: int = Field(None)
    action_mid: int = Field(None)
    action_email: str = Field(None)
    action_text: str = Field(None)
    photo_50: str = Field(None)
    photo_100: str = Field(None)
    photo_200: str = Field(None)


Message.update_forward_refs()
