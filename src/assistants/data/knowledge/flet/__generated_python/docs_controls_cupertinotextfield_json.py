def main(page: ft.Page):

ft.TextField(label="Material"),
   ```
   Este é um campo de entrada de texto básico com uma etiqueta (label) "Material". A etiqueta serve como uma descrição ou indicação do que deve ser inserido no campo.

2. **CupertinoTextField:**
   ```python
   ft.CupertinoTextField(placeholder_text="Placeholder"),
   ```
   `CupertinoTextField` é um estilo de campo de entrada de texto que segue o design do iOS (estilo Cupertino). O `placeholder_text="Placeholder"` define um texto de ajuda que é exibido no campo de entrada até que algo seja digitado.

3. **TextField adaptativo:**
   ```python
   ft.TextField(adaptive=True, label="Adaptive"),
   ```
   Este `TextField` é adaptativo, o que significa que ele mudará sua aparência baseado na plataforma em que a aplicação está sendo executada (por exemplo, terá uma aparência estilo Material Design em Android e estilo Cupertino em iOS). A etiqueta "Adaptive" serve como uma descrição.

### Iniciar a Aplicação

import flet as ft

import flet as ft

def main(page: ft.Page):
    page.add(
        ft.CupertinoTextField(
            placeholder_text="Digite algo...",
            border=ft.border.all(2, color=ft.colors.GREEN),
            padding=ft.EdgeInsets.all(10)
        )
    )

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.add(
        ft.TextField(
            label="Usuário",
            prefix_icon=ft.icons.PERSON,
            width=300
        ),
        ft.TextField(
            label="Senha",
            obscure_text=True,
            prefix_icon=ft.icons.LOCK,
            width=300
        )
    )

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.add(
        ft.TextField(label="Padrão"),
        ft.CupertinoTextField(placeholder_text="Estilo iOS"),
        ft.TextField(adaptive=True, label="Adaptativo com Estilo de Sistema")
    )

ft.app(main)

import flet as ft

def on_text_change(text_field: ft.TextField, event: ft.Event):
    print("Texto alterado:", text_field.value)

def on_text_submit(text_field: ft.TextField, event: ft.Event):
    print("Texto submetido:", text_field.value)

def main(page: ft.Page):
    adaptive_text_field = ft.TextField(
        adaptive=True,
        label="Digite e pressione Enter",
        on_change=on_text_change,
        on_submit=on_text_submit
    )
    page.add(adaptive_text_field)

ft.app(main)

import flet as ft

def validate_email(text_field: ft.TextField, event: ft.Event):
    if "@" not in text_field.value or "." not in text_field.value:
        text_field.error_text = "Por favor, insira um e-mail válido."
    else:
        text_field.error_text = None

def main(page: ft.Page):
    email_field = ft.TextField(
        label="E-mail",
        on_change=validate_email
    )
    page.add(email_field)

ft.app(main)
