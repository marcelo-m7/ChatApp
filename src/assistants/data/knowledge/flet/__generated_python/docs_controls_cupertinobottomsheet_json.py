import flet as ft

def main(page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def handle_click(e):
        response = f"Action clicked: {e.control.content.value}"
        page.add(ft.Text(response))
        page.update()  # Atualiza a página para mostrar a resposta selecionada
        page.close(bottom_sheet)

    action_sheet = ft.CupertinoActionSheet(
        title=ft.Text("Choose an Option"),
        actions=[
            ft.CupertinoActionSheetAction(
                content=ft.Text("Option A"),
                on_click=handle_click,
            ),
            ft.CupertinoActionSheetAction(
                content=ft.Text("Option B"),
                on_click=handle_click,
            ),
            ft.CupertinoActionSheetAction(
                content=ft.Text("Option C"),
                on_click=handle_click,
            ),
        ],
        cancel=ft.CupertinoActionSheetAction(
            content=ft.Text("Cancel"),
            on_click=handle_click,
        ),
    )
    bottom_sheet = ft.CupertinoBottomSheet(action_sheet)
    page.add(
        ft.CupertinoFilledButton(
            "Choose Option",
            on_click=lambda e: page.open(bottom_sheet),
        )
    )

ft.app(main)

import flet as ft
   ```
   Isso importa a biblioteca Flet e a abrevia como `ft` para facilitar o acesso aos seus componentes e funções.

2. **Função Principal `main`**:
   ```python
   def main(page):
   ```
   A função `main` é definida com um parâmetro `page`, que representa a página do aplicativo onde os UI components serão colocados.

3. **Configuração de Alinhamento Horizontal**:
   ```python
   page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
   ```
   Define o alinhamento horizontal dos elementos dentro da página para o centro.

4. **Função de Manipulação de Clique `handle_click`**:
   ```python
   def handle_click(e):
       page.add(ft.Text(f"Action clicked: {e.control.content.value}"))
       page.close(bottom_sheet)
   ```
   - `handle_click` é uma função que é chamada quando um botão no CupertinoActionSheet é clicado.
   - Ela adiciona um texto à página que indica qual ação foi clicada, acessando o valor do conteúdo do controle que disparou o evento.
   - Fecha o `bottom_sheet` após a ação.

5. **Definição do `CupertinoActionSheet`**:
   ```python
   action_sheet = ft.CupertinoActionSheet(
       title=ft.Row([...]),
       message=ft.Row([...]),
       cancel=...,
       actions=[...],
   )
   ```
   - **`title` e `message`**: Definidos como `Row` com um `Text` dentro, ambos centrados. São usados para mostrar um cabeçalho e uma descrição no sheet.
   - **`cancel`**: Um botão de cancelar que também usa a função `handle_click`.
   - **`actions`**: Uma lista de ações, cada uma com seu próprio botão e configurações, como ação padrão (`is_default_action`) e ação destrutiva (`is_destructive_action`), que também usam a função `handle_click`.

6. **CupertinoBottomSheet**:
   ```python
   bottom_sheet = ft.CupertinoBottomSheet(action_sheet)
   ```
   Inicializa um `CupertinoBottomSheet` que contém o `action_sheet` criado anteriormente.

7. **Botão para Abrir o `bottom_sheet`**:
   ```python
   page.add(
       ft.CupertinoFilledButton(
           "Open CupertinoBottomSheet",
           on_click=lambda e: page.open(bottom_sheet),
       )
   )
   ```
   - Adiciona um botão à página que, quando clicado, abre o `bottom_sheet`.
   - O evento de clique é tratado por uma função lambda que chama `page.open` com o `bottom_sheet`.

8. **Inicialização do Aplicativo**:
   ```python
   ft.app(main)
   ```
   Inicia o aplicativo Flet passando a função `main` como ponto de entrada.

### Conclusão

Este código demonstra como usar componentes específicos do iOS (estilo Cupertino) em um aplicativo Flet para criar uma interface de usuário interativa que responde a cliques, exibindo diferentes tipos de ações em um bottom sheet e manipulando eventos de clique de forma eficiente.
O código original que você forneceu é um exemplo de como utilizar a interface `CupertinoActionSheet` em conjunto com um `CupertinoBottomSheet` no framework Flet para criar uma interface de usuário interativa. O exemplo mostra a utilização de botões que, ao serem clicados, disparam ações que são refletidas em uma folha de ação estilo iOS.

A seguir, vou fornecer alguns exemplos adicionais que destacam diferentes formas de uso para expandir a funcionalidade ou adaptar o código a diferentes cenários.

### Exemplo 1: Adicionando Ícones às Ações

Neste exemplo, adicionaremos ícones às ações para tornar a interface mais visualmente atraente.
