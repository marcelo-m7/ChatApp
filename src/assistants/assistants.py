
from chat.entities.message import Message
from assistants.programador import Programador
from langchain.schema import HumanMessage, AIMessage    #, SystemMessage
# nomes = ["Programador", "assistente"]

class Assistants:
    def __init__(self, nome: str = "Programador"):
        self.nome = nome
        self.specialist = Programador() if nome == "Programador" else None
        self.call = str(f"@{self.nome}").lower()
        self.chat_history = []

    def process_message(self, message: Message):
        self.chat_history.append(HumanMessage(content=message.text, user=message.user_name))
        print(self.chat_history)

        if self.call in message.text.lower():
            print(self.call, message.text.lower())
            response = self.get_response_from_specialist(message)
            self.chat_history.append(AIMessage(content=message.text))
            print(self.chat_history)
            return self.format_response(response)
        
        return None
    
    def get_response_from_specialist(self, message: Message) -> str:
        return self.specialist.get_response(
            input=message.text, 
            conversation_history=self.chat_history)
    
    def format_response(self, message: Message):
        return Message(user_name=self.nome, text=message, message_type="chat_message")
    