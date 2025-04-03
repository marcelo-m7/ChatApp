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
        self.user_name: str
        self.current_room = self.page.session.get("current_room") or self.chat_app.current_room

        # Instancia os componentes de diálogo e file handler
        self.welcome_dialog = WelcomeDialog(self.join_chat_click)
        self.new_room_dialog = NewRoomDialog(self.save_new_room)
        self.file_handler = FileHandler(self.page, self.chat_app, self.on_message)

        # Adiciona os diálogos à sobreposição da página
        self.page.overlay.append(self.welcome_dialog.dialog)
        self.page.overlay.append(self.new_room_dialog.dialog)

        # Inscreve-se para receber mensagens via pubsub
        self.page.pubsub.subscribe(self.on_message)

        # Cria os componentes da interface divididos em blocos
        self.__create_menu_drawer()  # Menu lateral com salas e usuários online
        self.__create_chatbox()       # Área principal com chat e inputs

        # Foco para o nome de usuário e atualiza a página
        self.welcome_dialog.join_user_name.focus()
        self.page.update()


    # ========================
    # Criação do Menu Drawer
    # ========================
    def __create_menu_drawer(self):
        # Cria a parte de salas de chat
        self.__create_rooms_drawer()
        # Cria a parte de usuários online, utilizando active_users
        self.__create_users_drawer()

        # Junta as duas divisões em um NavigationDrawer
        self.menu_drawer = ft.NavigationDrawer(
            controls=[
                # Bloco de salas
                ft.Column(
                    controls=[
                        ft.Container(height=12),
                        ft.Text("Salas de Chat", size=18, weight="bold", text_align="center"),
                        ft.Divider(),
                        *self.rooms_drawer_controls  # Lista de ListTile das salas
                    ],
                    expand=True,
                ),
                # Bloco de usuários
                ft.Column(
                    controls=[
                        ft.Divider(),
                        ft.Text("Usuários Online", size=16, weight="bold", text_align="center"),
                        *self.users_drawer_controls  # Lista de ListTile dos usuários
                    ],
                    alignment=ft.MainAxisAlignment.END
                ),
                ft.Row([self.new_room_btn], alignment=ft.MainAxisAlignment.CENTER),
            ]
        )
        # Atualiza a página para que o drawer seja o novo menu_drawer
        self.page.drawer = self.menu_drawer

        self.menu_button = ft.IconButton(
            icon=ft.Icons.MENU,
            tooltip="Abrir menu",
            on_click=lambda _: self.open_drawer(),
        )

    def __create_rooms_drawer(self):
        # Botão para criar nova sala
        self.new_room_btn = ft.ElevatedButton(
            text="Nova sala",
            on_click=self.create_new_room_click,
            icon=ft.Icons.MEETING_ROOM,
            width=130,
        )
        # Cria controles para as salas de chat
        self.rooms_drawer_controls = [
            ft.ListTile(
                leading=ft.Icon(ft.Icons.CHAT_BUBBLE_OUTLINE),
                title=ft.Text(value.room.room_name),
                on_click=lambda e, room_id=key: self.change_room_by_id(room_id),
            ) for key, value in self.chat_app.rooms.items()
        ]

    def __create_users_drawer(self):
        # Obtém os nomes dos usuários ativos a partir do dicionário active_users
        current_users = [user.user_name for user in self.chat_app.active_users.values()]
        self.users_drawer_controls = [
            ft.ListTile(
                leading=ft.Icon(ft.Icons.ACCOUNT_CIRCLE),
                title=ft.Text(user),
                on_click=lambda e, user=user: self.send_private_message(user),
            ) for user in current_users
        ]

    def update_users_drawer(self):
        # Atualiza dinamicamente a lista de usuários online utilizando active_users
        current_users = [user.user_name for user in self.chat_app.active_users.values()]
        self.users_drawer_controls = [
            ft.ListTile(
                leading=ft.Icon(ft.Icons.ACCOUNT_CIRCLE),
                title=ft.Text(user),
                on_click=lambda e, user=user: self.send_private_message(user),
            ) for user in current_users
        ]
        # Atualiza o bloco de usuários dentro do menu_drawer
        self.menu_drawer.controls[-2] = ft.Column(
            controls=[
                ft.Divider(),
                ft.Text("Usuários Online", size=16, weight="bold", text_align="center"),
                *self.users_drawer_controls
            ],
            alignment=ft.MainAxisAlignment.END
        )
        self.page.update()

    def open_drawer(self):
        self.page.drawer.open = True
        self.page.update()

    # ========================
    # Criação do ChatBox
    # ========================
    def __create_chatbox(self):
        # Cria o ChatRoom (área de exibição das mensagens)
        self.__create_chat_room()
        # Cria o UserFormulary (inputs para envio de mensagem e arquivos)
        self.__create_user_formulary()

        # Junta os dois blocos em um container principal
        self.chatbox = ft.Column(
            controls=[
                # Cabeçalho com menu e identificação da sala
                ft.Row([self.menu_button, self.room_name], alignment=ft.MainAxisAlignment.START),
                # ChatRoom
                self.chat_room_container,
                # UserFormulary
                self.user_formulary_container,
            ],
            expand=True,
        )
        self.page.add(self.chatbox)

    def __create_chat_room(self):
        # Área de exibição das mensagens do chat
        self.chat = ft.ListView(expand=True, spacing=10, auto_scroll=True)
        self.chat_room_container = ft.Container(
            content=self.chat,
            border=ft.border.all(1, ft.Colors.OUTLINE),
            border_radius=5,
            padding=10,
            expand=True,
        )
        # Exibe o nome da sala atual
        self.room_name = ft.Text(
            f"Sala: {self.chat_app.rooms[self.current_room].room.room_name}",
            size=20, weight="bold"
        )

    def __create_user_formulary(self):
        # Campo para nova mensagem
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
        # Barra de envio com botões para upload e envio
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
        self.user_formulary_container = ft.Container(
            content=self.input_bar,
            padding=10,
            border_radius=5,
            alignment=ft.alignment.bottom_center,
        )

    # ========================
    # Outros Métodos de Ação
    # ========================
    def send_private_message(self, user: str):
        print("Enviando mensagem privada para: ", user)
        reciver = user.strip().lower()
        owner = self.user_id
        private_room_id = str(owner+reciver).lower()
        
        # Debito técnico para possibilitar criações de sala com mais user
        if private_room_id in self.chat_app.rooms.keys():
            self.change_room_by_id(private_room_id)
            return
        
        private_room_id2 = str(reciver+owner).lower()
        if private_room_id2 in self.chat_app.rooms.keys():
            self.change_room_by_id(private_room_id2)
            return
        
        private_room_id = self.chat_app.new_private_room(owner=self.user_name, reciver=user, room_id=private_room_id)
        self.change_room_by_id(private_room_id)
        
    def change_room_by_id(self, room_id):
        print(f"Changing room to: {room_id}")
        self.page.session.set("current_room", room_id)
        # self.current_room = room_id
        self.current_room = room_id
        self.room_name.value = f"Sala: {self.chat_app.rooms[room_id].room.room_name}"
        self.chat.controls.clear()
        for msg in self.chat_app.rooms[room_id].room.messages:
            self.on_message(msg) 
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
        self.new_room_dialog.dialog.open = False
        self.__create_menu_drawer()
        self.page.update()

    def create_new_room_click(self, e):
        self.new_room_dialog.room_name_field.value = ""
        self.new_room_dialog.room_id_field.value = ""
        self.new_room_dialog.open()
        self.page.update()

    def send_message_click(self, e):
        if self.new_message.value.strip():
            message = Message(
                user_name=self.user_name,
                text=self.new_message.value,
                message_type="chat_message",
                room_id=self.current_room,
            )

            self.chat_app.add_message_to_room(message)
            self.page.pubsub.send_all(message)

            self.new_message.value = ""
            self.new_message.focus()
            self.page.update()

    def join_chat_click(self, e):
        user_name = self.welcome_dialog.join_user_name.value
        user_id = self.welcome_dialog.join_user_name.value.strip().lower()

        if not user_name:
            self.welcome_dialog.join_user_name.error_text = "O nome não pode estar em branco!"
            self.welcome_dialog.join_user_name.update()
        else:
            self.page.session.set("user_name", user_name)
            self.page.session.set("user_id", user_id)
            self.page.session.set("current_room", 'geral')
            self.user_name = self.page.session.get("user_name")
            self.user_id = self.page.session.get("user_id")
            self.current_room = self.page.session.get("current_room")

            self.chat_app.add_user(user_name=self.user_name, user_id=self.user_id)
            self.welcome_dialog.dialog.open = False

            # Carrega as mensagens existentes da sala atual
            for msg in self.chat_app.rooms[self.current_room].room.messages:
                self.on_message(msg) 

            self.page.update()
            
            # Atualiza o drawer para que os usuários conectados vejam a lista atualizada
            msg = Message(user_name=user_name,
                          text=f"{user_name} entrou no chat.",
                          message_type="login_message",
                          room_id=self.current_room)
            
            self.chat_app.add_message_to_room(msg)
            self.page.pubsub.send_all(msg)

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
        if message.room_id != self.page.session.get("current_room"):
            return

        if message.message_type == "chat_message":
            m = ChatMessage(message, self.on_edit, self.on_delete)
            print("Messagem enviada: \n", message)
        
        if message.message_type == "login_message":
            m = ft.Text(message.text, italic=True, color=ft.Colors.WHITE, size=12)
            self.chat.controls.append(m)
            self.update_users_drawer()
            self.page.update()
            return
        
        elif message.room_id == "programador":
            assistant_response = self.programador_assistant.process_message(message)
            if assistant_response:
                ass_m = ChatMessage(assistant_response, self.on_edit, self.on_delete)
                self.chat.controls.append(ass_m)
                self.page.update()

        elif message.message_type == "file_message":
            file_ext = os.path.splitext(message.file.file_path)[1].lower()
            if file_ext in ['.png', '.jpg', '.jpeg', '.gif']:
                m = ft.Column([
                    ft.Text(f"{message.user_name} compartilhou uma imagem:"),
                    ft.Image(src=message.file.file_path, width=200, height=200, visible=True, fit=ft.ImageFit.CONTAIN)
                ])
            else:
                m = ft.Column([
                    ft.Text(f"{message.user_name} compartilhou um arquivo:"),
                    ft.ElevatedButton(
                        text=os.path.basename(message.file.file_path),
                        on_click=lambda _: self.page.launch_url(message.file.file_url)
                    )
                ])

        self.chat.controls.append(m)
        self.page.update()

        if message.room_id == "programador":
            assistant_response = self.programador_assistant.process_message(message)
            if assistant_response:
                ass_m = ChatMessage(assistant_response, self.on_edit, self.on_delete)
                self.chat.controls.append(ass_m)
                self.page.update()