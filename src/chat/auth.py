import os
import flet as ft
from flet.auth.providers import GitHubOAuthProvider

class AuthManager:
    def __init__(self, page: ft.Page):
        self.page = page
        self.provider = GitHubOAuthProvider(
            client_id=os.getenv("GITHUB_CLIENT_ID"),
            client_secret=os.getenv("GITHUB_CLIENT_SECRET"),
            redirect_url='http://localhost:8550/oauth_callback',
        )
            # redirect_url='https://9add73eb-1d78-4beb-99c1-ddcc8e613ebd-00-2c518dp4o8er8.riker.replit.dev:3000/oauth_callback', # Replit
        self.login_button = ft.ElevatedButton("Login with GitHub", on_click=self.login_button_click)
        self.logout_button = ft.ElevatedButton("Logout", on_click=self.logout_button_click)
        self.toggle_login_buttons()

    def login_button_click(self, e):
        """Inicia o processo de login."""
        self.page.login(self.provider, scope=["public_repo"])

    def logout_button_click(self, e):
        """Inicia o processo de logout."""
        self.page.logout()

    # def on_login(self, e: ft.LoginEvent):
    #     """Callback chamado após o login."""
    #     if not e.error:
    #         self.toggle_login_buttons()
    #         # self.start_app_func()

    def on_logout(self, e):
        """Callback chamado após o logout."""
        self.toggle_login_buttons()

    def toggle_login_buttons(self):
        """Alterna a visibilidade dos botões de login e logout."""
        self.login_button.visible = self.page.auth is None
        self.logout_button.visible = self.page.auth is not None
        self.page.update()
        