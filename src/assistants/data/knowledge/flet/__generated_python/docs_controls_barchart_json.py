import flet as ft

def main(page: ft.Page):
    data_values = [20, 40, 60, 80, 100]
    colors = [ft.Colors.RED, ft.Colors.ORANGE, ft.Colors.YELLOW, ft.Colors.GREEN, ft.Colors.BLUE]

    bar_groups = [
        ft.BarChartGroup(
            x=i,
            bar_rods=[
                ft.BarChartRod(
                    from_y=0,
                    to_y=data_values[i],
                    color=colors[i],
                    gradient=ft.Gradient(colors[i], ft.Colors.with_opacity(0.4, colors[i]))
                )
            ]
        ) for i in range(len(data_values))
    ]

    chart = ft.BarChart(
        bar_groups=bar_groups,
        expand=True,
    )
    page.add(chart)

ft.app(main)

import flet as ft
   ```
   Importa a biblioteca Flet, que é usada para construir interfaces de usuário.

2. **Função Principal**:
   ```python
   def main(page: ft.Page):
   ```
   Define a função principal que recebe um objeto `Page` como argumento. Este objeto representa a página web onde o gráfico será exibido.

3. **Criação do Gráfico de Barras**:
   - **`BarChart`**:
     Cria um gráfico de barras com várias propriedades como bordas, eixos e linhas de grade. Alguns pontos importantes:
     - `bar_groups`: Define grupos de barras. Cada grupo pode ter uma ou mais barras.
     - `BarChartRod`: Define a barra individual com propriedades como altura, cor, largura e bordas.
     - `ChartAxis`: Define os eixos do gráfico, incluindo os rótulos nos eixos.
     - `ChartGridLines`: Adiciona linhas de grade horizontais para melhor visualização dos valores.
   - **Eventos e Interações**:
     - `interactive`: Permite interações com o gráfico, como destacar ao passar o mouse.
   - **Adição ao Page**:
     ```python
     page.add(chart)
     ```
     Adiciona o gráfico à página.

4. **Execução da Aplicação**:
   ```python
   ft.app(main)
   ```
   Inicia a aplicação chamando a função `main`.

### Segundo Bloco de Código

Este bloco mostra uma implementação mais avançada com interatividade e customização de barras.

1. **Classe Customizada `SampleRod`**:
   - Herda de `BarChartRod` e adiciona comportamentos personalizados, como mudar a cor e adicionar bordas quando a barra é destacada (hover).
   - Métodos `_before_build_command` e `_build` são sobrescritos para modificar propriedades antes da construção da barra.

2. **Função Principal com Eventos**:
   - **`on_chart_event`**:
     Define um manipulador de eventos que atualiza o estado de "hover" das barras baseado na interação do usuário.
   - **Criação do `BarChart` com `SampleRod`**:
     Usa a classe `SampleRod` para criar barras que respondem ao evento de hover.
   - **Container**:
     Envolve o gráfico em um `Container` com propriedades visuais adicionais como cor de fundo e bordas arredondadas.

Ambos os blocos de código ilustram como construir gráficos interativos em uma aplicação web usando a biblioteca Flet em Python. As personalizações adicionadas no segundo exemplo demonstram a flexibilidade da biblioteca para atender a necessidades específicas de design e interação do usuário.
Aqui estão alguns exemplos adicionais que demonstram diferentes formas de usar o código original do gráfico de barras e o exemplo com `SampleRod`, modificando aspectos como o tipo de dados apresentados, a estilização e a interatividade. Cada exemplo foi criado para ilustrar como você pode adaptar o gráfico para diferentes cenários.

### Exemplo 1: Gráfico de Barras com Dados Dinâmicos e Eventos de Mouse

Este exemplo mostra como você pode modificar a altura das barras de forma dinâmica ao passar o mouse, fornecendo uma interação visual mais direta.

import flet as ft
import time

def main(page: ft.Page):
    data_values = [35, 50, 45, 60, 55]
    bar_groups = [
        ft.BarChartGroup(
            x=i,
            bar_rods=[ft.BarChartRod(from_y=0, to_y=0, color=ft.Colors.PURPLE)]
        ) for i in range(len(data_values))
    ]

    chart = ft.BarChart(bar_groups=bar_groups, expand=True)
    page.add(chart)

    # Animação de crescimento das barras
    for increment in range(1, 11):  # 10 passos de animação
        for i, group in enumerate(chart.bar_groups):
            group.bar_rods[0].to_y = data_values[i] * (increment / 10)
        chart.update()
        time.sleep(0.1)  # Pausa entre atualizações para visualizar a animação

ft.app(main)
