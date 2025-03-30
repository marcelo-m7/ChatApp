from dataclasses import dataclass
from typing import Optional

@dataclass
class File:
    # owner: str
    # room_id: Optional[str] = None
    file_url: Optional[str] = None
    file_name: Optional[str] = None
    file_path: Optional[str] = None
    file_size: Optional[str] = None