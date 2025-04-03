def drag_will_accept(e):
      e.control.content.border = border.all(
          2, colors.BLACK45 if e.data == "true" else colors.RED
      )
      e.control.update()
  ```
  Esta função é chamada quando um elemento arrastável está sobre um alvo de soltura. Ela modifica a borda do container alvo baseando-se na validade dos dados (`e.data`).

- **drag_accept**:
  ```python
  def drag_accept(e: DragTargetAcceptEvent):
      src = page.get_control(e.src_id)
      e.control.content.bgcolor = src.content.bgcolor
      e.control.content.border = None
      e.control.update()
  ```
  Chamada quando um elemento é solto sobre um alvo válido. Altera a cor de fundo do alvo para corresponder à do elemento arrastado e remove a borda.

- **drag_leave**:
  ```python
  def drag_leave(e):
      e.control.content.border = None
      e.control.update()
  ```
  Restaura o estilo do alvo de soltura quando o elemento arrastável é movido para fora dele.

### Configuração de Layout e Adição de Componentes

def main(page: Page):
    page.title = "Drag and Drop example"

flet.app(main)

import flet
from flet import (
    Column,
    Container,
    Draggable,
    DragTarget,
    DragTargetAcceptEvent,
    Page,
    Row,
    border,
    colors,
)

import flet
from flet import (
    Column, Container, Draggable, DragTarget, DragTargetAcceptEvent, Page, Row, border, colors,
)

def main(page: Page):
    page.title = "Multiple Drop Targets Example"

    def drag_will_accept(e):
        e.control.content.border = border.all(2, colors.BLACK45 if e.data == "true" else colors.RED)
        e.control.update()

    def drag_accept(e: DragTargetAcceptEvent):
        src = page.get_control(e.src_id)
        e.control.content.bgcolor = src.content.bgcolor
        e.control.content.border = None
        e.control.update()

    def drag_leave(e):
        e.control.content.border = None
        e.control.update()

    page.add(
        Row([
            Column([
                Draggable(
                    group="color",
                    content=Container(
                        width=50,
                        height=50,
                        bgcolor=colors.CYAN,
                        border_radius=5,
                    ),
                ),
                Draggable(
                    group="color",
                    content=Container(
                        width=50,
                        height=50,
                        bgcolor=colors.YELLOW,
                        border_radius=5,
                    ),
                ),
            ]),
            Container(width=100),
            Column([
                DragTarget(
                    group="color",
                    content=Container(
                        width=50,
                        height=50,
                        bgcolor=colors.BLUE_GREY_100,
                        border_radius=5,
                    ),
                    on_will_accept=drag_will_accept,
                    on_accept=drag_accept,
                    on_leave=drag_leave,
                ),
                DragTarget(
                    group="color",
                    content=Container(
                        width=50,
                        height=50,
                        bgcolor=colors.PINK_100,
                        border_radius=5,
                    ),
                    on_will_accept=drag_will_accept,
                    on_accept=drag_accept,
                    on_leave=drag_leave,
                ),
            ]),
        ])
    )

flet.app(main)

import flet
from flet import (
    Column, Container, Draggable, DragTarget, DragTargetAcceptEvent, Page, Row, border, colors, elevation,
)

def main(page: Page):
    page.title = "Drag Visual Feedback Example"

    def drag_will_accept(e):
        e.control.content.border = border.all(2, colors.GREEN200)
        e.control.update()

    def drag_accept(e: DragTargetAcceptEvent):
        src = page.get_control(e.src_id)
        e.control.content.bgcolor = src.content.bgcolor
        e.control.content.border = None
        e.control.update()

    def drag_leave(e):
        e.control.content.border = None
        e.control.update()

    page.add(
        Row([
            Column([
                Draggable(
                    group="color",
                    content=Container(
                        width=50,
                        height=50,
                        bgcolor=colors.CYAN,
                        border_radius=5,
                    ),
                    content_feedback=Container(
                        width=50,
                        height=50,
                        bgcolor=colors.CYAN,
                        border_radius=5,
                        elevation=10,
                    ),
                ),
                Draggable(
                    group="color",
                    content=Container(
                        width=50,
                        height=50,
                        bgcolor=colors.YELLOW,
                        border_radius=5,
                    ),
                    content_feedback=Container(
                        width=50,
                        height=50,
                        bgcolor=colors.YELLOW,
                        border_radius=5,
                        elevation=10,
                    ),
                ),
            ]),
            Container(width=100),
            DragTarget(
                group="color",
                content=Container(
                    width=50,
                    height=50,
                    bgcolor=colors.BLUE_GREY_100,
                    border_radius=5,
                ),
                on_will_accept=drag_will_accept,
                on_accept=drag_accept,
                on_leave=drag_leave,
            ),
        ])
    )

flet.app(main)
