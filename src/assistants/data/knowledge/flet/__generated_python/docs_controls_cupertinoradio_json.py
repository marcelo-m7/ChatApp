import flet as ft

def main(page):
    def dropdown_changed(e):
        t.value = f"Your favorite color is: {dd.value}"
        page.update()

    t = ft.Text()
    dd = ft.Dropdown(
        options=[
            ft.DropdownOption("red", "Red"),
            ft.DropdownOption("green", "Green"),
            ft.DropdownOption("blue", "Blue")
        ],
        on_change=dropdown_changed
    )
    page.add(ft.Text("Select your favorite color:"), dd, t)

ft.app(main)

import flet as ft

def main(page):
    def slider_changed(e):
        color_value = int(slider.value)
        t.value = f"Your favorite color intensity for blue is: {color_value}%"
        page.update()

    t = ft.Text()
    slider = ft.Slider(min=0, max=100, divisions=10, label="Intensity", on_change=slider_changed)
    
    page.add(ft.Text("Adjust the blue color intensity:"), slider, t)

ft.app(main)

import flet as ft
   ```
   Este código importa a biblioteca Flet que é usada para criar interfaces de usuário web.

2. **Definição da Função Principal `main`**:
   ```python
   def main(page):
   ```
   A função `main` é chamada automaticamente pelo Flet quando a aplicação é iniciada. O parâmetro `page` representa a página da aplicação web.

3. **Definição da Função `button_clicked`**:
   ```python
   def button_clicked(e):
       t.value = f"Your favorite color is: {cg.value}"
       page.update()
   ```
   Esta função é chamada quando o botão é clicado. Ela atualiza o valor do objeto `Text` `t` para mostrar o valor selecionado no grupo de rádio `cg`. Depois, atualiza a página para refletir a mudança na interface do usuário.

4. **Criação de Widgets**:
   - **Objeto Text**:
     ```python
     t = ft.Text()
     ```
     Cria um widget de texto vazio que será usado para mostrar a cor selecionada após o usuário clicar no botão.
   
   - **Botão Elevado**:
     ```python
     b = ft.ElevatedButton(text="Submit", on_click=button_clicked)
     ```
     Cria um botão com o texto "Submit". `on_click=button_clicked` especifica que a função `button_clicked` deve ser chamada quando o botão é clicado.

   - **Grupo de Rádio**:
     ```python
     cg = ft.RadioGroup(
         content=ft.Column(
             [
                 ft.CupertinoRadio(value="red", label="Red - Cupertino Radio", active_color=ft.Colors.RED, inactive_color=ft.Colors.RED),
                 ft.Radio(value="green", label="Green - Material Radio", fill_color=ft.Colors.GREEN),
                 ft.Radio(value="blue", label="Blue - Adaptive Radio", adaptive=True, active_color=ft.Colors.BLUE),
             ]
         )
     )
     ```
     Cria um grupo de rádio com três opções distintas, cada uma com estilos diferentes:
     - **CupertinoRadio**: Estilo específico para iOS com cores ativas e inativas definidas.
     - **Radio (Material)**: Estilo padrão do Material Design com uma cor de preenchimento.
     - **Adaptive Radio**: Um rádio que se adapta ao sistema operacional do usuário, com uma cor ativa definida.

5. **Adicionando Widgets à Página**:
   ```python
   page.add(ft.Text("Select your favorite color:"), cg, b, t)
   ```
   Adiciona um widget de texto com uma instrução, o grupo de rádio `cg`, o botão `b` e o texto `t` à página. Isso organiza os elementos na interface do usuário.

6. **Execução da Aplicação**:
   ```python
   ft.app(main)
   ```
   Esta linha inicia a aplicação chamando a função `main`.

Em resumo, o código cria uma aplicação web simples que permite ao usuário escolher uma cor favorita e submeter sua escolha. A escolha é então exibida na página. O código demonstra o uso de eventos, atualização de widgets e a criação de interfaces com diferentes estilos de widgets no Flet.
A partir do código fornecido, podemos criar variações para demonstrar diferentes funcionalidades do Flet e como ele pode ser usado para criar interfaces de usuário amigáveis e interativas em Python. Vamos explorar um conjunto de exemplos que utilizam diferentes elementos de UI e interações.

### Exemplo 1: Usando Checkbox para múltiplas seleções
Este exemplo modifica a escolha única para múltiplas seleções usando checkboxes, permitindo ao usuário selecionar mais de uma cor favorita.
