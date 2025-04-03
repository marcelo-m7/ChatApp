import flet as ft

def main(page: ft.Page):
    lottie_animation = ft.Lottie(
        src='https://raw.githubusercontent.com/xvrh/lottie-flutter/master/example/assets/Mobilo/A.json',
        width=300,
        height=300,
        animate=False  # Inicia sem animar
    )

    def start_animation(e):
        lottie_animation.animate = True
        lottie_animation.update()

    def stop_animation(e):
        lottie_animation.animate = False
        lottie_animation.update()

    start_button = ft.Button(text="Iniciar", on_click=start_animation)
    stop_button = ft.Button(text="Parar", on_click=stop_animation)

    page.add(lottie_animation, start_button, stop_button)

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Lottie(
            src='file:///path/to/your/animation.json',
            animate=True
        )
    )

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Lottie(
            src='https://raw.githubusercontent.com/xvrh/lottie-flutter/master/example/assets/Mobilo/A.json',
            animate=True,
            repeat=True  # Repete a animação infinitamente
        )
    )

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Lottie(
            src='https://raw.githubusercontent.com/xvrh/lottie-flutter/master/example/assets/Mobilo/A.json',
            animate=True,
            reverse=True  # Reproduz a animação de trás para frente
        )
    )

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Lottie(
            src='https://raw.githubusercontent.com/xvrh/lottie-flutter/master/example/assets/Mobilo/A.json',
            animate=True,
            speed=2.0  # Duplica a velocidade da animação
        )
    )

ft.app(main)
