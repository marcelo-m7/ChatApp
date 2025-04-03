columns=[
    ft.DataColumn(
        ft.Text("Column 1"),
        on_sort=lambda e: print(f"{e.column_index}, {e.ascending}"),
    ),
    ft.DataColumn(
        ft.Text("Column 2"),
        tooltip="This is a second column",
        numeric=True,
        on_sort=lambda e: print(f"{e.column_index}, {e.ascending}"),
    ),
]

def main(page: ft.Page):

ft.app(main)

import flet as ft

import flet as ft

def main(page: ft.Page):
    ROWS_PER_PAGE = 10
    current_page = 0

    all_data_rows = [
        ft.DataRow(cells=[ft.DataCell(ft.Text(f"Item {i}")), ft.DataCell(ft.Text(f"Category {i % 5}")), ft.DataCell(ft.Text(str(i * 10)))])
        for i in range(100)
    ]

    data_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Item")),
            ft.DataColumn(ft.Text("Category")),
            ft.DataColumn(ft.Text("Value"), numeric=True),
        ],
        rows=all_data_rows[:ROWS_PER_PAGE]
    )

    def update_rows(page_number):
        start_index = page_number * ROWS_PER_PAGE
        end_index = start_index + ROWS_PER_PAGE
        data_table.rows = all_data_rows[start_index:end_index]
        page.update()

    btn_next = ft.Button(text="Next", on_click=lambda e: update_rows(current_page + 1))
    btn_prev = ft.Button(text="Prev", on_click=lambda e: update_rows(current_page - 1))

    page.add(btn_prev, btn_next, data_table)

ft.app(main)

import flet as ft

def main(page: ft.Page):
    def filter_data(e):
        filter_text = e.control.value.lower()
        filtered_rows = [
            row for row in all_rows if filter_text in row.cells[1].control.text.lower()
        ]
        data_table.rows = filtered_rows
        page.update()

    all_rows = [
        ft.DataRow(cells=[ft.DataCell(ft.Text("John")), ft.DataCell(ft.Text("Smith")), ft.DataCell(ft.Text("43"))]),
        ft.DataRow(cells=[ft.DataCell(ft.Text("Jack")), ft.DataCell(ft.Text("Brown")), ft.DataCell(ft.Text("19"))]),
        ft.DataRow(cells=[ft.DataCell(ft.Text("Alice")), ft.DataCell(ft.Text("Wong")), ft.DataCell(ft.Text("25"))]),
    ]

    data_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("First Name")),
            ft.DataColumn(ft.Text("Last Name")),
            ft.DataColumn(ft.Text("Age"), numeric=True),
        ],
        rows=all_rows,
    )

    txt_filter = ft.TextField(label="Filter by name:", on_change=filter_data)
    
    page.add(txt_filter, data_table)

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.add(
        ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Status")),
                ft.DataColumn(ft.Text("Nome")),
                ft.DataColumn(ft.Text("Pontuação"), numeric=True),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Icon(ft.Icons.CHECK, color=ft.Colors.GREEN)),
                        ft.DataCell(ft.Text("Maria")),
                        ft.DataCell(ft.Text("85")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Icon(ft.Icons.CLOSE, color=ft.Colors.RED)),
                        ft.DataCell(ft.Text("João")),
                        ft.DataCell(ft.Text("45")),
                    ],
                ),
            ],
        ),
    )

ft.app(main)

page.add(
    ft.DataTable(
        width=700,
        bgcolor="yellow",
        border=ft.border.all(2, "red"),
        border_radius=10,
        vertical_lines=ft.BorderSide(3, "blue"),
        horizontal_lines=ft.BorderSide(1, "green"),
        sort_column_index=0,
        sort_ascending=True,
        heading_row_color=ft.Colors.BLACK12,
        heading_row_height=100,
        data_row_color={ft.ControlState.HOVERED: "0x30FF0000"},
        show_checkbox_column=True,
        divider_thickness=0,
        column_spacing=200,
        columns=[...],
        rows=[...]
    )
)

rows=[
    ft.DataRow(
        [ft.DataCell(ft.Text("A")), ft.DataCell(ft.Text("1"))],
        selected=True,
        on_select_changed=lambda e: print(f"row select changed: {e.data}"),
    ),
    ft.DataRow([ft.DataCell(ft.Text("B")), ft.DataCell(ft.Text("2"))]),
]
