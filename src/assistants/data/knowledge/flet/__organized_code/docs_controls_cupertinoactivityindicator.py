import flet as ftdef main(page):    page.theme_mode = ft.ThemeMode.LIGHT    page.add(        ft.CupertinoActivityIndicator(            radius=50,            color=ft.Colors.RED,            animating=True,        )    )ft.app(main)

