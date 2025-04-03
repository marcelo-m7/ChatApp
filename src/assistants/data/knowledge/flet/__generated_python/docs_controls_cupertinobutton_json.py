def main(page: ft.Page):

ft.app(main)

import flet as ft

import flet as ft

def main(page: ft.Page):
    def navigate_url(e):
        page.open_url("https://www.example.com")

    page.add(
        ft.CupertinoButton(
            content=ft.Text("Visite nosso site"),
            on_click=navigate_url,
        )
    )

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.add(
        ft.CupertinoButton(
            content=ft.Row([
                ft.Icon(name=ft.Icons.ADD, color=ft.Colors.BLUE),
                ft.Text("Adicionar", color=ft.Colors.BLUE)
            ]),
            on_click=lambda e: print("Adicionar botão clicado!"),
        )
    )

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.add(
        ft.CupertinoButton(
            content=ft.Text("Custom Border Button"),
            border=ft.Border.all(color=ft.Colors.GREEN, width=2),
            elevation=10,
            on_click=lambda e: print("Custom Border Button clicked!")
        )
    )

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.add(
        ft.CupertinoButton(
            content=ft.Text("Disabled Button"),
            disabled=True,
            on_click=lambda e: print("Este botão está desabilitado!")
        )
    )

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.add(
        ft.FloatingActionButton(
            content=ft.Icon(name=ft.Icons.ADD, color=ft.Colors.WHITE),
            bgcolor=ft.Colors.RED,
            on_click=lambda e: print("Floating Action Button clicked!"),
        )
    )

ft.app(main)
