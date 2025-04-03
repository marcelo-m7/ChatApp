import flet as ft
import flet.canvas as cv

def main(page: ft.Page):
    cp = cv.Canvas(
        [
            cv.Circle(
                250, 250, 200,
                paint=ft.Paint(
                    gradient=ft.PaintRadialGradient(
                        ft.Offset(250, 250), 200,
                        [ft.Colors.BLUE, ft.Colors.TRANSPARENT]
                    )
                )
            ),
            cv.Text(
                250, 250,
                "Centro do Universo",
                ft.TextStyle(color=ft.Colors.WHITE, size=24),
                alignment=ft.alignment.center
            )
        ],
        width=500, height=500
    )
    page.add(cp)

ft.app(main)

import flet as ft
import flet.canvas as cv

def main(page: ft.Page):
    def on_click(e: ft.MouseEvent):
        if circle.contains(e.local_x, e.local_y):
            circle.paint.color = ft.Colors.RED if circle.paint.color != ft.Colors.RED else ft.Colors.GREEN
        cp.update()

    circle = cv.Circle(100, 100, 50, paint=ft.Paint(style=ft.PaintingStyle.FILL, color=ft.Colors.GREEN))
    cp = cv.Canvas([circle], width=200, height=200, on_click=on_click)
    page.add(cp)

ft.app(main)

import flet as ft
import flet.canvas as cv
import math

def main(page: ft.Page):
    group = cv.Group(
        [
            cv.Circle(100, 100, 50, paint=ft.Paint(style=ft.PaintingStyle.STROKE)),
            cv.Rect(50, 50, 100, 100, paint=ft.Paint(style=ft.PaintingStyle.FILL, color=ft.Colors.RED))
        ],
        transform=cv.Matrix.rotation(math.pi / 4, center=(100, 100))
    )
    cp = cv.Canvas([group], width=200, height=200)
    page.add(cp)

ft.app(main)

import flet as ft
import flet.canvas as cv
import time

def main(page: ft.Page):
    rect = cv.Rect(100, 100, 100, 100, paint=ft.Paint(color=ft.Colors.GREEN))
    cp = cv.Canvas([rect], width=300, height=300)
    page.add(cp)

    while True:
        rect.x += 10
        rect.y += 10
        cp.update()
        time.sleep(0.1)

ft.app(main)
