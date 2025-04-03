import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter with custom increment/decrement"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)
    txt_increment = ft.TextField(value="1", label="Increment/Decrement value", width=100)

    def minus_click(e):
        increment = int(txt_increment.value)
        txt_number.value = str(int(txt_number.value) - increment)
        page.update()

    def plus_click(e):
        increment = int(txt_increment.value)
        txt_number.value = str(int(txt_number.value) + increment)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.Icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.Icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        txt_increment
    )

ft.app(main)

import flet as ft
   ```
   Isso importa a biblioteca Flet com um alias `ft`, que é usado para acessar os componentes e funcionalidades do Flet.

2. **Definição da função main**:
   ```python
   def main(page: ft.Page):
   ```
   Esta função `main` é a função principal que será executada pelo aplicativo Flet. Ela recebe um argumento `page`, que representa a página da aplicação.

3. **Configuração da página**:
   ```python
   page.title = "Flet counter example"
   page.vertical_alignment = ft.MainAxisAlignment.CENTER
   ```
   - `page.title` define o título da janela do navegador ou do aplicativo.
   - `page.vertical_alignment` é usado para alinhar verticalmente o conteúdo da página ao centro.

4. **Criação do campo de texto**:
   ```python
   txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)
   ```
   - `ft.TextField` cria um campo de entrada de texto.
   - `value="0"` define o valor inicial do campo de texto como "0".
   - `text_align=ft.TextAlign.RIGHT` alinha o texto à direita dentro do campo de texto.
   - `width=100` define a largura do campo de texto.

5. **Definição das funções de clique**:
   - **Função minus_click**:
     ```python
     def minus_click(e):
         txt_number.value = str(int(txt_number.value) - 1)
         page.update()
     ```
     Esta função é chamada quando o botão de decremento é clicado. Ela converte o valor atual do `txt_number` para um inteiro, subtrai 1 e atualiza o campo de texto com o novo valor. `page.update()` é chamado para atualizar a interface do usuário.
   
   - **Função plus_click**:
     ```python
     def plus_click(e):
         txt_number.value = str(int(txt_number.value) + 1)
         page.update()
     ```
     Similar à função `minus_click`, mas adiciona 1 ao valor atual.

6. **Adicionando os componentes à página**:
   ```python
   page.add(
       ft.Row(
           [
               ft.IconButton(ft.Icons.REMOVE, on_click=minus_click),
               txt_number,
               ft.IconButton(ft.Icons.ADD, on_click=plus_click),
           ],
           alignment=ft.MainAxisAlignment.CENTER,
       )
   )
   ```
   - `ft.Row` cria um layout de linha horizontal.
   - `ft.IconButton` cria um botão com um ícone. Existem dois botões: um com o ícone de "remover" (`ft.Icons.REMOVE`) associado à função `minus_click`, e outro com o ícone de "adicionar" (`ft.Icons.ADD`) associado à função `plus_click`.
   - `alignment=ft.MainAxisAlignment.CENTER` alinha os botões e o campo de texto no centro da linha.

7. **Iniciando o aplicativo**:
   ```python
   ft.app(main)
   ```
   Chama a função `main` dentro do contexto de um aplicativo Flet.

Este código cria uma aplicação básica com um contador que pode ser incrementado ou decrementado usando botões. É um exemplo prático de como usar componentes de entrada, manipulação de eventos e atualização de interface do usuário com a biblioteca Flet.
Para expandir o exemplo de contador usando Flet, podemos criar diferentes variações que incluem novas funcionalidades e ajustes de interface. Vou mostrar algumas ideias que podem ser úteis para entender como personalizar o comportamento e a aparência do aplicativo.

### Exemplo 1: Adicionando Reset e Limitação de Valores
Este exemplo adiciona um botão de reset e limita o contador para não exceder certos valores máximos e mínimos.

import flet as ft
import time

def main(page: ft.Page):
    page.title = "Flet counter with animation"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100, color=ft.colors.BLUE)

    def update_color():
        txt_number.color = ft.colors.RED
        page.update()
        time.sleep(0.1)  # Apenas para simulação, não usar sleep em produção real
        txt_number.color = ft.colors.BLUE
        page.update()

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        update_color()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        update_color()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.Icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.Icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(main)
