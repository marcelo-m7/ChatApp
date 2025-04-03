def handle_expansion_tile_change(e):

def main(page: ft.Page):

ft.app(main)

if e.control.trailing:
    e.control.trailing.name = (
        ft.Icons.ARROW_DROP_DOWN
        if e.control.trailing.name == ft.Icons.ARROW_DROP_DOWN_CIRCLE
        else ft.Icons.ARROW_DROP_DOWN_CIRCLE
    )
    page.update()

import flet as ft

import flet as ft

def main(page: ft.Page):
    def handle_checkbox_change(e):
        page.open(ft.SnackBar(ft.Text(f"Checkbox is now {'checked' if e.control.value else 'unchecked'}")))

    checkbox = ft.Checkbox(value=False, on_change=handle_checkbox_change)

    page.add(
        ft.ExpansionTile(
            title=ft.Text("ExpansionTile with Checkbox"),
            controls=[ft.ListTile(title=ft.Text("Check me!"), leading=checkbox)]
        )
    )

ft.app(main)

import flet as ft

def main(page: ft.Page):
    def handle_tile_change(tile, expanded):
        if expanded:
            for other_tile in [tile1, tile2, tile3]:
                if other_tile != tile:
                    other_tile.expanded = False
            page.update()

    tile1 = ft.ExpansionTile(title=ft.Text("Tile 1"), on_change=lambda e: handle_tile_change(tile1, e.data == 'true'))
    tile2 = ft.ExpansionTile(title=ft.Text("Tile 2"), on_change=lambda e: handle_tile_change(tile2, e.data == 'true'))
    tile3 = ft.ExpansionTile(title=ft.Text("Tile 3"), on_change=lambda e: handle_tile_change(tile3, e.data == 'true'))

    page.add(tile1, tile2, tile3)

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.add(
        ft.ExpansionTile(
            title=ft.Text("Colorful ExpansionTile"),
            subtitle=ft.Text("Click to expand"),
            collapsed_text_color=ft.Colors.PURPLE,
            text_color=ft.Colors.ORANGE,
            expanded_text_color=ft.Colors.GREEN,
            controls=[ft.ListTile(title=ft.Text("Content here"))]
        )
    )

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.add(
        ft.ExpansionTile(
            title=ft.Text("ExpansionTile with Custom Icons"),
            trailing=ft.Icon(ft.Icons.ADD),
            collapsed_icon=ft.Icon(ft.Icons.REMOVE),
            controls=[ft.ListTile(title=ft.Text("This is a sub-tile"))]
        )
    )

ft.app(main)

page.add(...)

page.open(
    ft.SnackBar(
        ft.Text(f"ExpansionTile was {'expanded' if e.data=='true' else 'collapsed'}"),
        duration=1000,
    )
)

page.spacing = 0
page.padding = 0
