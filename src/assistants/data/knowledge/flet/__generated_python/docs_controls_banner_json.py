import flet as ft

def main(page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def close_banner(e):
        page.close(banner)
        page.add(ft.Text("Action clicked: " + e.control.text))

    retry_button_style = ft.ButtonStyle(bgcolor=ft.Colors.ORANGE)
    ignore_button_style = ft.ButtonStyle(bgcolor=ft.Colors.GRAY)
    cancel_button_style = ft.ButtonStyle(bgcolor=ft.Colors.RED)

    banner = ft.Banner(
        bgcolor=ft.Colors.YELLOW_100,
        leading=ft.Icon(ft.Icons.ERROR_OUTLINE, color=ft.Colors.RED, size=40),
        content=ft.Text(
            value="Error processing your request. How would you like to proceed?",
            color=ft.Colors.BLACK
        ),
        actions=[
            ft.TextButton(text="Retry", style=retry_button_style, on_click=close_banner),
            ft.TextButton(text="Ignore", style=ignore_button_style, on_click=close_banner),
            ft.TextButton(text="Cancel", style=cancel_button_style, on_click=close_banner),
        ],
    )

    page.add(ft.ElevatedButton("Show Error Banner", on_click=lambda e: page.open(banner)))

ft.app(main)

import flet as ft
   ```
   Esta linha importa o módulo Flet, que é usado para criar interfaces de usuário baseadas na web usando Python.

2. **Definição da Função Principal `main`**:
   ```python
   def main(page):
   ```
   Esta função é chamada quando o aplicativo é inicializado. O parâmetro `page` representa a página web onde os elementos da UI são adicionados.

3. **Configuração de Alinhamento**:
   ```python
   page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
   ```
   Esta linha configura o alinhamento horizontal dos widgets na página para o centro.

4. **Definição da Função `close_banner`**:
   ```python
   def close_banner(e):
       page.close(banner)
       page.add(ft.Text("Action clicked: " + e.control.text))
   ```
   `close_banner` é uma função que é chamada quando qualquer um dos botões no banner é clicado. Ele fecha o banner e exibe uma nova mensagem na página indicando qual ação foi clicada.

5. **Estilo do Botão de Ação**:
   ```python
   action_button_style = ft.ButtonStyle(color=ft.Colors.BLUE)
   ```
   Define o estilo para os botões de ação no banner. Neste caso, a cor do botão é configurada como azul.

6. **Criação do Banner**:
   ```python
   banner = ft.Banner(
       bgcolor=ft.Colors.AMBER_100,
       leading=ft.Icon(ft.Icons.WARNING_AMBER_ROUNDED, color=ft.Colors.AMBER, size=40),
       content=ft.Text(
           value="Oops, there were some errors while trying to delete the file. What would you like me to do?",
           color=ft.Colors.BLACK,
       ),
       actions=[
           ft.TextButton(text="Retry", style=action_button_style, on_click=close_banner),
           ft.TextButton(text="Ignore", style=action_button_style, on_click=close_banner),
           ft.TextButton(text="Cancel", style=action_button_style, on_click=close_banner),
       ],
   )
   ```
   Aqui, um `Banner` é criado com um plano de fundo cor âmbar, um ícone de aviso à esquerda, uma mensagem de texto e três botões de ação ("Retry", "Ignore", "Cancel"). Cada botão usa o `action_button_style` definido anteriormente e está ligado à função `close_banner`.

7. **Adicionar Botão para Mostrar o Banner**:
   ```python
   page.add(ft.ElevatedButton("Show Banner", on_click=lambda e: page.open(banner)))
   ```
   Um botão elevado é adicionado à página. Quando clicado, ele abre o banner definido acima.

8. **Inicialização do Aplicativo Flet**:
   ```python
   ft.app(main)
   ```
   Esta linha inicia a aplicação, chamando a função `main`.

Este código ilustra como criar uma interface de usuário interativa e responder a eventos usando Flet em Python, permitindo a exibição de mensagens de erro e opções de ação ao usuário.
O exemplo de código que você forneceu mostra como criar uma `Banner` em Flet, a qual pode ser usada para mostrar mensagens ao usuário com ações específicas, como "Retry", "Ignore", e "Cancel". Aqui estão alguns exemplos adicionais que variam o uso de `Banner` para diferentes cenários e estilos, para demonstrar a flexibilidade deste widget:

### Exemplo 1: Banner com ação única
Este exemplo apresenta um banner com apenas uma ação. Pode ser útil para mensagens de confirmação simples ou notificações.

import flet as ft
import time

def main(page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def auto_close_banner():
        time.sleep(3)  # Espera 3 segundos antes de fechar
        page.close(banner)

    banner = ft.Banner(
        bgcolor=ft.Colors.BLUE_100,
        leading=ft.Icon(ft.Icons.INFO, color=ft.Colors.BLUE, size=40),
        content=ft.Text("This is an informational message that will close automatically.", color=ft.Colors.BLACK),
    )

    page.add(banner)
    page.update()
    auto_close_banner()

ft.app(main)
