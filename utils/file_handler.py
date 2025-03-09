import base64
import mimetypes
import flet as ft
from models.message import Message

class FileHandler:
    def __init__(self, page: ft.Page, on_file_upload):
        self.page = page
        self.on_file_upload = on_file_upload
        self.file_picker = ft.FilePicker(
            on_result=self.handle_file_upload
        )
        self.page.overlay.append(self.file_picker)
        self.page.update()

    def pick_file(self):
        self.file_picker.pick_files(allow_multiple=False)

    def handle_file_upload(self, e: ft.FilePickerResultEvent):
        if e.files and len(e.files) > 0:
            uploaded_file = e.files[0]
            if uploaded_file.path:
                try:
                    # Read file content
                    with open(uploaded_file.path, "rb") as file:
                        file_bytes = file.read()
                        file_b64 = base64.b64encode(file_bytes).decode()
                    
                    # Get file type
                    file_type = mimetypes.guess_type(uploaded_file.path)[0] or "application/octet-stream"
                    
                    # Create file data
                    file_data = {
                        "name": uploaded_file.name,
                        "type": file_type,
                        "content": file_b64
                    }
                    
                    # Call the callback with file data
                    self.on_file_upload(file_data)
                    
                    self.page.show_snack_bar(ft.SnackBar(
                        content=ft.Text("Arquivo enviado com sucesso!"),
                        bgcolor=ft.colors.GREEN
                    ))
                    
                except Exception as ex:
                    print(f"Error uploading file: {ex}")
                    self.page.show_snack_bar(ft.SnackBar(
                        content=ft.Text(f"Erro ao enviar arquivo: {str(ex)}"),
                        bgcolor=ft.colors.ERROR
                    ))
        self.page.update()
