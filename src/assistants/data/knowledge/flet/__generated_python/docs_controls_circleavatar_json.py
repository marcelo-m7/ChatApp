a1 = ft.CircleAvatar(
      foreground_image_src="https://avatars.githubusercontent.com/u/5041459?s=88&v=4",
      content=ft.Text("FF"),
  )
  ```
  Cria um avatar circular (`CircleAvatar`) com uma imagem de fundo (especificada pelo `foreground_image_src`) e texto "FF" sobreposto (`content=ft.Text("FF")`).

- **Avatar com Imagem de Fundo que Falha e Texto de Reserva**
  ```python
  a2 = ft.CircleAvatar(
      foreground_image_src="https://avatars.githubusercontent.com/u/_5041459?s=88&v=4",
      content=ft.Text("FF"),
  )
  ```
  Semelhante ao `a1`, mas a URL da imagem tem um erro proposital (com um `_` antes do número), mostrando como o avatar reage quando a imagem não pode ser carregada. O texto "FF" serve como reserva.

- **Avatar com Ícone**
  ```python
  a3 = ft.CircleAvatar(
      content=ft.Icon(ft.Icons.ABC),
  )
  ```
  Cria um avatar que contém um ícone (`ft.Icon(ft.Icons.ABC)`), sem outras customizações de cor ou imagem de fundo.

- **Avatar com Ícone e Cores Personalizadas**
  ```python
  a4 = ft.CircleAvatar(
      content=ft.Icon(ft.Icons.WARNING_ROUNDED),
      color=ft.Colors.YELLOW_200,
      bgcolor=ft.Colors.AMBER_700,
  )
  ```
  Similar ao `a3`, mas com cores personalizadas para o ícone (`color`) e para o fundo do avatar (`bgcolor`).

- **Avatar com Status Online**
  ```python
  a5 = ft.Stack(
      [
          ft.CircleAvatar(
              foreground_image_src="https://avatars.githubusercontent.com/u/5041459?s=88&v=4"
          ),
          ft.Container(
              content=ft.CircleAvatar(bgcolor=ft.Colors.GREEN, radius=5),
              alignment=ft.alignment.bottom_left,
          ),
      ],
      width=40,
      height=40,
  )
  ```
  Utiliza um `Stack` para sobrepor elementos, criando um avatar com uma pequena marca verde no canto inferior esquerdo (indicativo de status online). O `Stack` permite posicionar o pequeno círculo verde sobre o avatar maior.

### Adicionando os Avatares à Página

def main(page):

def main(page):
    # Avatar clicável que mostra um alerta
    def on_avatar_click(e):
        ft.dialogs.info(page, "Avatar clicado!")

    a8 = ft.CircleAvatar(
        foreground_image_src="https://avatars.githubusercontent.com/u/5041459?s=88&v=4",
        on_click=on_avatar_click
    )
    page.add(a8)

ft.app(main)

def main(page):
    # Avatar com borda colorida
    a6 = ft.CircleAvatar(
        foreground_image_src="https://avatars.githubusercontent.com/u/5041459?s=88&v=4",
        border_color=ft.Colors.BLUE_700,
        border_width=2,
    )
    page.add(a6)

ft.app(main)

def main(page):
    # Avatar com efeito de sombra
    a7 = ft.CircleAvatar(
        foreground_image_src="https://avatars.githubusercontent.com/u/5041459?s=88&v=4",
        elevation=4  # Adiciona sombra projetada
    )
    page.add(a7)

ft.app(main)

def main(page):
    # Vários avatares em diferentes tamanhos
    sizes = [20, 40, 60, 80]
    avatars = [
        ft.CircleAvatar(
            foreground_image_src="https://avatars.githubusercontent.com/u/5041459?s=88&v=4",
            radius=size
        ) for size in sizes
    ]
    page.add(*avatars)

ft.app(main)

ft.app(main)

import flet as ft
