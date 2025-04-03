def main(page: ft.Page):

ft.app(main)

import flet as ft

import flet as ft

def main(page: ft.Page):
    page.title = "Botões com Cores Customizadas"
    page.add(
        ft.FilledTonalButton(text="Botão Vermelho", color=ft.colors.RED),
        ft.FilledTonalButton(text="Botão Azul", color=ft.colors.BLUE),
        ft.FilledTonalButton(text="Botão Verde", color=ft.colors.GREEN),
    )

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.title = "Botões com Ícones e Tooltips"
    page.add(
        ft.FilledTonalButton(text="Adicionar", icon="add", tooltip="Adicionar item"),
        ft.FilledTonalButton(text="Editar", icon="edit", tooltip="Editar item"),
        ft.FilledTonalButton(text="Deletar", icon="delete", tooltip="Deletar item", disabled=True),
    )

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.title = "Botões de Diferentes Tamanhos"
    page.add(
        ft.FilledTonalButton(text="Pequeno", size=ft.ButtonSize.SMALL),
        ft.FilledTonalButton(text="Médio", size=ft.ButtonSize.MEDIUM),
        ft.FilledTonalButton(text="Grande", size=ft.ButtonSize.LARGE),
    )

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.title = "Organização de Botões"
    row = ft.Row([
        ft.FilledTonalButton(text="Botão 1"),
        ft.FilledTonalButton(text="Botão 2"),
        ft.FilledTonalButton(text="Botão 3"),
    ])
    column = ft.Column([
        ft.FilledTonalButton(text="Botão A"),
        ft.FilledTonalButton(text="Botão B"),
        ft.FilledTonalButton(text="Botão C"),
    ])
    page.add(row, column)

ft.app(main)

import flet as ft

def on_button_click(e):
    e.control.text = "Clicado!"

def main(page: ft.Page):
    page.title = "Botões com Eventos"
    button = ft.FilledTonalButton(text="Clique-me", on_click=on_button_click)
    page.add(button)

ft.app(main)

page.add(
        ft.FilledTonalButton(text="Filled tonal button"),
        ft.FilledTonalButton("Disabled button", disabled=True),
        ft.FilledTonalButton("Button with icon", icon="add"),
    )

page.title = "Basic filled tonal buttons"
