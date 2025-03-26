import os
from chat.chat_room import ChatRoom

class ChatApp:
    def __init__(self):
        self.rooms = {
            "geral": ChatRoom("geral", "Sala Geral"),
            "casual": ChatRoom("casual", "Bate-papo Casual"),
            "estudos": ChatRoom("estudos", "Sala de Estudos"),
            "programador": ChatRoom("programador", "Bate-papo com Assistente"),
        }
        self.current_room = "geral"
        self.upload_dir = "uploads/"
        self.download_url = "http://127.0.0.1:8000/download/{filename}"
        os.makedirs(self.upload_dir, exist_ok=True)

    def change_room(self, room_id):
        if room_id in self.rooms:
            self.current_room = room_id

    def add_message(self, message):
        self.rooms[self.current_room].add_message(message)
    
    def programador(self, message):
        self.rooms["programador"].add_message(message)
    
    def new_room(self, room_id, room_name):
        print(room_id, room_name)
        self.rooms[room_id] = ChatRoom(room_id, room_name)
        
