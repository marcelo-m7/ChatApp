import flet as ft
from chat.entities.message import Message

class ChatMessage(ft.Row):
    def __init__(self, message: Message, on_edit, on_delete):
        super().__init__()
        self.message = message
        self.controls = [
            ft.CircleAvatar(
                content=ft.Text(self.get_initials(message.user_name)),
                bgcolor=self.get_avatar_color(message.user_name),
            ),
            ft.Column(
                [
                    ft.Text(message.user_name, weight="bold"),
                    ft.Text(message.text, selectable=True),
                ]
            ),
            ft.IconButton(icon=ft.Icons.EDIT, on_click=lambda e: on_edit(self)),
            ft.IconButton(icon=ft.Icons.DELETE, on_click=lambda e: on_delete(self)),
        ]

    def get_initials(self, user_name: str):
        return user_name[:1].capitalize() if user_name else "?"

    def get_avatar_color(self, user_name: str):
        colors = [ft.Colors.AMBER, ft.Colors.BLUE, ft.Colors.GREEN, ft.Colors.RED]
        return colors[hash(user_name) % len(colors)]
