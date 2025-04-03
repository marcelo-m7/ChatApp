def main(page: ft.Page):

ft.app(main)

id_interstitial = (...)
id_banner = (...)

import flet as ft
import flet.ads as ads

import flet as ft
import flet.ads as ads

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    def interstitial_on_load(e):
        print("InterstitialAd loaded")
        # Adicionando lógica adicional aqui
        page.add(ft.Text("Anúncio intersticial carregado!"))

    def banner_on_error(e):
        print("BannerAd error", e.data)
        # Adicionar código para lidar com erros
        page.add(ft.Text(f"Erro ao carregar o banner: {e.data}"))
        
    # Restante do código aqui...
    
ft.app(main)

import flet as ft
import flet.ads as ads

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    tab_control = ft.TabControl(tabs=[
        ft.Tab(
            text="Interstitial",
            content=ft.OutlinedButton("Show InterstitialAd", on_click=lambda e: iad.show())
        ),
        ft.Tab(
            text="Banner",
            content=ft.OutlinedButton("Show BannerAd", on_click=lambda e: display_new_banner_ad())
        )
    ])
    
    page.add(tab_control)

ft.app(main)

import flet as ft
import flet.ads as ads

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    id_rewarded = "ca-app-pub-3940256099942544/5224354917"
    
    def handle_rewarded_ad_close(e):
        print("RewardedAd closed")
        
    def handle_reward(e):
        print("User earned reward!")
    
    rewarded_ad = ads.RewardedAd(
        unit_id=id_rewarded,
        on_load=lambda e: print("RewardedAd loaded"),
        on_error=lambda e: print("RewardedAd error", e.data),
        on_open=lambda e: print("RewardedAd opened"),
        on_close=handle_rewarded_ad_close,
        on_impression=lambda e: print("RewardedAd impression"),
        on_click=lambda e: print("RewardedAd clicked"),
        on_reward=handle_reward
    )
    
    # Botão para mostrar o anúncio recompensado
    show_rewarded_button = ft.OutlinedButton(
        "Show RewardedAd",
        on_click=lambda e: rewarded_ad.show()
    )
    page.add(show_rewarded_button)

ft.app(main)

page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
