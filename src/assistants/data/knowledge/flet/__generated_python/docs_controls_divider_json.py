def main(page: ft.Page):

ft.Column([...], spacing=0, expand=True)

ft.Container(bgcolor=ft.Colors.AMBER, alignment=ft.Alignment.center, expand=True)
ft.Container(bgcolor=ft.Colors.PINK, alignment=ft.Alignment.center, expand=True)
ft.Container(bgcolor=ft.Colors.BLUE_300, alignment=ft.Alignment.center, expand=True)
ft.Container(bgcolor=ft.Colors.DEEP_PURPLE_200, alignment=ft.Alignment.center, expand=True)

ft.Divider()
ft.Divider(height=1, color="white")
ft.Divider(height=9, thickness=3)

ft.app(main)

import flet as ft

import flet as ft

def main(page: ft.Page):
    def animate_bgcolor(e, container, color):
        container.bgcolor = color
        page.update()

    page.add(
        ft.Column(
            [
                ft.Container(
                    bgcolor=ft.Colors.AMBER,
                    alignment=ft.alignment.center,
                    expand=True,
                    content=ft.Text("Hover Me!", color=ft.Colors.WHITE),
                    on_mouse_enter=lambda e, c=ft.Container(): animate_bgcolor(e, c, ft.Colors.RED_100)
                ),
                ft.Divider(),
                ft.Container(
                    bgcolor=ft.Colors.PINK,
                    alignment=ft.alignment.center,
                    expand=True,
                    content=ft.Text("Click Me!", color=ft.Colors.WHITE),
                    on_click=lambda e, c=ft.Container(): animate_bgcolor(e, c, ft.Colors.GREEN_100)
                ),
            ],
            spacing=0,
            expand=True,
        ),
    )

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Column(
            [
                ft.Container(
                    bgcolor=ft.Colors.AMBER,
                    alignment=ft.alignment.center,
                    expand=True,
                    content=ft.Text("Amber Container", color=ft.Colors.WHITE)
                ),
                ft.Divider(),
                ft.Container(
                    bgcolor=ft.Colors.PINK,
                    alignment=ft.alignment.center,
                    expand=True,
                    content=ft.Text("Pink Container", color=ft.Colors.WHITE)
                ),
                ft.Divider(height=1, color="white"),
                ft.Container(
                    bgcolor=ft.Colors.BLUE_300,
                    alignment=ft.alignment.center,
                    expand=True,
                    content=ft.Button("Click Me", on_click=lambda e: print("Button in Blue Container clicked"))
                ),
                ft.Divider(height=9, thickness=3),
                ft.Container(
                    bgcolor=ft.Colors.DEEP_PURPLE_200,
                    alignment=ft.alignment.center,
                    expand=True,
                    content=ft.Text("Deep Purple Container", color=ft.Colors.WHITE)
                ),
            ],
            spacing=0,
            expand=True,
        ),
    )

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Wrap(
            spacing=10,
            run_spacing=10,
            children=[
                ft.Container(
                    bgcolor=ft.Colors.AMBER,
                    alignment=ft.alignment.center,
                    expand=True,
                    content=ft.Text("Amber", color=ft.Colors.WHITE),
                    width=200,
                    height=100
                ),
                ft.Container(
                    bgcolor=ft.Colors.PINK,
                    alignment=ft.alignment.center,
                    expand=True,
                    content=ft.Text("Pink", color=ft.Colors.WHITE),
                    width=200,
                    height=100
                ),
                ft.Container(
                    bgcolor=ft.Colors.BLUE_300,
                    alignment=ft.alignment.center,
                    expand=True,
                    content=ft.Text("Blue", color=ft.Colors.WHITE),
                    width=200,
                    height=100
                ),
                ft.Container(
                    bgcolor=ft.Colors.DEEP_PURPLE_200,
                    alignment=ft.alignment.center,
                    expand=True,
                    content=ft.Text("Deep Purple", color=ft.Colors.WHITE),
                    width=200,
                    height=100
                ),
            ]
        )
    )

ft.app(main)
