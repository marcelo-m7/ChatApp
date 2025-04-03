import flet as ftdef main(page: ft.Page):    page.floating_action_button = ft.FloatingActionButton(        content=ft.Row(            [ft.Icon(ft.Icons.ADD), ft.Text("Add")], alignment="center", spacing=5        ),        bgcolor=ft.Colors.AMBER_300,        shape=ft.RoundedRectangleBorder(radius=5),        width=100,        mini=True,    )    page.add(ft.Text("Just a text!"))ft.app(main)

