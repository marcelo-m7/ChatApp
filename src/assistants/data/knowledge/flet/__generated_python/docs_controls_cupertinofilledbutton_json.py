import flet as ft

def main(page: ft.Page):
    button_content = ft.Row([
        ft.Icon(name="face", size=24),
        ft.Text("Perfil")
    ], alignment="center")
    profile_button = ft.CupertinoFilledButton(
        content=button_content,
        on_click=lambda e: print("Perfil clicado!")
    )
    page.add(profile_button)

ft.app(main)

import flet as ft

def on_button_click(e, button_name):
    print(f"{button_name} button clicked!")

def main(page: ft.Page):
    buttons = ft.Row([
        ft.CupertinoFilledButton(
            content=ft.Text("Botão 1"),
            on_click=lambda e: on_button_click(e, "Botão 1")
        ),
        ft.CupertinoFilledButton(
            content=ft.Text("Botão 2"),
            color=ft.colors.RED,
            on_click=lambda e: on_button_click(e, "Botão 2")
        ),
        ft.CupertinoFilledButton(
            content=ft.Text("Botão 3"),
            color=ft.colors.PURPLE,
            on_click=lambda e: on_button_click(e, "Botão 3")
        ),
    ])
    page.add(buttons)

ft.app(main)

import flet as ft

def on_play_clicked(e):
    print("Play button clicked!")

def main(page: ft.Page):
    play_icon = ft.Icon(name="play_arrow", size=32)
    play_button = ft.CupertinoFilledButton(
        content=play_icon,
        color=ft.colors.GREEN,
        on_click=on_play_clicked
    )
    page.add(play_button)

ft.app(main)

import flet as ft
   ```
   Aqui, a biblioteca `flet` é importada com o alias `ft` para facilitar o acesso às suas classes e métodos.

2. **Definição da função `main`:**
   ```python
   def main(page: ft.Page):
   ```
   Esta função é definida para manipular a lógica principal do aplicativo. Ela recebe um parâmetro `page`, que é uma instância de `ft.Page`. Este objeto `page` representa a página web onde os elementos UI (interface de usuário) serão renderizados.

3. **Adicionando um botão ao `page`:**
   ```python
   page.add(
       ft.CupertinoFilledButton(
           content=ft.Text("CupertinoFilled"),
           opacity_on_click=0.3,
           on_click=lambda e: print("CupertinoFilledButton clicked!"),
       ),
   )
   ```
   Dentro da função `main`, um botão do tipo `CupertinoFilledButton` é adicionado à página. Este botão possui as seguintes propriedades e comportamentos:
   - `content`: Define o conteúdo do botão, que neste caso é um texto "CupertinoFilled". O texto é criado usando `ft.Text("CupertinoFilled")`.
   - `opacity_on_click`: Define a opacidade do botão quando clicado. O valor `0.3` implica que o botão se tornará 30% opaco quando clicado.
   - `on_click`: É um evento que é chamado quando o botão é clicado. Aqui, ele é definido usando uma expressão lambda que simplesmente imprime uma mensagem no console. `lambda e: print("CupertinoFilledButton clicked!")` é uma função anônima que recebe um evento `e` e executa o `print`.

4. **Iniciando o aplicativo Flet:**
   ```python
   ft.app(main)
   ```
   Esta linha inicia o aplicativo usando a função `main` como ponto de entrada. Quando o aplicativo é iniciado, a função `main` é chamada com um objeto `page` criado pela biblioteca Flet, e o UI especificado na função `main` é renderizado na página web.

Essencialmente, este código cria um aplicativo web simples com um único botão que altera sua opacidade ao ser clicado e imprime uma mensagem no console. É um exemplo básico de como usar componentes e eventos em um aplicativo Flet.
Claro! O código que você forneceu é um exemplo de aplicação simples usando a biblioteca Flet para criar uma interface de usuário com um botão do estilo Cupertino. Vou criar alguns exemplos adicionais destacando diferentes formas de uso, alterando propriedades do botão, adicionando mais componentes e interações.

### Exemplo 1: Alterando a Cor e o Texto do Botão

Este exemplo mostra como mudar a cor e o texto do botão.
