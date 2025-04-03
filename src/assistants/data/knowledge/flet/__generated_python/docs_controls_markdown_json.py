def hello_world():
    print("Hello, world!")

import flet as ft

def main(page: ft.Page):
    markdown_advanced = """
# Estilos Avançados

Este texto inclui ~~tachado~~, **_negrito itálico_**, e ***negrito itálico sublinhado***.

## Lista de Tarefas

- [ ] Tarefa 1
- [x] Tarefa 2 (concluída)
- [ ] Tarefa 3

Use `on_tap` para interagir com os links.
    """
    def open_url(e):
        page.launch_url(e.data)
        
    page.add(ft.Markdown(markdown_advanced, on_tap_link=open_url))
    
ft.app(main)

import flet as ft

def main(page: ft.Page):
    markdown_images_links = """
# Imagens e Links

![Flet Logo](https://flet.dev/images/logo.png)

Confira mais em [Flet Website](https://flet.dev).

## Imagem com Link
[![Flet](https://flet.dev/images/logo.png)](https://flet.dev)
    """
    def open_url(e):
        page.launch_url(e.data)
        
    page.add(ft.Markdown(markdown_images_links, on_tap_link=open_url))
    
ft.app(main)

import flet as ft

def main(page: ft.Page):
    markdown_list_table = """
# Listas e Tabelas

- Primeiro item
- Segundo item
  - Subitem 1
  - Subitem 2

## Tabela de Exemplo
| Nome  | Idade |
|-------|-------|
| Alice | 24    |
| Bob   | 29    |
    """
    page.add(ft.Markdown(markdown_list_table))
    
ft.app(main)

import flet as ft
   ```
   Importa a biblioteca Flet com o alias `ft`, que é uma biblioteca para criar aplicativos de interface gráfica usando apenas Python.

2. **String Multilinhas com Markdown:**
   ```python
   md1 = """# Markdown Example
   ...
   """
   ```
   Esta string `md1` contém um texto formatado em Markdown, que inclui exemplos de cabeçalhos, links, imagens, tabelas, estilo de texto (itálico, negrito, tachado), listas e blocos de código. Este texto será renderizado no componente Markdown.

3. **Função Principal (`main`):**
   ```python
   def main(page: ft.Page):
   ```
   Define a função principal que configura a página da aplicação.

4. **Configurações de Página:**
   ```python
   page.scroll = "auto"
   ```
   Configura a rolagem automática para a página, permitindo ao usuário rolar pelo conteúdo se ele exceder a visualização da página.

5. **Adicionando o Componente Markdown:**
   ```python
   page.add(
       ft.Markdown(
           md1,
           selectable=True,
           extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
           on_tap_link=lambda e: page.launch_url(e.data),
       )
   )
   ```
   - **`md1`**: A string Markdown a ser renderizada.
   - **`selectable=True`**: Permite que o texto dentro do componente Markdown seja selecionável pelo usuário.
   - **`extension_set=ft.MarkdownExtensionSet.GITHUB_WEB`**: Usa um conjunto de extensões de Markdown compatível com o estilo do GitHub.
   - **`on_tap_link`**: Um callback que é chamado quando um link é clicado. Aqui, ele abre o URL clicado usando `page.launch_url(e.data)`.

6. **Iniciando o Aplicativo:**
   ```python
   ft.app(main)
   ```
   Inicia a aplicação chamando a função `main`.

### Segundo Bloco de Código

Este bloco é uma versão simplificada e focada em um componente específico de Markdown:

1. **Função `open_url`:**
   ```python
   def open_url(e):
       page.launch_url(e.data)
   ```
   Define uma função que será chamada quando um link dentro do Markdown for clicado, abrindo o URL correspondente.

2. **Adicionando Componente Markdown Simplificado:**
   ```python
   page.add(
       ft.Markdown(
           "[inline-style](https://www.google.com)",
           extension_set="gitHubWeb",
           on_tap_link=open_url,
           expand=True,
       ),
   )
   ```
   - **Markdown Text**: Um link simples em Markdown.
   - **`extension_set="gitHubWeb"`**: Define o conjunto de extensões para renderização (deve ser `ft.MarkdownExtensionSet.GITHUB_WEB` para consistência com o primeiro exemplo).
   - **`expand=True`**: Faz com que o componente Markdown expanda para ocupar todo o espaço disponível.

Ambos os exemplos demonstram como integrar conteúdo Markdown em uma aplicação Flet, com funcionalidades adicionais como links clicáveis e texto selecionável.
Para ilustrar diferentes formas de uso do componente `Markdown` do Flet, vamos criar exemplos variados que destacam diferentes funcionalidades e estilos de formatação Markdown. Além disso, vamos explorar formas diferentes de manipular eventos e configurar a exibição.

### Exemplo 1: Uso básico de Markdown com texto formatado e código
