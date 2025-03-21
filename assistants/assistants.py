
from chat.message import Message
from assistants.programador import Programador
# nomes = ["Programador", "assistente"]
class Assistants:
    def __init__(self, nome: str = "Programador"):
        self.nome = nome
        self.specialist = Programador() if nome == "Programador" else None
        self.call = str(f"@{self.nome}").lower()
        self.chat_history = []

    def process_message(self, message: Message):
        self.chat_history.append(message)
        # print(self.chat_history)

        if self.call in message.text.lower():
            print(self.call, message.text.lower())
            response = self.get_response_from_specialist(message)
            print("Response:", response)
            return self.format_response(response)
        return None

    def get_response_from_specialist(self, message: Message) -> str:
        return self.specialist.get_response(
            input=message.text, 
            conversation_history=self.chat_history)
    
    def format_response(self, message: Message):
        return Message(user_name=self.nome, text=message, message_type="chat_message")
    