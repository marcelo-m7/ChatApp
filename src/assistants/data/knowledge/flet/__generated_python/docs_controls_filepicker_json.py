from fastapi import FastAPI, Response, FileResponse
import flet as ft

def main(page: ft.Page):
    def download_file(_):
        page.launch_url("/download/sample.txt")

    page.add(
        ft.ElevatedButton(
            "Download Sample File",
            icon=ft.Icons.DOWNLOAD,
            on_click=download_file
        )
    )

app = flet.fastapi.app(main)

@app.get("/download/{filename}")
def download(filename: str):
    path = f"/path/to/your/files/{filename}"  # Ajuste ao caminho correto
    return FileResponse(path)

ft.app(main)

import flet as ft

   def main(page: ft.Page):
   ```
   Importa a biblioteca Flet e define a função principal `main`, que aceita um objeto `page` do tipo `ft.Page`.

2. **Função Interna para Resultado de Seleção de Arquivos:**
   ```python
   def pick_files_result(e: ft.FilePickerResultEvent):
       selected_files.value = (
           ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
       )
       selected_files.update()
   ```
   Esta função é chamada quando o usuário seleciona arquivos usando o diálogo de seleção de arquivos. Os nomes dos arquivos selecionados são juntados em uma string e atribuídos a um componente `Text` para exibição. Se nenhum arquivo for selecionado, exibe "Cancelled!".

3. **Configuração do Diálogo de Seleção de Arquivos e Componentes UI:**
   ```python
   pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
   selected_files = ft.Text()
   page.overlay.append(pick_files_dialog)
   ```
   Cria um `FilePicker` que é usado para selecionar arquivos e um componente `Text` para exibir os nomes dos arquivos selecionados. O `FilePicker` é adicionado ao overlay da página, o que significa que ele pode aparecer sobre outros componentes.

4. **Adição de Botão e Texto à Página:**
   ```python
   page.add(
       ft.Row(
           [
               ft.ElevatedButton(
                   "Pick files",
                   icon=ft.Icons.UPLOAD_FILE,
                   on_click=lambda _: pick_files_dialog.pick_files(
                       allow_multiple=True
                   ),
               ),
               selected_files,
           ]
       )
   )
   ```
   Adiciona um botão que, quando clicado, abre o diálogo de seleção de arquivos com a capacidade de selecionar múltiplos arquivos. O botão e o texto são organizados horizontalmente usando `ft.Row`.

### Parte 2: Código FastAPI

1. **Integração com FastAPI e Definição de Rota:**
   ```python
   from fastapi import FastAPI, Response
   from fastapi.responses import FileResponse

   app = flet_fastapi.app(main)

   @app.get("/download/{filename}")
   def download(filename: str):
       path = prepare_file(filename)
       return FileResponse(path)
   ```
   Define uma aplicação FastAPI integrada com a aplicação Flet. A rota `/download/{filename}` serve para baixar arquivos, onde `prepare_file` seria uma função definida pelo usuário para localizar o caminho do arquivo no servidor.

2. **Botão de Download e URL de Upload:**
   ```python
   ft.ElevatedButton("Download myfile", on_click=lambda _: page.launch_url("/download/myfile.txt"))

   upload_url = page.get_upload_url("dir/filename.ext", 60)
   ```
   Cria um botão na aplicação Flet que, ao ser clicado, direciona para a URL de download do arquivo. `page.get_upload_url` gera uma URL temporária para upload de arquivos.

3. **Configuração do Diretório de Upload:**
   ```python
   ft.app(main, upload_dir="uploads")
   ```
   Inicia a aplicação Flet especificando o diretório onde os arquivos carregados serão armazenados.

### Conclusão

O código utiliza a biblioteca Flet para criar uma interface gráfica que permite aos usuários selecionar arquivos para upload e baixar arquivos, integrando funcionalidades de backend através de FastAPI para o manuseio de arquivos, tanto para upload quanto para download.
Para expandir o exemplo dado e mostrar diferentes formas de utilização do código com a biblioteca Flet, podemos criar variações nos componentes e funcionalidades, explorando mais características da biblioteca. Vamos dividir isso em três cenários diferentes.

### Cenário 1: Uso de Filtros de Tipo de Arquivo no FilePicker
Neste exemplo, vamos modificar o `FilePicker` para permitir que o usuário selecione apenas arquivos de imagem.

import flet as ft

def main(page: ft.Page):
    file_type_input = ft.TextField(hint_text="Enter file type (e.g., .txt, .pdf)")

    def on_button_click(_):
        file_type = file_type_input.value.strip()
        if file_type:
            pick_files_dialog.file_types = [file_type]
        pick_files_dialog.pick_files(allow_multiple=True)
    
    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        )
        selected_files.update()

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()
    page.overlay.append(pick_files_dialog)
    page.add(
        ft.Column([
            file_type_input,
            ft.ElevatedButton(
                "Pick files",
                icon=ft.Icons.FOLDER_OPEN,
                on_click=on_button_click
            ),
            selected_files,
        ])
    )

ft.app(main)
