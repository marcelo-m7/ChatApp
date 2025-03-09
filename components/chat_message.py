import flet as ft
import base64
from models.message import Message

class ChatMessage(ft.Row):
    def __init__(self, message: Message, page: ft.Page, is_private: bool = False):
        super().__init__()
        self.vertical_alignment = ft.CrossAxisAlignment.START
        self.page = page

        # Basic message content
        message_content = [
            ft.Text(message.user_name, weight="bold"),
        ]

        # Add private message indicator
        if is_private:
            message_content.append(
                ft.Text(
                    "(Mensagem Privada)",
                    size=10,
                    color=ft.colors.PURPLE_400,
                    italic=True
                )
            )

        # Handle file attachments
        if message.file_data:
            if message.file_data["type"].startswith("image/"):
                # Display image preview
                message_content.append(
                    ft.Image(
                        src_base64=message.file_data["content"],
                        width=200,
                        height=200,
                        fit=ft.ImageFit.CONTAIN,
                    )
                )
            else:
                # Display file download link
                message_content.append(
                    ft.TextButton(
                        text=f"📎 {message.file_data['name']} ({message.file_data['type']})",
                        data={"content": message.file_data["content"], "name": message.file_data["name"]},
                        on_click=self.download_file
                    )
                )

        # Add text message if present
        if message.text:
            message_content.append(ft.Text(message.text, selectable=True))

        self.controls = [
            ft.CircleAvatar(
                content=ft.Text(self.get_initials(message.user_name)),
                color=ft.Colors.WHITE,
                bgcolor=self.get_avatar_color(message.user_name),
            ),
            ft.Column(
                message_content,
                tight=True,
                spacing=5,
            ),
        ]

    def get_initials(self, user_name: str):
        return user_name[:1].capitalize() if user_name else "?"

    def get_avatar_color(self, user_name: str):
        colors_lookup = [
            ft.Colors.AMBER,
            ft.Colors.BLUE,
            ft.Colors.BROWN,
            ft.Colors.CYAN,
            ft.Colors.GREEN,
            ft.Colors.INDIGO,
            ft.Colors.LIME,
            ft.Colors.ORANGE,
            ft.Colors.PINK,
            ft.Colors.PURPLE,
            ft.Colors.RED,
            ft.Colors.TEAL,
            ft.Colors.YELLOW,
        ]
        return colors_lookup[hash(user_name) % len(colors_lookup)]

    def download_file(self, e):
        content = e.control.data["content"]
        filename = e.control.data["name"]
        
        # Create a temporary file picker for downloading
        picker = ft.FilePicker(
            on_result=lambda e: self.save_file(e, content, filename)
        )
        self.page.overlay.append(picker)
        picker.save_file(
            allowed_extensions=["*"],
            file_name=filename
        )
        self.page.update()

    def save_file(self, e, content: str, filename: str):
        if e.path:
            try:
                with open(e.path, "wb") as f:
                    f.write(base64.b64decode(content))
                self.page.show_snack_bar(ft.SnackBar(
                    content=ft.Text("Arquivo salvo com sucesso!"),
                    bgcolor=ft.colors.GREEN
                ))
            except Exception as ex:
                print(f"Error saving file: {ex}")
                self.page.show_snack_bar(ft.SnackBar(
                    content=ft.Text(f"Erro ao salvar arquivo: {str(ex)}"),
                    bgcolor=ft.colors.ERROR
                ))
