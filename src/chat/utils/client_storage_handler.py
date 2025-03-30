from chat.chat_app import ChatApp
import flet as ft

class StorageHandler:
    @staticmethod
    def load_message_from_storage(page: ft.Page, chat_app: ChatApp) -> None:
        messages = page.client_storage.get("messages")
        if messages:
            chat_app.messages = messages
    
    @staticmethod
    def load_rooms_from_storage(page: ft.Page, chat_app: ChatApp) -> None:
        rooms = page.client_storage.get("rooms")	
        if rooms:
            return rooms
            
    @staticmethod
    def save_message(page: ft.Page, chat_app: ChatApp) -> None:
        page.client_storage.get("messages")    #set("messages", chat_app.)

class ClientStorageHandler:
    def __init__(self, page: ft.Page, chat_app: ChatApp) -> None:
        self.page = page
        self.chat_app = chat_app
    
    def save(self, key: str, value: str) -> None:
        self.page.client_storage.set(key, value)

    def load(self, key: str) -> str:
        return self.page.client_storage.get(key)
    
    def delete(self, key: str) -> None:
        self.page.client_storage.remove(key)

    def save_mutiples(self, **kwargs) -> None:
        for key, value in kwargs.items():
            self.save(key, value)

    def load_mutiples(self, *keys) -> dict:
        return {key: self.load(key) for key in keys}
    