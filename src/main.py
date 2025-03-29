import flet as ft
from chat.chat_interface import ChatInterface
from dotenv import load_dotenv
from chat.chat_app import ChatApp
from chat.auth import AuthManager

load_dotenv(".env")
chat_app = ChatApp()

def main(page: ft.Page):
    # Configurações da página
    page.title = "Chat Em Tempo Real - Flet App"
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # page.scroll = ft.ScrollMode.ADAPTIVE
    page.update()

    # Inicializa o gerenciador de autenticação
    auth_manager = AuthManager(page)

    # Função para iniciar o aplicativo após o login
    def start_app():
        # page.clean()
        ChatInterface(page, chat_app)
        page.update()

    # Callback para o evento de login
    def on_login(e: ft.LoginEvent):
        if not e.error:
            auth_manager.toggle_login_buttons()
            start_app()
        else:
            print(f"Error logging in: {e.error}")
            start_app() # Para Testes

    # Configura o callback de login
    page.on_login = on_login
    page.add(auth_manager.login_button, auth_manager.logout_button)


if __name__ == "__main__":
    ft.app(main, port=8550, view=ft.AppView.WEB_BROWSER, upload_dir="uploads/", host="localhost", assets_dir="assets")
    # ft.app(main, port=8550, view=ft.AppView.WEB_BROWSER, upload_dir="uploads/", host="0.0.0.0", assets_dir="assets") # Replit
