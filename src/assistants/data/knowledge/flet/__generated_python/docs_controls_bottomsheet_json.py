bs = ft.BottomSheet(
    on_dismiss=handle_dismissal,
    content=ft.Container(
        padding=50,
        content=ft.Column(
            tight=True,
            controls=[
                ft.Text("This is bottom sheet's content!"),
                ft.ElevatedButton("Close bottom sheet", on_click=lambda _: page.close(bs)),
            ],
        ),
    ),
)

def handle_dismissal(e):
    page.add(ft.Text("Bottom sheet dismissed"))

def main(page: ft.Page):

ft.app(main)

import flet as ft

import flet as ft

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def handle_dismissal(e):
        page.add(ft.Text("Bottom sheet dismissed"))

    bs = ft.BottomSheet(
        on_dismiss=handle_dismissal,
        content=ft.Container(
            padding=50,
            content=ft.Column(
                tight=True,
                controls=[
                    ft.Text("Escolha uma imagem:"),
                    ft.Image(src="https://via.placeholder.com/150", width=150, height=150),
                    ft.ElevatedButton("Close", on_click=lambda _: page.close(bs))
                ],
            ),
        ),
    )

    page.add(ft.ElevatedButton("Display bottom sheet", on_click=lambda _: page.open(bs)))

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def handle_dismissal(e):
        page.add(ft.Text("Bottom sheet dismissed"))

    bs = ft.BottomSheet(
        on_dismiss=handle_dismissal,
        content=ft.Container(
            padding=50,
            content=ft.Column(
                tight=True,
                controls=[
                    ft.TextField(label="Nome"),
                    ft.TextField(label="Email"),
                    ft.ElevatedButton("Submit", on_click=lambda _: page.close(bs))
                ],
            ),
        ),
    )

    page.add(ft.ElevatedButton("Display bottom sheet", on_click=lambda _: page.open(bs)))

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def handle_dismissal(e):
        page.add(ft.Text("Bottom sheet dismissed"))

    list_items = [
        ft.ListTile(title=ft.Text("Opção 1")),
        ft.ListTile(title=ft.Text("Opção 2")),
        ft.ListTile(title=ft.Text("Opção 3")),
    ]

    bs = ft.BottomSheet(
        on_dismiss=handle_dismissal,
        content=ft.Container(
            padding=50,
            content=ft.Column(
                tight=True,
                controls=list_items + [ft.ElevatedButton("Close", on_click=lambda _: page.close(bs))],
            ),
        ),
    )

    page.add(ft.ElevatedButton("Display bottom sheet", on_click=lambda _: page.open(bs)))

ft.app(main)

page.add(ft.ElevatedButton("Display bottom sheet", on_click=lambda _: page.open(bs)))

page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
