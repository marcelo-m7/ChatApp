from dataclasses import dataclass
from typing import Optional
from chat.entities.file import File
@dataclass
class Message:
    user_name: str
    text: str
    message_type: str
    room_id: Optional[str] = None
    to_user: Optional[str] = None
    file: Optional[File] = None