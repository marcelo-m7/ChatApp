import os
import flet as ft
from chat.chat_app import ChatApp
from chat.chat_message import ChatMessage
from chat.message import Message
from assistants.assistants import Assistants


class ChatInterface:
    programador_assistant = Assistants(nome="Programador") 
    def __init__(self, page: ft.Page):
        self.page = page
        self.chat_app = ChatApp()
        self.page.title = "Chat em Tempo Real"

        # Criando componentes principais
        self.new_message = ft.TextField(
            hint_text="Escreva uma mensagem...",
            autofocus=True,
            shift_enter=True,
            min_lines=1,
            max_lines=5,
            filled=True,
            expand=True,
            on_submit=self.send_message_click,
        )

        self.chat = ft.ListView(expand=True, spacing=10, auto_scroll=True)

        self.file_picker = ft.FilePicker(
            on_result=self.pick_files_result,
            on_upload=self.on_upload_progress,
        )

        self.page.overlay.append(self.file_picker)
        self.page.pubsub.subscribe(self.on_message)

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

        # Navegação entre salas
        self.room_rail = ft.NavigationRail(
            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            on_change=self.change_room,
            destinations=[
                ft.NavigationRailDestination(
                    icon=ft.Icons.CHAT_BUBBLE_OUTLINE,
                    selected_icon=ft.Icons.CHAT_BUBBLE,
                    label=room.name,
                ) for room in self.chat_app.rooms.values()
            ],
        )

        self.room_name = ft.Text(
            f"Sala: {self.chat_app.rooms[self.chat_app.current_room].name}",
            size=20, weight="bold"
        )

        # Layout principal
        self.content = ft.Column(
            [
                self.room_name,
                ft.Container(
                    content=self.chat,
                    border=ft.border.all(1, ft.Colors.OUTLINE),
                    border_radius=5,
                    padding=10,
                    expand=True,
                ),
                ft.Row(
                    [
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
                    ]
                ),
            ],
            expand=True,
        )

        self.page.add(
            ft.Row(
                [
                    self.room_rail,
                    ft.VerticalDivider(width=1),
                    self.content,
                ],
                expand=True,
            )
        )

    def send_message_click(self, e):
        if self.new_message.value.strip():
            message = Message(
                user_name=self.page.session.get("user_name"),
                text=self.new_message.value,
                message_type="chat_message",
                room_id=self.chat_app.current_room,
            )
            self.page.pubsub.send_all(message)
            self.new_message.value = ""
            self.new_message.focus()
            self.page.update()

    def change_room(self, e):
        selected_index = e.control.selected_index
        self.chat_app.current_room = list(self.chat_app.rooms.keys())[selected_index]
        self.room_name.value = f"Sala: {self.chat_app.rooms[self.chat_app.current_room].name}"
        self.chat.controls.clear()
        self.page.update()

    def pick_files_result(self, e: ft.FilePickerResultEvent):
        if e.files:
            file : ft.FilePickerFile
            for file in e.files:
                print(file)
                file_ext = os.path.splitext(file.name)[1].lower()
                allowed_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.pdf', '.doc', '.docx', '.txt']
                
                if file_ext not in allowed_extensions:

                    snack_bar = ft.SnackBar(ft.Text("Tipo de arquivo não permitido!"), open=True)
                    self.chat.controls.append(snack_bar)
                    self.page.update()
                    continue

                room_dir = os.path.join(self.chat_app.upload_dir, self.chat_app.rooms[self.chat_app.current_room].room_id)
                os.makedirs(room_dir, exist_ok=True)
                file_path = os.path.join(room_dir, file.name).replace('\\', '/')
                print(f"[DEBUG] Saving file to: {file_path}")

       
                snack_bar = ft.SnackBar(ft.Text(f"Arquivo enviado: {file.name}"), open=True)
                self.chat.controls.append(snack_bar)

                self.page.update()
                print("tentando do upload")

                try:
                    print(f"[DEBUG] Getting upload URL for {file.name}")
                    upload_url = self.page.get_upload_url(file_path, 60)
                    print(f"[DEBUG] Upload URL for {file.name}: {upload_url}")

                    if upload_url:
                        self.file_picker.upload([ft.FilePickerUploadFile(file.name, upload_url=upload_url)])
                    else:
                        print(f"[ERROR] Failed to get upload URL for {file.name}")

                    self.page.pubsub.send_all(
                        Message(
                            user_name=self.page.session.get("user_name"),
                            text=f"Arquivo compartilhado: {file.name}",
                            message_type="file_message",
                            room_id=self.chat_app.current_room,
                            file_path=file_path
                        )
                    )
                except Exception as ex:
                    snack_bar = ft.SnackBar(ft.Text(f"Erro ao enviar arquivo: {str(ex)}"), open=True)
                    self.chat.controls.append(snack_bar)
                    self.page.update()

    def on_upload_progress(self, e: ft.FilePickerUploadEvent):
        print(f"Upload progress: {e.progress}% for {e.file_name}")

    def join_chat_click(self, e):
        if not self.join_user_name.value.strip():
            self.join_user_name.error_text = "O nome não pode estar em branco!"
            self.join_user_name.update()
        else:
            self.page.session.set("user_name", self.join_user_name.value)
            self.welcome_dlg.open = False
            self.page.update()

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

            # Fecha o diálogo e atualiza a página
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
                                on_click=lambda _: self.page.launch_url(f"/download/{message.file_path}")
                            )
                        ]
                    )
            else:
                m = ft.Text(message.text, italic=True, color=ft.Colors.BLACK45, size=12)

        self.chat.controls.append(m)
        self.page.update()

        if message.room_id == "programador":
            assistant_response = self.programador_assistant.process_message(message)
            if assistant_response:
                assistant_response_control = ChatMessage(assistant_response, self.on_edit, self.on_delete)
                self.chat.controls.append(assistant_response_control)
                self.page.update()
