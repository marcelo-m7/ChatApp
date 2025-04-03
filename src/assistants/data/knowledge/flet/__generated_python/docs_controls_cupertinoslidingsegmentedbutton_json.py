import flet as ft

def main(page):
    page.theme_mode = ft.ThemeMode.LIGHT
    
    def update_text(e):
        text.value = f"Você selecionou: {['Primeiro', 'Segundo', 'Terceiro'][e.data]}"
        text.update()

    text = ft.Text(value="Selecione uma opção")
    
    segmented_button = ft.CupertinoSlidingSegmentedButton(
        selected_index=1,
        thumb_color=ft.Colors.TEAL_400,
        on_change=update_text,
        controls=[
            ft.Text("Primeiro"),
            ft.Text("Segundo"),
            ft.Text("Terceiro"),
        ],
    )
    
    page.add(segmented_button, text)

ft.app(main)

import flet as ft

def main(page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.add(
        ft.CupertinoSlidingSegmentedButton(
            selected_index=0,
            thumb_color=ft.Colors.ORANGE_400,
            on_change=lambda e: print(f"selected_index: {e.data}"),
            padding=ft.padding.symmetric(vertical=10, horizontal=5),
            margin=ft.margin.all(20),
            controls=[
                ft.Text("Item 1"),
                ft.Text("Item 2"),
                ft.Text("Item 3"),
            ],
        ),
    )

ft.app(main)

import flet as ft

def main(page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.add(
        ft.CupertinoSlidingSegmentedButton(
            selected_index=1,
            thumb_color=ft.Colors.PURPLE_200,
            on_change=lambda e: print(f"selected_index: {e.data}"),
            controls=[
                ft.Icon(ft.Icons.HOME, color=ft.Colors.PURPLE_900),
                ft.Icon(ft.Icons.SETTINGS, color=ft.Colors.PURPLE_900),
                ft.Icon(ft.Icons.ACCOUNT_CIRCLE, color=ft.Colors.PURPLE_900),
            ],
        ),
    )

ft.app(main)

import flet as ft
   ```
   Isso importa a biblioteca Flet com o alias `ft`, permitindo que você acesse os componentes e funcionalidades dessa biblioteca usando `ft.`.

2. **Definição da função `main`**:
   ```python
   def main(page):
   ```
   A função `main` é definida recebendo um parâmetro `page`. Este parâmetro representa a página da aplicação, onde os componentes da UI serão adicionados.

3. **Configuração do Modo do Tema da Página**:
   ```python
   page.theme_mode = ft.ThemeMode.LIGHT
   ```
   Aqui, o modo de tema da página é definido como `LIGHT`, o que significa que a página usará cores claras.

4. **Adicionando um Componente na Página**:
   ```python
   page.add(...)
   ```
   Esta linha adiciona um componente específico à `page`. O componente adicionado é um `CupertinoSlidingSegmentedButton`.

5. **CupertinoSlidingSegmentedButton**:
   ```python
   ft.CupertinoSlidingSegmentedButton(
       selected_index=1,
       thumb_color=ft.Colors.BLUE_400,
       on_change=lambda e: print(f"selected_index: {e.data}"),
       padding=ft.padding.symmetric(0, 10),
       controls=[
           ft.Text("One"),
           ft.Text("Two"),
           ft.Text("Three"),
       ],
   )
   ```
   - **selected_index=1**: Define o índice do botão selecionado inicialmente como 1 (o segundo botão, considerando que a indexação começa em 0).
   - **thumb_color=ft.Colors.BLUE_400**: Define a cor do controle deslizante como azul.
   - **on_change**: Define um evento que é chamado quando o valor selecionado muda. Neste caso, imprimirá o índice selecionado no console.
   - **padding**: Aplica um preenchimento simétrico horizontal de 10 pixels aos lados esquerdo e direito do botão segmentado.
   - **controls**: Uma lista de controles que será exibida no botão segmentado. Cada controle é representado por um componente `Text`.

6. **Inicialização da Aplicação Flet**:
   ```python
   ft.app(main)
   ```
   Esta linha inicia a aplicação utilizando a função `main` como ponto de entrada. Quando a aplicação é executada, a função `main` é chamada com o objeto `page` correspondente, onde a interface do usuário é construída.

Em resumo, este script Python usa a biblioteca Flet para criar uma interface gráfica simples com um botão segmentado do estilo Cupertino. O botão permite ao usuário escolher entre três opções ("One", "Two", "Three"), e exibe no console o índice da opção selecionada sempre que o usuário muda sua seleção.
Aqui estão alguns exemplos adicionais que mostram diferentes maneiras de utilizar o `ft.CupertinoSlidingSegmentedButton` em um aplicativo Flet. Cada exemplo destaca um aspecto diferente, como a alteração de cores, o uso de ícones e a interação com outros elementos da interface do usuário.

### Exemplo 1: Alterando a cor do botão selecionado e do texto
