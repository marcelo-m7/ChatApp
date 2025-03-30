from dataclasses import dataclass
from typing import Optional

@dataclass
class Message:
    user_name: str
    text: str
    message_type: str
    room_id: Optional[str] = None
    to_user: Optional[str] = None
    file_url: Optional[str] = None
    file_name: Optional[str] = None
    file_path: Optional[str] = None
    file_size: Optional[str] = None