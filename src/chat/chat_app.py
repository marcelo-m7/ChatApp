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

    def add_user(self, user_name: str, user_id):
        new_user = User(user_name=user_name, 
                        user_id=user_id,
                        current_room_id='geral')
        
        self.active_users[user_id] = new_user
        print(f"User added: {self.active_users[user_id]}")
    
    def new_room(self, room_id, room_name):
        self.rooms[room_id] = ChatRoom(room_id, room_name)
        print(f"Room added: {self.rooms[room_id].room}")

    def new_private_room(self, owner: str, reciver: str, room_id: str):
        room_name = f"Chat Privado entre {owner} e {reciver}"
        self.rooms[room_id] = ChatRoom(room_id, 
                                room_name,
                                owner=owner,
                                private=True)
        
        private_room = self.rooms[room_id]
        private_room.add_user(reciver)
        print(f"Private Room added: {private_room}")
        return room_id
    
    def add_message_to_room(self, message: Message):
        self.rooms[message.room_id].add_message(message)
        print("Room current messages: \n", self.rooms[message.room_id].room.messages)
