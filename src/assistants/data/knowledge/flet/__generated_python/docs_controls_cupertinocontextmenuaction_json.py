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
                    text="Abrir em nova aba",
                    on_click=lambda e: print("Abrindo nova aba..."),
                ),
                ft.CupertinoContextMenuAction(
                    text="Salvar imagem",
                    on_click=lambda e: print("Imagem salva!"),
                ),
                ft.CupertinoContextMenuAction(
                    text="Sair",
                    is_destructive_action=True,
                    on_click=lambda e: print("Saindo..."),
                ),
            ],
        )
    )

ft.app(main)

import flet as ft

def main(page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.add(
        ft.CupertinoContextMenu(
            enable_haptic_feedback=True,
            content=ft.TextField(hint_text="Digite algo aqui"),
            actions=[
                ft.CupertinoContextMenuAction(
                    text="Limpar",
                    on_click=lambda e: print("Campo limpo!"),
                ),
                ft.CupertinoContextMenuAction(
                    text="Submeter",
                    on_click=lambda e: print("Dados submetidos!"),
                ),
            ],
        )
    )

ft.app(main)

import flet as ft
   ```
   Esta linha importa a biblioteca Flet e dá a ela o apelido de `ft` para facilitar seu uso no restante do código.

2. **Definição da função main**:
   ```python
   def main(page):
   ```
   Esta função é definida como ponto de entrada da aplicação. A função recebe um parâmetro `page`, que representa a página ou janela da aplicação onde os componentes UI serão adicionados.

3. **Configurações de alinhamento da página**:
   ```python
   page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
   page.vertical_alignment = ft.MainAxisAlignment.CENTER
   ```
   Estas linhas definem o alinhamento dos elementos na página. `horizontal_alignment` é configurado para centrar os elementos horizontalmente, e `vertical_alignment` para centrar verticalmente, usando as propriedades de alinhamento disponíveis em Flet.

4. **Adicionando um CupertinoContextMenu à página**:
   ```python
   page.add(
       ft.CupertinoContextMenu(
           enable_haptic_feedback=True,
           content=ft.Image("https://picsum.photos/200/200"),
           actions=[
               ft.CupertinoContextMenuAction(...),
               ft.CupertinoContextMenuAction(...),
               ft.CupertinoContextMenuAction(...)
           ],
       )
   )
   ```
   - `ft.CupertinoContextMenu`: Cria um menu de contexto ao estilo Cupertino. Este componente aceita várias propriedades:
     - `enable_haptic_feedback`: Ativa o feedback tátil quando o menu é aberto (se suportado pelo dispositivo).
     - `content`: Define o conteúdo sobre o qual o menu de contexto é exibido, neste caso uma imagem carregada de "https://picsum.photos/200/200".
     - `actions`: Uma lista de ações que serão mostradas no menu de contexto. Cada ação é representada por um objeto `CupertinoContextMenuAction`.

5. **Ações do CupertinoContextMenu**:
   Cada `CupertinoContextMenuAction` representa uma opção no menu de contexto. Você pode definir o texto da ação, se a ação é a padrão ou destrutiva, um ícone para acompanhar o texto, e uma função callback para lidar com cliques:
   - `text`: O texto mostrado na opção do menu.
   - `is_default_action`: Se verdadeiro, indica que esta é a ação padrão.
   - `is_destructive_action`: Se verdadeiro, indica que a ação tem consequências potencialmente destrutivas (geralmente indicado com uma cor diferente como vermelho).
   - `trailing_icon`: Um ícone mostrado ao lado do texto da ação.
   - `on_click`: Uma função lambda que é chamada quando a ação é clicada. Aqui, simplesmente imprime uma mensagem no console.

6. **Execução da aplicação**:
   ```python
   ft.app(main)
   ```
   Esta linha inicia a aplicação chamando a função `main`.

O resultado será uma aplicação com uma imagem centralizada que, ao ser clicada, exibirá um menu de contexto com três opções, cada uma com diferentes configurações e comportamentos.
Para criar exemplos adicionais do código Flet fornecido, podemos variar o conteúdo principal, as ações do menu e suas funcionalidades. Vamos explorar diferentes cenários para ilustrar o uso do `CupertinoContextMenu` com outros widgets e funcionalidades.

### Exemplo 1: Usando um Texto como Conteúdo
Neste exemplo, substituímos a imagem por um texto. Isso é útil se você deseja que o contexto do menu seja aplicado a elementos de texto.
