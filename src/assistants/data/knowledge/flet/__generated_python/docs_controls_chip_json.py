import flet as ft

def main(page: ft.Page):
    amenities = {
        "Washer / Dryer": ft.Icons.LOCAL_LAUNDRY_SERVICE,
        "Ramp access": ft.Icons.ACCESSIBILITY,
        "Dogs OK": ft.Icons.PETS,
        "Cats OK": ft.Icons.PETS,
        "Smoke-free": ft.Icons.SMOKE_FREE
    }

    amenity_chips = []
    for amenity, icon in amenities.items():
        amenity_chips.append(
            ft.Chip(
                label=ft.Text(amenity),
                leading=ft.Icon(icon),
                bgcolor=ft.Colors.GREEN_200,
                disabled_color=ft.Colors.GREEN_100,
                autofocus=True
            )
        )

    page.add(ft.Row([ft.Icon(ft.Icons.HOTEL_CLASS), ft.Text("Amenities")]), ft.Row(amenity_chips))

ft.app(main)

import flet as ft

def main(page: ft.Page):
    def open_link(e, url):
        page.launch_url(url)
        page.update()

    destinations = {
        "Google Maps": "https://maps.google.com",
        "Weather": "https://weather.com",
        "News": "https://news.google.com"
    }

    chips = []
    for label, url in destinations.items():
        chips.append(ft.Chip(
            label=ft.Text(label),
            leading=ft.Icon(ft.Icons.LINK),
            bgcolor=ft.Colors.BLUE_200,
            on_click=lambda e, url=url: open_link(e, url)
        ))

    page.add(ft.Row(chips))

ft.app(main)

import flet as ft

def main(page: ft.Page):
    def save_to_favorites_clicked(e):
        e.control.label.value = "Saved!"
        e.control.leading = ft.Icon(ft.Icons.FAVORITE)
        e.control.bgcolor = ft.Colors.RED_200
        e.control.disabled = True
        page.update()

    save_to_favourites = ft.Chip(
        label=ft.Text("Save to favourites"),
        leading=ft.Icon(ft.Icons.FAVORITE_BORDER_OUTLINED),
        bgcolor=ft.Colors.GREEN_200,
        disabled_color=ft.Colors.GREEN_100,
        autofocus=True,
        on_click=save_to_favorites_clicked,
    )

    page.add(save_to_favourites)

ft.app(main)
