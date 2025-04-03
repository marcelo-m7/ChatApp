content=ft.Column(
    [
        # Diversos ListTile aqui
    ],
    spacing=0,
)

def main(page):

ft.Card(
    content=ft.Container(
        width=500,
        ...
    )
)

ft.ListTile(
    title=ft.Text("One-line list tile"),
),

ft.app(main)

import flet as ft

import flet as ft

def main(page):
    page.title = "Grouped ListTile with Dividers"
    page.add(
        ft.Card(
            content=ft.Container(
                width=500,
                content=ft.Column(
                    [
                        ft.ListTile(
                            title=ft.Text("First item in group"),
                        ),
                        ft.Divider(),
                        ft.ListTile(
                            title=ft.Text("Second item in group"),
                        ),
                        ft.Divider(),
                        ft.ListTile(
                            title=ft.Text("Third item in group"),
                        ),
                    ],
                    spacing=0,
                ),
                padding=ft.padding.symmetric(vertical=10),
            )
        )
    )

ft.app(main)

import flet as ft

def main(page):
    page.title = "ListTile with Action Example"
    page.add(
        ft.Card(
            content=ft.Container(
                width=500,
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.Icons.FAVORITE, color=ft.colors.RED),
                            title=ft.Text("List tile with colored icon"),
                            onTap=lambda _: page.snackbar_show(ft.SnackBar(content=ft.Text("You clicked the ListTile!")))
                        ),
                    ],
                    spacing=10,
                ),
                padding=ft.padding.symmetric(vertical=10),
            )
        )
    )

ft.app(main)

import flet as ft

def main(page):
    page.title = "ListTile with Multiple Menu Items"
    page.add(
        ft.Card(
            content=ft.Container(
                width=500,
                content=ft.Column(
                    [
                        ft.ListTile(
                            title=ft.Text("List tile with multiple menu actions"),
                            trailing=ft.PopupMenuButton(
                                icon=ft.Icons.MORE_VERT,
                                items=[
                                    ft.PopupMenuItem(text="Edit", icon=ft.Icon(ft.Icons.EDIT)),
                                    ft.PopupMenuItem(text="Delete", icon=ft.Icon(ft.Icons.DELETE)),
                                    ft.PopupMenuItem(text="Share", icon=ft.Icon(ft.Icons.SHARE)),
                                ],
                            ),
                        ),
                    ],
                    spacing=10,
                ),
                padding=ft.padding.symmetric(vertical=10),
            )
        )
    )

ft.app(main)

page.add(...)

page.title = "ListTile Examples"

trailing=ft.PopupMenuButton(
    icon=ft.Icons.MORE_VERT,
    items=[
        ft.PopupMenuItem(text="Item 1"),
        ft.PopupMenuItem(text="Item 2"),
    ],
),
