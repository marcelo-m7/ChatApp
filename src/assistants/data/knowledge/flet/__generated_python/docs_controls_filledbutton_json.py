import flet as ft

def main(page: ft.Page):
    page.title = "Botões com Diferentes Tamanhos"
    page.add(
        ft.FilledButton(
            text="Pequeno",
            elevation=1
        ),
        ft.FilledButton(
            text="Médio",
            elevation=4
        ),
        ft.FilledButton(
            text="Grande",
            elevation=8
        )
    )

ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.title = "Botões com Ícones e Layout"
    page.add(
        ft.Row([
            ft.FilledButton(
                text="Adicionar",
                icon="add",
                icon_color=ft.colors.BLUE_500
            ),
            ft.FilledButton(
                text="Editar",
                icon="edit",
                icon_color=ft.colors.AMBER_500
            ),
            ft.FilledButton(
                text="Excluir",
                icon="delete",
                icon_color=ft.colors.RED_500
            )
        ], alignment="spaceAround")
    )

ft.app(main)

import flet as ft

def on_button_click(e):
    e.control.text = "Clicado!"
    e.control.update()

def main(page: ft.Page):
    page.title = "Botões com Eventos"
    btn = ft.FilledButton(
        text="Clique-me",
        on_click=on_button_click
    )
    page.add(btn)

ft.app(main)

import flet as ft
   ```
   Este código importa a biblioteca Flet com um alias `ft`, que é utilizado para acessar as funções e classes da biblioteca.

2. **Definição da função `main`**:
   ```python
   def main(page: ft.Page):
   ```
   A função `main` é definida com um parâmetro `page`, que é do tipo `ft.Page`. Este é um objeto que representa a página da aplicação web onde os elementos da UI (Interface do Usuário) serão adicionados.

3. **Configurando o título da página**:
   ```python
   page.title = "Basic filled buttons"
   ```
   Aqui o título da página é definido como "Basic filled buttons". Este título aparece na aba do navegador quando a página é carregada.

4. **Adicionando botões à página**:
   ```python
   page.add(
       ft.FilledButton(text="Filled button"),
       ft.FilledButton("Disabled button", disabled=True),
       ft.FilledButton("Button with icon", icon="add"),
   )
   ```
   Nesta parte, três botões são adicionados à página usando o método `add` do objeto `page`:

   - `ft.FilledButton(text="Filled button")`: Adiciona um botão preenchido com o texto "Filled button". Por padrão, o botão é habilitado e sem ícone.
   - `ft.FilledButton("Disabled button", disabled=True)`: Adiciona um botão com o texto "Disabled button", mas este está desabilitado (`disabled=True`), o que significa que não pode ser clicado ou interagido.
   - `ft.FilledButton("Button with icon", icon="add")`: Adiciona um botão com o texto "Button with icon" e um ícone representado pela string "add". O ícone "add" geralmente representa um sinal de mais (+), indicativo de uma ação de adição ou criação.

5. **Executando a aplicação**:
   ```python
   ft.app(main)
   ```
   Este comando inicia a aplicação, chamando a função `main` e passando a ela o objeto `page` que será usado para construir a interface gráfica. A função `ft.app` é responsável por configurar e executar o servidor web que serve a aplicação Flet.

### Conclusão

Este script cria uma interface gráfica simples com três botões usando a biblioteca Flet, que é projetada para facilitar a criação de aplicativos web com Python. Cada botão demonstra diferentes propriedades que podem ser configuradas, como texto, estado habilitado/desabilitado e ícones. Flet permite o desenvolvimento de interfaces de usuário de forma rápida e eficiente, sendo uma excelente opção para projetos que necessitam de uma interface gráfica simples rodando em um navegador.
Abaixo estão alguns exemplos adicionais que ilustram diferentes maneiras de utilizar o `FilledButton` no Flet para criar interfaces de usuário interativas e visuais. Esses exemplos expandem o código básico fornecido, mostrando como configurar cores, eventos e muito mais.

### Exemplo 1: Alterando Cores do Botão
Este exemplo mostra como alterar as cores de fundo e do texto de um `FilledButton`.
