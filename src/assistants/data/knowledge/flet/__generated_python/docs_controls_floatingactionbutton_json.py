count = 0

def fab_pressed(e):
        nonlocal count  # to modify the count variable found in the outer scope
        ...

def main(page: ft.Page):

ft.app(main)

import flet as ft

import flet as ft

def main(page: ft.Page):
    page.title = "Dynamic Icon FAB"
    page.appbar = ft.AppBar(title=ft.Text("Dynamic Icon FAB"))
    
    count = 0
    icons = [ft.Icons.ADD, ft.Icons.REMOVE]
    
    def fab_pressed(e):
        nonlocal count
        page.add(ft.ListTile(title=ft.Text(f"Tile {count}")))
        count += 1
        # Change icon dynamically
        page.floating_action_button.icon = icons[count % 2]
    
    page.floating_action_button = ft.FloatingActionButton(
        icon=icons[0],
        on_click=fab_pressed
    )
    
ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.title = "FAB with Visual Feedback"
    page.appbar = ft.AppBar(title=ft.Text("FAB with Snackbar"))
    
    count = 0
    
    def fab_pressed(e):
        nonlocal count
        new_tile = ft.ListTile(title=ft.Text(f"Tile {count}"))
        page.add(new_tile)
        page.open(ft.SnackBar(content=ft.Text(f"Tile {count} added!"), action=ft.TextButton("UNDO", on_click=lambda x: page.remove(new_tile))))
        count += 1
    
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD,
        on_click=fab_pressed
    )
    
ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.title = "Themed Floating Action Button"
    page.theme = ft.ThemeData(
        primary_color=ft.Colors.INDIGO,
        secondary_color=ft.Colors.PINK
    )
    page.appbar = ft.AppBar(
        title=ft.Text("Themed FAB", weight=ft.FontWeight.BOLD),
        bgcolor=page.theme.primary_color
    )
    
    count = 0
    
    def fab_pressed(e):
        nonlocal count
        page.add(ft.ListTile(title=ft.Text(f"Tile {count}")))
        count += 1
        # Change FAB color after each press
        page.floating_action_button.bgcolor = page.theme.secondary_color if count % 2 == 0 else page.theme.primary_color
    
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD,
        on_click=fab_pressed,
        bgcolor=page.theme.primary_color
    )
    
ft.app(main)

page.add(
            ft.ListTile(
                title=ft.Text(f"Tile {count}"),
                on_click=lambda x: print(x.control.title.value + " was clicked!"),
            )
        )

page.add(ft.Text("Press the FAB to add a tile!"))

page.appbar = ft.AppBar(
        title=ft.Text("Floating Action Button", weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK87),
        actions=[ft.IconButton(ft.Icons.MENU, tooltip="Menu", icon_color=ft.Colors.BLACK87)],
        bgcolor=ft.Colors.BLUE,
        center_title=True,
        color=ft.Colors.WHITE,
    )

page.floating_action_button = ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=fab_pressed, bgcolor=ft.Colors.LIME_300)

page.open(ft.SnackBar(ft.Text("Tile was added successfully!")))

page.title = "Floating Action Button"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.auto_scroll = True
    page.scroll = ft.ScrollMode.HIDDEN
