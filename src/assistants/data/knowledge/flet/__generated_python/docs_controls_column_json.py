import flet as ft

def main(page: ft.Page):
    def items(count, color):
        items = []
        for i in range(1, count + 1):
            items.append(
                ft.Container(
                    content=ft.Text(value=str(i)),
                    alignment=ft.alignment.center,
                    width=50,
                    height=50,
                    bgcolor=color,
                    border_radius=ft.border_radius.all(5),
                )
            )
        return items

    def color_slider_change(e):
        new_color_value = int(e.control.value)
        new_color = ft.Colors.get_color_by_value(new_color_value)
        for item in col.controls:
            item.bgcolor = new_color
        col.update()

    color_slider = ft.Slider(
        min=0,
        max=0xFFFFFF,  # RGB Color range
        value=0xFFC107,  # Default to AMBER
        label="Change Color",
        width=500,
        on_change=color_slider_change,
    )
    
    col = ft.Column(spacing=10, controls=items(5, ft.Colors.AMBER))
    page.add(ft.Column([ft.Text("Change Background Color:"), color_slider]), col)

ft.app(main)

import flet as ft

def main(page: ft.Page):
    list_items = ft.Column(spacing=10)

    def add_item(e):
        new_item = ft.Text(f"Item {len(list_items.controls) + 1}")
        list_items.controls.append(new_item)
        list_items.update()

    def remove_item(e):
        if list_items.controls:
            list_items.controls.pop()
            list_items.update()

    add_button = ft.ElevatedButton("Add Item", on_click=add_item)
    remove_button = ft.ElevatedButton("Remove Item", on_click=remove_item)
    controls_row = ft.Row([add_button, remove_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

    scrollable_list = ft.Container(content=list_items, height=200, scroll=ft.ScrollMode.ALWAYS)
    page.add(controls_row, scrollable_list)

ft.app(main)

import flet as ft

def main(page: ft.Page):
    toggle_container = ft.Container(visible=False, content=ft.Text("This text is toggleable."))

    def toggle_visibility(e):
        toggle_container.visible = not toggle_container.visible
        page.update()

    toggle_switch = ft.ToggleSwitch(label="Show/Hide Text", on_change=toggle_visibility)
    page.add(toggle_switch, toggle_container)

ft.app(main)
