t = ft.Text(value="Hello, world!", color="green")

import flet as ftdef main(page: ft.Page):    t = ft.Text(value="Hello, world!", color="green")    page.controls.append(t)    page.update()ft.app(main)

t = ft.Text()page.add(t) # it's a shortcut for page.controls.append(t) and then page.update()for i in range(10):    t.value = f"Step {i}"    page.update()    time.sleep(1)

page.add(    ft.Row(controls=[        ft.Text("A"),        ft.Text("B"),        ft.Text("C")    ]))

page.add(    ft.Row(controls=[        ft.TextField(label="Your name"),        ft.ElevatedButton(text="Say my name!")    ]))

for i in range(10):    page.controls.append(ft.Text(f"Line {i}"))    if i > 4:        page.controls.pop(0)    page.update()    time.sleep(0.3)

def button_clicked(e):    page.add(ft.Text("Clicked!"))page.add(ft.ElevatedButton(text="Click me", on_click=button_clicked))

import flet as ftdef main(page):    def add_clicked(e):        page.add(ft.Checkbox(label=new_task.value))        new_task.value = ""        new_task.focus()        new_task.update()    new_task = ft.TextField(hint_text="What's needs to be done?", width=300)    page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))ft.app(main)

first_name = ft.TextField()last_name = ft.TextField()first_name.disabled = Truelast_name.disabled = Truepage.add(first_name, last_name)

first_name = ft.TextField()last_name = ft.TextField()c = ft.Column(controls=[    first_name,    last_name])c.disabled = Truepage.add(c)

btn = ft.ElevatedButton("Click me!")page.add(btn)

import flet as ftdef main(page: ft.Page):    page.title = "Flet counter example"    page.vertical_alignment = ft.MainAxisAlignment.CENTER    txt_number = ft.TextField(value="0", text_align="right", width=100)    def minus_click(e):        txt_number.value = str(int(txt_number.value) - 1)        page.update()    def plus_click(e):        txt_number.value = str(int(txt_number.value) + 1)        page.update()    page.add(        ft.Row(            [                ft.IconButton(ft.Icons.REMOVE, on_click=minus_click),                txt_number,                ft.IconButton(ft.Icons.ADD, on_click=plus_click),            ],            alignment=ft.MainAxisAlignment.CENTER,        )    )ft.app(main)

import flet as ftdef main(page):    def btn_click(e):        if not txt_name.value:            txt_name.error_text = "Please enter your name"            page.update()        else:            name = txt_name.value            page.clean()            page.add(ft.Text(f"Hello, {name}!"))    txt_name = ft.TextField(label="Your name")    page.add(txt_name, ft.ElevatedButton("Say hello!", on_click=btn_click))ft.app(main)

import flet as ftdef main(page):    def checkbox_changed(e):        output_text.value = (            f"You have learned how to ski :  {todo_check.value}."        )        page.update()    output_text = ft.Text()    todo_check = ft.Checkbox(label="ToDo: Learn how to use ski", value=False, on_change=checkbox_changed)    page.add(todo_check, output_text)ft.app(main)

import flet as ftdef main(page: ft.Page):    def button_clicked(e):        output_text.value = f"Dropdown value is:  {color_dropdown.value}"        page.update()    output_text = ft.Text()    submit_btn = ft.ElevatedButton(text="Submit", on_click=button_clicked)    color_dropdown = ft.Dropdown(        width=100,        options=[            ft.dropdown.Option("Red"),            ft.dropdown.Option("Green"),            ft.dropdown.Option("Blue"),        ],    )    page.add(color_dropdown, submit_btn, output_text)ft.app(main)

