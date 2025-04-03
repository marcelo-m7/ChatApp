import flet as ft

def button_clicked(e):
    e.control.text = "Clicked!"

def main(page: ft.Page):
    page.add(
        ft.Row([
            ft.Button(
                content=ft.Row([ft.Icon(name=ft.Icons.PLAY_ARROW, size=24), ft.Text("Play")], alignment="center"),
                on_click=button_clicked
            ),
            ft.Button(
                content=ft.Row([ft.Icon(name=ft.Icons.PAUSE, size=24), ft.Text("Pause")], alignment="center"),
                on_click=button_clicked
            )
        ])
    )

ft.app(main)

import flet as ft

def main(page: ft.Page):
    tooltip1 = ft.Tooltip(text="Home icon")
    icon1 = ft.Icon(name=ft.Icons.HOME, tooltip=tooltip1, size=40)
    
    tooltip2 = ft.Tooltip(text="Settings icon")
    icon2 = ft.Icon(name=ft.Icons.SETTINGS, tooltip=tooltip2, size=40)
    
    page.add(ft.Row([icon1, icon2]))

ft.app(main)

import flet as ft

def toggle_icon_color(icon: ft.Icon):
    icon.color = ft.Colors.RED if icon.color != ft.Colors.RED else ft.Colors.GREEN
    icon.update()

def main(page: ft.Page):
    icon1 = ft.Icon(name=ft.Icons.FACE, color=ft.Colors.BLUE, size=40, on_click=lambda e: toggle_icon_color(icon1))
    icon2 = ft.Icon(name=ft.Icons.WORK, color=ft.Colors.ORANGE, size=40, on_click=lambda e: toggle_icon_color(icon2))
    
    page.add(
        ft.Column([
            icon1,
            icon2
        ])
    )

ft.app(main)

import flet as ft
   ```
   Esta linha importa a biblioteca Flet e a renomeia como `ft` para facilitar o acesso às suas funcionalidades.

2. **Definição da função principal:**
   ```python
   def main(page: ft.Page):
   ```
   A função `main` é definida com um parâmetro `page`, que é do tipo `ft.Page`. Este objeto `page` representa uma página da aplicação web ou desktop criada com Flet.

3. **Adicionando elementos à página:**
   ```python
   page.add(
       ft.Row(
           [
               ft.Icon(name=ft.Icons.FAVORITE, color=ft.Colors.PINK),
               ft.Icon(name=ft.Icons.AUDIOTRACK, color=ft.Colors.GREEN_400, size=30),
               ft.Icon(name=ft.Icons.BEACH_ACCESS, color=ft.Colors.BLUE, size=50),
               ft.Icon(name="settings", color="#c1c1c1"),
           ]
       )
   )
   ```
   - `ft.Row([])`: Cria um contêiner do tipo Row (linha), que organiza seus elementos filho em uma linha horizontal.
   - `ft.Icon(...)`: Cada elemento dentro da lista do `Row` é um ícone (`ft.Icon`). Os ícones têm diferentes propriedades definidas:
     - `name`: Nome do ícone, que pode ser um valor de `ft.Icons` ou uma string representando o nome do ícone.
     - `color`: A cor do ícone, que pode ser um valor de `ft.Colors` ou uma string representando um código de cor hexadecimal.
     - `size`: O tamanho do ícone em pixels (opcional).

   O código adiciona quatro ícones com diferentes configurações de cor e tamanho à linha. Os ícones usados são:
   - `FAVORITE`: Ícone de coração, cor rosa.
   - `AUDIOTRACK`: Ícone de nota musical, cor verde e tamanho 30.
   - `BEACH_ACCESS`: Ícone de guarda-chuva de praia, cor azul e tamanho 50.
   - Um ícone personalizado chamado "settings", com cor cinza claro.

4. **Inicialização da aplicação Flet:**
   ```python
   ft.app(main)
   ```
   Esta linha inicia a aplicação, passando a função `main` como argumento. A função `main` será chamada sempre que a aplicação iniciar, criando e configurando a página conforme definido na função.

### Propósito e Uso:
Este código é um exemplo básico de como usar ícones e organizar elementos horizontalmente usando a biblioteca Flet em Python. Ele pode ser usado como parte de interfaces gráficas mais complexas, ajudando a melhorar a estética e a funcionalidade de aplicações web ou desktop. É particularmente útil para desenvolvedores que querem criar rapidamente interfaces gráficas sem se aprofundar em tecnologias de front-end mais complexas como HTML, CSS ou JavaScript.
Claro! O código que você forneceu usa a biblioteca Flet para criar uma interface gráfica simples contendo uma linha (`ft.Row`) de ícones. Vou fornecer alguns exemplos adicionais que expandem o uso de ícones, demonstram outros widgets e interações com eventos.

### Exemplo 1: Adicionando Texto aos Ícones
Este exemplo mostra como combinar ícones com texto usando `ft.Column` para criar um layout de botões com ícones e legendas.
