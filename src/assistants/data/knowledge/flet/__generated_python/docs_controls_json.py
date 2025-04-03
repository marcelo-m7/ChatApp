c = ft.Column(controls=[ft.TextField(), ft.TextField()])
c.disabled = True
page.add(c)

from dataclasses import field

class Scale:
    scale: float = field(default=None)
    scale_x: float = field(default=None)
    scale_y: float = field(default=None)
    alignment: Alignment = field(default=None)

ft.Image(
    src="https://picsum.photos/100/100",
    width=100,
    height=100,
    border_radius=5,
    rotate=Rotate(angle=0.25 * pi, alignment=ft.alignment.center_left)
)

ft.Image(
    src="https://picsum.photos/100/100",
    width=100,
    height=100,
    border_radius=5,
    scale=Scale(scale_x=2, scale_y=0.5)
)

import flet as ft

class Message(ft.Container):
    def __init__(self, author, body):
        super().__init__()
        self.content = ft.Column(
            controls=[
                ft.Text(author, weight=ft.FontWeight.BOLD),
                ft.Text(body),
            ],
        )
        self.border = ft.border.all(1, ft.Colors.BLACK)
        self.border_radius = ft.border_radius.all(10)
        self.bgcolor = ft.Colors.GREEN_200
        self.padding = 10
        self.expand = True
        self.expand_loose = True

def main(page: ft.Page):
    ...
ft.app(main)

import flet as ft

def add_task(e, page, task_input, tasks_list):
    if task_input.value:
        tasks_list.controls.append(ft.ListTile(title=ft.Text(task_input.value)))
        task_input.value = ""
        page.update()

def main(page: ft.Page):
    task_input = ft.TextField(hint_text="Adicione uma nova tarefa", width=300)
    tasks_list = ft.ListView()
    add_button = ft.ElevatedButton(text="Adicionar", on_click=lambda e: add_task(e, page, task_input, tasks_list))
    page.add(ft.Column([task_input, add_button, tasks_list]))

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Stack(
            [
                ft.Container(
                    bgcolor="red",
                    width=100,
                    height=100,
                    left=100,
                    top=100,
                    offset=ft.transform.Offset(-1, -1),
                )
            ],
            width=1000,
            height=1000,
        )
    )
ft.app(main)

import flet as ft

def main(page: ft.Page):
    tab_control = ft.TabControl(tabs=[], width=400, height=300)
    add_tab_button = ft.ElevatedButton(
        text="Adicionar Tab",
        on_click=lambda e: tab_control.tabs.append(ft.Tab(text=f"Tab {len(tab_control.tabs) + 1}", content=ft.Text("Conteúdo")))
    )
    page.add(ft.Column([add_tab_button, tab_control]))

ft.app(main)

import flet as ft

def validate_form(e):
    if e.control.name == "age" and not e.control.value.isdigit():
        e.control.error_text = "Por favor, insira um número válido."
    else:
        e.control.error_text = ""

def main(page: ft.Page):
    form = ft.Column([
        ft.TextField(label="Nome", name="name", on_change=validate_form),
        ft.TextField(label="Idade", name="age", on_change=validate_form),
        ft.ElevatedButton(text="Enviar", on_click=lambda e: print("Formulário enviado"))
    ])
    page.add(form)

ft.app(main)

import flet as ft
import math

def main(page: ft.Page):
    image = ft.Image(
        src="https://picsum.photos/200/200",
        width=200,
        height=200,
        rotate=ft.Rotate(angle=0.5 * math.pi, alignment=ft.alignment.center)
    )
    page.add(image)

ft.app(main)
