import flet as ft

   def main(page: ft.Page):
       page.title = "Basic elevated buttons"
       page.add(
           ft.ElevatedButton(text="Elevated button"),
           ft.Button("Disabled button", disabled=True),
       )

   ft.app(main)
   ```
   - **Descrição**: Este código cria uma página com dois botões - um botão elevado ativo e um botão padrão desativado.
   - **Funcionalidades**:
     - `ft.ElevatedButton(text="Elevated button")`: Cria um botão elevado com o texto "Elevated button".
     - `ft.Button("Disabled button", disabled=True)`: Cria um botão padrão com o texto "Disabled button" que está desativado (não pode ser clicado).

2. **Botões Elevados com Ícones**:
   ```python
   import flet as ft

   def main(page: ft.Page):
       page.title = "Elevated buttons with icons"
       page.add(
           ft.ElevatedButton("Button with icon", icon="chair_outlined"),
           ft.ElevatedButton(
               "Button with colorful icon",
               icon="park_rounded",
               icon_color="green400",
           ),
       )

   ft.app(main)
   ```
   - **Descrição**: Cria uma página com dois botões elevados, ambos com ícones. O segundo botão tem um ícone colorido.
   - **Funcionalidades**:
     - `icon="chair_outlined"`: Adiciona um ícone de cadeira ao primeiro botão.
     - `icon="park_rounded", icon_color="green400"`: Adiciona um ícone de parque ao segundo botão e define a cor do ícone para verde.

3. **Botão Elevado com Evento de Clique**:
   ```python
   import flet as ft

   def main(page: ft.Page):
       page.title = "Elevated button with 'click' event"
       def button_clicked(e):
           b.data += 1
           t.value = f"Button clicked {b.data} time(s)"
           page.update()
       b = ft.ElevatedButton("Button with 'click' event", on_click=button_clicked, data=0)
       t = ft.Text()
       page.add(b, t)

   ft.app(main)
   ```
   - **Descrição**: Este código cria um botão que, ao ser clicado, atualiza um texto que conta quantas vezes o botão foi pressionado.
   - **Funcionalidades**:
     - `on_click=button_clicked`: Define uma função a ser chamada quando o botão é clicado.
     - `b.data`: Armazena um valor que é incrementado cada vez que o botão é clicado.
     - `t.value`: Atualiza o texto exibido na página com o número de cliques.

4. **Botões Elevados com Conteúdo Personalizado**:
   ```python
   import flet as ft

   def main(page: ft.Page):
       page.title = "Elevated buttons with custom content"
       page.add(
           ft.ElevatedButton(
               width=150,
               content=ft.Row(
                   [
                       ft.Icon(name=ft.Icons.FAVORITE, color="pink"),
                       ft.Icon(name=ft.Icons.AUDIOTRACK, color="green"),
                       ft.Icon(name=ft.Icons.BEACH_ACCESS, color="blue"),
                   ],
                   alignment=ft.MainAxisAlignment.SPACE_AROUND,
               ),
           ),
           ft.ElevatedButton(
               content=ft.Container(
                   content=ft.Column(
                       [
                           ft.Text(value="Compound button", size=20),
                           ft.Text(value="This is secondary text"),
                       ],
                       alignment=ft.MainAxisAlignment.CENTER,
                       spacing=5,
                   ),
                   padding=ft.padding.all(10),
               ),
           ),
       )

   ft.app(main)
   ```
   - **Descrição**: Cria uma página com dois botões elevados contendo conteúdos personalizados, como ícones e textos formatados.
   - **Funcionalidades**:
     - `ft.Row` e `ft.Column`: Utilizados para organizar os ícones e textos dentro dos botões.
     - `ft.Container`: Usado para adicionar padding ao conteúdo de um dos botões.

5. **Mudança de Cor no Evento Hover**:
   ```python
   import flet as ft

   def main(page: ft.Page):
       def on_hover(e):
           e.control.bgcolor = "orange" if e.data == "true" else "yellow"
           e.control.update()
       page.add(
           ft.ElevatedButton(
               "I'm changing color on hover", bgcolor="yellow", on_hover=on_hover
           )
       )

   ft.app(main)
   ```
   - **Descrição**: Este código adiciona um botão que muda sua cor de fundo quando o cursor está sobre ele.
   - **Funcionalidades**:
     - `on_hover=on_hover`: Define uma função que altera a cor de fundo do botão quando o mouse está sobre ele, alternando entre amarelo e laranja.
Aqui estão exemplos adicionais de diferentes usos de botões elevados (ElevatedButton) usando a biblioteca Flet em Python. Cada exemplo apresenta uma variação no design ou interação para ilustrar a flexibilidade dos componentes de UI que podem ser criados com Flet.

### Exemplo 1: Botão com Tamanho e Cor Personalizados

import flet as ft

def main(page: ft.Page):
    page.title = "Elevated Button with Custom Border and Shadow"
    button_with_border = ft.ElevatedButton(
        text="Stylish Button",
        border_radius=30,
        elevation=10,
        border=ft.border.all(3, "black")
    )
    page.add(button_with_border)

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.title = "Elevated Button with Multiple Events"

    def on_click(e):
        e.control.text = "Clicked!"
        e.control.update()
    
    def on_hover(e):
        e.control.bgcolor = "red" if e.data == "true" else "blue"
        e.control.update()

    multi_event_button = ft.ElevatedButton(
        "Click or Hover", bgcolor="blue", on_click=on_click, on_hover=on_hover
    )
    
    page.add(multi_event_button)

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.title = "Elevated Button with Tooltip"
    button_with_tooltip = ft.ElevatedButton(
        text="Hover Over Me",
        tooltip="This is a tooltip for the button!"
    )
    page.add(button_with_tooltip)

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.title = "Elevated Buttons with Reset Action"
    
    def reset_counter(e):
        counter.data = 0
        text_counter.value = f"Count: {counter.data}"
        page.update()

    def increment_counter(e):
        counter.data += 1
        text_counter.value = f"Count: {counter.data}"
        page.update()

    counter = ft.ElevatedButton("Increment", on_click=increment_counter, data=0)
    reset = ft.ElevatedButton("Reset", on_click=reset_counter)
    text_counter = ft.Text(value="Count: 0")
    
    page.add(counter, text_counter, reset)

ft.app(main)
