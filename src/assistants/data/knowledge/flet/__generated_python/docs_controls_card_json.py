import flet as ft

def main(page):
    page.title = "Interactive Card"
    page.add(
        ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.TextField(label="Your name"),
                        ft.TextField(label="Your email", keyboard_type=ft.KeyboardType.EMAIL),
                        ft.TextButton("Submit", on_click=lambda e: submit_form(page)),
                    ]
                ),
                width=400,
                padding=10,
            )
        )
    )

def submit_form(page):
    page.update()

ft.app(main)

import flet as ft

def main(page):
    page.title = "Shopping List Card"
    page.add(
        ft.Card(
            content=ft.Container(
                content=ft.ListView(
                    items=[
                        ft.ListTile(title=ft.Text("Apples"), leading=ft.Icon(ft.Icons.CHECK_BOX_OUTLINE_BLANK)),
                        ft.ListTile(title=ft.Text("Bread"), leading=ft.Icon(ft.Icons.CHECK_BOX_OUTLINE_BLANK)),
                        ft.ListTile(title=ft.Text("Cheese"), leading=ft.Icon(ft.Icons.CHECK_BOX_OUTLINE_BLANK)),
                    ],
                    spacing=10,
                ),
                width=400,
                padding=10,
            )
        )
    )

ft.app(main)

import flet as ft
   ```
   Este comando importa a biblioteca Flet, que é usada para construir interfaces de usuário baseadas na web com Python.

2. **Definição da função principal:**
   ```python
   def main(page):
   ```
   Define a função `main` que recebe um objeto `page`, que representa a página da web onde os elementos da UI serão adicionados.

3. **Configuração do Título da Página:**
   ```python
   page.title = "Card Example"
   ```
   Define o título da página da web como "Card Example".

4. **Adicionando um Cartão à Página:**
   ```python
   page.add(
       ft.Card(
           ...
       )
   )
   ```
   A função `add` do objeto `page` é usada para adicionar elementos à página. Neste caso, está sendo adicionado um objeto `Card`.

5. **Conteúdo do Cartão:**
   Dentro do `Card`, há um `Container` definido, que ajuda a organizar o layout e o estilo dos itens dentro dele. O `Container` tem um conteúdo que é uma `Column` (coluna), permitindo que os itens sejam organizados verticalmente.

   - **ListTile:**
     ```python
     ft.ListTile(
         leading=ft.Icon(ft.Icons.ALBUM),
         title=ft.Text("The Enchanted Nightingale"),
         subtitle=ft.Text("Music by Julie Gable. Lyrics by Sidney Stein.")
     )
     ```
     Este widget é usado para adicionar uma linha de item de lista no cartão, com um ícone de um álbum à esquerda (definido com `leading=ft.Icon(ft.Icons.ALBUM)`), um título e um subtítulo.

   - **Row de Botões:**
     ```python
     ft.Row(
         [ft.TextButton("Buy tickets"), ft.TextButton("Listen")],
         alignment=ft.MainAxisAlignment.END,
     )
     ```
     Define uma linha (`Row`) que contém dois botões de texto ("Buy tickets" e "Listen"). A propriedade `alignment=ft.MainAxisAlignment.END` alinha os botões ao final da linha (à direita).

6. **Propriedades do Container:**
   O `Container` é configurado com uma largura de 400 pixels e um padding de 10 pixels, definindo assim o espaço interno ao redor do conteúdo dentro dele.

7. **Execução do Aplicativo:**
   ```python
   ft.app(main)
   ```
   Esta linha de código inicia o aplicativo usando a função `main` como a função de entrada para manipular a página.

Este código, quando executado, criará um aplicativo web com um cartão que exibe informações sobre uma peça musical fictícia, acompanhada de botões para ações pertinentes, como comprar ingressos ou ouvir a música. É um exemplo simples de como usar a biblioteca Flet para criar interfaces de usuário interativas e visualmente agradáveis.
O código fornecido utiliza a biblioteca Flet para criar uma interface de usuário simples com um card contendo informações sobre uma música, juntamente com botões para ações. Abaixo estão alguns exemplos adicionais que exploram diferentes formas de uso do Flet para criar interfaces com variações de conteúdo, layout e interatividade.

### Exemplo 1: Card com Imagem e Texto

Este exemplo mostra como adicionar uma imagem ao card junto com o texto.
