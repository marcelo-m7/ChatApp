c1 = ft.Container(bgcolor='#ff0000')

color = ft.Colors.with_opacity(0.5, ft.Colors.PRIMARY)color = ft.Colors.with_opacity(0.5, '#ff6666')

color = "surface,0.5"

color = "#7fff6666"

c = ft.Container(width=100, height=100, bgcolor=ft.Colors.GREEN_200)

import flet as ftdef main(page: ft.Page):              page.add(        ft.Container(            width=200,            height=200,            border=ft.border.all(1, ft.Colors.BLACK),            content=ft.FilledButton("Primary color"),            theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.Colors.YELLOW))        )    )ft.app(main)

>>> import flet as ft>>> ft.Icons.ABC>>> ft.CupertinoIcons.BACK>>> ft.Icons.random()>>> ft.CupertinoIcons.random()>>> ft.Icons.random(exclude=[ft.Icons.FAVORITE, ft.Icons.SCHOOL], weights={ft.Icons.SCHOOL: 150, ft.Icons.ADJUST: 5})>>> ft.CupertinoIcons.random(exclude=[ft.CupertinoIcons.CAMERA, ft.CupertinoIcons.TABLE], weights={ft.CupertinoIcons.TABLE: 150, ft.CupertinoIcons.PENCIL: 5})

