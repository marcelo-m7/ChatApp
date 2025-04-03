import flet as ft

def main(page):
    c = ft.Checkbox(
        label="Custom Style Checkbox",
        value=True,
        label_position=ft.LabelPosition.LEFT,
        style=ft.styles.CheckboxStyle(
            active_color=ft.colors.GREEN,
            check_color=ft.colors.WHITE,
            focus_color=ft.colors.RED
        )
    )
    page.add(c)

ft.app(main)

import flet as ft

def main(page):
    def checkbox_changed(e):
        t.value = f"{e.control.label} is now {'checked' if e.control.value else 'unchecked'}"
        page.update()

    c1 = ft.Checkbox(label="Dynamic Feedback Checkbox", on_change=checkbox_changed)
    t = ft.Text()

    page.add(c1, t)

ft.app(main)

import flet as ft

def main(page):
    def settings_changed(e):
        settings[e.control.label] = e.control.value
        t.value = f"Settings updated: {settings}"
        page.update()

    settings = {
        "Enable Notifications": False,
        "Dark Mode": False,
        "Auto Sync": False
    }
    checkboxes = [
        ft.Checkbox(label=setting, value=value, on_change=settings_changed)
        for setting, value in settings.items()
    ]
    t = ft.Text()

    page.add(*checkboxes, t)

ft.app(main)

import flet as ft

def main(page):
    def submit_clicked(e):
        selected = [cb.label for cb in checkboxes if cb.value]
        t.value = f"Selected checkboxes: {', '.join(selected)}"
        page.update()
    
    checkboxes = [
        ft.Checkbox(label=f"Option {i}") for i in range(1, 6)
    ]
    b = ft.ElevatedButton(text="Submit", on_click=submit_clicked)
    t = ft.Text()

    page.add(*checkboxes, b, t)

ft.app(main)

import flet as ft

def main(page):
    row = ft.Row([
        ft.Checkbox(label=f"Item {i+1}") for i in range(5)
    ])
    page.add(row)

ft.app(main)
