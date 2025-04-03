appbar_text_ref = ft.Ref[ft.Text]()

def main(page: ft.Page):

ft.app(main)

import flet as ft

import flet as ft

def main(page: ft.Page):
    appbar_text_ref = ft.Ref[ft.Text]()

    def handle_menu_item_click(e):
        page.open(ft.SnackBar(content=ft.Text(f"{e.control.content.value} was clicked!")))
        appbar_text_ref.current.value = e.control.content.value
        page.update()

    page.appbar = ft.AppBar(
        title=ft.Text("Menus", ref=appbar_text_ref),
        center_title=True,
        bgcolor=ft.Colors.BLUE,
    )

    menubar = ft.MenuBar(
        expand=True,
        controls=[
            ft.SubmenuButton(
                content=ft.Text("Help"),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Documentation"),
                        leading=ft.Icon(ft.Icons.BOOK),
                        on_click=handle_menu_item_click,
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Submit Feedback"),
                        leading=ft.Icon(ft.Icons.FEEDBACK),
                        on_click=handle_menu_item_click,
                    ),
                ],
            ),
        ],
    )

    page.add(ft.Row([menubar]))

ft.app(main)

import flet as ft

def main(page: ft.Page):
    appbar_text_ref = ft.Ref[ft.Text]()

    def handle_menu_item_click(e):
        page.open(ft.SnackBar(content=ft.Text(f"{e.control.content.value} was clicked!")))
        appbar_text_ref.current.value = e.control.content.value
        page.update()

    page.appbar = ft.AppBar(
        title=ft.Text("Menus", ref=appbar_text_ref),
        center_title=True,
        bgcolor=ft.Colors.BLUE,
    )

    menubar = ft.MenuBar(
        expand=True,
        controls=[
            ft.SubmenuButton(
                content=ft.Text("Settings"),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Preferences"),
                        leading=ft.Icon(ft.Icons.SETTINGS),
                        on_click=handle_menu_item_click,
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Update"),
                        leading=ft.Icon(ft.Icons.UPGRADE),
                        on_click=handle_menu_item_click,
                    ),
                ],
            ),
        ],
    )

    page.add(ft.Row([menubar]))

ft.app(main)

import flet as ft

def main(page: ft.Page):
    appbar_text_ref = ft.Ref[ft.Text]()

    def handle_menu_item_click(e):
        page.open(ft.SnackBar(content=ft.Text(f"{e.control.content.value} was clicked!")))
        appbar_text_ref.current.value = e.control.content.value
        page.update()

    page.appbar = ft.AppBar(
        title=ft.Text("Menus", ref=appbar_text_ref),
        center_title=True,
        bgcolor=ft.Colors.BLUE,
    )

    menubar = ft.MenuBar(
        expand=True,
        style=ft.MenuStyle(
            bgcolor=ft.Colors.GREY_900,
            mouse_cursor={
                ft.ControlState.HOVERED: ft.MouseCursor.POINTER
            },
        ),
        controls=[
            ft.SubmenuButton(
                content=ft.Text("File"),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Open"),
                        leading=ft.Icon(ft.Icons.FOLDER_OPEN),
                        style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.Colors.ORANGE_200}),
                        on_click=handle_menu_item_click,
                    ),
                ],
            ),
        ],
    )

    page.add(ft.Row([menubar]))

ft.app(main)

menubar = ft.MenuBar(
    expand=True,
    style=ft.MenuStyle(
        alignment=ft.alignment.top_left,
        bgcolor=ft.Colors.RED_300,
        mouse_cursor={
            ft.ControlState.HOVERED: ft.MouseCursor.WAIT,
            ft.ControlState.DEFAULT: ft.MouseCursor.ZOOM_OUT,
        },
    ),
    controls=[
        # Submenus e itens aqui
    ],
)

page.add(ft.Row([menubar]))

page.appbar = ft.AppBar(
    title=ft.Text("Menus", ref=appbar_text_ref),
    center_title=True,
    bgcolor=ft.Colors.BLUE,
)
