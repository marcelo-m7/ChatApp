import flet as ft

def main(page: ft.Page):
    panel = ft.ExpansionPanelList(
        expand_icon_color=ft.Colors.BLUE,
        elevation=8,
        divider_color=ft.Colors.BLUE,
        controls=[]
    )

    def add_panel():
        new_panel = ft.ExpansionPanel(
            header=ft.ListTile(title=ft.Text(f"New Dynamic Panel")),
            bgcolor=ft.Colors.ORANGE_300
        )
        new_panel.content = ft.ListTile(
            title=ft.Text("New Panel Content"),
            subtitle=ft.Text("Added dynamically")
        )
        panel.controls.append(new_panel)
        page.update()

    add_button = ft.FloatingActionButton(
        content=ft.Icon(ft.Icons.ADD),
        on_click=lambda e: add_panel(),
        bgcolor=ft.Colors.GREEN
    )

    page.add(panel)
    page.add(add_button)

ft.app(main)

import flet as ft

def main(page: ft.Page):
    panel = ft.ExpansionPanelList(
        expand_icon_color=ft.Colors.RED,
        elevation=8,
        controls=[]
    )

    # Primeiro painel com imagem
    panel1 = ft.ExpansionPanel(
        header=ft.ListTile(title=ft.Text("Image Panel")),
        bgcolor=ft.Colors.BLUE_100
    )
    panel1.content = ft.Image(src="path/to/image.png")
    panel.controls.append(panel1)

    # Segundo painel com formulário
    panel2 = ft.ExpansionPanel(
        header=ft.ListTile(title=ft.Text("Form Panel")),
        bgcolor=ft.Colors.GREEN_100
    )
    form_content = ft.Column(
        controls=[
            ft.TextField(label="Name"),
            ft.TextField(label="Email"),
            ft.ElevatedButton(text="Submit")
        ]
    )
    panel2.content = form_content
    panel.controls.append(panel2)

    page.add(panel)

ft.app(main)

import flet as ft
   ```
   Importa a biblioteca Flet, que é usada para criar a interface de usuário.

2. **Definição da função main**:
   ```python
   def main(page: ft.Page):
   ```
   Define a função principal `main`, que aceita um parâmetro `page`. Este é um objeto `Page` que representa a página da aplicação onde os componentes da UI serão adicionados.

3. **Funções de manipulação de eventos**:
   ```python
   def handle_change(e: ft.ControlEvent):
       print(f"change on panel with index {e.data}")

   def handle_delete(e: ft.ControlEvent):
       panel.controls.remove(e.control.data)
       page.update()
   ```
   - `handle_change`: Função chamada quando há uma mudança no estado de expansão dos painéis. Ela imprime no console qual painel teve seu estado alterado.
   - `handle_delete`: Função que permite deletar um painel. Ela remove o painel da lista de controles do `panel` e atualiza a página para refletir essa mudança.

4. **Criação do ExpansionPanelList**:
   ```python
   panel = ft.ExpansionPanelList(
       expand_icon_color=ft.Colors.AMBER,
       elevation=8,
       divider_color=ft.Colors.AMBER,
       on_change=handle_change,
       controls=[
           ft.ExpansionPanel(
               bgcolor=ft.Colors.BLUE_400,
               expanded=True,
           )
       ]
   )
   ```
   Cria um objeto `ExpansionPanelList`, que é um container para múltiplos `ExpansionPanel`. Há configurações para cor do ícone de expansão, elevação, cor do divisor e um evento que é chamado quando há mudança de expansão. Inicialmente, adiciona-se um `ExpansionPanel` sem conteúdo especificado, apenas com cor de fundo e estado expandido.

5. **Adição de ExpansionPanels dinamicamente**:
   ```python
   colors = [ft.Colors.GREEN_500, ft.Colors.BLUE_800, ft.Colors.RED_800]
   for i in range(3):
       exp = ft.ExpansionPanel(
           bgcolor=colors[i % len(colors)],
           header=ft.ListTile(title=ft.Text(f"Panel {i}")),
       )
       exp.content = ft.ListTile(
           title=ft.Text(f"This is in Panel {i}"),
           subtitle=ft.Text(f"Press the icon to delete panel {i}"),
           trailing=ft.IconButton(ft.Icons.DELETE, on_click=handle_delete, data=exp),
       )
       panel.controls.append(exp)
   ```
   Este bloco adiciona três painéis (`ExpansionPanel`), cada um com uma cor de fundo específica, um cabeçalho e um conteúdo. O conteúdo de cada painel inclui um texto explicativo, um subtítulo e um ícone para deletar o painel. O método `on_click` do ícone está ligado à função `handle_delete`.

6. **Adição do painel à página**:
   ```python
   page.add(panel)
   ```
   Adiciona o `panel` completo à página.

7. **Execução da aplicação**:
   ```python
   ft.app(main)
   ```
   Inicia a aplicação chamando a função `main`, que configura e exibe a página.

Este script é um exemplo de como criar interfaces dinâmicas e interativas usando a biblioteca Flet em Python, permitindo aos usuários interagir com painéis expansíveis e manipular componentes da UI em tempo real.
O código fornecido em Python utiliza a biblioteca Flet para criar uma interface gráfica de usuário (GUI) que consiste em uma lista de painéis expansíveis (Expansion Panels). Abaixo, apresentarei diferentes exemplos modificando o código original para demonstrar diversas formas de uso dos Expansion Panels, incluindo alterações de estilo, interações e funcionalidades.

### Exemplo 1: Alterando Cores e Ícones
Neste exemplo, modificaremos as cores e ícones dos painéis para torná-los mais personalizados.
