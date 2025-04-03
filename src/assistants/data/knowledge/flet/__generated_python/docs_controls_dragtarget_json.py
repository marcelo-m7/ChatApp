import flet as ft

def main(page: ft.Page):
    page.title = "Dynamic Drag and Drop Example"
    
    colors = [ft.Colors.RED, ft.Colors.GREEN, ft.Colors.BLUE, ft.Colors.ORANGE]
    def create_draggable(color):
        return ft.Draggable(
            group="color",
            content=ft.Container(
                width=50,
                height=50,
                bgcolor=color,
                border_radius=5,
            )
        )

    def drag_will_accept(e):
        e.control.content.border = ft.border.all(
            2, ft.Colors.BLACK if e.data == "true" else ft.Colors.RED
        )
        e.control.update()

    def drag_accept(e: ft.DragTargetEvent):
        src = page.get_control(e.src_id)
        e.control.content.bgcolor = src.content.bgcolor
        e.control.content.border = None
        e.control.update()

    def drag_leave(e):
        e.control.content.border = None
        e.control.update()

    draggables = ft.Column([create_draggable(color) for color in colors])
    drag_target = ft.DragTarget(
        group="color",
        content=ft.Container(
            width=50,
            height=50,
            bgcolor=ft.Colors.WHITE,
            border_radius=5,
        ),
        on_will_accept=drag_will_accept,
        on_accept=drag_accept,
        on_leave=drag_leave,
    )

    page.add(ft.Row([draggables, ft.Container(width=100), drag_target]))

ft.app(main)

import flet as ft
   ```
   Esta linha importa a biblioteca Flet, que é usada para criar interfaces gráficas de usuário.

2. **Função Principal `main`**:
   ```python
   def main(page: ft.Page):
   ```
   Define a função principal que recebe um objeto `page` do tipo `ft.Page`, representando a página da aplicação.

3. **Configuração do Título da Página**:
   ```python
   page.title = "Drag and Drop example"
   ```
   Define o título da página como "Drag and Drop example".

4. **Funções de Eventos de Arrastar e Soltar**:
   - **`drag_will_accept`**:
     Essa função é chamada quando um elemento arrastável é movido sobre um alvo de soltar. Ela modifica a borda do container de destino para indicar se o elemento pode ser aceito ou não.
   - **`drag_accept`**:
     Executada quando um elemento arrastável é soltado em um alvo compatível. Atualiza a cor de fundo do container de destino para corresponder à do elemento arrastado e remove a borda.
   - **`drag_leave`**:
     Chamada quando um elemento arrastável é movido para fora de um alvo sem ser soltado. Remove a borda do container de destino.

5. **Adição de Elementos Arrastáveis e Alvos de Soltar**:
   - **Elementos `ft.Draggable`**:
     Três elementos arrastáveis são criados, cada um com um grupo específico (dois no grupo "color" e um no grupo "color1"). Cada elemento tem uma cor e bordas arredondadas.
   - **Alvo `ft.DragTarget`**:
     Um alvo de soltar é definido para aceitar elementos do grupo "color". Ele tem uma cor de fundo específica e bordas arredondadas.
   - Eventos como `on_will_accept`, `on_accept` e `on_leave` são associados a suas respectivas funções de manipulação.

6. **Layout da Página**:
   A página é organizada usando `ft.Row` e `ft.Column` para posicionar os elementos arrastáveis e o alvo de soltar.

7. **Iniciando a Aplicação**:
   ```python
   ft.app(main)
   ```
   Esta linha inicia a aplicação, chamando a função `main`.

### Propriedades dos Elementos:
- **`ft.Container`**:
  Usado para definir áreas retangulares com propriedades como cor de fundo (`bgcolor`), largura (`width`), altura (`height`) e raio da borda (`border_radius`).
- **`ft.Draggable`** e **`ft.DragTarget`**:
  Componentes usados para criar interações de arrastar e soltar. `ft.Draggable` representa o elemento que pode ser arrastado, e `ft.DragTarget` é o local onde esses elementos podem ser soltados. Cada um pode ter um grupo associado que define quais elementos são compatíveis entre si.

Este exemplo ilustra como criar uma interface simples de arrastar e soltar usando o Flet, manipulando a aparência e comportamento dos elementos com base em eventos de interação do usuário.
Certamente! Vou criar alguns exemplos adicionais para o código Flet que você forneceu, mostrando diferentes formas de uso e funcionalidades. Essas variações incluirão mudanças no layout, estilos e interações.

### Exemplo 1: Alterando Estilos e Adicionando Texto aos Draggables

Neste exemplo, adicionaremos texto aos contêineres `Draggable` e modificaremos os estilos para torná-los mais visíveis e interativos.
