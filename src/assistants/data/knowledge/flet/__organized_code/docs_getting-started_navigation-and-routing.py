import flet as ftdef main(page: ft.Page):    page.add(ft.Text(f"Initial route: {page.route}"))ft.app(main, view=ft.AppView.WEB_BROWSER)

import flet as ftdef main(page: ft.Page):    page.add(ft.Text(f"Initial route: {page.route}"))    def route_change(e: ft.RouteChangeEvent):        page.add(ft.Text(f"New route: {e.route}"))    page.on_route_change = route_change    page.update()ft.app(main, view=ft.AppView.WEB_BROWSER)

import flet as ftdef main(page: ft.Page):    page.add(ft.Text(f"Initial route: {page.route}"))    def route_change(e: ft.RouteChangeEvent):        page.add(ft.Text(f"New route: {e.route}"))    def go_store(e):        page.route = "/store"        page.update()    page.on_route_change = route_change    page.add(ft.ElevatedButton("Go to Store", on_click=go_store))ft.app(main, view=ft.AppView.WEB_BROWSER)

import flet as ftdef main(page: ft.Page):    page.title = "Routes Example"    def route_change(route):        page.views.clear()        page.views.append(            ft.View(                "/",                [                    ft.AppBar(title=ft.Text("Flet app"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),                    ft.ElevatedButton("Visit Store", on_click=lambda _: page.go("/store")),                ],            )        )        if page.route == "/store":            page.views.append(                ft.View(                    "/store",                    [                        ft.AppBar(title=ft.Text("Store"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),                    ],                )            )        page.update()    def view_pop(view):        page.views.pop()        top_view = page.views[-1]        page.go(top_view.route)    page.on_route_change = route_change    page.on_view_pop = view_pop    page.go(page.route)ft.app(main, view=ft.AppView.WEB_BROWSER)

troute = TemplateRoute(page.route)if troute.match("/books/:id"):    print("Book view ID:", troute.id)elif troute.match("/account/:account_id/orders/:order_id"):    print("Account:", troute.account_id, "Order:", troute.order_id)else:    print("Unknown route")

ft.app(main, route_url_strategy="hash")

