cupertino_date_picker = ft.CupertinoDatePicker(
    date_picker_mode=ft.CupertinoDatePickerMode.DATE_AND_TIME,
    on_change=handle_date_change,
)

def handle_date_change(e: ft.ControlEvent):
    page.add(ft.Text(f"Date changed: {e.control.value.strftime('%Y-%m-%d %H:%M %p')}"))

def main(page):

ft.app(main)

import flet as ft

import flet as ft

def main(page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def handle_date_change(e: ft.ControlEvent):
        page.add(ft.Text(f"Date changed: {e.control.value.strftime('%Y-%m-%d %H:%M %p')}"))

    cupertino_date_picker = ft.CupertinoDatePicker(
        date_picker_mode=ft.CupertinoDatePickerMode.DATE_AND_TIME,
        on_change=handle_date_change,
    )

    open_button = ft.CupertinoButton(
        text="Open Simple CupertinoDatePicker",
        on_click=lambda e: page.open(
            ft.CupertinoBottomSheet(
                cupertino_date_picker,
                height=216,
                padding=ft.padding.only(top=6),
            )
        ),
    )
    
    page.add(open_button)

ft.app(main)

import flet as ft

def main(page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def handle_date_change(e: ft.ControlEvent):
        page.add(ft.Text(f"Date changed: {e.control.value.strftime('%Y-%m-%d')}"))

    cupertino_date_picker = ft.CupertinoDatePicker(
        date_picker_mode=ft.CupertinoDatePickerMode.DATE,
        on_change=handle_date_change,
    )

    page.add(
        ft.CupertinoFilledButton(
            "Open CupertinoDatePicker",
            on_click=lambda e: page.open(
                ft.CupertinoBottomSheet(
                    cupertino_date_picker,
                    height=216,
                    padding=ft.padding.only(top=6),
                )
            ),
        )
    )

ft.app(main)

import flet as ft

def main(page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    date_text = ft.TextField(value="Select a date", read_only=True)

    def handle_date_change(e: ft.ControlEvent):
        date_text.value = f"Date selected: {e.control.value.strftime('%Y-%m-%d %H:%M %p')}"
        page.update()

    cupertino_date_picker = ft.CupertinoDatePicker(
        date_picker_mode=ft.CupertinoDatePickerMode.DATE_AND_TIME,
        on_change=handle_date_change,
    )

    page.add(date_text)

    page.add(
        ft.CupertinoFilledButton(
            "Open CupertinoDatePicker",
            on_click=lambda e: page.open(
                ft.CupertinoBottomSheet(
                    cupertino_date_picker,
                    height=216,
                    padding=ft.padding.only(top=6),
                )
            ),
        )
    )

ft.app(main)

page.add(
    ft.CupertinoFilledButton(
        "Open CupertinoDatePicker",
        on_click=lambda e: page.open(
            ft.CupertinoBottomSheet(
                cupertino_date_picker,
                height=216,
                padding=ft.padding.only(top=6),
            )
        ),
    )
)

page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
