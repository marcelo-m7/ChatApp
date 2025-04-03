ft.Stack(
    [
        ft.Container(
            content=ft.Text("Hello"),
            image_src="https://picsum.photos/100/100",
            width=100,
            height=100,
        ),
        ft.Container(
            width=50,
            height=50,
            blur=10,
            bgcolor="#44CCCC00",
        ),
        ft.Container(
            width=50,
            height=50,
            left=10,
            top=60,
            blur=(0, 10),
        ),
        ft.Container(
            top=10,
            left=60,
            blur=ft.Blur(10, 0, ft.BlurTileMode.MIRROR),
            width=50,
            height=50,
            bgcolor="#44CCCCCC",
            border=ft.border.all(2, ft.Colors.BLACK),
        ),
    ]
)

import flet as ft

def main(page: ft.Page):
    def on_hover(e):
        e.control.bgcolor = "blue" if e.data == "true" else "red"
        e.control.update()
    page.add(
        ft.Container(width=100, height=100, bgcolor="red", ink=False, on_hover=on_hover)
    )

ft.app(main)

import flet as ft

def main(page: ft.Page):
    def on_hover(e):
        e.control.bgcolor = ft.Colors.YELLOW_200 if e.data == "true" else ft.Colors.ORANGE_200
        e.control.update()

    page.add(
        ft.Container(
            content=ft.Text("Hover over me!"),
            width=200,
            height=100,
            bgcolor=ft.Colors.ORANGE_200,
            ink=True,
            on_hover=on_hover
        )
    )

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Container(
            content=ft.Column([
                ft.Image(src="https://picsum.photos/200/100"),
                ft.Text("This is a beautiful scenery!", max_lines=2)
            ]),
            padding=10,
            bgcolor=ft.Colors.LIGHT_BLUE_100,
            width=220,
            height=200,
            border_radius=10
        )
    )

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Container(
            content=ft.Text("Elevated Container"),
            width=200,
            height=100,
            padding=20,
            bgcolor=ft.Colors.PURPLE_100,
            border=ft.border.all(3, ft.Colors.PURPLE_700),
            elevation=10
        )
    )

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Row([
            ft.Container(
                content=ft.Text("Left Align"),
                padding=10,
                bgcolor=ft.Colors.BLUE_100,
                width=200,
                height=100,
                alignment=ft.alignment.top_left,
            ),
            ft.Container(
                content=ft.Text("Center Align"),
                padding=10,
                bgcolor=ft.Colors.GREEN_100,
                width=200,
                height=100,
                alignment=ft.alignment.center,
            ),
            ft.Container(
                content=ft.Text("Right Align"),
                padding=10,
                bgcolor=ft.Colors.RED_100,
                width=200,
                height=100,
                alignment=ft.alignment.bottom_right,
            ),
        ])
    )

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.title = "Containers - clickable and not"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(
        ft.Row(
            [
                ft.Container(
                    content=ft.Text("Non clickable"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.Colors.AMBER,
                    width=150,
                    height=150,
                    border_radius=10,
                ),
                ft.Container(
                    content=ft.Text("Clickable without Ink"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.Colors.GREEN_200,
                    width=150,
                    height=150,
                    border_radius=10,
                    on_click=lambda e: print("Clickable without Ink clicked!"),
                ),
                ft.Container(
                    content=ft.Text("Clickable with Ink"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.Colors.CYAN_200,
                    width=150,
                    height=150,
                    border_radius=10,
                    ink=True,
                    on_click=lambda e: print("Clickable with Ink clicked!"),
                ),
                ft.Container(
                    content=ft.Text("Clickable transparent with Ink"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    width=150,
                    height=150,
                    border_radius=10,
                    ink=True,
                    on_click=lambda e: print("Clickable transparent with Ink clicked!"),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    def on_long_press(e):
        print("on long press")
        page.add(ft.Text("on_long_press triggered"))
    def on_click(e):
        print("on click")
        page.add(ft.Text("on_click triggered"))
    def on_tap_down(e: ft.ContainerTapEvent):
        print("on tap down", e.local_x, e.local_y)
        page.add(ft.Text("on_tap_down triggered"))
    c = ft.Container(
        bgcolor=ft.Colors.RED,
        content=ft.Text("Test Long Press"),
        height=100,
        width=100,
        on_click=on_click,
        on_long_press=on_long_press,
        on_tap_down=on_tap_down,
    )
    page.add(c)

ft.app(main)
