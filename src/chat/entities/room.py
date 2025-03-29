from dataclasses import dataclass
from typing import Optional
from .message import Message

@dataclass
class Room:
    room_id: str
    room_name: str
    owner: Optional[str] = None
    messages: Optional[list[Message]] = None
    current_users: Optional[list[str]] = None