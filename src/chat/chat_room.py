from typing import Optional
from chat.entities.message import Message
from chat.entities.room import Room


class ChatRoom:
    def __init__(self, room_id: str, room_name: str, owner=None, private=False):
        self.room = Room(room_id=room_id, 
                         room_name=room_name,
                         owner=owner if owner else 'system',
                         messages=[],
                         private=private)
        
        if private and owner:
            try:
                self.room.owner = owner
                self.room.current_users = list()
                self.room.current_users.append(owner)
        
            except Exception as ex:
                print(ex)
        
    def add_message(self, message: Message):
        if message.room_id != self.room.room_id:
            return
        self.room.messages.append(message)

    def remove_message(self, message: Message):
        self.room.messages.remove(message)

    def add_user(self, user_name):
        self.room.current_users.append(user_name)

    def remove_user(self, user_name):
        self.room.current_users.remove(user_name)

    def get_messages(self) -> Optional[list[Message]]:
        return self.room.messages

    def get_users(self) -> Optional[list[str]]:
        return self.room.current_users
    