
from chat.message import Message

# nomes = ["Programador", "assistente"]
class Assistant:
    def __init__(self):
        self.nome = "Programador"
        self.chamado = f"@{self.nome}"
        self.chat_history = []
    def process_message(self, message: Message):
        if self.chamado in message.text.lower():
            response = self.get_response(message)
            return self.format_response(response)
        return None

    def get_response(self, message: Message):
        return f"Olá, {message.user_name}. Como posso ajudar?"
    
    def format_response(self, message: Message):
        return Message(user_name=self.nome, text=message, message_type="chat_message")