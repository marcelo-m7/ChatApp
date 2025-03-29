import os
import flet as ft
from chat.chat_app import ChatApp
from chat.chat_message import ChatMessage
from chat.entities.message import Message
from assistants.assistants import Assistants

class ChatInterface:
    programador_assistant = Assistants(nome="Programador") 
    
    def __init__(self, page: ft.Page, chat_app: ChatApp):
        self.page = page
        self.chat_app = chat_app
        self.page.title = "Chat em Tempo Real"
        
        self.file_picker = ft.FilePicker(
            on_result=self.pick_files_result,
            on_upload=self.on_upload_progress,
        )
        
        self.page.overlay.append(self.file_picker)
        self.page.pubsub.subscribe(self.on_message)

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

        self.chat = ft.ListView(expand=True, spacing=10, auto_scroll=True)

        # Caixa de diálogo de boas-vindas
        self.join_user_name = ft.TextField(
            label="Digite seu nome para entrar no chat",
            autofocus=True,
            on_submit=self.join_chat_click,
        )

        self.welcome_dlg = ft.AlertDialog(
            open=True,
            modal=True,
            title=ft.Text("Bem-vindo!"),
            content=ft.Column([self.join_user_name], width=300, height=70, tight=True),
            actions=[ft.ElevatedButton(text="Entrar no chat", on_click=self.join_chat_click)],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        
        self.page.overlay.append(self.welcome_dlg)
        
        self.new_room_btn = ft.ElevatedButton(
            text="Nova sala",
            on_click=lambda e: self.create_new_room_click(e),
            icon=ft.Icons.MEETING_ROOM,
            width=130,
        )
        # Drawer (Menu Lateral)
        self.room_drawer = ft.NavigationDrawer(
            controls=[
                ft.Container(height=12),
                ft.Text("Salas de Chat", size=18, weight="bold", text_align="center"),
                ft.Divider(),
            ] + [
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.CHAT_BUBBLE_OUTLINE),
                    title=ft.Text(value.room.room_name),
                    on_click=lambda e, room_id=key: self.change_room_by_id(room_id),
                ) for key, value in self.chat_app.rooms.items()
            ] + [
                ft.Divider(),
                ft.Row([self.new_room_btn], alignment=ft.MainAxisAlignment.CENTER),
                # ft.Text("Criar sala", size=18, weight="bold", text_align="center"),
            ]

        )

        self.room_name = ft.Text(
            f"Sala: {self.chat_app.rooms[self.chat_app.current_room].room.room_name}",
            size=20, weight="bold"
        )

        self.room_name_field = ft.TextField(label="Nome da sala", hint_text="TP1 Computação Móvel", width=300, autofocus=True, on_submit=self.save_new_room)
        self.room_id_field = ft.TextField(label="ID da sala", hint_text="tp_1_cm", width=300, on_submit=self.save_new_room)
        
        self.new_room_dlg = ft.AlertDialog(
            title=ft.Text("Criar nova sala"),
            open=False,
            modal=True,
            content=ft.Column([self.room_name_field, self.room_id_field], expand=True, width=300, height=100, tight=True),
            actions=[
                ft.ElevatedButton(text="Criar sala", on_click=lambda e: self.save_new_room(e)),
                ft.ElevatedButton(text="Cancelar", on_click=lambda e: setattr(self.new_room_dlg, "open", False) or self.page.update()),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        self.page.overlay.append(self.new_room_dlg)
        setattr(self.new_room_dlg, "open", False)

        # Botão de menu para abrir o Drawer
        self.menu_button = ft.IconButton(
            icon=ft.Icons.MENU,
            tooltip="Abrir menu de salas",
            on_click=lambda _: setattr(self.page.drawer, "open", True) or self.page.update(),
        )

        # Layout principal
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

        # Barra fixa de envio de mensagens
        self.input_bar = ft.Row(
            controls=[
                self.new_message,
                ft.IconButton(
                    icon=ft.Icons.FILE_UPLOAD,
                    tooltip="Compartilhar arquivo",
                    on_click=lambda _: self.file_picker.pick_files(
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

        # Estrutura final da página
        self.page.drawer = self.room_drawer
        self.page.add(
            ft.Column(
                [
                    self.content,
                    ft.Container(
                        content=self.input_bar,
                        padding=10,
                        # bgcolor=ft.Colors.GREY_200,
                        border_radius=5,
                        alignment=ft.alignment.bottom_center,
                    ),
                ],
                expand=True,
            )
        )
        
        self.join_user_name.focus()
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
        room_name = self.room_name_field.value.strip()
        room_id = self.room_id_field.value.strip()
        if not room_name:
            self.room_name_field.error_text = "O nome não pode estar em branco!"
            self.page.update()
            return
        elif not room_id:
            self.room_id_field.error_text = "O ID não pode estar em branco!"
            self.page.update()
            return
        self.chat_app.new_room(room_id, room_name)
        self.page.update()

        # Atualiza a lista de salas no Drawer
        self.room_drawer = ft.NavigationDrawer(
            controls=[
                ft.Container(height=12),
                ft.Text("Salas de Chat", size=18, weight="bold", text_align="center"),
                ft.Divider(),
            ] + [
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.CHAT_BUBBLE_OUTLINE),
                    title=ft.Text(value.room.room_name),
                    on_click=lambda e, room_id=key: self.change_room_by_id(room_id),
                ) for key, value in self.chat_app.rooms.items()
            ] + [
                ft.Divider(),
                ft.Row([self.new_room_btn], alignment=ft.MainAxisAlignment.CENTER),
                # ft.Text("Criar sala", size=18, weight="bold", text_align="center"),
            ]

        )
        self.page.drawer = self.room_drawer
        
        self.new_room_dlg.open = False
        self.page.update()
  
    def create_new_room_click(self, e):
        setattr(self.new_room_dlg, "open", True)
        self.room_name_field.value = ""
        self.room_id_field.value = ""
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
        if not self.join_user_name.value.strip():
            self.join_user_name.error_text = "O nome não pode estar em branco!"
            self.join_user_name.update()
        else:
            self.page.session.set("user_name", self.join_user_name.value)
            self.chat_app.add_user(self.join_user_name.value)
            self.welcome_dlg.open = False

            for msg in self.chat_app.rooms[self.chat_app.current_room].room.messages:
                chat_msg = ChatMessage(msg, self.on_edit, self.on_delete)
                self.chat.controls.append(chat_msg)
            self.page.update()

    def pick_files_result(self, e: ft.FilePickerResultEvent):
        if e.files:
            # file : ft.FilePickerFileType
            for file in e.files:
                print(file)
                file_ext = os.path.splitext(file.name)[1].lower()
                allowed_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.pdf', '.doc', '.docx', '.txt']
                
                if file_ext not in allowed_extensions:
                    snack_bar = ft.SnackBar(ft.Text("Tipo de arquivo não permitido!"), open=True)
                    self.chat.controls.append(snack_bar)
                    self.page.update()
                    continue

                try:
                    print(f"[DEBUG] File name: {file.name}: \nFile size:{file.size}")

                    upload_url = self.page.get_upload_url(file.name, 60)
                    if upload_url:
                        self.file_picker.upload([ft.FilePickerUploadFile(file.name, upload_url=upload_url)])

                        snack_bar = ft.SnackBar(ft.Text(f"Arquivo enviado: {file.name}, Tamanho: {file.size}"), open=True)
                        print("File: \n", file)
                        self.chat.controls.append(snack_bar)
                        self.page.update()
                        file_path = os.path.join(self.chat_app.upload_dir, file.name).replace('\\', '/')

                        message = Message(
                            user_name=self.page.session.get("user_name"),
                            text=f"Arquivo compartilhado: {file.name}",
                            message_type="file_message",
                            room_id=self.chat_app.current_room,
                            file_url=self.chat_app.download_url.format(filename=file.name), 
                            file_name=file.name,
                            file_path=file_path
                        )
                        
                        self.on_message(message)

                    else:
                        print(f"[ERROR] Failed to get upload URL for {file.name}")

                    # self.page.pubsub.send_all(
                except Exception as ex:
                    snack_bar = ft.SnackBar(ft.Text(f"Erro ao enviar arquivo: {str(ex)}"), open=True)
                    snack_bar = print(f"Erro ao enviar arquivo: {str(ex)}")
                    self.chat.controls.append(snack_bar)
                    self.page.update()

    def on_upload_progress(self, e: ft.FilePickerUploadEvent):
        print(f"Upload progress: {e.progress}% for {e.file_name}")

    def on_edit(self, chat_message: ChatMessage):
        print("Botão de editar clicado")  # Depuração

        def save_edit(e):
            print("Salvando mensagem:", edit_field.value)

            # Atualiza o texto da mensagem e a UI correspondente
            chat_message.message.text = edit_field.value
            chat_message.controls[1].controls[1].value = chat_message.message.text  

            # Atualiza a interface do chat
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

        # Adiciona o diálogo à sobreposição da página
        self.page.overlay.append(edit_dlg)  

        # Abre o diálogo e atualiza a página
        edit_dlg.open = True  
        self.page.update()  

    def on_delete(self, chat_message):
        self.chat.controls.remove(chat_message)
        self.page.update()
        
    def on_message(self, message: Message):
        # Só processa mensagens da sala atual
        if message.room_id != self.chat_app.current_room:
            return
        if message.message_type == "chat_message":
            m = ChatMessage(message, self.on_edit, self.on_delete)
        elif message.message_type == "login_message":
            m = ft.Text(message.text, italic=True, color=ft.Colors.WHITE, size=12)
        elif message.message_type == "file_message":
            print(f"Received file message: {message}")
            if message.file_url:
                file_ext = os.path.splitext(message.file_path)[1].lower()
                if file_ext in ['.png', '.jpg', '.jpeg', '.gif']:
                    print(f"Displaying image preview for: {message.file_path}")
                    m = ft.Column(
                        [
                            ft.Text(f"{message.user_name} compartilhou uma imagem:"),
                            ft.Image(src=f"{message.file_path}", width=200, height=200, visible=True, fit=ft.ImageFit.CONTAIN)
                        ]
                    )

                else:
                    print(f"Displaying file download for: {message.file_path}")
                    m = ft.Column(
                        [
                            ft.Text(f"{message.user_name} compartilhou um arquivo:"),
                            ft.ElevatedButton(
                                text=os.path.basename(message.file_path),
                                on_click=lambda _: self.page.launch_url(message.file_url)
                            )
                        ]
                    )
                
            else:
                m = ft.Text(message.text, italic=True, color=ft.Colors.BLACK45, size=12)

        self.chat_app.rooms[self.chat_app.current_room].add_message(message)
        self.chat.controls.append(m)
        self.page.update()

        if message.room_id == "programador":
            assistant_response = self.programador_assistant.process_message(message)
            if assistant_response:
                assistant_response_control = ChatMessage(assistant_response, self.on_edit, self.on_delete)
                self.chat.controls.append(assistant_response_control)
                self.page.update()
