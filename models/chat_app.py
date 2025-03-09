from .message import ChatRoom

class ChatApp:
    def __init__(self):
        self.rooms = {
            "geral": ChatRoom("geral", "Sala Geral"),
            "casual": ChatRoom("casual", "Bate-papo Casual"),
            "estudos": ChatRoom("estudos", "Sala de Estudos"),
        }
        self.current_room = "geral"
        self.users = set()  # Set to store all online users
        self.private_chats = {}  # Dictionary to store private chat messages

    def get_private_chat_key(self, user1, user2):
        # Create a consistent key for private chats regardless of user order
        return tuple(sorted([user1, user2]))

    def add_user(self, username: str):
        self.users.add(username)
        self.rooms["geral"].users.add(username)

    def add_private_message(self, message):
        if message.to_user:
            chat_key = self.get_private_chat_key(message.user_name, message.to_user)
            if chat_key not in self.private_chats:
                self.private_chats[chat_key] = []
            self.private_chats[chat_key].append(message)

    def get_private_chat(self, user1: str, user2: str):
        chat_key = self.get_private_chat_key(user1, user2)
        return self.private_chats.get(chat_key, [])
