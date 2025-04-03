import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Column(
            controls=[
                ft.CupertinoCheckbox(label="Cupertino Checkbox", value=True),
                ft.Checkbox(label="Material Checkbox", value=True),
                ft.Text("Adaptive Checkbox shows as CupertinoCheckbox on macOS and iOS and as Checkbox on other platforms:"),
                ft.Checkbox(adaptive=True, label="Adaptive Checkbox", value=True)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            cross_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Container(
            content=ft.Column(controls=[
                ft.CupertinoCheckbox(label="Cupertino Checkbox", value=True),
                ft.Container(height=10),  # Espaçamento vertical
                ft.Checkbox(label="Material Checkbox", value=True),
                ft.Container(height=20),  # Espaçamento maior
                ft.Text("Adaptive Checkbox shows as CupertinoCheckbox on macOS and iOS and as Checkbox on other platforms:"),
                ft.Checkbox(adaptive=True, label="Adaptive Checkbox", value=True)
            ]),
            padding=ft.EdgeInsets.all(20),  # Padding interno
            border=ft.Border.all(color=ft.colors.BLUE_GREY, width=2),  # Borda ao redor do container
            width=300
        )
    )

ft.app(main)

import flet as ft
   ```
   Este comando importa a biblioteca Flet e a referencia com o alias `ft`. Isso significa que você pode acessar todas as funções e classes de Flet usando o prefixo `ft`.

2. **Definição da função main**:
   ```python
   def main(page: ft.Page):
   ```
   Aqui, a função `main` é definida, tendo como parâmetro `page`, que é um objeto do tipo `ft.Page`. Esse objeto representa a página da aplicação onde os componentes da interface serão adicionados.

3. **Adicionando componentes à página**:
   ```python
   page.add(
       ft.CupertinoCheckbox(label="Cupertino Checkbox", value=True),
       ft.Checkbox(label="Material Checkbox", value=True),
       ft.Container(height=20),
       ft.Text("Adaptive Checkbox shows as CupertinoCheckbox on macOS and iOS and as Checkbox on other platforms:"),
       ft.Checkbox(adaptive=True, label="Adaptive Checkbox", value=True),
   )
   ```
   Dentro da função `main`, os componentes são adicionados à página usando o método `add` do objeto `page`. Os componentes adicionados são:
   
   - **CupertinoCheckbox**: Este é um tipo específico de caixa de seleção estilizada conforme o design do sistema operacional iOS (parte do design da Apple). O parâmetro `label` define o texto que aparece ao lado da caixa de seleção, e `value=True` indica que a caixa está marcada por padrão.
   
   - **Checkbox**: Este é um tipo de caixa de seleção baseado no design Material (do Google). Assim como o `CupertinoCheckbox`, ele aceita um `label` e um `value`.
   
   - **Container**: Um container com altura de 20 pixels, provavelmente usado para criar um espaço entre os componentes anteriores e os seguintes.
   
   - **Text**: Um componente que exibe um texto explicativo sobre o próximo componente.
   
   - **Checkbox (adaptive)**: Esta caixa de seleção é adaptativa, o que significa que ela muda de estilo dependendo da plataforma em que a aplicação está sendo executada. Em plataformas macOS e iOS, ela se parece com `CupertinoCheckbox`, enquanto em outras plataformas se parece com `Checkbox`. Também possui as propriedades `label` e `value`.

4. **Execução da aplicação**:
   ```python
   ft.app(main)
   ```
   Esta linha inicia a aplicação, passando a função `main` como argumento para `ft.app`. Isso diz ao Flet para usar a função `main` como ponto de entrada da aplicação, que configura e exibe a página com os componentes definidos.

Em resumo, o código cria uma aplicação GUI simples com diferentes tipos de caixas de seleção usando a biblioteca Flet, demonstrando tanto um uso específico de estilo (Cupertino e Material) quanto um uso adaptativo de componentes de acordo com a plataforma.
O código Python que você forneceu usa Flet, uma biblioteca para criar aplicativos de interface gráfica multiplataforma em Python. O exemplo mostra como adicionar diferentes tipos de caixas de seleção (checkboxes) a uma página, incluindo um checkbox estilo Cupertino, um checkbox estilo Material e um checkbox adaptativo que muda de estilo dependendo da plataforma. Abaixo, vou expandir este exemplo com mais variações e funcionalidades para explorar outras capacidades de Flet.

### Exemplo 1: Adicionando Eventos aos Checkboxes
Vamos adicionar eventos para que, ao alterar o estado de cada checkbox, uma mensagem seja exibida.
