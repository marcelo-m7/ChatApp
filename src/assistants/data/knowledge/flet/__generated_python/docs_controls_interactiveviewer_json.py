import flet as ft

def main(page: ft.Page):
    form = ft.Container(
        content=[
            ft.TextField(label="Nome"),
            ft.TextField(label="Email"),
            ft.Button(text="Submit")
        ],
        width=300
    )
    page.add(
        ft.InteractiveViewer(
            min_scale=1,
            max_scale=5,
            boundary_margin=ft.margin.all(20),
            content=form
        )
    )

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.add(
        ft.InteractiveViewer(
            min_scale=0.2,
            max_scale=8,
            boundary_margin=ft.margin.all(25),
            on_interaction_start=lambda e: print("Interação começou:", e),
            on_interaction_end=lambda e: print("Interação terminou:", e),
            on_interaction_update=lambda e: print("Atualização de interação:", e),
            content=ft.Image(src="https://picsum.photos/600/400"),
        )
    )

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.add(
        ft.InteractiveViewer(
            min_scale=0.5,
            max_scale=10,
            boundary_margin=ft.margin.all(15),
            content=ft.Container(
                content=[
                    ft.Image(src="https://picsum.photos/200/300"),
                    ft.Text("Descrição da imagem")
                ],
                spacing=10,
                alignment=ft.Alignment.TOP_CENTER
            ),
        )
    )

ft.app(main)

import flet as ft
   ```
   Esta linha importa a biblioteca Flet e a abrevia como `ft`, facilitando a referência a seus componentes e funcionalidades subsequentemente no código.

2. **Definição da função `main`**:
   ```python
   def main(page: ft.Page):
   ```
   Esta função é responsável por configurar e exibir os componentes na página web. O parâmetro `page` é um objeto do tipo `ft.Page`, que é usado para adicionar e gerenciar componentes na interface do usuário.

3. **Adição de um `InteractiveViewer` ao `page`**:
   ```python
   page.add(
       ft.InteractiveViewer(
           ...
       )
   )
   ```
   O método `add` do objeto `page` é usado para adicionar componentes à página. Aqui, está sendo adicionado um `ft.InteractiveViewer`, que é um componente que permite interações como zoom e pan sobre o conteúdo que ele encapsula.

4. **Configurações do `InteractiveViewer`**:
   - `min_scale=0.1` e `max_scale=15`: Estes parâmetros definem os limites de zoom mínimo e máximo permitidos para o `InteractiveViewer`.
   - `boundary_margin=ft.margin.all(20)`: Define a margem ao redor do conteúdo dentro do `InteractiveViewer`, em todos os lados, com um valor de 20 pixels.
   - `on_interaction_start`, `on_interaction_end`, `on_interaction_update`: Estes são eventos que disparam funções lambda quando a interação começa, termina ou é atualizada, respectivamente. Cada função lambda recebe um evento `e` como parâmetro e imprime este evento.

5. **Adição de conteúdo ao `InteractiveViewer`**:
   ```python
   content=ft.Image(
       src="https://picsum.photos/500/500",
   )
   ```
   Dentro do `InteractiveViewer`, um componente `ft.Image` é adicionado. Este componente mostra uma imagem obtida da URL especificada (`https://picsum.photos/500/500`), que é um serviço que fornece imagens aleatórias para uso em testes e prototipagem.

6. **Execução da aplicação**:
   ```python
   ft.app(main)
   ```
   Esta linha inicia a aplicação Flet, utilizando a função `main` como ponto de entrada. A função `main` será chamada automaticamente quando a aplicação iniciar.

Em resumo, o código cria uma aplicação web que contém um visualizador interativo com uma imagem que pode ser ampliada ou reduzida, com margens definidas e com a capacidade de detectar e responder a interações do usuário.
Claro! Vou criar alguns exemplos que demonstram diferentes formas de uso do `ft.InteractiveViewer` em Flet, explorando variações de conteúdo interno, configurações de escala e eventos de interação.

### Exemplo 1: Uso de Texto no Conteúdo
Neste exemplo, ao invés de uma imagem, vamos colocar um texto grande dentro do `InteractiveViewer` para permitir que o usuário faça zoom e desloque o texto na tela.
