import flet as ft
from dataclasses import dataclass
from typing import Optional
import os
import uuid
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/download/{file_path:path}")
async def download_file(file_path: str):
    return FileResponse(file_path)

@dataclass
class Message:
    user_name: str
    text: str
    message_type: str
    room_id: Optional[str] = None
    to_user: Optional[str] = None
    file_path: Optional[str] = None

class ChatRoom:
    def __init__(self, room_id: str, name: str):
        self.room_id = room_id
        self.name = name
        self.messages = []
        self.users = set()

class ChatMessage(ft.Row):
    def __init__(self, message: Message, on_edit, on_delete):
        super().__init__()
        self.message = message
        self.vertical_alignment = ft.CrossAxisAlignment.START
        self.controls = [
            ft.CircleAvatar(
                content=ft.Text(self.get_initials(message.user_name)),
                color=ft.Colors.WHITE,
                bgcolor=self.get_avatar_color(message.user_name),
            ),
            ft.Column(
                [
                    ft.Text(message.user_name, weight="bold"),
                    ft.Text(message.text, selectable=True),
                ],
                tight=True,
                spacing=5,
            ),
            ft.IconButton(icon=ft.Icons.EDIT, tooltip="Edit", on_click=lambda e: on_edit(self)),
            ft.IconButton(icon=ft.Icons.DELETE, tooltip="Delete", on_click=lambda e: on_delete(self)),
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

class ChatApp:
    def __init__(self):
        self.rooms = {
            "geral": ChatRoom("geral", "Sala Geral"),
            "casual": ChatRoom("casual", "Bate-papo Casual"),
            "estudos": ChatRoom("estudos", "Sala de Estudos"),
        }
        self.current_room = "geral"
        self.upload_dir = "uploads"
        os.makedirs(self.upload_dir, exist_ok=True)

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.title = "Chat em Tempo Real"

    chat_app = ChatApp()

    def save_file(file_path: str, data: bytes):
        with open(file_path, 'wb') as f:
            f.write(data)

    def pick_files_result(e: ft.FilePickerResultEvent):
        if e.files:
            print(f"Files selected: {len(e.files)}")
            for file in e.files:
                print(f"Processing file: {file.name}")
                file_ext = os.path.splitext(file.name)[1].lower()
                allowed_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.pdf', '.doc', '.docx', '.txt']
                if file_ext not in allowed_extensions:
                    print(f"File type not allowed: {file_ext}")
                    page.snack_bar = ft.SnackBar(ft.Text("Tipo de arquivo não permitido!"))
                    page.snack_bar.open = True
                    page.update()
                    continue

                # Create room directory if it doesn't exist
                room_dir = os.path.join(chat_app.upload_dir, chat_app.rooms[chat_app.current_room].name)
                os.makedirs(room_dir, exist_ok=True)
                file_path = os.path.join(room_dir, file.name).replace('\\', '/')
                print(f"Saving file to: {file_path}")

                try:
                    # Use Flet's upload functionality
                    upload_url = page.get_upload_url(file_path, 60)
                    file_picker.upload(
                        [
                            ft.FilePickerUploadFile(
                                file.name,
                                upload_url=upload_url
                            )
                        ]
                    )
                    print(f"File upload started for: {file.name}")

                    page.pubsub.send_all(
                        Message(
                            user_name=page.session.get("user_name"),
                            text=f"Arquivo compartilhado: {file.name}",
                            message_type="file_message",
                            room_id=chat_app.current_room,
                            file_path=file_path
                        )
                    )
                    print(f"File message published for: {file.name}")
                except Exception as e:
                    print(f"Error saving file: {str(e)}")
                    page.snack_bar = ft.SnackBar(ft.Text(f"Erro ao enviar arquivo: {str(e)}"))
                    page.snack_bar.open = True
                    page.update()

    def on_upload_progress(e: ft.FilePickerUploadEvent):
        print(f"Upload progress: {e.progress}% for {e.file_name}")

    file_picker = ft.FilePicker(on_result=pick_files_result, on_upload=on_upload_progress)
    page.overlay.append(file_picker)

    def join_chat_click(e):
        if not join_user_name.value:
            join_user_name.error_text = "O nome não pode estar em branco!"
            join_user_name.update()
        else:
            page.session.set("user_name", join_user_name.value)
            welcome_dlg.open = False
            new_message.prefix = ft.Text(f"{join_user_name.value}: ")
            
            # Adiciona o usuário à sala geral
            chat_app.rooms["geral"].users.add(join_user_name.value)
            
            page.pubsub.send_all(
                Message(
                    user_name=join_user_name.value,
                    text=f"{join_user_name.value} entrou no chat.",
                    message_type="login_message",
                    room_id="geral"
                )
            )
            page.update()

    def send_message_click(e):
        if new_message.value != "":
            page.pubsub.send_all(
                Message(
                    user_name=page.session.get("user_name"),
                    text=new_message.value,
                    message_type="chat_message",
                    room_id=chat_app.current_room
                )
            )
            new_message.value = ""
            new_message.focus()
            page.update()

    def change_room(e):
        selected_index = e.control.selected_index
        chat_app.current_room = list(chat_app.rooms.keys())[selected_index]
        room_name.value = f"Sala: {chat_app.rooms[chat_app.current_room].name}"
        chat.controls.clear()
        page.update()

    def on_edit(chat_message):
        print("Botão de editar clicado")  # Depuração

        def save_edit(e):
            print("Salvando mensagem:", edit_field.value)

            # Atualiza o texto da mensagem e a UI correspondente
            chat_message.message.text = edit_field.value
            chat_message.controls[1].controls[1].value = chat_message.message.text  

            # Atualiza a interface do chat
            chat_message.controls[1].controls[1].update()
            chat_message.update()

            # Fecha o diálogo e atualiza a página
            edit_dlg.open = False
            page.update()

        edit_field = ft.TextField(value=chat_message.message.text)

        edit_dlg = ft.AlertDialog(
            title=ft.Text("Editar Mensagem"),
            content=edit_field,
            actions=[
                ft.ElevatedButton(text="Salvar", on_click=save_edit),
                ft.ElevatedButton(text="Cancelar", on_click=lambda e: setattr(edit_dlg, "open", False) or page.update()),
            ],
        )

        # Adiciona o diálogo à sobreposição da página
        page.overlay.append(edit_dlg)  

        # Abre o diálogo e atualiza a página
        edit_dlg.open = True  
        page.update()  


    def on_delete(chat_message):
        chat.controls.remove(chat_message)
        page.update()
        
    def on_message(message: Message):
        # Só processa mensagens da sala atual
        if message.room_id != chat_app.current_room:
            return

        if message.message_type == "chat_message":
            m = ChatMessage(message, on_edit, on_delete)
        elif message.message_type == "login_message":
            m = ft.Text(message.text, italic=True, color=ft.Colors.BLACK45, size=12)
        elif message.message_type == "file_message":
            print(f"Received file message: {message.file_path}")
            if message.file_path:
                file_ext = os.path.splitext(message.file_path)[1].lower()
                if file_ext in ['.png', '.jpg', '.jpeg', '.gif']:
                    print(f"Displaying image preview for: {message.file_path}")
                    m = ft.Column(
                        [
                            ft.Text(f"{message.user_name} compartilhou uma imagem:"),
                            ft.Image(src=message.file_path, width=200, height=200, fit=ft.ImageFit.CONTAIN)
                        ]
                    )
                else:
                    print(f"Displaying file download for: {message.file_path}")
                    m = ft.Column(
                        [
                            ft.Text(f"{message.user_name} compartilhou um arquivo:"),
                            ft.ElevatedButton(
                                text=os.path.basename(message.file_path),
                                on_click=lambda _: page.launch_url(f"/download/{message.file_path}")
                            )
                        ]
                    )
            else:
                m = ft.Text(message.text, italic=True, color=ft.Colors.BLACK45, size=12)

        chat.controls.append(m)
        page.update()

    page.pubsub.subscribe(on_message)

    # Diálogo de boas-vindas pedindo o nome do usuário
    join_user_name = ft.TextField(
        label="Digite seu nome para entrar no chat",
        autofocus=True,
        on_submit=join_chat_click,
    )
    welcome_dlg = ft.AlertDialog(
        open=True,
        modal=True,
        title=ft.Text("Bem-vindo!"),
        content=ft.Column([join_user_name], width=300, height=70, tight=True),
        actions=[ft.ElevatedButton(text="Entrar no chat", on_click=join_chat_click)],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    page.overlay.append(welcome_dlg)

    # Lista de salas usando NavigationRail
    room_rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        on_change=change_room,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icons.CHAT_BUBBLE_OUTLINE,
                selected_icon=ft.Icons.CHAT_BUBBLE,
                label=room.name,
            ) for room in chat_app.rooms.values()
        ],
    )

    # Nome da sala atual
    room_name = ft.Text(f"Sala: {chat_app.rooms[chat_app.current_room].name}", size=20, weight="bold")

    # Mensagens do chat
    chat = ft.ListView(
        expand=True,
        spacing=10,
        auto_scroll=True,
    )

    # Formulário para nova mensagem
    new_message = ft.TextField(
        hint_text="Escreva uma mensagem...",
        autofocus=True,
        shift_enter=True,
        min_lines=1,
        max_lines=5,
        filled=True,
        expand=True,
        on_submit=send_message_click,
    )

    # Layout principal
    content = ft.Column(
        [
            room_name,
            ft.Container(
                content=chat,
                border=ft.border.all(1, ft.Colors.OUTLINE),
                border_radius=5,
                padding=10,
                expand=True,
            ),
            ft.Row(
                [
                    new_message,
                    ft.IconButton(
                        icon=ft.Icons.FILE_UPLOAD,
                        tooltip="Compartilhar arquivo",
                        on_click=lambda _: file_picker.pick_files(
                            allow_multiple=True,
                            allowed_extensions=['png', 'jpg', 'jpeg', 'gif', 'pdf', 'doc', 'docx', 'txt']
                        ),
                    ),
                    ft.IconButton(
                        icon=ft.Icons.SEND_ROUNDED,
                        tooltip="Enviar mensagem",
                        on_click=send_message_click,
                    ),
                ]
            ),
        ],
        expand=True,
    )

    # Adiciona tudo à página
    page.add(
        ft.Row(
            [
                room_rail,
                ft.VerticalDivider(width=1),
                content,
            ],
            expand=True,
        )
    )

if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER, upload_dir="uploads")
