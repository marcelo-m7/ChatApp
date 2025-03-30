from dataclasses import dataclass
from typing import Optional
from chat.entities.message import Message
from chat.entities.user import User

@dataclass
class Room:
    room_id: str
    room_name: str
    owner: Optional[str] = None
    messages: Optional[list[Message]] = None
    current_users: Optional[list[str]] = None
    private: bool = False