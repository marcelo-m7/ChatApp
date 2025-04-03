import flet as ft

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def dialog_dismissed(e):
        page.add(ft.Text("Dialog dismissed"))

    def handle_action_click(e):
        page.add(ft.Text(f"Action clicked: {e.control.text}"))
        page.close(cupertino_alert_dialog)

    cupertino_alert_dialog = ft.CupertinoAlertDialog(
        title=ft.Text("Cupertino Alert Dialog"),
        content=ft.Text("Do you want to delete this file?"),
        on_dismiss=dialog_dismissed,
        actions=[
            ft.CupertinoDialogAction(
                text="Yes",
                is_destructive_action=True,
                on_click=handle_action_click,
            ),
            ft.CupertinoDialogAction(
                text="No",
                is_default_action=True,
                on_click=handle_action_click
            ),
        ],
    )

    page.add(
        ft.CupertinoFilledButton(
            text="Open Dialog",
            icon=ft.Icon(ft.icons.WARNING_AMBER_OUTLINED),
            on_click=lambda e: page.open(cupertino_alert_dialog),
        )
    )

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def dialog_dismissed(e):
        page.add(ft.Text("Dialog dismissed"))

    def handle_action_click(e):
        page.add(ft.Text(f"Action clicked: {e.control.text}"))
        page.close(cupertino_alert_dialog)

    cupertino_alert_dialog = ft.CupertinoAlertDialog(
        title=ft.Text("Importante", style=ft.TextStyle(color=ft.colors.RED, weight="bold")),
        content=ft.Text("Você realmente deseja excluir este arquivo?", style=ft.TextStyle(italic=True)),
        on_dismiss=dialog_dismissed,
        actions=[
            ft.CupertinoDialogAction(
                text="Sim",
                is_destructive_action=True,
                on_click=handle_action_click,
            ),
            ft.CupertinoDialogAction(
                text="Não",
                is_default_action=True,
                on_click=handle_action_click
            ),
        ],
    )

    page.add(
        ft.CupertinoFilledButton(
            text="Abrir Diálogo",
            on_click=lambda e: page.open(cupertino_alert_dialog),
        )
    )

ft.app(main)

import flet as ft
   ```
   Esta linha importa a biblioteca Flet, que é usada para construir interfaces de usuário.

2. **Função Principal `main`**:
   ```python
   def main(page: ft.Page):
   ```
   Define a função principal chamada `main`, que recebe um objeto `page` do tipo `ft.Page`. Este objeto é usado para controlar e modificar a página da aplicação.

3. **Configuração da Alinhamento Horizontal**:
   ```python
   page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
   ```
   Esta linha define o alinhamento horizontal dos elementos na página para o centro. `CrossAxisAlignment.CENTER` é uma enumeração que especifica que os widgets devem ser centralizados horizontalmente na página.

4. **Função `dialog_dismissed`**:
   ```python
   def dialog_dismissed(e):
       page.add(ft.Text("Dialog dismissed"))
   ```
   Esta função é chamada quando o diálogo é fechado (dismissed). Ela adiciona um texto `Dialog dismissed` à página.

5. **Função `handle_action_click`**:
   ```python
   def handle_action_click(e):
       page.add(ft.Text(f"Action clicked: {e.control.text}"))
       page.close(cupertino_alert_dialog)
   ```
   Esta função é chamada quando qualquer ação (botão) dentro do diálogo é clicada. Ela adiciona um texto informando qual ação foi clicada, usando o texto do botão clicado (`e.control.text`). Em seguida, fecha o diálogo.

6. **Criação do Diálogo CupertinoAlertDialog**:
   ```python
   cupertino_alert_dialog = ft.CupertinoAlertDialog(
       ...
   )
   ```
   Cria uma instância de `CupertinoAlertDialog`, um diálogo ao estilo iOS, com um título, uma mensagem e ações definidas. O diálogo chama `dialog_dismissed` quando é fechado e possui botões para "Yes" e "No".

   Dentro deste diálogo, são definidas duas ações (`CupertinoDialogAction`) para os botões "Yes" e "No". O botão "Yes" é marcado como destrutivo (`is_destructive_action=True`), enquanto o botão "No" é marcado como ação padrão (`is_default_action=True`). Ambos os botões usam `handle_action_click` para lidar com cliques.

7. **Adicionando Botão na Página**:
   ```python
   page.add(
       ft.CupertinoFilledButton(
           text="Open CupertinoAlertDialog",
           on_click=lambda e: page.open(cupertino_alert_dialog),
       )
   )
   ```
   Adiciona um botão `CupertinoFilledButton` à página que, quando clicado, abre o `CupertinoAlertDialog`. O texto do botão é "Open CupertinoAlertDialog".

8. **Execução da Aplicação**:
   ```python
   ft.app(main)
   ```
   Esta linha inicia a aplicação, configurando `main` como a função de entrada.

Este código demonstra como criar e manipular diálogos no estilo iOS usando a biblioteca Flet em Python, permitindo a criação de interfaces de usuário interativas.
O código fornecido apresenta uma implementação básica de um diálogo de alerta estilo Cupertino (estética iOS) usando a biblioteca Flet em Python. Vamos explorar diferentes exemplos adicionais para expandir o uso e compreensão de como manipular diálogos e interações na biblioteca Flet.

### Exemplo 1: Adicionando uma Ação Adicional
Vamos adicionar uma terceira opção ao diálogo, tal como "Cancel", que simplesmente fecha o diálogo sem adicionar nenhuma ação adicional.
