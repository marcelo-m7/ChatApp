import flet as ft

def main(page: ft.Page):
    def toggle_icon_button(e):
        e.control.selected = not e.control.selected
        e.control.update()
    page.add(
        ft.IconButton(
            icon=ft.Icons.BATTERY_1_BAR,
            selected_icon=ft.Icons.BATTERY_FULL,
            on_click=toggle_icon_button,
            selected=False,
            style=ft.ButtonStyle(color={"selected": ft.Colors.GREEN, "": ft.Colors.RED}),
        )
    )

ft.app(main)

import flet as ft

def main(page: ft.Page):
    def toggle_theme(e):
        e.control.selected = not e.control.selected
        page.background_color = ft.Colors.BLACK if e.control.selected else ft.Colors.WHITE
        page.update()

    dark_mode_button = ft.IconButton(
        icon=ft.Icons.LIGHT_MODE,
        selected_icon=ft.Icons.DARK_MODE,
        on_click=toggle_theme,
        selected=False,
        tooltip="Toggle dark/light mode",
        style=ft.ButtonStyle(color={"selected": ft.Colors.YELLOW, "": ft.Colors.GREY}),
    )
    page.add(dark_mode_button)

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.title = "Icon button with 'click' event"
    def button_clicked(e):
        b.data += 1
        t.value = f"Button clicked {b.data} time(s)"
        page.update()
    b = ft.IconButton(
        icon=ft.Icons.PLAY_CIRCLE_FILL_OUTLINED,
        on_click=button_clicked,
        data=0
    )
    t = ft.Text()
    page.add(b, t)

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.title = "Icon button with dynamic icon size"
    
    def button_clicked(e):
        b.data += 1
        b.icon_size = 20 + 5 * b.data  # Aumenta o tamanho do ícone a cada clique
        t.value = f"Button clicked {b.data} time(s)"
        page.update()

    b = ft.IconButton(
        icon=ft.Icons.PLAY_CIRCLE_FILL_OUTLINED,
        on_click=button_clicked,
        data=0,
        icon_size=20
    )
    t = ft.Text()
    page.add(b, t)

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.title = "Icon buttons with different styles"
    page.add(
        ft.Row(
            [
                ft.IconButton(
                    icon=ft.Icons.PAUSE_CIRCLE_FILLED_ROUNDED,
                    icon_color="blue400",
                    icon_size=20,
                    tooltip="Pause",
                ),
                ft.IconButton(
                    icon=ft.Icons.DELETE_FOREVER_ROUNDED,
                    icon_color="red400",
                    icon_size=40,
                    tooltip="Delete",
                ),
                ft.IconButton(
                    icon=ft.Icons.CHECK_CIRCLE,
                    icon_color="green400",
                    icon_size=30,
                    tooltip="Approve",
                ),
                ft.IconButton(
                    icon=ft.Icons.WARNING_AMBER_ROUNDED,
                    icon_color="orange400",
                    icon_size=25,
                    tooltip="Warning",
                ),
            ]
        ),
    )

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.title = "Icon buttons"
    page.add(
        ft.Row(
            [
                ft.IconButton(
                    icon=ft.Icons.PAUSE_CIRCLE_FILLED_ROUNDED,
                    icon_color="blue400",
                    icon_size=20,
                    tooltip="Pause record",
                ),
                ft.IconButton(
                    icon=ft.Icons.DELETE_FOREVER_ROUNDED,
                    icon_color="pink600",
                    icon_size=40,
                    tooltip="Delete record",
                ),
            ]
        ),
    )

ft.app(main)
