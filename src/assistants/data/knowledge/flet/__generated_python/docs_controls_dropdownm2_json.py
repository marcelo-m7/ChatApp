import flet as ft

def main(page: ft.Page):
    dd = ft.DropdownM2(
        options=[
            ft.dropdownm2.OptionGroup(
                label="Cores Primárias",
                options=[
                    ft.dropdownm2.Option("Red"),
                    ft.dropdownm2.Option("Blue"),
                    ft.dropdownm2.Option("Yellow"),
                ]
            ),
            ft.dropdownm2.OptionGroup(
                label="Cores Secundárias",
                options=[
                    ft.dropdownm2.Option("Green"),
                    ft.dropdownm2.Option("Orange"),
                    ft.dropdownm2.Option("Purple"),
                ]
            )
        ],
        width=250,
    )
    page.add(dd)

ft.app(main)

import flet as ft

def main(page: ft.Page):
    def button_clicked(e):
        t.value = f"Dropdown value is:  {dd.value}"
        page.update()
    t = ft.Text()
    b = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    dd = ft.DropdownM2(
        width=100,
        options=[
            ft.dropdownm2.Option("Red"),
            ft.dropdownm2.Option("Green"),
            ft.dropdownm2.Option("Blue"),
        ],
    )
    page.add(dd, b, t)

ft.app(main)

import flet as ft

def main(page: ft.Page):
    def dropdown_changed(e):
        t.value = f"Dropdown changed to {dd.value}"
        page.update()
    t = ft.Text()
    dd = ft.DropdownM2(
        on_change=dropdown_changed,
        options=[
            ft.dropdownm2.Option("Red"),
            ft.dropdownm2.Option("Green"),
            ft.dropdownm2.Option("Blue"),
        ],
        width=200,
    )
    page.add(dd, t)

ft.app(main)

import flet as ft

def main(page: ft.Page):
    def find_option(option_name):
        for option in d.options:
            if option_name == option.key:
                return option
        return None
    def add_clicked(e):
        d.options.append(ft.dropdown.Option(option_textbox.value))
        d.value = option_textbox.value
        option_textbox.value = ""
        page.update()
    def delete_clicked(e):
        option = find_option(d.value)
        if option != None:
            d.options.remove(option)
            # d.value = None
            page.update()
    d = ft.DropdownM2()
    option_textbox = ft.TextField(hint_text="Enter item name")
    add = ft.ElevatedButton("Add", on_click=add_clicked)
    delete = ft.OutlinedButton("Delete selected", on_click=delete_clicked)
    page.add(d, ft.Row(controls=[option_textbox, add, delete]))

ft.app(main)

import flet as ft

def main(page: ft.Page):
    def selections_changed(e):
        selected_values.value = ", ".join(dd.values)
        page.update()

    dd = ft.DropdownM2(
        options=[
            ft.dropdownm2.Option("Apple"),
            ft.dropdownm2.Option("Banana"),
            ft.dropdownm2.Option("Cherry"),
        ],
        multiple=True,
        on_change=selections_changed,
        width=200,
    )
    selected_values = ft.Text(value="")

    page.add(dd, selected_values)

ft.app(main)

import flet as ft

def main(page: ft.Page):
    def submit_clicked(e):
        if not dd.value:
            error_message.value = "Por favor, selecione uma cor!"
        else:
            error_message.value = ""
        page.update()

    dd = ft.DropdownM2(
        options=[
            ft.dropdownm2.Option("Red"),
            ft.dropdownm2.Option("Green"),
            ft.dropdownm2.Option("Blue"),
        ],
        width=200,
    )
    submit_button = ft.ElevatedButton(text="Submit", on_click=submit_clicked)
    error_message = ft.Text(value="", color=0xFF0000)

    page.add(dd, submit_button, error_message)

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.add(
        ft.DropdownM2(
            label="Color",
            hint_text="Choose your favourite color?",
            options=[
                ft.dropdownm2.Option("Red"),
                ft.dropdownm2.Option("Green"),
                ft.dropdownm2.Option("Blue"),
            ],
            autofocus=True,
        )
    )

ft.app(main)
