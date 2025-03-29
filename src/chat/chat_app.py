import os
from chat.chat_room import ChatRoom
from chat.entities.message import Message
from typing import Optional
from chat.entities.user import User
from chat.entities.room import Room
from chat.entities.message import Message

class ChatApp:
    def __init__(self):
        self.rooms = {
            "geral": ChatRoom("geral", "Sala Geral"),
            "casual": ChatRoom("casual", "Bate-papo Casual"),
            "estudos": ChatRoom("estudos", "Sala de Estudos"),
            "programador": ChatRoom("programador", "Bate-papo com Assistente"),
        }
        self.active_users: dict[str, User] = {}
        self.current_room = "geral"
        self.upload_dir = "uploads/"
        self.download_url = "http://127.0.0.1:3000/download/{filename}"
        os.makedirs(self.upload_dir, exist_ok=True)

    def add_user(self, user_name: str):
        user_id = user_name.strip().lower()
        new_user = User(user_name=user_name, 
                        user_id= user_id,
                        current_room_id='geral')
        
        self.active_users[user_id] = new_user
        print(f"User added: {self.active_users[user_id]}")
    
    def new_room(self, room_id, room_name):
        self.rooms[room_id] = ChatRoom(room_id, room_name)
        print(f"Room added: {self.rooms[room_id].room}")
