import flet as ft

def main(page: ft.Page):
    page.horizontal_alignment = page.vertical_alignment = "center"

    def tab_change(e):
        page.controls.clear()
        if e.control.active_tab == 0:
            page.add(ft.Text("Home tab selected!"))
        elif e.control.active_tab == 1:
            page.add(ft.Text("Profile tab selected!"))
        elif e.control.active_tab == 2:
            page.add(ft.Text("Settings tab selected!"))
        page.update()

    tabs = ft.Tabs(
        tabs=[
            ft.Tab(text="Home"),
            ft.Tab(text="Profile"),
            ft.Tab(text="Settings"),
        ],
        on_change=tab_change
    )
    page.add(tabs)

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.horizontal_alignment = page.vertical_alignment = "center"

    input_field = ft.TextField(hint_text="Enter something...", width=200)
    submit_button = ft.ElevatedButton(text="Submit", on_click=lambda e: page.add(ft.Text(input_field.value)))
    
    page.add(input_field)
    page.add(submit_button)

ft.app(main)

import flet as ft
   ```
   Esta linha importa a biblioteca Flet, que é renomeada como `ft` para simplificar as chamadas subsequentes de funções e classes da biblioteca.

2. **Definição da função principal**:
   ```python
   def main(page: ft.Page):
   ```
   A função `main` é definida com um parâmetro `page`, que é uma instância de `ft.Page`. Esta função será usada para configurar a página do aplicativo.

3. **Configurações de alinhamento da página**:
   ```python
   page.horizontal_alignment = page.vertical_alignment = "center"
   ```
   Define o alinhamento horizontal e vertical do conteúdo da página como centralizado.

4. **Botão de ação flutuante (Floating Action Button - FAB)**:
   ```python
   page.floating_action_button = ft.FloatingActionButton(icon=ft.Icons.ADD)
   page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED
   ```
   Um FAB com ícone de adição (`ft.Icons.ADD`) é criado e posicionado no centro da parte inferior da página (`CENTER_DOCKED`).

5. **Barra de aplicativos superior (AppBar)**:
   ```python
   page.appbar = ft.AppBar(
       title=ft.Text("Bottom AppBar Demo"),
       center_title=True,
       bgcolor=ft.Colors.GREEN_300,
       automatically_imply_leading=False,
   )
   ```
   Configura a barra de aplicativos superior com um título centralizado, cor de fundo verde clara (`ft.Colors.GREEN_300`) e sem um botão de navegação automático (ícone de menu à esquerda).

6. **Barra de aplicativos inferior (BottomAppBar)**:
   ```python
   page.bottom_appbar = ft.BottomAppBar(
       bgcolor=ft.Colors.BLUE,
       shape=ft.NotchShape.CIRCULAR,
       content=ft.Row(
           controls=[
               ft.IconButton(icon=ft.Icons.MENU, icon_color=ft.Colors.WHITE),
               ft.Container(expand=True),
               ft.IconButton(icon=ft.Icons.SEARCH, icon_color=ft.Colors.WHITE),
               ft.IconButton(icon=ft.Icons.FAVORITE, icon_color=ft.Colors.WHITE),
           ]
       ),
   )
   ```
   Define uma barra de aplicativos na parte inferior com fundo azul e um recorte circular para o FAB. Inclui botões de ícone para menu, pesquisa e favoritos, com ícones coloridos em branco.

7. **Adicionando texto ao corpo da página**:
   ```python
   page.add(ft.Text("Body!"))
   ```
   Adiciona um texto simples "Body!" ao corpo da página.

8. **Iniciando o aplicativo**:
   ```python
   ft.app(main)
   ```
   Esta linha inicia o aplicativo chamando a função `main`.

Em resumo, este código cria uma interface de usuário com barras de aplicativos superior e inferior personalizadas, um botão de ação flutuante e texto no corpo, usando a biblioteca Flet para gerenciamento de layout e elementos de UI.
O código fornecido configura uma aplicação Flet com uma barra de aplicativos na parte inferior, um botão de ação flutuante e uma AppBar no topo da página. Vou criar alguns exemplos adicionais para demonstrar diferentes formas de uso da biblioteca Flet, alterando componentes, estilos e comportamentos.

### Exemplo 1: AppBar com Menu Dropdown e Troca de Tema

Neste exemplo, adicionaremos um menu dropdown na AppBar para selecionar entre temas claros e escuros.
