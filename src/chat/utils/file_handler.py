import os
import flet as ft
from chat.entities.message import Message
from chat.entities.file import File
from chat.chat_app import ChatApp

ALLOWED_EXTENSIONS = ['.png', '.jpg', '.jpeg', '.gif', '.pdf', '.doc', '.docx', '.txt']

class FileHandler:
    def __init__(self, page: ft.Page, chat_app: ChatApp, on_message):
        self.page = page
        self.chat_app = chat_app
        self.on_message = on_message
        self.file_picker = ft.FilePicker(
            on_result=self.pick_files_result,
            on_upload=self.on_upload_progress,
        )
        self.page.overlay.append(self.file_picker)

    def pick_files_result(self, e: ft.FilePickerResultEvent):
        if e.files:
            for file in e.files:
                file_ext = os.path.splitext(file.name)[1].lower()
                if file_ext not in ALLOWED_EXTENSIONS:
                    self.show_snack("Tipo de arquivo não permitido!")
                    continue

                try:
                    upload_url = self.page.get_upload_url(file.name, 60)
                    if upload_url:
                        self.file_picker.upload([
                            ft.FilePickerUploadFile(file.name, upload_url=upload_url)
                        ])
                        self.show_snack(f"Arquivo enviado: {file.name}, Tamanho: {file.size} KBs")
                        file_path = os.path.join(self.chat_app.upload_dir, file.name).replace('\\', '/')
                        message = Message(
                            user_name=self.page.session.get("user_name"),
                            text=f"Arquivo compartilhado: {file.name}",
                            message_type="file_message",
                            room_id=self.page.session.get("current_room") or self.current_room,
                            file=File(
                                file_url=self.chat_app.download_url.format(filename=file.name),
                                file_name=file.name,
                                file_path=file_path,
                                file_size=file.size
                            )
                        )
                        self.chat_app.add_message_to_room(message)
                        self.page.pubsub.send_all(message)

                    else:
                        raise Exception(f"[ERROR] Falha ao obter URL de upload para {file.name}")
                    
                except Exception as ex:
                    self.show_snack(f"Erro ao enviar arquivo: {str(ex)}")

    def on_upload_progress(self, e: ft.FilePickerUploadEvent):
        print(f"Upload progress: {e.progress*100}% para {e.file_name}")

    def show_snack(self, message: str):
        snack_bar = ft.SnackBar(ft.Text(message), open=True)
        self.page.controls.append(snack_bar)    # Precisa reorganizar para remover o snack_bar anterior
        self.page.update()
