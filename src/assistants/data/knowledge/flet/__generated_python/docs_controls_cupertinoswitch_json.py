import flet as ft

def main(page: ft.Page):
    def submit_form(e):
        values = [switch1.value, switch2.value]
        page.controls[2].value = "Valores: " + str(values)
        page.update()

    switch1 = ft.Switch(label="Accept Terms", value=False)
    switch2 = ft.Switch(label="Receive Newsletter", value=True)
    submit_button = ft.ElevatedButton(text="Submit", on_click=submit_form)
    result_label = ft.TextField(value="", enabled=False)

    page.add(switch1, switch2, submit_button, result_label)

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Column([
            ft.Switch(label="Switch 1", value=True),
            ft.Switch(label="Switch 2", value=False),
            ft.Switch(label="Switch 3", value=True)
        ])
    )

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Switch(
            label="Custom Color Switch",
            value=True,
            thumb_color={
                ft.ControlState.SELECTED: ft.Colors.GREEN,
                ft.ControlState.UNSELECTED: ft.Colors.RED
            },
            track_color={
                ft.ControlState.SELECTED: ft.Colors.LIGHT_GREEN,
                ft.ControlState.UNSELECTED: ft.Colors.LIGHT_PINK
            }
        )
    )

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Switch(
            label="Large Switch",
            value=True,
            size=ft.SwitchSize.LARGE
        ),
        ft.Switch(
            label="Small Switch",
            value=False,
            size=ft.SwitchSize.SMALL
        )
    )

ft.app(main)

import logging
   import flet as ft
   import asyncio
   logging.basicConfig(level=logging.DEBUG)
   ```
   - `logging`: Utilizado para configurar o registro de mensagens de depuração, informação, avisos, entre outros. Aqui, o nível de log é definido como `DEBUG`, o que significa que todas as mensagens de nível DEBUG e acima serão logadas.
   - `flet`: É a biblioteca para construir aplicações GUI que podem ser acessadas através de navegadores web.
   - `asyncio`: Uma biblioteca para escrever código concorrente usando a sintaxe `async`/`await`.

2. **Definição da Função Principal**:
   ```python
   def main(page: ft.Page):
   ```
   Esta função `main` aceita um parâmetro `page`, que é um objeto `Page` do Flet. Este objeto é usado para adicionar e gerenciar os componentes da UI na página.

3. **Adicionando Componentes à Página**:
   ```python
   page.add(...)
   ```
   O método `add` é usado para adicionar componentes à página. Vamos detalhar os componentes adicionados:

   - **CupertinoSwitch**:
     ```python
     ft.CupertinoSwitch(
         label="Cupertino Switch",
         value=True,
     )
     ```
     Este componente representa um switch no estilo iOS (Cupertino). `label` define o texto ao lado do switch e `value` define o estado inicial (ligado ou desligado, `True` para ligado).

   - **Switch (Material Design)**:
     ```python
     ft.Switch(
         label="Material Switch",
         value=True,
         thumb_color={ft.ControlState.SELECTED: ft.Colors.BLUE},
         track_color=ft.Colors.YELLOW,
         focus_color=ft.Colors.PURPLE,
     )
     ```
     Este é um switch no estilo Material Design. Além de `label` e `value`, ele tem propriedades adicionais para personalizar a cor: `thumb_color` para a cor da alavanca quando selecionada, `track_color` para a cor do trilho, e `focus_color` para a cor quando o componente está focado.

   - **Container**:
     ```python
     ft.Container(height=20)
     ```
     Um componente que serve como um espaço vazio (spacer) para adicionar espaço entre elementos na UI.

   - **Text**:
     ```python
     ft.Text("Adaptive Switch shows as CupertinoSwitch on macOS and iOS and as Switch on other platforms:")
     ```
     Um componente de texto para adicionar informação na página.

   - **Switch Adaptativo**:
     ```python
     ft.Switch(
         adaptive=True,
         label="Adaptive Switch",
         value=True,
     )
     ```
     Um switch adaptativo que automaticamente muda sua aparência para CupertinoSwitch em plataformas macOS e iOS, e para Switch estilo Material em outras plataformas.

4. **Execução da Aplicação**:
   ```python
   ft.app(main)
   ```
   Esta linha inicia a aplicação chamando a função `main` com a página que será servida aos usuários.

O código acima ilustra bem como criar uma interface simples com diferentes tipos de switches usando a biblioteca Flet, permitindo a criação de aplicações GUI de forma rápida e acessível através de navegadores web.
O código que você forneceu é um exemplo de utilização de diferentes tipos de switches (interruptores) na biblioteca Flet, que é uma biblioteca para criar aplicações web com Python. O exemplo inclui o uso de `CupertinoSwitch`, `Switch` e um `Switch` adaptativo que muda de aparência conforme a plataforma em que é executado. Vamos explorar mais algumas variações e usos desses componentes para tornar seu exemplo ainda mais robusto e ilustrativo.

### Exemplo 1: Switch com Eventos
Adicionando a funcionalidade de capturar mudanças de estado do switch, que pode ser útil em cenários reais de aplicativos:
