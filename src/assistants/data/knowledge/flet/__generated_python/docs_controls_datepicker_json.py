import datetime
   import flet as ft
   ```
   - `datetime`: importada para manipulação de datas e horários em Python.
   - `flet`: importada para criar interfaces de usuário interativas em aplicativos web.

2. **Definição da Função Principal:**
   ```python
   def main(page: ft.Page):
   ```
   Esta função é chamada quando o aplicativo é iniciado. Ela recebe um objeto `page`, que representa a página do aplicativo web.

3. **Configuração da Página:**
   ```python
   page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
   ```
   Define o alinhamento horizontal dos elementos na página para o centro.

4. **Definição das Funções de Callback:**
   - `handle_change(e)`: Esta função é chamada quando uma data é selecionada no DatePicker. Ela adiciona um texto à página informando a data selecionada.
     ```python
     def handle_change(e):
         page.add(ft.Text(f"Date changed: {e.control.value.strftime('%Y-%m-%d')}"))
     ```
   - `handle_dismissal(e)`: Esta função é chamada quando o DatePicker é fechado sem uma seleção de data. Ela adiciona um texto à página indicando que o DatePicker foi dispensado.
     ```python
     def handle_dismissal(e):
         page.add(ft.Text("DatePicker dismissed"))
     ```

5. **Adição de um Botão à Página:**
   ```python
   page.add(
       ft.ElevatedButton(
           "Pick date",
           icon=ft.Icons.CALENDAR_MONTH,
           on_click=lambda e: page.open(
               ft.DatePicker(
                   first_date=datetime.datetime(year=2023, month=10, day=1),
                   last_date=datetime.datetime(year=2024, month=10, day=1),
                   on_change=handle_change,
                   on_dismiss=handle_dismissal,
               )
           ),
       )
   )
   ```
   - `ft.ElevatedButton`: Adiciona um botão elevado (com sombra) à página.
   - `"Pick date"`: Texto exibido no botão.
   - `icon=ft.Icons.CALENDAR_MONTH`: Define um ícone de calendário para o botão.
   - `on_click`: Define o que acontece quando o botão é clicado. Aqui, ele abre o `DatePicker`.
   - `ft.DatePicker`: Controla para seleção de datas. `first_date` e `last_date` definem o intervalo de datas disponíveis para seleção.

6. **Início do Aplicativo:**
   ```python
   ft.app(main)
   ```
   Chama a função `ft.app` passando `main` como argumento para iniciar o aplicativo.

Este script cria um interface simples com um botão que, ao ser clicado, permite ao usuário escolher uma data dentro de um intervalo específico. Ações adicionais são definidas para registrar e exibir a seleção ou o cancelamento da escolha.
No código fornecido, um botão é criado usando o Flet, que, quando clicado, abre um seletor de datas (`DatePicker`). O `DatePicker` permite ao usuário escolher uma data entre 1 de outubro de 2023 e 1 de outubro de 2024. Quando uma data é selecionada, ela é exibida na página, e quando o `DatePicker` é dispensado, uma mensagem é exibida na página também.

Aqui estão alguns exemplos adicionais que exploram diferentes aspectos do Flet e do `DatePicker`:

### Exemplo 1: Adicionar uma Etiqueta Inicial
Adicionar uma etiqueta que exiba uma mensagem inicial para o usuário, guiando-o a clicar no botão para selecionar uma data.

import datetime
import flet as ft

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def handle_change(e):
        page.add(ft.Text(f"Date changed: {e.control.value.strftime('%Y-%m-%d')}"))

    def handle_dismissal(e):
        page.add(ft.Text("DatePicker dismissed"))

    page.add(
        ft.ElevatedButton(
            "Pick date",
            icon=ft.Icons.CALENDAR_MONTH,
            on_click=lambda e: page.open(
                ft.DatePicker(
                    initial_date=datetime.datetime(year=2023, month=11, day=15),  # Data inicial
                    first_date=datetime.datetime(year=2023, month=10, day=1),
                    last_date=datetime.datetime(year=2024, month=10, day=1),
                    on_change=handle_change,
                    on_dismiss=handle_dismissal,
                )
            ),
        )
    )

ft.app(main)

import datetime
import flet as ft

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.SPACE_AROUND
    page.add(ft.Text("Escolha uma Data", style=ft.TextStyle(size=25)))

    def handle_change(e):
        page.add(ft.Text(f"Data selecionada: {e.control.value.strftime('%Y-%m-%d')}"))

    def handle_dismissal(e):
        page.add(ft.Text("Seleção de data cancelada"))

    page.add(
        ft.ElevatedButton(
            "Selecionar data",
            icon=ft.Icons.CALENDAR_MONTH,
            on_click=lambda e: page.open(
                ft.DatePicker(
                    first_date=datetime.datetime(year=2023, month=10, day=1),
                    last_date=datetime.datetime(year=2024, month=10, day=1),
                    on_change=handle_change,
                    on_dismiss=handle_dismissal,
                )
            ),
        )
    )

ft.app(main)
