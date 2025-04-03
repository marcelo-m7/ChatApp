c = ft.AnimatedSwitcher(
    c1,
    transition=ft.AnimatedSwitcherTransition.SCALE,
    duration=500,
    reverse_duration=100,
    switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,
    switch_out_curve=ft.AnimationCurve.BOUNCE_IN,
)

c1 = ft.Container(
    ft.Text("Hello!", style=ft.TextThemeStyle.HEADLINE_MEDIUM),
    alignment=ft.alignment.center,
    width=200,
    height=200,
    bgcolor=ft.Colors.GREEN,
)
c2 = ft.Container(
    ft.Text("Bye!", size=50),
    alignment=ft.alignment.center,
    width=200,
    height=200,
    bgcolor=ft.Colors.YELLOW,
)

def animate(e):
    c.content = c2 if c.content == c1 else c1
    c.update()

def main(page: ft.Page):

ft.app(main)

import flet as ft

import flet as ft

def main(page: ft.Page):
    c1 = ft.Container(
        [
            ft.Text("Welcome!", style=ft.TextThemeStyle.HEADLINE_MEDIUM),
            ft.Image(src="https://example.com/welcome.png", width=100, height=100)
        ],
        alignment=ft.alignment.center,
        width=300,
        height=300,
        bgcolor=ft.Colors.LIGHT_GREEN,
    )
    c2 = ft.Container(
        [
            ft.Text("Goodbye!", size=50),
            ft.Image(src="https://example.com/goodbye.png", width=100, height=100)
        ],
        alignment=ft.alignment.center,
        width=300,
        height=300,
        bgcolor=ft.Colors.LIGHT_BLUE,
    )
    c = ft.AnimatedSwitcher(
        c1,
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=500,
        reverse_duration=300,
    )

    def animate(e):
        c.content = c2 if c.content == c1 else c1
        c.update()

    page.add(
        c,
        ft.ElevatedButton("Switch!", on_click=animate),
    )

ft.app(main)

import flet as ft

def main(page: ft.Page):
    c1 = ft.Container(
        ft.Text("Fade In!", style=ft.TextThemeStyle.HEADLINE_MEDIUM),
        alignment=ft.alignment.center,
        width=200,
        height=200,
        bgcolor=ft.Colors.PURPLE,
    )
    c2 = ft.Container(
        ft.Text("Fade Out!", size=50),
        alignment=ft.alignment.center,
        width=200,
        height=200,
        bgcolor=ft.Colors.ORANGE,
    )
    c = ft.AnimatedSwitcher(
        c1,
        transition=ft.AnimatedSwitcherTransition.FADE,
        duration=500,
        reverse_duration=300,
    )

    def animate(e):
        c.content = c2 if c.content == c1 else c1
        c.update()

    page.add(
        c,
        ft.ElevatedButton("Fade!", on_click=animate),
    )

ft.app(main)

import flet as ft

def main(page: ft.Page):
    c1 = ft.Container(
        ft.Text("Left!", style=ft.TextThemeStyle.HEADLINE_MEDIUM),
        alignment=ft.alignment.center,
        width=200,
        height=200,
        bgcolor=ft.Colors.BLUE,
    )
    c2 = ft.Container(
        ft.Text("Right!", size=50),
        alignment=ft.alignment.center,
        width=200,
        height=200,
        bgcolor=ft.Colors.RED,
    )
    c = ft.AnimatedSwitcher(
        c1,
        transition=ft.AnimatedSwitcherTransition.SLIDE_HORIZONTAL,
        duration=300,
        reverse_duration=200,
    )

    def animate(e):
        c.content = c2 if c.content == c1 else c1
        c.update()

    page.add(
        c,
        ft.ElevatedButton("Slide!", on_click=animate),
    )

ft.app(main)

page.add(
    c,
    ft.ElevatedButton("Animate!", on_click=animate),
)
