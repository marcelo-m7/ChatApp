import flet as ft

def main(page: ft.Page):
    def switch_changed(e):
        print("Switch is now:", e.control.value)

    def checkbox_changed(e):
        print("Checkbox is:", e.control.value)

    switch = ft.Switch(value=True, on_change=switch_changed)
    checkbox = ft.Checkbox(value=False, on_change=checkbox_changed)

    page.add(
        ft.CupertinoListTile(
            title=ft.Text("Settings Option 1"),
            subtitle=ft.Text("This is a switch"),
            trailing=switch,
        ),
        ft.CupertinoListTile(
            title=ft.Text("Settings Option 2"),
            subtitle=ft.Text("This is a checkbox"),
            trailing=checkbox,
        ),
    )

ft.app(main)

import flet as ft

def main(page: ft.Page):
    def tile_clicked(e):
        print("Clicked on:", e.control.title.text)

    page.add(
        ft.CupertinoListTile(
            title=ft.Text("First Tile"),
            subtitle=ft.Text("This tile is simple"),
            on_click=tile_clicked,
        ),
        ft.CupertinoListTile(
            notched=True,
            title=ft.Text("Second Tile"),
            subtitle=ft.Text("This tile is notched"),
            trailing=ft.Icon(name=ft.cupertino_icons.ADD),
            on_click=tile_clicked,
        ),
        ft.CupertinoListTile(
            title=ft.Text("Third Tile"),
            subtitle=ft.Text("With a long subtitle demonstrating wrapping text in the Cupertino list tile."),
            trailing=ft.Icon(name=ft.cupertino_icons.FORWARD),
            on_click=tile_clicked,
        ),
    )

ft.app(main)

import flet as ft
   ```
   Esta linha importa a biblioteca Flet, que é usada para criar a interface do usuário.

2. **Definição da função principal `main`:**
   ```python
   def main(page: ft.Page):
   ```
   A função `main` é definida recebendo um argumento `page`, que é um objeto `Page` da biblioteca Flet. Esta função será chamada para configurar a página do aplicativo.

3. **Função de callback para cliques:**
   ```python
   def tile_clicked(e):
       print("Tile clicked")
   ```
   Esta função é definida dentro de `main` e será chamada quando um item da lista (tile) for clicado. Ela simplesmente imprime "Tile clicked" no console.

4. **Adição de componentes à página:**
   ```python
   page.add(
       ft.CupertinoListTile(...),
       ft.CupertinoListTile(...)
   )
   ```
   Este método `add` do objeto `page` adiciona componentes à página. Cada componente adicionado é um `CupertinoListTile`, que é um tipo de widget que simula uma linha de lista no estilo iOS.

5. **Configuração dos CupertinoListTiles:**
   Cada `CupertinoListTile` é configurado com vários parâmetros:
   - `notched`: Um booleano que indica se o tile deve ter um recorte visual. No segundo tile, `notched=True` faz com que ele tenha um recorte.
   - `additional_info`: Um widget de texto que aparece como informação adicional no tile.
   - `bgcolor_activated`: Define a cor de fundo do tile quando ativado.
   - `leading`: Um ícone que aparece no início do tile.
   - `title`: O texto principal do tile.
   - `subtitle`: Um texto secundário.
   - `trailing`: Um ícone que aparece no final do tile.
   - `on_click`: Um callback que é chamado quando o tile é clicado.

6. **Iniciando o aplicativo com a função `app`:**
   ```python
   ft.app(main)
   ```
   Esta linha inicia o aplicativo chamando a função `main` como ponto de entrada, que configura a página.

### Propriedades dos Componentes
- **CupertinoListTile**: Este widget é uma forma de apresentar uma linha em uma lista com estilo inspirado no iOS. Suporta elementos visuais como ícones à esquerda (leading) e à direita (trailing), título e subtítulo, e pode ser configurado para responder a cliques.
- **Icon**: Representa um ícone, e o nome do ícone é passado como parâmetro.
- **Text**: Exibe um texto.

Este código é um exemplo simples de como criar uma interface de usuário interativa com Flet usando componentes específicos do estilo visual Cupertino, com feedback visual e interação através de cliques.
O código fornecido utiliza a biblioteca Flet para criar uma interface de usuário simples com dois tiles do estilo Cupertino. Vamos expandir esse exemplo para mostrar diferentes maneiras de usar os componentes `CupertinoListTile` com variações de layout, cores e interações:

### Exemplo 1: Alterando Cores e Usando Imagens
