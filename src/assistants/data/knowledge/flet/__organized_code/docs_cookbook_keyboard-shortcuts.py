import flet as ftdef main(page: ft.Page):    def on_keyboard(e: ft.KeyboardEvent):        page.add(            ft.Text(                f"Key: {e.key}, Shift: {e.shift}, Control: {e.ctrl}, Alt: {e.alt}, Meta: {e.meta}"            )        )    page.on_keyboard_event = on_keyboard    page.add(        ft.Text("Press any key with a combination of CTRL, ALT, SHIFT and META keys...")    )ft.app(main)

