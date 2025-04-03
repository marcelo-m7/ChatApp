import flet as ft

def main(page: ft.Page):
    page.title = "CupertinoNavigationBar - Extended Example"
    page.navigation_bar = ft.CupertinoNavigationBar(
        bgcolor=ft.Colors.PINK_100,
        inactive_color=ft.Colors.PINK_300,
        active_color=ft.Colors.PINK_900,
        on_change=lambda e: print("Tab changed to:", e.control.selected_index),
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),
            ft.NavigationBarDestination(icon=ft.Icons.SEARCH, label="Search"),
            ft.NavigationBarDestination(icon=ft.Icons.NOTIFICATIONS, label="Alerts"),
            ft.NavigationBarDestination(icon=ft.Icons.SETTINGS, label="Settings"),
            ft.NavigationBarDestination(icon=ft.Icons.HELP_OUTLINE, label="Help"),
        ]
    )
    page.add(ft.SafeArea(ft.Text("More options available!")))

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.title = "CupertinoNavigationBar - Minimalist Example"
    page.navigation_bar = ft.CupertinoNavigationBar(
        inactive_color=ft.Colors.GREY,
        active_color=ft.Colors.BLACK,
        on_change=lambda e: print("You are now on tab:", e.control.selected_index),
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.MENU, label="Menu"),
            ft.NavigationBarDestination(icon=ft.Icons.INFO, label="Info"),
            ft.NavigationBarDestination(icon=ft.Icons.PUBLIC, label="Public"),
        ]
    )
    page.add(ft.SafeArea(ft.Text("Minimal design is beautiful!", style=ft.TextStyle(font_size=18))))

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.title = "CupertinoNavigationBar - News App Example"
    page.navigation_bar = ft.CupertinoNavigationBar(
        bgcolor=ft.Colors.INDIGO_100,
        inactive_color=ft.Colors.INDIGO_300,
        active_color=ft.Colors.WHITE,
        on_change=lambda e: print("Selected news category:", e.control.selected_index),
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.TODAY, label="Today"),
            ft.NavigationBarDestination(icon=ft.Icons.TRENDING_UP, label="Trending"),
            ft.NavigationBarDestination(icon=ft.Icons.LIBRARY_BOOKS, label="Library"),
        ]
    )
    page.add(ft.SafeArea(ft.Text("Today's top news!")))

ft.app(main)

page.navigation_bar = ft.CupertinoNavigationBar(
       bgcolor=ft.Colors.AMBER_100,
       inactive_color=ft.Colors.GREY,
       active_color=ft.Colors.BLACK,
       on_change=lambda e: print("Selected tab:", e.control.selected_index),
       destinations=[
           ft.NavigationBarDestination(icon=ft.Icons.EXPLORE, label="Explore"),
           ft.NavigationBarDestination(icon=ft.Icons.COMMUTE, label="Commute"),
           ft.NavigationBarDestination(
               icon=ft.Icons.BOOKMARK_BORDER,
               selected_icon=ft.Icons.BOOKMARK,
               label="Explore",
           ),
       ]
   )
   ```
   - `CupertinoNavigationBar`: Cria uma barra de navegação com estilo similar ao iOS.
   - `bgcolor`: Define a cor de fundo da barra como AMBER_100.
   - `inactive_color`: Cor dos ícones/tabs quando estão inativos.
   - `active_color`: Cor dos ícones/tabs quando estão ativos.
   - `on_change`: Função callback chamada quando um item da barra de navegação é selecionado. Aqui, imprime o índice do tab selecionado.
   - `destinations`: Lista de destinos (tabs) para a barra de navegação. Cada destino é representado por um `NavigationBarDestination` que inclui um ícone, um ícone selecionado (opcional), e um rótulo.

5. **Adição de um Texto na Página dentro de uma SafeArea:** `page.add(ft.SafeArea(ft.Text("Body!")))`
   - `SafeArea`: Um widget que adiciona um espaço seguro, evitando áreas que possam ser cobertas por barras de navegação ou outros elementos intrusivos do sistema.
   - `Text`: Widget que exibe um texto simples, neste caso "Body!".

6. **Inicialização do Aplicativo Flet:** `ft.app(main)`
   - `ft.app`: Função que inicia o aplicativo usando a função `main` como ponto de entrada.

Esse código demonstra como criar uma interface de usuário interativa e visualmente agradável utilizando a biblioteca Flet em Python, com foco em um design que é familiar para usuários de dispositivos iOS.
Para explorar a utilização do `CupertinoNavigationBar` em diferentes contextos e estilos, abaixo estão alguns exemplos variados que modificam o exemplo original para demonstrar a flexibilidade e as diversas possibilidades de uso dentro da biblioteca Flet. Cada exemplo altera diferentes aspectos como cores, comportamento e conteúdo das abas.

### Exemplo 1: Trocando a Paleta de Cores e Adicionando Efeitos
