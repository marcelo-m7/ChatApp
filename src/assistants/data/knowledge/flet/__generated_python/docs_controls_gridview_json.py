import flet as ft

def image_clicked(e, image_index):
    e.page.alert(f"You clicked on image {image_index}")

def main(page: ft.Page):
    page.title = "Interactive GridView"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 30
    page.update()

    images = ft.GridView(
        expand=1,
        runs_count=4,
        max_extent=150,
        child_aspect_ratio=1.0,
        spacing=8,
        run_spacing=8,
    )
    page.add(images)

    for i in range(0, 40):
        img = ft.Image(
            src=f"https://picsum.photos/150?{i}",
            fit=ft.ImageFit.COVER,
            border_radius=ft.border_radius.all(5),
        )
        # Adicionando evento de clique
        img.on_click = lambda e, img_index=i: image_clicked(e, img_index)
        images.controls.append(img)

    page.update()

ft.app(main, view=ft.AppView.WEB_BROWSER)

import flet as ft

def main(page: ft.Page):
    page.title = "GridView with Titles"
    page.theme_mode = ft.ThemeMode.DARK
    page.update()

    images = ft.GridView(
        expand=1,
        runs_count=4,
        max_extent=120,
        child_aspect_ratio=1.0,
        spacing=10,
        run_spacing=10,
    )
    page.add(images)

    for i in range(0, 40):
        col = ft.Column([
            ft.Image(
                src=f"https://picsum.photos/120?{i}",
                fit=ft.ImageFit.COVER,
                border_radius=ft.border_radius.all(5),
            ),
            ft.Text(f"Image {i+1}")
        ])
        images.controls.append(col)

    page.update()

ft.app(main, view=ft.AppView.WEB_BROWSER)

import flet as ft
   ```
   Esta linha importa a biblioteca Flet, que é usada para construir a interface do usuário.

2. **Definição da função `main`**:
   ```python
   def main(page: ft.Page):
   ```
   A função `main` é definida com um parâmetro `page`, que é do tipo `ft.Page`. Essa função será usada para configurar a página da aplicação.

3. **Configurações da página**:
   ```python
   page.title = "GridView Example"
   page.theme_mode = ft.ThemeMode.DARK
   page.padding = 50
   page.update()
   ```
   - `page.title`: Define o título da página como "GridView Example".
   - `page.theme_mode`: Configura o tema da página para o modo escuro (`DARK`).
   - `page.padding`: Adiciona um padding de 50 pixels em todos os lados da página.
   - `page.update()`: Atualiza a página para refletir as configurações aplicadas.

4. **Criação de um GridView para armazenar imagens**:
   ```python
   images = ft.GridView(
       expand=1,
       runs_count=5,
       max_extent=150,
       child_aspect_ratio=1.0,
       spacing=5,
       run_spacing=5,
   )
   page.add(images)
   ```
   - `GridView` é usado para criar um layout de grade para os controles, neste caso, imagens.
   - `expand=1`: Permite que o GridView se expanda para preencher o espaço disponível.
   - `runs_count=5`: Define o número de colunas na grade.
   - `max_extent=150`: Define a largura máxima de cada item na grade.
   - `child_aspect_ratio=1.0`: Mantém a proporção de aspecto dos filhos como 1:1 (quadrado).
   - `spacing=5`: Define o espaçamento entre itens na mesma linha.
   - `run_spacing=5`: Define o espaçamento entre linhas.
   - `page.add(images)`: Adiciona o GridView à página.

5. **Adicionando imagens ao GridView**:
   ```python
   for i in range(0, 60):
       images.controls.append(
           ft.Image(
               src=f"https://picsum.photos/150/150?{i}",
               fit=ft.ImageFit.NONE,
               repeat=ft.ImageRepeat.NO_REPEAT,
               border_radius=ft.border_radius.all(10),
           )
       )
   ```
   - Este loop adiciona 60 imagens ao GridView.
   - `ft.Image`: Cria um widget de imagem.
   - `src`: Define a URL da imagem. Aqui, ele usa imagens aleatórias do serviço Picsum.
   - `fit=ft.ImageFit.NONE`: A imagem não é redimensionada para se ajustar ao espaço disponível.
   - `repeat=ft.ImageRepeat.NO_REPEAT`: A imagem não se repete.
   - `border_radius=ft.border_radius.all(10)`: Define um raio de borda de 10 para todas as bordas da imagem.

6. **Atualização final da página**:
   ```python
   page.update()
   ```
   Atualiza a página novamente após adicionar todas as imagens ao GridView.

7. **Executando a aplicação**:
   ```python
   ft.app(main, view=ft.AppView.WEB_BROWSER)
   ```
   Esta linha inicializa a aplicação usando a função `main` e define que a aplicação deve ser visualizada em um navegador web.

Esse código exemplifica como usar a biblioteca Flet para criar uma aplicação web com um layout visual organizado e interativo, mostrando um uso prático de criação de interface gráfica em Python.
O código fornecido cria uma página usando a biblioteca Flet em Python, que apresenta uma grade de imagens obtidas a partir do serviço Picsum. Vamos explorar algumas variações deste código para demonstrar diferentes funcionalidades e usos do `GridView` e outros componentes do Flet.

### Exemplo 1: Alteração do Layout e da Aparência das Imagens
No exemplo a seguir, vamos alterar o número de colunas, o tamanho máximo das células e a aparência das imagens (como o modo de ajuste da imagem e a borda).
