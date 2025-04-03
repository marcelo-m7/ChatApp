import flet as ftdef main(page: ft.Page):    page.add(ft.Text(value="Hello, world!"))ft.app(main)

import flet as ftdef main(page: ft.Page):    chat = ft.Column()    new_message = ft.TextField()    def send_click(e):        chat.controls.append(ft.Text(new_message.value))        new_message.value = ""        page.update()    page.add(        chat, ft.Row(controls=[new_message, ft.ElevatedButton("Send", on_click=send_click)])    )ft.app(main)

page.pubsub.subscribe(on_message)

def on_message(message: Message):        chat.controls.append(ft.Text(f"{message.user}: {message.text}"))        page.update()

def send_click(e):        page.pubsub.send_all(Message(user=page.session_id, text=new_message.value))        new_message.value = ""        page.update()    page.add(chat, ft.Row([new_message, ft.ElevatedButton("Send", on_click=send_click)]))

import flet as ftclass Message():    def __init__(self, user: str, text: str):        self.user = user        self.text = textdef main(page: ft.Page):    chat = ft.Column()    new_message = ft.TextField()    def on_message(message: Message):        chat.controls.append(ft.Text(f"{message.user}: {message.text}"))        page.update()    page.pubsub.subscribe(on_message)    def send_click(e):        page.pubsub.send_all(Message(user=page.session_id, text=new_message.value))        new_message.value = ""        page.update()    page.add(chat, ft.Row([new_message, ft.ElevatedButton("Send", on_click=send_click)]))ft.app(main)

user_name = ft.TextField(label="Enter your name")    page.dialog = ft.AlertDialog(        open=True,        modal=True,        title=ft.Text("Welcome!"),        content=ft.Column([user_name], tight=True),        actions=[ft.ElevatedButton(text="Join chat", on_click=join_click)],        actions_alignment="end",    )

class Message():    def __init__(self, user: str, text: str, message_type: str):        self.user = user        self.text = text        self.message_type = message_type

def on_message(message: Message):    if message.message_type == "chat_message":        chat.controls.append(ft.Text(f"{message.user}: {message.text}"))    elif message.message_type == "login_message":        chat.controls.append(            ft.Text(message.text, italic=True, color=ft.Colors.BLACK45, size=12)        )    page.update()

def join_click(e):    if not user_name.value:        user_name.error_text = "Name cannot be blank!"        user_name.update()    else:        page.session.set("user_name", user_name.value)        page.dialog.open = False        page.pubsub.send_all(Message(user=user_name.value, text=f"{user_name.value} has joined the chat.", message_type="login_message"))        page.update()

def send_click(e):    page.pubsub.send_all(Message(user=page.session.get('user_name'), text=new_message.value, message_type="chat_message"))    new_message.value = ""    page.update()

class ChatMessage(ft.Row):    def __init__(self, message: Message):        super().__init__()        self.vertical_alignment = ft.CrossAxisAlignment.START        self.controls=[                ft.CircleAvatar(                    content=ft.Text(self.get_initials(message.user_name)),                    color=ft.Colors.WHITE,                    bgcolor=self.get_avatar_color(message.user_name),                ),                ft.Column(                    [                        ft.Text(message.user_name, weight="bold"),                        ft.Text(message.text, selectable=True),                    ],                    tight=True,                    spacing=5,                ),            ]    def get_initials(self, user_name: str):        return user_name[:1].capitalize()    def get_avatar_color(self, user_name: str):        colors_lookup = [            ft.Colors.AMBER,            ft.Colors.BLUE,            ft.Colors.BROWN,            ft.Colors.CYAN,            ft.Colors.GREEN,            ft.Colors.INDIGO,            ft.Colors.LIME,            ft.Colors.ORANGE,            ft.Colors.PINK,            ft.Colors.PURPLE,            ft.Colors.RED,            ft.Colors.TEAL,            ft.Colors.YELLOW,        ]        return colors_lookup[hash(user_name) % len(colors_lookup)]

def on_message(message: Message):        if message.message_type == "chat_message":            m = ChatMessage(message)        elif message.message_type == "login_message":            m = ft.Text(message.text, italic=True, color=ft.Colors.BLACK45, size=12)        chat.controls.append(m)        page.update()

# Chat messages    chat = ft.ListView(        expand=True,        spacing=10,        auto_scroll=True,    )    # A new message entry form    new_message = ft.TextField(        hint_text="Write a message...",        autofocus=True,        shift_enter=True,        min_lines=1,        max_lines=5,        filled=True,        expand=True,        on_submit=send_message_click,    )    # Add everything to the page    page.add(        ft.Container(            content=chat,            border=ft.border.all(1, ft.Colors.OUTLINE),            border_radius=5,            padding=10,            expand=True,        ),        ft.Row(            [                new_message,                ft.IconButton(                    icon=ft.Icons.SEND_ROUNDED,                    tooltip="Send message",                    on_click=send_message_click,                ),            ]        ),    )

page.title = "Flet Chat"page.update()

