import flet as ft
from chat.chat_interface import ChatInterface
from dotenv import load_dotenv
from chat.chat_app import ChatApp

load_dotenv(".env")

chat_app = ChatApp()
def main(page: ft.Page):
    ChatInterface(page, chat_app)

if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER, upload_dir="uploads/", port=3000, host="localhost")

