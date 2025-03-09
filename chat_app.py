import flet as ft
from dataclasses import dataclass
from typing import Optional
import base64
import os
import mimetypes

@dataclass
class Message:
    user_name: str
    text: str
    message_type: str
    room_id: Optional[str] = None
    to_user: Optional[str] = None
    file_data: Optional[dict] = None  # For storing file information

class ChatRoom:
    def __init__(self, room_id: str, name: str):
        self.room_id = room_id
        self.name = name
        self.messages = []
        self.users = set()

class ChatMessage(ft.Row):
    def __init__(self, message: Message, page: ft.Page):
        super().__init__()
        self.vertical_alignment = ft.CrossAxisAlignment.START
        self.page = page

        # Basic message content
        message_content = [
            ft.Text(message.user_name, weight="bold"),
        ]

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
                        text=f" {message.file_data['name']} ({message.file_data['type']})",
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

class ChatApp:
    def __init__(self):
        self.rooms = {
            "geral": ChatRoom("geral", "Sala Geral"),
            "casual": ChatRoom("casual", "Bate-papo Casual"),
            "estudos": ChatRoom("estudos", "Sala de Estudos"),
        }
        self.current_room = "geral"
        self.users = set()  # Set to store all online users
        self.private_chats = {}  # Dictionary to store private chat messages

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.title = "Chat em Tempo Real"

    chat_app = ChatApp()
    
    def get_private_chat_key(user1, user2):
        # Create a consistent key for private chats regardless of user order
        return tuple(sorted([user1, user2]))

    def join_chat_click(e):
        if not join_user_name.value:
            join_user_name.error_text = "O nome não pode estar em branco!"
            join_user_name.update()
        else:
            page.session.set("user_name", join_user_name.value)
            welcome_dlg.open = False
            new_message.prefix = ft.Text(f"{join_user_name.value}: ")
            
            # Add user to general room and global users list
            chat_app.rooms["geral"].users.add(join_user_name.value)
            chat_app.users.add(join_user_name.value)
            update_user_list()
            
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
            selected_user = user_dropdown.value if user_dropdown.value != "Todos" else None
            message = Message(
                user_name=page.session.get("user_name"),
                text=new_message.value,
                message_type="chat_message",
                room_id=chat_app.current_room if not selected_user else None,
                to_user=selected_user
            )
            
            if selected_user:
                # Store private message
                chat_key = get_private_chat_key(page.session.get("user_name"), selected_user)
                if chat_key not in chat_app.private_chats:
                    chat_app.private_chats[chat_key] = []
                chat_app.private_chats[chat_key].append(message)
            
            page.pubsub.send_all(message)
            new_message.value = ""
            new_message.focus()
            page.update()

    def update_user_list():
        user_dropdown.options = [
            ft.dropdown.Option("Todos")
        ] + [
            ft.dropdown.Option(user) 
            for user in sorted(chat_app.users) 
            if user != page.session.get("user_name")
        ]
        page.update()

    def change_room(e):
        selected_index = e.control.selected_index
        chat_app.current_room = list(chat_app.rooms.keys())[selected_index]
        room_name.value = f"Sala: {chat_app.rooms[chat_app.current_room].name}"
        user_dropdown.value = "Todos"
        refresh_chat()
        page.update()

    def refresh_chat():
        chat.controls.clear()
        if user_dropdown.value != "Todos":
            # Show private chat history
            chat_key = get_private_chat_key(page.session.get("user_name"), user_dropdown.value)
            if chat_key in chat_app.private_chats:
                for msg in chat_app.private_chats[chat_key]:
                    chat.controls.append(ChatMessage(msg, page))
        page.update()

    def on_message(message: Message):
        current_user = page.session.get("user_name")
        
        # Handle user join/leave messages
        if message.message_type == "login_message":
            m = ft.Text(message.text, italic=True, color=ft.Colors.BLACK45, size=12)
            chat.controls.append(m)
            page.update()
            return
            
        # Handle private messages
        if message.to_user:
            if message.to_user == current_user or message.user_name == current_user:
                chat_key = get_private_chat_key(message.user_name, message.to_user)
                
                # Only show if we're currently viewing this private chat
                if user_dropdown.value == message.user_name or user_dropdown.value == message.to_user:
                    m = ChatMessage(message, page)
                    m.controls[1].controls.insert(0, 
                        ft.Text("(Mensagem Privada)", 
                               size=10, 
                               color=ft.colors.PURPLE_400,
                               italic=True)
                    )
                    chat.controls.append(m)
        # Handle room messages
        elif message.room_id == chat_app.current_room and user_dropdown.value == "Todos":
            m = ChatMessage(message, page)
            chat.controls.append(m)
            
        page.update()

    def handle_file_upload(e: ft.FilePickerResultEvent):
        if e.files and len(e.files) > 0:
            uploaded_file = e.files[0]  # Get the first file
            if uploaded_file.path:  # Check if path exists
                try:
                    # Read file content
                    with open(uploaded_file.path, "rb") as file:
                        file_bytes = file.read()
                        file_b64 = base64.b64encode(file_bytes).decode()
                    
                    # Get file type
                    file_type = mimetypes.guess_type(uploaded_file.path)[0] or "application/octet-stream"
                    
                    # Create message with file
                    selected_user = user_dropdown.value if user_dropdown.value != "Todos" else None
                    message = Message(
                        user_name=page.session.get("user_name"),
                        text="",  # Empty text for file-only messages
                        message_type="chat_message",
                        room_id=chat_app.current_room if not selected_user else None,
                        to_user=selected_user,
                        file_data={
                            "name": uploaded_file.name,
                            "type": file_type,
                            "content": file_b64
                        }
                    )
                    
                    if selected_user:
                        chat_key = get_private_chat_key(page.session.get("user_name"), selected_user)
                        if chat_key not in chat_app.private_chats:
                            chat_app.private_chats[chat_key] = []
                        chat_app.private_chats[chat_key].append(message)
                    
                    page.pubsub.send_all(message)
                    page.show_snack_bar(ft.SnackBar(
                        content=ft.Text("Arquivo enviado com sucesso!"),
                        bgcolor=ft.colors.GREEN
                    ))
                    
                except Exception as ex:
                    print(f"Error uploading file: {ex}")
                    page.show_snack_bar(ft.SnackBar(
                        content=ft.Text(f"Erro ao enviar arquivo: {str(ex)}"),
                        bgcolor=ft.colors.ERROR
                    ))
        page.update()

    page.pubsub.subscribe(on_message)

    # Welcome dialog asking for username
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

    # Room list using NavigationRail
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

    # Current room name
    room_name = ft.Text(f"Sala: {chat_app.rooms[chat_app.current_room].name}", size=20, weight="bold")

    # User dropdown for private messages
    user_dropdown = ft.Dropdown(
        width=200,
        label="Enviar para",
        hint_text="Selecione um usuário",
        options=[ft.dropdown.Option("Todos")],
        value="Todos",
        on_change=lambda _: refresh_chat()
    )

    # Chat messages
    chat = ft.ListView(
        expand=True,
        spacing=10,
        auto_scroll=True,
    )

    # New message form
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

    # File picker for uploads
    file_picker = ft.FilePicker(
        on_result=handle_file_upload,
    )
    page.overlay.append(file_picker)
    page.update()  # Make sure the page is updated after adding the file picker

    # Main layout
    content = ft.Column(
        [
            ft.Row([room_name, user_dropdown], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
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
                        icon=ft.Icons.ATTACH_FILE,
                        tooltip="Anexar arquivo",
                        on_click=lambda _: file_picker.pick_files(
                            allow_multiple=False
                        ),
                    ),
                    ft.IconButton(
                        icon=ft.Icons.SEND_ROUNDED,
                        tooltip="Enviar mensagem",
                        on_click=send_message_click,
                    ),
                ],
            ),
        ],
        expand=True,
    )

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
    ft.app(target=main, view=ft.WEB_BROWSER)
