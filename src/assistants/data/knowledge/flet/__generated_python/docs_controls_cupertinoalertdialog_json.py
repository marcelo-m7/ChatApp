cupertino_actions = [...]
    material_actions = [...]

def handle_action_click(e):
        page.add(ft.Text(f"Action clicked: {e.control.text}"))
        page.close(e.control.parent)

ft.app(main)

import flet as ft

def main(page: ft.Page):

import flet as ft

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = True

    def handle_action_click(e):
        page.add(ft.Text(f"Ação selecionada: {e.control.text}"))
        page.close(e.control.parent)

    actions = [
        ft.TextButton(text="Confirmar", on_click=handle_action_click, bgcolor=ft.colors.GREEN, color=ft.colors.WHITE),
        ft.TextButton(text="Cancelar", on_click=handle_action_click, bgcolor=ft.colors.RED, color=ft.colors.WHITE),
    ]

    def open_custom_style_dialog(e):
        dialog = ft.AlertDialog(
            title=ft.Text("Confirmação"),
            content=ft.Text("Você deseja confirmar esta ação?"),
            actions=actions,
        )
        page.open(dialog)

    page.add(
        ft.FilledButton(
            text="Abrir Diálogo Estilizado",
            on_click=open_custom_style_dialog
        ),
    )

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = True

    def handle_option_click(e):
        page.add(ft.Text(f"Opção escolhida: {e.control.text}"))
        page.close(e.control.parent)

    options = [ft.TextButton(text=f"Opção {i}", on_click=handle_option_click) for i in range(1, 6)]

    def open_options_dialog(e):
        dialog = ft.AlertDialog(
            title=ft.Text("Escolha uma Opção"),
            content=ft.Column(children=options),
            actions=[ft.TextButton(text="Fechar", on_click=lambda e: page.close(e.control.parent))]
        )
        page.open(dialog)

    page.add(
        ft.FilledButton(
            text="Abrir Diálogo de Opções",
            on_click=open_options_dialog
        ),
    )

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = True

    def handle_text_submit(e):
        user_input = e.control.parent.controls[1].value
        page.add(ft.Text(f"Você digitou: {user_input}"))
        page.close(e.control.parent)

    def open_text_input_dialog(e):
        dialog = ft.AlertDialog(
            title=ft.Text("Entrada de Texto"),
            content=ft.TextField(label="Digite algo:"),
            actions=[
                ft.TextButton(text="Enviar", on_click=handle_text_submit)
            ],
        )
        page.open(dialog)

    page.add(
        ft.FilledButton(
            text="Abrir Diálogo de Texto",
            on_click=open_text_input_dialog
        ),
    )

ft.app(main)

page.add(...)

page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = True
