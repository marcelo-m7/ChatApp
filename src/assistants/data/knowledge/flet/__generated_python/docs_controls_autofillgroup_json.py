controls=[

def main(page: ft.Page):

ft.TextField(
                    label="Name",
                    autofill_hints=ft.AutofillHint.NAME,
                ),
                ft.TextField(
                    label="Email",
                    autofill_hints=[ft.AutofillHint.EMAIL],
                ),
                ...

ft.app(main)

import flet as ft

import flet as ft

def main(page: ft.Page):
    page.add(
        ft.AutofillGroup(
            ft.Column(
                controls=[
                    ft.TextField(
                        label="Credit Card Number",
                        autofill_hints=ft.AutofillHint.CREDIT_CARD_NUMBER,
                    ),
                    ft.TextField(
                        label="Credit Card Expiry Date",
                        autofill_hints=ft.AutofillHint.CREDIT_CARD_EXPIRATION_DATE,
                    ),
                    ft.TextField(
                        label="CVV",
                        autofill_hints=ft.AutofillHint.CREDIT_CARD_SECURITY_CODE,
                    ),
                ]
            )
        )
    )

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.add(
        ft.AutofillGroup(
            ft.Column(
                controls=[
                    ft.TextField(
                        label="First Name",
                        autofill_hints=ft.AutofillHint.GIVEN_NAME,
                    ),
                    ft.TextField(
                        label="Last Name",
                        autofill_hints=ft.AutofillHint.FAMILY_NAME,
                    ),
                    ft.TextField(
                        label="Email",
                        autofill_hints=ft.AutofillHint.EMAIL,
                    ),
                    ft.TextField(
                        label="Company",
                        autofill_hints=ft.AutofillHint.ORGANIZATION_NAME,
                    ),
                    ft.TextField(
                        label="Job Title",
                        autofill_hints=ft.AutofillHint.JOB_TITLE,
                    ),
                ]
            )
        )
    )

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.add(
        ft.AutofillGroup(
            ft.Column(
                controls=[
                    ft.TextField(
                        label="Full Name",
                        autofill_hints=ft.AutofillHint.NAME,
                    ),
                    ft.TextField(
                        label="Email",
                        autofill_hints=ft.AutofillHint.EMAIL,
                    ),
                    ft.TextField(
                        label="Message",
                        multiline=True,
                        autofill_hints=None,
                    ),
                ]
            )
        )
    )

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.add(
        ft.AutofillGroup(
            ft.Column(
                controls=[
                    ft.TextField(
                        label="Username",
                        autofill_hints=ft.AutofillHint.USERNAME,
                    ),
                    ft.TextField(
                        label="Password",
                        autofill_hints=ft.AutofillHint.PASSWORD,
                        obscure_text=True
                    ),
                ]
            )
        )
    )

ft.app(main)

page.add(
    ft.AutofillGroup(
        ft.Column(
