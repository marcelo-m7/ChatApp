class ChatRoom:
    def __init__(self, room_id: str, name: str):
        self.room_id = room_id
        self.name = name
        self.messages = []
        self.users = set()

    def add_message(self, message):
        self.messages.append(message)

    def add_user(self, user_name):
        self.users.add(user_name)
