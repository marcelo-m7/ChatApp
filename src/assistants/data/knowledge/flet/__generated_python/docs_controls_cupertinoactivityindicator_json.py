import flet as ft

def main(page):
    def switch_theme(e):
        page.theme_mode = ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        page.update()

    spinner = ft.CupertinoActivityIndicator(
        radius=50,
        color=ft.Colors.RED,
        animating=True,
    )

    theme_btn = ft.Button(
        text="Switch Theme",
        on_click=switch_theme,
    )

    page.add(spinner, theme_btn)

ft.app(main)

import flet as ft

def main(page):
    def toggle_animation(e):
        spinner.animating = not spinner.animating
        page.update()

    spinner = ft.CupertinoActivityIndicator(
        radius=50,
        color=ft.Colors.BLUE,
        animating=False,
    )

    toggle_btn = ft.Button(
        text="Start/Stop",
        on_click=toggle_animation
    )

    page.add(spinner, toggle_btn)

ft.app(main)

import flet as ft

def main(page):
    page.add(
        ft.CupertinoActivityIndicator(radius=20, color=ft.Colors.ORANGE, animating=True),
        ft.CupertinoActivityIndicator(radius=30, color=ft.Colors.TEAL, animating=True),
        ft.CupertinoActivityIndicator(radius=40, color=ft.Colors.PINK, animating=True),
    )

ft.app(main)

import flet as ft

def main(page):
    spinner = ft.CupertinoActivityIndicator(
        radius=20,
        color=ft.Colors.PURPLE,
        animating=True,
    )

    text = ft.Text("Carregando, por favor aguarde...", style=ft.TextStyle(fontSize=20))

    page.add(ft.Row([spinner, ft.Padding(child=text, padding=ft.EdgeInsets.only(left=10))]))

ft.app(main)

import flet as ft
   ```
   Esse comando importa a biblioteca Flet com o alias `ft`, permitindo que suas funções e classes sejam acessadas mais facilmente no código.

2. **Definição da Função Principal**:
   ```python
   def main(page):
   ```
   Aqui, a função `main` é definida, e ela recebe um parâmetro chamado `page`, que representa a página ou janela da aplicação onde os widgets serão adicionados.

3. **Configuração do Modo de Tema da Página**:
   ```python
   page.theme_mode = ft.ThemeMode.LIGHT
   ```
   Esta linha configura o tema da página para o modo claro (`LIGHT`). O Flet também suporta um modo escuro (`DARK`), e essa configuração afeta a aparência de todos os elementos da interface.

4. **Adição de Widgets à Página**:
   ```python
   page.add(
       ft.CupertinoActivityIndicator(
           radius=50,
           color=ft.Colors.RED,
           animating=True,
       )
   )
   ```
   - `page.add(...)`: Este método é usado para adicionar widgets à página. 
   - `ft.CupertinoActivityIndicator(...)`: Este é um widget específico que cria um indicador de atividade, comumente usado para mostrar que um processo está em andamento. É estilizado de acordo com as diretrizes do design Cupertino, que é inspirado no iOS.
     - `radius=50`: Define o raio do indicador de atividade. Neste caso, o raio é 50, o que determina o tamanho do widget.
     - `color=ft.Colors.RED`: Define a cor do indicador. Aqui, a cor é vermelha.
     - `animating=True`: Um booleano que controla se o indicador deve estar animando (girando) ou não. `True` significa que o indicador estará animado.

5. **Execução da Aplicação**:
   ```python
   ft.app(main)
   ```
   Esta linha inicia a aplicação chamando a função `main` e passando a ela um objeto `page` criado internamente pela biblioteca Flet. A função `main` configura e adiciona os widgets necessários a essa página, e a aplicação começa a ser executada.

Em resumo, o código cria uma aplicação GUI simples usando a biblioteca Flet, onde um indicador de atividade vermelho e grande é exibido em uma página com tema claro. Esse tipo de indicador é frequentemente usado para indicar que algum processamento ou carregamento está ocorrendo.
No código fornecido, um aplicativo simples usando a biblioteca Flet está sendo criado. Este aplicativo exibe um `CupertinoActivityIndicator`, um widget que mostra uma animação de carregamento (um spinner) típica do design do iOS. Aqui estão alguns exemplos adicionais para mostrar diferentes formas de uso do `CupertinoActivityIndicator` e outros elementos que você pode adicionar para enriquecer a interface do usuário.

### Exemplo 1: Alterando a cor e o tamanho do indicador
