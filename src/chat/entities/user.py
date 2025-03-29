from dataclasses import dataclass

@dataclass
class User:
    user_name: str
    user_id: str
    current_room_id: str
