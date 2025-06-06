import flet as ftdef main(page):    first_name = ft.TextField(label="First name", autofocus=True)    last_name = ft.TextField(label="Last name")    greetings = ft.Column()    def btn_click(e):        greetings.controls.append(ft.Text(f"Hello, {first_name.value} {last_name.value}!"))        first_name.value = ""        last_name.value = ""        page.update()        first_name.focus()    page.add(        first_name,        last_name,        ft.ElevatedButton("Say hello!", on_click=btn_click),        greetings,    )ft.app(main)

page.add(        first_name,        last_name,        ft.ElevatedButton("Say hello!", on_click=btn_click),        greetings,    )

first_name = ft.Ref[ft.TextField]()

# empty first namefirst_name.current.value = ""

page.add(    ft.TextField(ref=first_name, label="First name", autofocus=True))

import flet as ftdef main(page):    first_name = ft.Ref[ft.TextField]()    last_name = ft.Ref[ft.TextField]()    greetings = ft.Ref[ft.Column]()    def btn_click(e):        greetings.current.controls.append(            ft.Text(f"Hello, {first_name.current.value} {last_name.current.value}!")        )        first_name.current.value = ""        last_name.current.value = ""        page.update()        first_name.current.focus()    page.add(        ft.TextField(ref=first_name, label="First name", autofocus=True),        ft.TextField(ref=last_name, label="Last name"),        ft.ElevatedButton("Say hello!", on_click=btn_click),        ft.Column(ref=greetings),    )ft.app(main)

