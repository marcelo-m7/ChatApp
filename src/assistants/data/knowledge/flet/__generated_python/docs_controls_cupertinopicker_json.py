cupertino_picker = ft.CupertinoPicker(
    selected_index=3,
    magnification=1.22,
    squeeze=1.2,
    use_magnifier=True,
    on_change=handle_picker_change,
    controls=[ft.Text(value=f) for f in fruits],
)

def handle_picker_change(e):
    selected_fruit_ref.current.value = fruits[int(e.data)]
    page.update()

def main(page):

fruits = ["Apple", "Mango", "Banana", "Orange", "Pineapple", "Strawberry"]

ft.app(main)

import flet as ft

import flet as ft

def main(page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    selected_fruit_ref = ft.Ref[ft.Text]()
    fruits = ["Apple", "Mango", "Banana", "Orange", "Pineapple", "Strawberry"]

    def handle_dropdown_change(e):
        selected_fruit_ref.current.value = e.control.value
        page.update()

    dropdown = ft.Dropdown(
        value=fruits[3],
        options=[ft.DropdownOption(text=f, value=f) for f in fruits],
        on_change=handle_dropdown_change
    )

    page.add(
        ft.Row(
            tight=True,
            controls=[
                ft.Text("Selected Fruit:", size=23),
                dropdown,
                ft.Text(value=fruits[3], ref=selected_fruit_ref, size=23),
            ],
        ),
    )

ft.app(main)

import flet as ft

def main(page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    selected_fruit_ref = ft.Ref[ft.Text]()
    fruits = ["Apple", "Mango", "Banana", "Orange", "Pineapple", "Strawberry"]
    loading_ref = ft.Ref[ft.CupertinoActivityIndicator]()

    def handle_picker_change(e):
        loading_ref.current.visible = True  # Mostra o loading
        selected_fruit_ref.current.value = fruits[int(e.data)]
        page.update()

        # Simula uma operação que leva tempo
        import time
        time.sleep(2)  # Pausa para simulação
        loading_ref.current.visible = False  # Esconde o loading
        page.update()

    cupertino_picker = ft.CupertinoPicker(
        selected_index=3,
        magnification=1.22,
        squeeze=1.2,
        use_magnifier=True,
        on_change=handle_picker_change,
        controls=[ft.Text(value=f) for f in fruits],
    )

    page.add(
        ft.Row(
            tight=True,
            controls=[
                ft.Text("Selected Fruit:", size=23),
                ft.TextButton(
                    content=ft.Text(value=fruits[3], ref=selected_fruit_ref, size=23),
                    style=ft.ButtonStyle(color=ft.Colors.BLUE),
                    on_click=lambda e: page.open(
                        ft.CupertinoBottomSheet(
                            cupertino_picker,
                            height=216,
                            padding=ft.padding.only(top=6),
                        )
                    ),
                ),
                ft.CupertinoActivityIndicator(ref=loading_ref, visible=False),
            ],
        ),
    )

ft.app(main)

page.add(
    ft.Row(
        tight=True,
        controls=[
            ft.Text("Selected Fruit:", size=23),
            ft.TextButton(
                content=ft.Text(value=fruits[3], ref=selected_fruit_ref, size=23),
                style=ft.ButtonStyle(color=ft.Colors.BLUE),
                on_click=lambda e: page.open(
                    ft.CupertinoBottomSheet(
                        cupertino_picker,
                        height=216,
                        padding=ft.padding.only(top=6),
                    )
                ),
            ),
        ],
    ),
)

page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

selected_fruit_ref = ft.Ref[ft.Text]()
