from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    user_name: str
    user_id: str
    current_room_id: str
    private_rooms: Optional[list[str]] = None
