import flet as ft

def image_clicked(e):
    print("Imagem clicada!")

def main(page: ft.Page):
    page.title = "Image Event Example"
    page.padding = 50
    
    img = ft.Image(
        src="https://picsum.photos/200/300",
        width=200,
        height=300,
        fit=ft.ImageFit.FILL,
        on_click=image_clicked  # Adicionando evento de clique
    )
    
    page.add(img)
    page.update()

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.add(ft.Image(src_base64="iVBORw0KGgo..."))

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.title = "Dynamic Theme Example"
    page.theme_mode = ft.ThemeMode.DARK  # Alterado para Tema Escuro
    page.padding = 20
    page.update()
    
    img = ft.Image(
        src="/icons/icon-512.png",
        width=200,
        height=200,
        fit=ft.ImageFit.COVER,
        shadow=ft.BoxShadow(10, 10, blur_radius=20)  # Adicionando sombra à imagem
    )
    
    page.add(img)
    page.update()

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.title = "Images Example"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 50
    page.update()

    img = ft.Image(
        src=f"/icons/icon-512.png",
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )
    images = ft.Row(expand=1, wrap=False, scroll="always")
    page.add(img, images)

    for i in range(0, 30):
        images.controls.append(
            ft.Image(
                src=f"https://picsum.photos/200/200?{i}",
                width=200,
                height=200,
                fit=ft.ImageFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),
            )
        )
    page.update()

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.title = "Stylish Image Example"
    page.padding = 50
    
    img = ft.Image(
        src="https://picsum.photos/200/200",
        width=200,
        height=200,
        fit=ft.ImageFit.SCALE_DOWN,
        border_radius=ft.border_radius.all(50),  # Bordas arredondadas
        rotate=45  # Rotação de 45 graus
    )
    
    page.add(img)
    page.update()

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.title = "Transparent Image Example"
    page.padding = 50
    
    img = ft.Image(
        src="https://picsum.photos/250/250",
        width=250,
        height=250,
        fit=ft.ImageFit.CONTAIN,
        opacity=0.5  # 50% de opacidade
    )
    
    page.add(img)
    page.update()

ft.app(main)
