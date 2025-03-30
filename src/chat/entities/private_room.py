from dataclasses import dataclass
from typing import Optional
from chat.entities.room import Room

@dataclass
class PrivateRoom(Room):
    visibility: bool = False
    owner: Optional[str] = None
    current_users: Optional[list[str]] = None