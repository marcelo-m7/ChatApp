def main(page):

import flet as ft

import flet as ft

def main(page):
    def handle_dismiss(e):
        print("Item dismissed")
        e.control.parent.controls.remove(e.control)
        page.update()

    page.add(
        ft.ListView(
            expand=True,
            controls=[
                ft.Dismissible(
                    content=ft.ListTile(title=ft.Text(f"Vertical Item {i}")),
                    dismiss_direction=ft.DismissDirection.VERTICAL,
                    background=ft.Container(bgcolor=ft.Colors.BLUE),
                    on_dismiss=handle_dismiss,
                    dismiss_thresholds={
                        ft.DismissDirection.UP_TO_DOWN: 0.3,
                        ft.DismissDirection.DOWN_TO_UP: 0.3,
                    },
                )
                for i in range(5)
            ],
        )
    )

ft.app(main)

import flet as ft

def main(page):
    def handle_dlg_action_clicked(e):
        page.close(dlg)

    dlg = ft.AlertDialog(
        modal=True,
        title=ft.Text("Custom Styled Dialog", color=ft.Colors.YELLOW),
        content=ft.Text("Do you want to proceed with the action?", color=ft.Colors.WHITE),
        actions=[
            ft.TextButton("Confirm", on_click=handle_dlg_action_clicked, bgcolor=ft.Colors.GREEN),
            ft.TextButton("Cancel", on_click=handle_dlg_action_clicked, bgcolor=ft.Colors.RED),
        ],
        bgcolor=ft.Colors.DARK_BLUE,
        actions_alignment=ft.MainAxisAlignment.CENTER,
    )

    page.add(
        ft.TextButton("Open Dialog", on_click=lambda e: page.open(dlg))
    )

ft.app(main)

import flet as ft

def main(page):
    def handle_update(e: ft.DismissibleUpdateEvent):
        print(f"Update - direction: {e.direction}, progress: {e.progress}")
        if e.progress > 0.5:
            e.control.background.bgcolor = ft.Colors.ORANGE
        else:
            e.control.background.bgcolor = ft.Colors.GREEN
        page.update()

    def handle_dismiss(e):
        e.control.parent.controls.remove(e.control)
        page.update()

    page.add(
        ft.ListView(
            expand=True,
            controls=[
                ft.Dismissible(
                    content=ft.ListTile(title=ft.Text(f"Dynamic Background Item {i}")),
                    dismiss_direction=ft.DismissDirection.HORIZONTAL,
                    background=ft.Container(bgcolor=ft.Colors.GREEN),
                    on_dismiss=handle_dismiss,
                    on_update=handle_update,
                    dismiss_thresholds={
                        ft.DismissDirection.END_TO_START: 0.2,
                        ft.DismissDirection.START_TO_END: 0.2,
                    },
                )
                for i in range(10)
            ],
        )
    )

ft.app(main)
