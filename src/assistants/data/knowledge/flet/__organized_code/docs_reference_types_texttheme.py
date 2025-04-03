import flet as ftdef main(page: ft.Page):    page.theme = ft.Theme(        text_theme=ft.TextTheme(body_medium=ft.TextStyle(color=ft.Colors.GREEN))    )    page.add(ft.Text("Hello, green world!"))  # Text uses Body Medium style by defaultft.app(main)

