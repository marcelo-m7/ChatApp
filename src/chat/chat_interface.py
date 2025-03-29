import os
import flet as ft
from chat.chat_app import ChatApp
from chat.chat_message import ChatMessage
from chat.entities.message import Message
from assistants.assistants import Assistants
from chat.use_cases.dialogs import WelcomeDialog, NewRoomDialog
from chat.utils.file_handler import FileHandler

class ChatInterface:
    programador_assistant = Assistants(nome="Programador")

    def __init__(self, page: ft.Page, chat_app: ChatApp):
        self.page = page
        self.chat_app = chat_app
        self.page.title = "Chat em Tempo Real"

        # Instancia os componentes de diálogo e file handler
        self.welcome_dialog = WelcomeDialog(self.join_chat_click)
        self.new_room_dialog = NewRoomDialog(self.save_new_room)
        self.file_handler = FileHandler(self.page, self.chat_app, self.on_message)

        # Adiciona os diálogos à sobreposição da página
        self.page.overlay.append(self.welcome_dialog.dialog)
        self.page.overlay.append(self.new_room_dialog.dialog)

        # Inscreve-se para receber mensagens via pubsub
        self.page.pubsub.subscribe(self.on_message)

        # Criação dos componentes de interface
        self.__create_message_input()
        self.__create_chat_list()
        self.__create_room_drawer()
        self.__create_layout()
        # self.__create_snack_bar()

        self.welcome_dialog.join_user_name.focus()
        self.page.update()

    # def __create_snack_bar(self):
    #     self.snack_bar = ft.SnackBar(ft.Text(""), open=False)
    #     self.page.controls.append(self.snack_bar)

    def __create_message_input(self):
        self.new_message = ft.TextField(
            hint_text="Escreva uma mensagem...",
            autofocus=True,
            shift_enter=True,
            min_lines=1,
            max_lines=5,
            filled=True,
            expand=True,
            on_submit=self.send_message_click,
            border_radius=5,
        )
        self.input_bar = ft.Row(
            controls=[
                self.new_message,
                ft.IconButton(
                    icon=ft.Icons.FILE_UPLOAD,
                    tooltip="Compartilhar arquivo",
                    on_click=lambda _: self.file_handler.file_picker.pick_files(
                        allow_multiple=True,
                        allowed_extensions=['png', 'jpg', 'jpeg', 'gif', 'pdf', 'doc', 'docx', 'txt']
                    ),
                ),
                ft.IconButton(
                    icon=ft.Icons.SEND_ROUNDED,
                    tooltip="Enviar mensagem",
                    on_click=self.send_message_click,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.END,
            spacing=10,
        )

    def __create_chat_list(self):
        self.chat = ft.ListView(expand=True, spacing=10, auto_scroll=True)
    
    def __create_room_drawer(self):
        self.new_room_btn = ft.ElevatedButton(
            text="Nova sala",
            on_click=self.create_new_room_click,
            icon=ft.Icons.MEETING_ROOM,
            width=130,
        )
        self.update_room_drawer()

        self.menu_button = ft.IconButton(
            icon=ft.Icons.MENU,
            tooltip="Abrir menu de salas",
            on_click=lambda _: self.open_drawer(),
        )

    def __create_layout(self):
        self.room_name = ft.Text(
            f"Sala: {self.chat_app.rooms[self.chat_app.current_room].room.room_name}",
            size=20, weight="bold"
        )
        self.content = ft.Column(
            [
                ft.Row([self.menu_button, self.room_name], alignment=ft.MainAxisAlignment.START),
                ft.Container(
                    content=self.chat,
                    border=ft.border.all(1, ft.Colors.OUTLINE),
                    border_radius=5,
                    padding=10,
                    expand=True,
                ),
            ],
            expand=True,
        )
        self.page.add(
            ft.Column(
                [
                    self.content,
                    ft.Container(
                        content=self.input_bar,
                        padding=10,
                        border_radius=5,
                        alignment=ft.alignment.bottom_center,
                    ),
                ],
                expand=True,
            )
        )

    def update_room_drawer(self):
        # Atualiza a lista de salas dinamicamente
        self.room_drawer = ft.NavigationDrawer(
            controls=[ft.Container(height=12),
                      ft.Text("Salas de Chat", size=18, weight="bold", text_align="center"),
                      ft.Divider()] +
                     [
                        ft.ListTile(
                            leading=ft.Icon(ft.Icons.CHAT_BUBBLE_OUTLINE),
                            title=ft.Text(value.room.room_name),
                            on_click=lambda e, room_id=key: self.change_room_by_id(room_id),
                        ) for key, value in self.chat_app.rooms.items()
                     ] + [
                        ft.Divider(),
                        ft.Row([self.new_room_btn], alignment=ft.MainAxisAlignment.CENTER),
                     ]
        )
        self.page.drawer = self.room_drawer

    def open_drawer(self):
        self.page.drawer.open = True
        self.page.update()

    def change_room_by_id(self, room_id):
        self.chat_app.current_room = room_id
        self.room_name.value = f"Sala: {self.chat_app.rooms[self.chat_app.current_room].room.room_name}"
        self.chat.controls.clear()
        for msg in self.chat_app.rooms[self.chat_app.current_room].room.messages:
            chat_msg = ChatMessage(msg, self.on_edit, self.on_delete)
            self.chat.controls.append(chat_msg)
        self.page.drawer.open = False
        self.page.update()

    def save_new_room(self, e):
        room_name = self.new_room_dialog.room_name_field.value.strip()
        room_id = self.new_room_dialog.room_id_field.value.strip()
        if not room_name:
            self.new_room_dialog.room_name_field.error_text = "O nome não pode estar em branco!"
            self.page.update()
            return
        elif not room_id:
            self.new_room_dialog.room_id_field.error_text = "O ID não pode estar em branco!"
            self.page.update()
            return
        self.chat_app.new_room(room_id, room_name)
        self.update_room_drawer()
        self.new_room_dialog.dialog.open = False
        self.page.update()

    def create_new_room_click(self, e):
        self.new_room_dialog.room_name_field.value = ""
        self.new_room_dialog.room_id_field.value = ""
        self.new_room_dialog.open()
        self.page.update()

    def send_message_click(self, e):
        if self.new_message.value.strip():
            message = Message(
                user_name=self.page.session.get("user_name"),
                text=self.new_message.value,
                message_type="chat_message",
                room_id=self.chat_app.current_room,
            )
            self.on_message(message)
            self.new_message.value = ""
            self.new_message.focus()
            self.page.update()

    def join_chat_click(self, e):
        if not self.welcome_dialog.join_user_name.value.strip():
            self.welcome_dialog.join_user_name.error_text = "O nome não pode estar em branco!"
            self.welcome_dialog.join_user_name.update()
        else:
            self.page.session.set("user_name", self.welcome_dialog.join_user_name.value)
            self.chat_app.add_user(self.welcome_dialog.join_user_name.value)
            self.welcome_dialog.dialog.open = False

            # Carrega as mensagens existentes da sala atual
            for msg in self.chat_app.rooms[self.chat_app.current_room].room.messages:
                chat_msg = ChatMessage(msg, self.on_edit, self.on_delete)
                self.chat.controls.append(chat_msg)
            self.page.update()

    def on_edit(self, chat_message: ChatMessage):
        def save_edit(e):
            chat_message.message.text = edit_field.value
            # Atualiza a interface da mensagem editada
            chat_message.controls[1].controls[1].value = chat_message.message.text  
            chat_message.controls[1].controls[1].update()
            chat_message.update()
            edit_dlg.open = False
            self.page.update()

        edit_field = ft.TextField(value=chat_message.message.text)
        edit_dlg = ft.AlertDialog(
            title=ft.Text("Editar Mensagem"),
            content=edit_field,
            actions=[
                ft.ElevatedButton(text="Salvar", on_click=save_edit),
                ft.ElevatedButton(text="Cancelar", on_click=lambda e: setattr(edit_dlg, "open", False) or self.page.update()),
            ],
        )
        self.page.overlay.append(edit_dlg)
        edit_dlg.open = True
        self.page.update()

    def on_delete(self, chat_message: ChatMessage):
        self.chat.controls.remove(chat_message)
        self.page.update()

    def on_message(self, message: Message):
        # Processa apenas mensagens da sala atual
        if message.room_id != self.chat_app.current_room:
            return

        if message.message_type == "chat_message":
            m = ChatMessage(message, self.on_edit, self.on_delete)
        elif message.message_type == "login_message":
            m = ft.Text(message.text, italic=True, color=ft.Colors.WHITE, size=12)
        elif message.message_type == "file_message":
            file_ext = os.path.splitext(message.file_path)[1].lower()
            if file_ext in ['.png', '.jpg', '.jpeg', '.gif']:
                m = ft.Column([
                    ft.Text(f"{message.user_name} compartilhou uma imagem:"),
                    ft.Image(src=message.file_path, width=200, height=200, visible=True, fit=ft.ImageFit.CONTAIN)
                ])
            else:
                m = ft.Column([
                    ft.Text(f"{message.user_name} compartilhou um arquivo:"),
                    ft.ElevatedButton(
                        text=os.path.basename(message.file_path),
                        on_click=lambda _: self.page.launch_url(message.file_url)
                    )
                ])
        else:
            m = ft.Text(message.text, italic=True, color=ft.Colors.BLACK45, size=12)

        self.chat_app.rooms[self.chat_app.current_room].add_message(message)
        self.chat.controls.append(m)
        self.page.update()

        # Se for mensagem para o "assistente programador", processa a resposta
        if message.room_id == "programador":
            assistant_response = self.programador_assistant.process_message(message)
            if assistant_response:
                response_control = ChatMessage(assistant_response, self.on_edit, self.on_delete)
                self.chat.controls.append(response_control)
                self.page.update()
