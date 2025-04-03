c = ft.Container(gd, bgcolor=ft.Colors.AMBER, width=50, height=50, left=0, top=0)

def main(page: ft.Page):

def on_pan_update1(e: ft.DragUpdateEvent):
    c.top = max(0, c.top + e.delta_y)
    c.left = max(0, c.left + e.delta_x)
    c.update()

def on_pan_update2(e: ft.DragUpdateEvent):
    e.control.top = max(0, e.control.top + e.delta_y)
    e.control.left = max(0, e.control.left + e.delta_x)
    e.control.update()

ft.app(main)

gd = ft.GestureDetector(
    mouse_cursor=ft.MouseCursor.MOVE,
    drag_interval=50,
    on_pan_update=on_pan_update1,
)

gd1 = ft.GestureDetector(
    mouse_cursor=ft.MouseCursor.MOVE,
    drag_interval=10,
    on_vertical_drag_update=on_pan_update2,
    left=100,
    top=100,
    content=ft.Container(bgcolor=ft.Colors.BLUE, width=50, height=50),
)

import flet as ft

import flet as ft

def main(page: ft.Page):
    def on_pan_update(e: ft.DragUpdateEvent):
        e.control.top += e.delta_y
        e.control.left += e.delta_x
        # Alternar cor ao arrastar
        e.control.bgcolor = ft.Colors.GREEN if e.control.bgcolor == ft.Colors.RED else ft.Colors.RED
        e.control.update()

    container = ft.Container(
        width=100,
        height=100,
        bgcolor=ft.Colors.RED,
        alignment=ft.Alignment.CENTER
    )

    gesture_detector = ft.GestureDetector(
        on_pan_update=on_pan_update,
        content=container
    )

    page.add(gesture_detector)

ft.app(main)

import flet as ft

def main(page: ft.Page):
    def on_pan_update(e: ft.DragUpdateEvent):
        e.control.top += e.delta_y
        e.control.left += e.delta_x
        e.control.update()

    def create_draggable_container(color, initial_left, initial_top):
        container = ft.Container(
            width=50,
            height=50,
            bgcolor=color,
            left=initial_left,
            top=initial_top
        )
        return ft.GestureDetector(
            on_pan_update=on_pan_update,
            content=container
        )

    colors = [ft.Colors.RED, ft.Colors.GREEN, ft.Colors.BLUE]
    positions = [(0, 0), (60, 60), (120, 120)]
    containers = [create_draggable_container(color, *pos) for color, pos in zip(colors, positions)]

    page.add(ft.Stack(containers, width=500, height=500))

ft.app(main)

import flet as ft

def main(page: ft.Page):
    def on_pan_update(e: ft.DragUpdateEvent):
        new_x = max(0, min(page.width - e.control.width, e.control.left + e.delta_x))
        new_y = max(0, min(page.height - e.control.height, e.control.top + e.delta_y))
        e.control.left = new_x
        e.control.top = new_y
        e.control.update()

    container = ft.Container(
        width=100,
        height=100,
        bgcolor=ft.Colors.BLUE,
        left=50,
        top=50
    )

    gesture_detector = ft.GestureDetector(
        on_pan_update=on_pan_update,
        content=container
    )

    page.add(ft.Stack([gesture_detector], width=500, height=500))

ft.app(main)

page.add(ft.Stack([c, gd1], width=1000, height=500))
