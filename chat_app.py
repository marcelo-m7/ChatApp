import flet as ft


class Message:
    def __init__(self, user_name: str, text: str, message_type: str):
        self.user_name = user_name
        self.text = text
        self.message_type = message_type


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


def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.title = "Flet Chat"

    def join_chat_click(e):
        if not join_user_name.value:
            join_user_name.error_text = "Name cannot be blank!"
            join_user_name.update()
        else:
            page.session.set("user_name", join_user_name.value)
            welcome_dlg.open = False
            new_message.prefix = ft.Text(f"{join_user_name.value}: ")
            page.pubsub.send_all(
                Message(
                    user_name=join_user_name.value,
                    text=f"{join_user_name.value} has joined the chat.",
                    message_type="login_message",
                )
            )
            page.update()

    def send_message_click(e):
        if new_message.value != "":
            page.pubsub.send_all(
                Message(
                    page.session.get("user_name"),
                    new_message.value,
                    message_type="chat_message",
                )
            )
            new_message.value = ""
            new_message.focus()
            page.update()

    def on_edit(chat_message):
        def save_edit(e):
            chat_message.message.text = edit_field.value
            chat_message.controls[1].controls[1] = ft.Text(chat_message.message.text, selectable=True)
            page.update()
            edit_dlg.open = False
            page.update()
        
        edit_field = ft.TextField(value=chat_message.message.text)
        edit_dlg = ft.AlertDialog(
            title=ft.Text("Edit Message"),
            content=edit_field,
            actions=[
                ft.ElevatedButton(text="Save", on_click=save_edit),
                ft.ElevatedButton(text="Cancel", on_click=lambda e: setattr(edit_dlg, "open", False) or page.update()),
            ]
        )
        page.dialog = edit_dlg
        edit_dlg.open = True
        page.update()

    def on_delete(chat_message):
        chat.controls.remove(chat_message)
        page.update()

    def on_message(message: Message):
        if message.message_type == "chat_message":
            m = ChatMessage(message, on_edit, on_delete)
        elif message.message_type == "login_message":
            m = ft.Text(message.text, italic=True, color=ft.Colors.BLACK45, size=12)
        chat.controls.append(m)
        page.update()

    page.pubsub.subscribe(on_message)

    join_user_name = ft.TextField(label="Enter your name to join the chat", autofocus=True, on_submit=join_chat_click)
    welcome_dlg = ft.AlertDialog(
        open=True,
        modal=True,
        title=ft.Text("Welcome!"),
        content=ft.Column([join_user_name], width=300, height=70, tight=True),
        actions=[ft.ElevatedButton(text="Join chat", on_click=join_chat_click)],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    page.overlay.append(welcome_dlg)

    chat = ft.ListView(expand=True, spacing=10, auto_scroll=True)

    new_message = ft.TextField(
        hint_text="Write a message...",
        autofocus=True,
        shift_enter=True,
        min_lines=1,
        max_lines=5,
        filled=True,
        expand=True,
        on_submit=send_message_click,
    )

    page.add(
        ft.Container(content=chat, border=ft.border.all(1, ft.Colors.OUTLINE), border_radius=5, padding=10, expand=True),
        ft.Row([
            new_message,
            ft.IconButton(icon=ft.Icons.SEND_ROUNDED, tooltip="Send message", on_click=send_message_click),
        ]),
    )


ft.app(target=main, view=ft.WEB_BROWSER)