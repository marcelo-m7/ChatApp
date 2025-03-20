import flet as ft
from chat.chat_interface import ChatInterface
# from fastapi import FastAPI
# from fastapi.responses import FileResponse
# from fastapi import UploadFile, File

# app = FastAPI()

from dotenv import load_dotenv
load_dotenv(".env")

def main(page: ft.Page):
    ChatInterface(page)

# if __name__ == "__main__":
ft.app(target=main, view=ft.WEB_BROWSER, upload_dir="uploads/")

