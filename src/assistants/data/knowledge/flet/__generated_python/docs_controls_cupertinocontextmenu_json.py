import flet as ft

def main(page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.add(
        ft.CupertinoContextMenu(
            enable_haptic_feedback=True,
            content=ft.Image("https://picsum.photos/200/200"),
            actions=[
                ft.CupertinoContextMenuAction(
                    text="Opções",
                    on_click=lambda e: print("Opções"),
                    sub_menu=ft.CupertinoContextMenu(
                        actions=[
                            ft.CupertinoContextMenuAction(
                                text="Sub-opção 1", 
                                on_click=lambda e: print("Sub-opção 1")
                            ),
                            ft.CupertinoContextMenuAction(
                                text="Sub-opção 2", 
                                on_click=lambda e: print("Sub-opção 2")
                            ),
                        ]
                    )
                ),
                ft.CupertinoContextMenuAction(
                    text="Fechar",
                    is_destructive_action=True,
                    on_click=lambda e: print("Fechar"),
                ),
            ],
        )
    )

ft.app(main)

import flet as ft

def main(page):
    page.horizontal_alignment = ft.CrossAxisAlignment.END
    page.vertical_alignment = ft.MainAxisAlignment.SPACE_BETWEEN
    page.add(
        ft.CupertinoContextMenu(
            enable_haptic_feedback=False,
            content=ft.Text("Clique com o botão direito aqui!"),
            actions=[
                ft.CupertinoContextMenuAction(
                    text="Notificação",
                    on_click=lambda e: print("Notificação ativada"),
                ),
                ft.CupertinoContextMenuAction(
                    text="Configurações",
                    on_click=lambda e: print("Abrindo configurações"),
                ),
            ],
        )
    )

ft.app(main)

import flet as ft
   ```
   Esta linha importa a biblioteca Flet e a renomeia como `ft` para facilitar o acesso aos seus módulos e funções.

2. **Definição da função `main`**:
   ```python
   def main(page):
   ```
   Esta função é chamada quando a aplicação é iniciada. Ela recebe um objeto `page`, que representa a página da aplicação onde os widgets (componentes da interface) serão adicionados.

3. **Configuração do alinhamento da página**:
   ```python
   page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
   page.vertical_alignment = ft.MainAxisAlignment.CENTER
   ```
   Estas linhas configuram o alinhamento dos elementos na página. `horizontal_alignment` é definido para centralizar os elementos horizontalmente, e `vertical_alignment` para centralizá-los verticalmente.

4. **Adição de um menu de contexto Cupertino**:
   ```python
   page.add(
       ft.CupertinoContextMenu(
           enable_haptic_feedback=True,
           content=ft.Image("https://picsum.photos/200/200"),
           actions=[
               ...
           ],
       )
   )
   ```
   Esta parte do código adiciona um `CupertinoContextMenu` à página. O menu tem as seguintes propriedades:
   - `enable_haptic_feedback=True`: Ativa o feedback háptico (vibração) quando o menu é utilizado, tipicamente em dispositivos que suportam essa funcionalidade.
   - `content=ft.Image("https://picsum.photos/200/200")`: Define o conteúdo principal do menu, que neste caso é uma imagem obtida de uma URL.

5. **Ações do menu de contexto**:
   Dentro do `CupertinoContextMenu`, há uma lista de `actions` que define as ações disponíveis no menu. Cada ação é uma instância de `CupertinoContextMenuAction` e tem várias propriedades:
   - `text`: O texto da ação exibido no menu.
   - `is_default_action`, `is_destructive_action`: Booleanos que definem se a ação é a ação padrão ou uma ação destrutiva (estilizada para indicar que pode ter consequências sérias, como deletar algo).
   - `trailing_icon`: Um ícone exibido ao lado do texto da ação.
   - `on_click`: Uma função que é chamada quando a ação é clicada. Aqui, simplesmente imprime uma mensagem para o console.

6. **Iniciar a aplicação**:
   ```python
   ft.app(main)
   ```
   Esta linha inicia a aplicação, chamando a função `main` e passando a ela o objeto `page` que será usado para construir a UI.

Em resumo, o código cria uma aplicação com um menu de contexto estilo Cupertino que contém três ações. Cada ação tem um ícone e uma função associada que é chamada quando a ação é clicada. A imagem serve como o conteúdo sobre o qual o menu de contexto é ativado.
Para explorar diferentes formas de uso da `CupertinoContextMenu` no Flet, podemos criar exemplos variados que mostrem como ajustar o menu de contexto para diferentes cenários de interface. Abaixo, fornecerei três exemplos adicionais, cada um com um propósito diferente.

### Exemplo 1: Menu de Contexto com Texto e Imagens
Este exemplo mostra como usar texto combinado com imagens dentro das ações para fornecer mais informações visuais ao usuário.
