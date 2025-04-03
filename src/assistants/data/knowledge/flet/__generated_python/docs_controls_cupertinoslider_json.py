import flet as ft

def main(page):
    page.horizontal_alignment = page.vertical_alignment = "center"
    page.theme_mode = ft.ThemeMode.LIGHT

    def handle_change(e, slider_id):
        if slider_id == 1:
            slider1_value.value = str(e.control.value)
        elif slider_id == 2:
            slider2_value.value = str(e.control.value)
        page.update()

    slider1_value = ft.Text("0")
    slider2_value = ft.Text("0")

    page.add(
        slider1_value,
        ft.CupertinoSlider(
            min=0, max=100, divisions=10, value=50,
            active_color=ft.Colors.RED, thumb_color=ft.Colors.RED,
            on_change=lambda e: handle_change(e, 1),
        ),
        ft.Text("Slider 2"),
        slider2_value,
        ft.CupertinoSlider(
            min=0, max=200, divisions=20, value=100,
            active_color=ft.Colors.GREEN, thumb_color=ft.Colors.GREEN,
            on_change=lambda e: handle_change(e, 2),
        ),
    )

ft.app(main)

import flet as ft

def main(page):
    page.horizontal_alignment = page.vertical_alignment = "center"
    page.theme_mode = ft.ThemeMode.LIGHT

    def handle_change_start(e):
        slider_status.value = "Sliding"
        page.update()

    def handle_change(e):
        slider_value.value = f"{e.control.value:.2f}"
        page.update()

    def handle_change_end(e):
        slider_status.value = "Finished sliding"
        page.update()

    page.add(
        slider_value := ft.Text("25.0"),
        ft.CupertinoSlider(
            min=25,  # Definindo valor inicial
            max=75,  # Definindo valor final
            value=25,  # Valor inicial do controle deslizante
            divisions=5,
            active_color=ft.Colors.BLUE,
            thumb_color=ft.Colors.BLUE,
            on_change_start=handle_change_start,
            on_change_end=handle_change_end,
            on_change=handle_change,
        ),
        slider_status := ft.Text(),
    )

ft.app(main)

import flet as ft
   ```
   Esta linha importa a biblioteca Flet, que é usada para criar interfaces gráficas de usuário (GUI).

2. **Definição da função `main`**:
   ```python
   def main(page):
   ```
   Esta função é chamada quando a aplicação é iniciada. O argumento `page` representa a página principal da aplicação.

3. **Configurações da página**:
   ```python
   page.horizontal_alignment = page.vertical_alignment = "center"
   page.theme_mode = ft.ThemeMode.LIGHT
   ```
   - `horizontal_alignment` e `vertical_alignment` são configurados para "center" para centralizar os controles na página.
   - `theme_mode` é definido como `ft.ThemeMode.LIGHT`, o que aplica um tema claro à página.

4. **Eventos do Slider**:
   - `handle_change_start(e)`: Função chamada quando o usuário começa a mover o slider. Ela atualiza o texto de `slider_status` para "Sliding".
   - `handle_change(e)`: Função chamada enquanto o valor do slider está mudando. Atualiza o texto de `slider_value` para mostrar o valor atual do slider.
   - `handle_change_end(e)`: Função chamada quando o usuário termina de mover o slider. Define o `slider_status` para "Finished sliding".

5. **Adicionando controles à página**:
   ```python
   page.add(
       slider_value := ft.Text("0.0"),
       ft.CupertinoSlider(
           divisions=5,
           max=100,
           active_color=ft.Colors.PURPLE,
           thumb_color=ft.Colors.PURPLE,
           on_change_start=handle_change_start,
           on_change_end=handle_change_end,
           on_change=handle_change,
       ),
       slider_status := ft.Text(),
   )
   ```
   - `slider_value` é uma instância de `ft.Text` inicializada com o texto "0.0". Este texto mostra o valor atual do slider.
   - `ft.CupertinoSlider` cria um controle deslizante estilo Cupertino com:
     - `divisions=5`: Divide o slider em 5 partes.
     - `max=100`: Define o valor máximo do slider como 100.
     - `active_color` e `thumb_color` definidos como roxo (`ft.Colors.PURPLE`).
     - Eventos `on_change_start`, `on_change` e `on_change_end` associados às funções definidas anteriormente.
   - `slider_status` é outra instância de `ft.Text` que mostra o estado atual do slider ("Sliding" ou "Finished sliding").

6. **Iniciando a aplicação com Flet**:
   ```python
   ft.app(main)
   ```
   Esta linha inicia a aplicação chamando a função `main`.

Esse código exemplifica como criar uma interface de usuário interativa com um slider usando a biblioteca Flet, gerenciando eventos de interação do usuário e atualizando a interface com base nas ações do usuário.
O código Python que você forneceu utiliza a biblioteca Flet para criar uma interface gráfica simples com um controle deslizante (slider) e texto que reflete o valor do slider e o status da ação de deslizar. Vamos explorar algumas variações desse código para demonstrar diferentes formas de uso e estilização dos componentes na biblioteca Flet.

### Exemplo 1: Adicionando Título e Alterando o Tema

Neste exemplo, adicionaremos um título à página e mudaremos o tema para o modo escuro.
