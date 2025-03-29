import flet as ft

class WelcomeDialog:
    def __init__(self, on_submit):
        self.join_user_name = ft.TextField(
            label="Digite seu nome para entrar no chat",
            autofocus=True,
            on_submit=on_submit,
        )
        self.dialog = ft.AlertDialog(
            open=True,
            modal=True,
            title=ft.Text("Bem-vindo!"),
            content=ft.Column([self.join_user_name], width=300, height=70, tight=True),
            actions=[ft.ElevatedButton(text="Entrar no chat", on_click=on_submit)],
            actions_alignment=ft.MainAxisAlignment.END,
        )

class NewRoomDialog:
    def __init__(self, on_submit):
        self.room_name_field = ft.TextField(
            label="Nome da sala", 
            hint_text="TP1 Computação Móvel", 
            width=300, 
            autofocus=True, 
            on_submit=on_submit
        )
        self.room_id_field = ft.TextField(
            label="ID da sala", 
            hint_text="tp_1_cm", 
            width=300, 
            on_submit=on_submit
        )
        self.dialog = ft.AlertDialog(
            title=ft.Text("Criar nova sala"),
            open=False,
            modal=True,
            content=ft.Column([self.room_name_field, self.room_id_field], expand=True, width=300, height=100, tight=True),
            actions=[
                ft.ElevatedButton(text="Criar sala", on_click=on_submit),
                ft.ElevatedButton(text="Cancelar", on_click=lambda e: self.close(e)),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

    def open(self):
        self.dialog.open = True

    def close(self, e):
        self.dialog.open = False
