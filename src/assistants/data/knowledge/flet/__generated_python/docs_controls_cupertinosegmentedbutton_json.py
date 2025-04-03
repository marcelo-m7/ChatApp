import flet as ft

def main(page):
    page.add(
        ft.CupertinoSegmentedButton(
            selected_index=0,
            selected_color=ft.Colors.BLUE_400,
            on_change=lambda e: print(f"selected_index: {e.data}"),
            controls=[
                ft.Text("Active"),
                ft.Text("Disabled"),
                ft.Text("Active"),
            ],
            disabled_indices=[1],  # Desabilitar o segundo botão
        ),
    )

ft.app(main)

import flet as ft

def main(page):
    page.add(
        ft.CupertinoSegmentedButton(
            selected_index=1,
            selected_color=ft.Colors.ORANGE_400,
            on_change=lambda e: print(f"selected_index: {e.data}"),
            controls=[
                ft.Container(
                    padding=ft.padding.symmetric(0, 5),
                    content=ft.Text("Short"),
                ),
                ft.Container(
                    padding=ft.padding.symmetric(0, 20),
                    content=ft.Text("Medium Length"),
                ),
                ft.Container(
                    padding=ft.padding.symmetric(0, 35),
                    content=ft.Text("A Very Long Segment Text"),
                ),
            ],
        ),
    )

ft.app(main)

import flet as ft

def main(page):
    page.add(
        ft.CupertinoSegmentedButton(
            selected_index=2,
            selected_color=ft.Colors.BLUE_400,
            on_change=lambda e: print(f"selected_index: {e.data}"),
            controls=[
                ft.Icon(ft.Icons.FAVORITE, color=ft.Colors.PINK_300),
                ft.Icon(ft.Icons.HOME, color=ft.Colors.BLUE_300),
                ft.Icon(ft.Icons.SEARCH, color=ft.Colors.GREEN_300),
            ],
        ),
    )

ft.app(main)

import flet as ft
   ```
   Esta linha importa a biblioteca Flet, que é usada para criar interfaces de usuário baseadas na web usando Python.

2. **Definindo a função principal**:
   ```python
   def main(page):
   ```
   A função `main` é definida com um parâmetro `page`, que representa a página da aplicação web onde os elementos da UI serão adicionados.

3. **Configurando o modo de tema da página**:
   ```python
   page.theme_mode = ft.ThemeMode.LIGHT
   ```
   Esta linha configura o modo de tema da página para "LIGHT". Flet suporta temas claros e escuros, e aqui está sendo especificado explicitamente o uso do tema claro.

4. **Adicionando um botão segmentado ao estilo Cupertino**:
   ```python
   page.add(
       ft.CupertinoSegmentedButton(
   ```
   Aqui, um `CupertinoSegmentedButton` é adicionado à página. Este widget é uma representação de um botão segmentado que segue o design típico do iOS (Cupertino).

5. **Propriedades do `CupertinoSegmentedButton`**:
   - **`selected_index=1`**: Define o índice do segmento inicialmente selecionado como 1 (0 é o primeiro índice, então 1 representa o segundo segmento).
   - **`selected_color=ft.Colors.RED_400`**: Define a cor do segmento selecionado como vermelho (especificamente o tom `RED_400` da paleta de cores pré-definidas de Flet).
   - **`on_change`**: É um evento que é chamado quando o índice selecionado muda. A função lambda associada imprime o novo índice selecionado.
     ```python
     on_change=lambda e: print(f"selected_index: {e.data}"),
     ```
     Onde `e.data` contém o índice do segmento selecionado.

6. **Controles dentro do botão segmentado**:
   Cada controle dentro do `CupertinoSegmentedButton` é um segmento que pode ser selecionado. Aqui, três controles são definidos:
   - **Primeiro Segmento**: Simplesmente um texto "One".
     ```python
     ft.Text("One"),
     ```
   - **Segundo Segmento**: Um texto "Two" dentro de um `Container` com padding horizontal de 30 pixels.
     ```python
     ft.Container(
         padding=ft.padding.symmetric(0, 30),
         content=ft.Text("Two"),
     ),
     ```
   - **Terceiro Segmento**: Um texto "Three" dentro de um `Container` com padding horizontal de 10 pixels.
     ```python
     ft.Container(
         padding=ft.padding.symmetric(0, 10),
         content=ft.Text("Three"),
     ),
     ```

7. **Iniciando a aplicação**:
   ```python
   ft.app(main)
   ```
   Esta linha inicia a aplicação, usando a função `main` como ponto de entrada para a construção da interface do usuário.

Este código cria uma interface de usuário web simples com um botão segmentado, permitindo ao usuário escolher entre três opções, com feedback visual e funcional sobre a opção selecionada.
Claro, abaixo estão alguns exemplos adicionais que mostram diferentes formas de uso do widget `CupertinoSegmentedButton` no framework Flet, ajustando diferentes propriedades e comportamentos para ilustrar a flexibilidade deste componente.

### Exemplo 1: Alterando Cores e Modo Tema
Neste exemplo, vou mudar as cores do botão selecionado e do texto, e também definir o modo de tema para escuro.
