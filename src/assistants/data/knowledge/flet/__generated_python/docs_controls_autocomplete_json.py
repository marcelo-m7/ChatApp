import flet as ft

def main(page: ft.Page):
    autocomplete = ft.AutoComplete(
        suggestions=[
            ft.AutoCompleteSuggestion(key="one 1", value="One"),
            ft.AutoCompleteSuggestion(key="two 2", value="Two"),
            ft.AutoCompleteSuggestion(key="three 3", value="Three"),
        ],
        on_select=lambda e: print(e.control.selected_index, e.selection),
        width=300,
        border_radius=10,
        bg_color=ft.colors.LIGHT_BLUE_100,
        focused_bg_color=ft.colors.LIGHT_BLUE_50,
    )
    page.add(autocomplete)

ft.app(main)

import flet as ft

def main(page: ft.Page):
    def update_suggestions(e):
        typed_text = e.control.value
        # Aqui você poderia incluir uma chamada a uma API para buscar sugestões
        suggestions = [
            ft.AutoCompleteSuggestion(key=typed_text + "1", value=typed_text.capitalize() + " One"),
            ft.AutoCompleteSuggestion(key=typed_text + "2", value=typed_text.capitalize() + " Two"),
        ]
        e.control.suggestions = suggestions
        e.control.update()

    autocomplete = ft.AutoComplete(on_input=update_suggestions)
    page.add(autocomplete)

ft.app(main)

import flet as ft
   ```
   Esta linha importa a biblioteca `flet` com um alias `ft`. Flet é uma biblioteca que permite criar aplicações web usando Python de forma simples e rápida.

2. **Definição da função principal `main`**:
   ```python
   def main(page: ft.Page):
   ```
   Esta função é o ponto de entrada da aplicação Flet. Ela recebe um objeto `Page` como argumento, que representa a página da web onde os widgets serão exibidos.

3. **Adição de um widget `AutoComplete` à página**:
   ```python
   page.add(
       ft.AutoComplete(
           ...
       )
   )
   ```
   Aqui, o método `add` do objeto `page` é usado para adicionar widgets à página web. Neste caso, está sendo adicionado um widget `AutoComplete`.

4. **Configuração do widget `AutoComplete`**:
   ```python
   ft.AutoComplete(
       suggestions=[
           ft.AutoCompleteSuggestion(key="one 1", value="One"),
           ft.AutoCompleteSuggestion(key="two 2", value="Two"),
           ft.AutoCompleteSuggestion(key="three 3", value="Three"),
       ],
       on_select=lambda e: print(e.control.selected_index, e.selection),
   )
   ```
   - `suggestions`: Esta é uma lista de sugestões que serão exibidas no widget `AutoComplete`. Cada sugestão é uma instância de `AutoCompleteSuggestion`, que possui as propriedades `key` e `value`. O `key` é um identificador único para cada entrada, e o `value` é o texto que será exibido na interface do usuário.
   - `on_select`: Este é um manipulador de eventos que é chamado quando uma sugestão é selecionada pelo usuário. O `lambda e: print(e.control.selected_index, e.selection)` é uma função anônima que recebe um evento `e` e imprime o índice da seleção (`selected_index`) e a sugestão selecionada (`selection`).

5. **Início da aplicação Flet**:
   ```python
   ft.app(main)
   ```
   Esta linha inicia a aplicação Flet e estabelece `main` como a função de entrada. Isso configura a biblioteca para criar a interface de usuário baseada no que foi definido na função `main`.

Em resumo, este código cria uma aplicação web simples com um campo de `AutoComplete` que permite ao usuário escolher entre três opções ("One", "Two", "Three"). Quando uma opção é selecionada, o índice da seleção e o valor são impressos no console.
O exemplo que você forneceu é um bom ponto de partida para explorar as funcionalidades do componente `AutoComplete` no framework Flet. Vamos expandir esse exemplo em diferentes variações para ilustrar como você pode personalizar e utilizar o `AutoComplete` em diferentes cenários.

### Exemplo 1: AutoComplete com Filtragem Personalizada

Podemos modificar o comportamento padrão de filtragem do `AutoComplete` para permitir uma busca mais complexa ou específica, como ignorar espaços ou diferenciar maiúsculas de minúsculas.
