import flet as ft

def main(page: ft.Page):
    page.title = "Dialog with Image"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    dlg = ft.AlertDialog(
        modal=True,
        title=ft.Text("Important Notice"),
        content=ft.Column([
            ft.Image(src="https://via.placeholder.com/150", width=150),
            ft.Text("Please make sure to check this important information.")
        ]),
        actions=[
            ft.TextButton("OK", on_click=lambda e: page.close(dlg))
        ]
    )

    page.add(
        ft.ElevatedButton("Open Dialog with Image", on_click=lambda e: page.open(dlg))
    )

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.title = "Styled Confirmation Dialog"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def handle_response(e):
        page.add(ft.Text(f"Response: {e.control.text}"))
        page.close(dlg)

    dlg = ft.AlertDialog(
        modal=True,
        title=ft.Text("Confirm Action", style=ft.TextStyle(color=ft.colors.RED)),
        content=ft.Text("Are you sure you want to proceed?", style=ft.TextStyle(font_size=16)),
        actions=[
            ft.TextButton("Yes", on_click=handle_response, style=ft.ButtonStyle(bgcolor=ft.colors.GREEN)),
            ft.TextButton("No", on_click=handle_response, style=ft.ButtonStyle(bgcolor=ft.colors.RED))
        ],
        actions_alignment=ft.MainAxisAlignment.END
    )

    page.add(
        ft.ElevatedButton("Open Styled Dialog", on_click=lambda e: page.open(dlg))
    )

ft.app(main)

import flet as ft
   ```
   Este comando importa a biblioteca Flet, que é usada para construir interfaces de usuário em Python.

   ```python
   def main(page: ft.Page):
   ```
   A função `main` é definida com um parâmetro `page`, que representa a página da aplicação onde os componentes UI são adicionados.

   ```python
   page.title = "AlertDialog examples"
   page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
   ```
   Aqui, o título da página é definido como "AlertDialog examples", e o alinhamento horizontal dos elementos na página é centralizado.

2. **Criação do Diálogo Não Modal**:
   ```python
   dlg = ft.AlertDialog(
       title=ft.Text("Hi, this is a non-modal dialog!"),
       on_dismiss=lambda e: page.add(ft.Text("Non-modal dialog dismissed")),
   )
   ```
   `dlg` é um diálogo não modal. O título do diálogo é definido e uma função lambda é usada para adicionar um texto à página quando o diálogo for dispensado (fechado).

3. **Função para Manipular o Fechamento de Diálogos**:
   ```python
   def handle_close(e):
       page.close(dlg_modal)
       page.add(ft.Text(f"Modal dialog closed with action: {e.control.text}"))
   ```
   Esta função é chamada quando qualquer botão de ação do diálogo modal é clicado. Ela fecha o diálogo modal e adiciona um texto à página indicando qual ação foi escolhida (sim ou não).

4. **Criação do Diálogo Modal**:
   ```python
   dlg_modal = ft.AlertDialog(
       modal=True,
       title=ft.Text("Please confirm"),
       content=ft.Text("Do you really want to delete all those files?"),
       actions=[
           ft.TextButton("Yes", on_click=handle_close),
           ft.TextButton("No", on_click=handle_close),
       ],
       actions_alignment=ft.MainAxisAlignment.END,
       on_dismiss=lambda e: page.add(ft.Text("Modal dialog dismissed")),
   )
   ```
   `dlg_modal` é um diálogo modal. Isso significa que ele bloqueia a interação com outros elementos da interface até ser fechado. O diálogo tem um título, um conteúdo, dois botões de ação ("Yes" e "No"), e uma função lambda que adiciona um texto à página quando ele for dispensado.

5. **Adicionando Botões para Abrir os Diálogos**:
   ```python
   page.add(
       ft.ElevatedButton("Open dialog", on_click=lambda e: page.open(dlg)),
       ft.ElevatedButton("Open modal dialog", on_click=lambda e: page.open(dlg_modal)),
   )
   ```
   Dois botões são adicionados à página. O primeiro abre o diálogo não modal e o segundo abre o diálogo modal. Cada botão tem um manipulador de evento `on_click` que chama o método `open` do objeto `page` para abrir os respectivos diálogos.

6. **Inicialização do Aplicativo**:
   ```python
   ft.app(main)
   ```
   Esta linha inicia o aplicativo passando a função `main` como entrada, que configura e exibe a página.

Em resumo, este código demonstra como criar e manipular diálogos modais e não modais em uma aplicação Flet, permitindo interações básicas e tratamento de eventos.
O código Python usando a biblioteca Flet que você forneceu cria uma interface de usuário com dois tipos de diálogos: um não modal e um modal. Vamos criar mais alguns exemplos para explorar diferentes funcionalidades e usos dos diálogos em Flet.

### Exemplo 1: Diálogo com Campos de Entrada

Este exemplo demonstra como criar um diálogo que contém campos de entrada para coletar dados do usuário.
