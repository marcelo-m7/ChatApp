def check_item_clicked(e):
    e.control.checked = not e.control.checked
    page.update()

ft.app(main)

import flet as ft

def main(page: ft.Page):

import flet as ft

def main(page: ft.Page):
    def nav_item_selected(e):
        content.text = f"Você selecionou: {e.control.text}"
        page.update()

    nav = ft.NavigationRail(
        selected_index=0,
        group_alignment=0,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.FAVORITE),
                text="Favoritos",
                on_click=nav_item_selected
            ),
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.HOME),
                text="Início",
                on_click=nav_item_selected
            ),
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.SETTINGS),
                text="Configurações",
                on_click=nav_item_selected
            ),
        ]
    )

    content = ft.Text("")

    page.add(ft.Row([nav, content]))

ft.app(main)

import flet as ft

def main(page: ft.Page):
    def submit_text(e):
        result.text = f"Você escreveu: {user_input.value}"
        page.update()

    page.appbar = ft.AppBar(
        title=ft.Text("TextField com Botão"),
        bgcolor=ft.Colors.BLUE
    )

    user_input = ft.TextField(hint_text="Escreva algo aqui...")
    submit_button = ft.ElevatedButton(text="Enviar", on_click=submit_text)
    result = ft.Text("")

    form = ft.Column(
        controls=[user_input, submit_button, result],
        spacing=10
    )

    page.add(form)

ft.app(main)

import flet as ft

def main(page: ft.Page):
    tab1_content = ft.Text("Conteúdo da Aba 1")
    tab2_content = ft.Text("Conteúdo da Aba 2")

    tabs = ft.Tabs(
        tabs=[
            ft.Tab(text="Aba 1", content=tab1_content),
            ft.Tab(text="Aba 2", content=tab2_content),
        ]
    )

    page.add(tabs)

ft.app(main)

page.add(ft.Text("Body!"))

page.appbar = ft.AppBar(
    leading=ft.Icon(ft.Icons.PALETTE),
    leading_width=40,
    title=ft.Text("AppBar Example"),
    center_title=False,
    bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
    actions=[
        ft.IconButton(ft.Icons.WB_SUNNY_OUTLINED),
        ft.IconButton(ft.Icons.FILTER_3),
        ft.PopupMenuButton(
            items=[
                ft.PopupMenuItem(text="Item 1"),
                ft.PopupMenuItem(),  # divider
                ft.PopupMenuItem(
                    text="Checked item", checked=False, on_click=check_item_clicked
                ),
            ]
        ),
    ],
)
