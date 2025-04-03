action_sheet = ft.CupertinoActionSheet(
    title=ft.Row([ft.Text("Title")], alignment=ft.MainAxisAlignment.CENTER),
    message=ft.Row([ft.Text("Description")], alignment=ft.MainAxisAlignment.CENTER),
    cancel=ft.CupertinoActionSheetAction(
        content=ft.Text("Cancel"),
        on_click=handle_click,
    ),
    actions=[
        ft.CupertinoActionSheetAction(
            content=ft.Text("Default Action"),
            is_default_action=True,
            on_click=handle_click,
        ),
        ft.CupertinoActionSheetAction(
            content=ft.Text("Normal Action"),
            on_click=handle_click,
        ),
        ft.CupertinoActionSheetAction(
            content=ft.Text("Destructive Action"),
            is_destructive_action=True,
            on_click=handle_click,
        ),
    ],
)

bottom_sheet = ft.CupertinoBottomSheet(action_sheet)

def handle_click(e):
    page.add(ft.Text(f"Action clicked: {e.control.content.value}"))
    page.close(bottom_sheet)

def main(page):

ft.app(main)

import flet as ft

import flet as ft

def main(page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def handle_click(e):
        page.add(ft.Text(f"Action clicked: {e.control.content.children[1].value}"))
        page.close(bottom_sheet)

    action_sheet = ft.CupertinoActionSheet(
        title=ft.Row([ft.Text("Choose Option")], alignment=ft.MainAxisAlignment.CENTER),
        message=ft.Row([ft.Text("Select an action to perform.")], alignment=ft.MainAxisAlignment.CENTER),
        cancel=ft.CupertinoActionSheetAction(
            content=ft.Row([
                ft.Icon(ft.icons.CLOSE),
                ft.Text(" Cancel")
            ]),
            on_click=handle_click,
        ),
        actions=[
            ft.CupertinoActionSheetAction(
                content=ft.Row([
                    ft.Icon(ft.icons.CHECK),
                    ft.Text(" Accept")
                ]),
                on_click=handle_click,
            ),
            ft.CupertinoActionSheetAction(
                content=ft.Row([
                    ft.Icon(ft.icons.WARNING),
                    ft.Text(" Warning")
                ]),
                is_destructive_action=True,
                on_click=handle_click,
            ),
        ],
    )
    bottom_sheet = ft.CupertinoBottomSheet(action_sheet)
    page.add(
        ft.CupertinoFilledButton(
            "Open Actions",
            on_click=lambda e: page.open(bottom_sheet),
        )
    )

ft.app(main)

import flet as ft

def main(page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def handle_click(e):
        page.add(ft.Text(f"Action clicked: {e.control.content.value}"))
        page.close(bottom_sheet)

    action_sheet = ft.CupertinoActionSheet(
        title=ft.Row([ft.Text("Settings")], alignment=ft.MainAxisAlignment.CENTER),
        message=ft.Row([ft.Text("Configure your preferences.")], alignment=ft.MainAxisAlignment.CENTER),
        cancel=ft.CupertinoActionSheetAction(
            content=ft.Text("Cancel"),
            on_click=handle_click,
        ),
        actions=[
            ft.CupertinoActionSheetAction(
                content=ft.Text("Sound"),
                on_click=handle_click,
            ),
            ft.Divider(),
            ft.CupertinoActionSheetAction(
                content=ft.Text("Display"),
                on_click=handle_click,
            ),
            ft.Divider(),
            ft.CupertinoActionSheetAction(
                content=ft.Text("Network"),
                on_click=handle_click,
            ),
        ],
    )
    bottom_sheet = ft.CupertinoBottomSheet(action_sheet)
    page.add(
        ft.CupertinoFilledButton(
            "Open Settings",
            on_click=lambda e: page.open(bottom_sheet),
        )
    )

ft.app(main)

page.add(
    ft.CupertinoFilledButton(
        "Open CupertinoBottomSheet",
        on_click=lambda e: page.open(bottom_sheet),
    )
)

page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
