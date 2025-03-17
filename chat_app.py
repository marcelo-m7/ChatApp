import flet as ft
from dataclasses import dataclass
from typing import Optional

@dataclass
class Message:
    user_name: str
    text: str
    message_type: str
    room_id: Optional[str] = None


class ChatMessage(ft.Row):
    def __init__(self, message: Message, page, chat, chat_app):
        super().__init__()
        self.message = message
        self.page = page
        self.chat = chat
        self.chat_app = chat_app
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
            ft.IconButton(icon=ft.Icons.EDIT, tooltip="Editar", on_click=self.on_edit),
            ft.IconButton(icon=ft.Icons.DELETE, tooltip="Excluir", on_click=self.on_delete),
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

    def on_edit(self, e):
        def save_edit(e):
            self.message.text = edit_field.value
            self.controls[1].controls[1] = ft.Text(self.message.text, selectable=True)
            
            # Atualiza a mensagem na lista da sala
            room = self.chat_app.rooms[self.message.room_id]
            for i, msg in enumerate(room.messages):
                if msg == self.message:
                    room.messages[i] = self.message
                    break
            
            edit_dlg.open = False
            self.page.update()
        
        edit_field = ft.TextField(value=self.message.text, expand=True)
        edit_dlg = ft.AlertDialog(
            title=ft.Text("Editar Mensagem"),
            content=ft.Column([edit_field], tight=True),
            actions=[
                ft.ElevatedButton(text="Salvar", on_click=save_edit),
                ft.ElevatedButton(text="Cancelar", on_click=lambda e: setattr(edit_dlg, "open", False) or self.page.update()),
            ],
            actions_alignment=ft.MainAxisAlignment.END
        )
        self.page.dialog = edit_dlg
        edit_dlg.open = True
        self.page.update()

    def on_delete(self, e):
        self.chat.controls.remove(self)
        self.page.update()


class ChatRoom:
    def __init__(self, room_id: str, name: str):
        self.room_id = room_id
        self.name = name
        self.messages = []
        self.users = set()


class ChatApp:
    def __init__(self):
        self.rooms = {
            "geral": ChatRoom("geral", "Sala Geral"),
            "casual": ChatRoom("casual", "Bate-papo Casual"),
            "estudos": ChatRoom("estudos", "Sala de Estudos"),
        }
        self.current_room = "geral"
        self.users = set()


def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.title = "Flet Chat"

    chat_app = ChatApp()

    def join_chat_click(e):
        if not join_user_name.value:
            join_user_name.error_text = "O nome não pode estar em branco!"
            join_user_name.update()
        else:
            page.session.set("user_name", join_user_name.value)
            welcome_dlg.open = False
            new_message.prefix = ft.Text(f"{join_user_name.value}: ")
            chat_app.rooms["geral"].users.add(join_user_name.value)
            chat_app.users.add(join_user_name.value)
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
            message = Message(
                user_name=page.session.get("user_name"),
                text=new_message.value,
                message_type="chat_message",
                room_id=chat_app.current_room
            )
            page.pubsub.send_all(message)
            new_message.value = ""
            new_message.focus()
            page.update()

    def change_room(e):
        selected_index = e.control.selected_index
        chat_app.current_room = list(chat_app.rooms.keys())[selected_index]
        room_name.value = f"Sala: {chat_app.rooms[chat_app.current_room].name}"
        chat.controls.clear()
        for message in chat_app.rooms[chat_app.current_room].messages:
            if message.message_type == "chat_message":
                m = ChatMessage(message, page, chat, chat_app)
            elif message.message_type == "login_message":
                m = ft.Text(message.text, italic=True, color=ft.Colors.GREEN_400, size=12)
            chat.controls.append(m)
        page.update()

    def on_message(message: Message):
        if message.message_type == "login_message":
            m = ft.Text(message.text, italic=True, color=ft.Colors.GREEN_400, size=12)
        elif message.room_id == chat_app.current_room:
            m = ChatMessage(message, page, chat, chat_app)
        chat.controls.append(m)
        page.update()

    page.pubsub.subscribe(on_message)

    join_user_name = ft.TextField(label="Digite seu nome para entrar no chat", autofocus=True, on_submit=join_chat_click)
    welcome_dlg = ft.AlertDialog(
        open=True,
        modal=True,
        title=ft.Text("Bem-vindo!"),
        content=ft.Column([join_user_name], width=300, height=70, tight=True),
        actions=[ft.ElevatedButton(text="Entrar no chat", on_click=join_chat_click)],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    page.overlay.append(welcome_dlg)

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

    room_name = ft.Text(f"Sala: {chat_app.rooms[chat_app.current_room].name}", size=20, weight="bold")

    chat = ft.ListView(
        expand=True,
        spacing=10,
        auto_scroll=True,
    )

    new_message = ft.TextField(
        hint_text="Digite uma mensagem...",
        autofocus=True,
        shift_enter=True,
        min_lines=1,
        max_lines=5,
        filled=True,
        expand=True,
        on_submit=send_message_click,
    )

    content = ft.Column(
        [
            ft.Row([room_name], alignment=ft.MainAxisAlignment.CENTER),
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


ft.app(target=main, view=ft.WEB_BROWSER)