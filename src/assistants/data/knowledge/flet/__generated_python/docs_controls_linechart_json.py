chart = ft.LineChart(...)

data_1 = [...]
data_2 = [...]

def main(page: ft.Page):
    ...

def toggle_data(e):
    ...

ft.app(main)

import flet as ft

class State:
    toggle = True

s = State()

import flet as ft

class State:
    toggle = True

s = State()

def main(page: ft.Page):
    # Dados para o gráfico de linha - duas séries de dados distintas
    data_1 = [
        ft.LineChartData(
            data_points=[
                ft.LineChartDataPoint(i, i**0.5) for i in range(1, 15)
            ],
            stroke_width=2,
            color=ft.Colors.BLUE,
            curved=True
        ),
        ft.LineChartData(
            data_points=[
                ft.LineChartDataPoint(i, i) for i in range(1, 15)
            ],
            stroke_width=2,
            color=ft.Colors.RED,
            curved=False
        )
    ]
    
    # Configuração inicial do gráfico
    chart = ft.LineChart(
        data_series=data_1,
        animate=1000,  # Animação de 1000 ms ao carregar dados
        min_y=0,
        max_y=15,
        min_x=1,
        max_x=14,
        expand=True
    )
    
    # Função para alternar entre curvas e linhas retas
    def toggle_curve(e):
        if s.toggle:
            for data in chart.data_series:
                data.curved = False
        else:
            for data in chart.data_series:
                data.curved = True
        s.toggle = not s.toggle
        chart.update()

    page.add(ft.IconButton(ft.Icons.REFRESH, on_click=toggle_curve), chart)

ft.app(main)

import flet as ft

class State:
    toggle = True

s = State()

def main(page: ft.Page):
    # Dados para o gráfico de linha com efeito de transparência
    data_1 = [
        ft.LineChartData(
            data_points=[
                ft.LineChartDataPoint(i, 2*i % 5 + 1) for i in range(1, 20)
            ],
            stroke_width=3,
            color=ft.Colors.with_opacity(0.75, ft.Colors.GREEN),
            below_line_bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.GREEN)
        )
    ]

    chart = ft.LineChart(
        data_series=data_1,
        min_y=0,
        max_y=6,
        min_x=1,
        max_x=19,
        expand=True
    )

    page.add(chart)

ft.app(main)

import flet as ft
import random

class State:
    update = True

s = State()

def main(page: ft.Page):
    # Dados iniciais
    data_series = [
        ft.LineChartData(
            data_points=[ft.LineChartDataPoint(x, random.uniform(0, 10)) for x in range(10)],
            color=ft.Colors.BLUE
        )
    ]
    
    chart = ft.LineChart(
        data_series=data_series,
        min_y=0, max_y=10, min_x=0, max_x=10,
        expand=True
    )

    # Função para atualizar os dados
    def update_data(e):
        new_data = [
            ft.LineChartData(
                data_points=[ft.LineChartDataPoint(x, random.uniform(0, 10)) for x in range(10)],
                color=ft.Colors.RED if s.update else ft.Colors.BLUE
            )
        ]
        chart.data_series = new_data
        s.update = not s.update
        chart.update()

    page.add(ft.IconButton(ft.Icons.REFRESH, on_click=update_data), chart)

ft.app(main)

page.add(ft.ElevatedButton("avg", on_click=toggle_data), chart)
